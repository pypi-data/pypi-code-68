# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/18_callback.fp16.ipynb (unless otherwise specified).

__all__ = ['get_master', 'to_master_grads', 'to_model_params', 'test_overflow', 'grad_overflow', 'copy_clone',
           'ModelToHalf', 'MixedPrecision', 'NativeMixedPrecision']

# Cell
from ..basics import *
from .progress import *

from torch.cuda.amp import GradScaler, autocast

# Cell
from ..fp16_utils import convert_network, model_grads_to_master_grads, master_params_to_model_params

# Cell
from torch.nn.utils import parameters_to_vector

# Cell
def get_master(opt, flat_master=False):
    model_params = [[param for param in pg if param.requires_grad] for pg in opt.param_lists]
    if flat_master:
        master_params = []
        for pg in model_params:
            mp = parameters_to_vector([param.data.float() for param in pg])
            mp = nn.Parameter(mp, requires_grad=True)
            if mp.grad is None: mp.grad = mp.new(*mp.size())
            master_params.append([mp])
    else:
        master_params = [[nn.Parameter(param.data.clone().float().detach(), requires_grad=True) for param in pg] for pg in model_params]
    return model_params, master_params

# Cell
def to_master_grads(model_pgs, master_pgs, flat_master=False):
    for (model_params,master_params) in zip(model_pgs,master_pgs):
        model_grads_to_master_grads(model_params, master_params, flat_master=flat_master)

# Cell
def to_model_params(model_pgs, master_pgs, flat_master=False)->None:
    for (model_params,master_params) in zip(model_pgs,master_pgs):
        master_params_to_model_params(model_params, master_params, flat_master=flat_master)

# Cell
def test_overflow(x):
    s = float(x.float().sum())
    return (s == float('inf') or s == float('-inf') or s != s)

# Cell
def grad_overflow(pgs):
    for pg in pgs:
        for p in pg:
            if p.grad is not None and test_overflow(p.grad.data): return True
    return False

# Cell
def copy_clone(d):
    return {k:(v.detach().clone().float() if isinstance(v,Tensor) else v) for k,v in d.items()}

# Cell
def _copy_state(opt, pgs1, pgs2):
    opt.param_lists = pgs2
    for pg1,pg2 in zip(pgs1, pgs2):
        for p1,p2 in zip(pg1, pg2): opt.state[p2] = copy_clone(opt.state.pop(p1, {}))

# Cell
class ModelToHalf(Callback):
    "Use with MixedPrecision callback (but it needs to run at the very beginning)"
    run_before=TrainEvalCallback
    def before_fit(self): self.learn.model = convert_network(self.model, dtype=torch.float16)
    def after_fit(self): self.learn.model = convert_network(self.model, dtype=torch.float32)

# Cell
@docs
class MixedPrecision(Callback):
    "Run training in mixed precision"
    toward_end=True

    def __init__(self, loss_scale=512, flat_master=False, dynamic=True, max_loss_scale=2.**24,
                 div_factor=2., scale_wait=500, clip=None):
        assert torch.backends.cudnn.enabled, "Mixed precision training requires cudnn."
        self.flat_master,self.dynamic,self.max_loss_scale = flat_master,dynamic,max_loss_scale
        self.div_factor,self.scale_wait,self.clip = div_factor,scale_wait,clip
        self.loss_scale = max_loss_scale if dynamic else loss_scale

    def before_fit(self):
        assert self.dls.device.type == 'cuda', "Mixed-precision training requires a GPU, remove the call `to_fp16`"
        if self.learn.opt is None: self.learn.create_opt()
        self.model_pgs,self.master_pgs = get_master(self.opt, self.flat_master)
        self.old_pgs = self.opt.param_lists
        #Changes the optimizer so that the optimization step is done in FP32.
        _copy_state(self.learn.opt, self.model_pgs, self.master_pgs)
        if self.dynamic: self.count = 0

    def before_batch(self): self.learn.xb = to_half(self.xb)
    def after_pred(self): self.learn.pred = to_float(self.pred)
    def before_backward(self): self.learn.loss *= self.loss_scale

    def after_backward(self):
        self.learn.loss /= self.loss_scale #To record the real loss
        #First, check for an overflow
        if self.dynamic and grad_overflow(self.model_pgs):
            self.loss_scale /= self.div_factor
            self.model.zero_grad()
            raise CancelBatchException() #skip step and zero_grad

        to_master_grads(self.model_pgs, self.master_pgs, self.flat_master)
        for master_params in self.master_pgs:
            for param in master_params:
                if param.grad is not None: param.grad.div_(self.loss_scale)
        if self.clip is not None:
            for group in self.master_pgs: nn.utils.clip_grad_norm_(group, self.clip)
        # Check if it's been long enough without overflow
        if self.dynamic:
            self.count += 1
            if self.count == self.scale_wait:
                self.count = 0
                self.loss_scale *= self.div_factor

    def after_step(self):
        self.model.zero_grad() #Zero the gradients of the model manually (optimizer disconnected)
        to_model_params(self.model_pgs, self.master_pgs, self.flat_master)

    def after_fit(self):
        if not hasattr(self,'master_pgs'): return
        _copy_state(self.learn.opt, self.master_pgs, self.model_pgs)
        self.learn.opt.param_lists  = self.old_pgs
        delattr(self, "master_pgs")
        delattr(self, "model_pgs")
        delattr(self, "old_pgs")

    _docs = dict(before_fit="Put the model in FP16 and prepare the two copies of the parameters",
                 before_batch="Put the input in FP16",
                 after_pred="Put the output back to FP32 so that the loss is computed in FP32",
                 before_backward="Apply loss scaling to avoid gradient underflow",
                 after_backward="Copy the gradients to the master param and undo the loss scaling",
                 after_step="Copy the master params to the model params",
                 after_fit="Put the model back in FP32"
    )

# Cell
@delegates(MixedPrecision.__init__)
@patch
def to_fp16(self:Learner, **kwargs):
    self.add_cbs([ModelToHalf(), MixedPrecision(**kwargs)])
    return self

# Cell
@patch
def to_fp32(self: Learner):
    self.remove_cbs([ModelToHalf, MixedPrecision])
    return self

# Cell
class NativeMixedPrecision(Callback):
    "Mixed precision training using Pytorch's `autocast` and `GradScaler`"
    @delegates(GradScaler.__init__)
    def __init__(self, **kwargs): self.scaler_kwargs,self.autocast = kwargs,autocast()

    def before_fit(self):
        self.learn.scaler = GradScaler(**self.scaler_kwargs)
        self.learn._step,self.learn._backward = self._step,self._backward

    def before_batch(self): self.autocast.__enter__()
    def after_step(self): self.learn.scaler.update()
    def after_loss(self): self.autocast.__exit__()
    def _backward(self): self.scaler.scale(self.loss).backward()
    def _step(self): self.scaler.step(self.opt)

# Cell
@delegates(GradScaler.__init__)
@patch
def to_native_fp16(self:Learner, **kwargs):
    self.add_cb(NativeMixedPrecision(**kwargs))
    return self

# Cell
@patch
def to_native_fp32(self:Learner):
    self.remove_cb(NativeMixedPrecision)
    return self