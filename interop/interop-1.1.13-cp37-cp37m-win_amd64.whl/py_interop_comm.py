# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_py_interop_comm', [dirname(__file__)])
        except ImportError:
            import _py_interop_comm
            return _py_interop_comm
        if fp is not None:
            try:
                _mod = imp.load_module('_py_interop_comm', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _py_interop_comm = swig_import_helper()
    del swig_import_helper
else:
    import _py_interop_comm
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _py_interop_comm.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _py_interop_comm.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _py_interop_comm.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _py_interop_comm.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _py_interop_comm.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _py_interop_comm.SwigPyIterator_equal(self, x)

    def copy(self):
        return _py_interop_comm.SwigPyIterator_copy(self)

    def next(self):
        return _py_interop_comm.SwigPyIterator_next(self)

    def __next__(self):
        return _py_interop_comm.SwigPyIterator___next__(self)

    def previous(self):
        return _py_interop_comm.SwigPyIterator_previous(self)

    def advance(self, n):
        return _py_interop_comm.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _py_interop_comm.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _py_interop_comm.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _py_interop_comm.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _py_interop_comm.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _py_interop_comm.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _py_interop_comm.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _py_interop_comm.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import interop.py_interop_run
import interop.py_interop_metrics
class format_exception(interop.py_interop_run.base_exception):
    __swig_setmethods__ = {}
    for _s in [interop.py_interop_run.base_exception]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, format_exception, name, value)
    __swig_getmethods__ = {}
    for _s in [interop.py_interop_run.base_exception]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, format_exception, name)
    __repr__ = _swig_repr

    def __init__(self, mesg):
        this = _py_interop_comm.new_format_exception(mesg)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def __str__(self):
        return _py_interop_comm.format_exception___str__(self)
    __swig_destroy__ = _py_interop_comm.delete_format_exception
    __del__ = lambda self: None
format_exception_swigregister = _py_interop_comm.format_exception_swigregister
format_exception_swigregister(format_exception)

class file_not_found_exception(interop.py_interop_run.base_exception):
    __swig_setmethods__ = {}
    for _s in [interop.py_interop_run.base_exception]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, file_not_found_exception, name, value)
    __swig_getmethods__ = {}
    for _s in [interop.py_interop_run.base_exception]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, file_not_found_exception, name)
    __repr__ = _swig_repr

    def __init__(self, mesg):
        this = _py_interop_comm.new_file_not_found_exception(mesg)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def __str__(self):
        return _py_interop_comm.file_not_found_exception___str__(self)
    __swig_destroy__ = _py_interop_comm.delete_file_not_found_exception
    __del__ = lambda self: None
file_not_found_exception_swigregister = _py_interop_comm.file_not_found_exception_swigregister
file_not_found_exception_swigregister(file_not_found_exception)

class bad_format_exception(format_exception):
    __swig_setmethods__ = {}
    for _s in [format_exception]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, bad_format_exception, name, value)
    __swig_getmethods__ = {}
    for _s in [format_exception]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, bad_format_exception, name)
    __repr__ = _swig_repr

    def __init__(self, mesg):
        this = _py_interop_comm.new_bad_format_exception(mesg)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def __str__(self):
        return _py_interop_comm.bad_format_exception___str__(self)
    __swig_destroy__ = _py_interop_comm.delete_bad_format_exception
    __del__ = lambda self: None
bad_format_exception_swigregister = _py_interop_comm.bad_format_exception_swigregister
bad_format_exception_swigregister(bad_format_exception)

class incomplete_file_exception(format_exception):
    __swig_setmethods__ = {}
    for _s in [format_exception]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, incomplete_file_exception, name, value)
    __swig_getmethods__ = {}
    for _s in [format_exception]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, incomplete_file_exception, name)
    __repr__ = _swig_repr

    def __init__(self, mesg):
        this = _py_interop_comm.new_incomplete_file_exception(mesg)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def __str__(self):
        return _py_interop_comm.incomplete_file_exception___str__(self)
    __swig_destroy__ = _py_interop_comm.delete_incomplete_file_exception
    __del__ = lambda self: None
incomplete_file_exception_swigregister = _py_interop_comm.incomplete_file_exception_swigregister
incomplete_file_exception_swigregister(incomplete_file_exception)

class invalid_argument(interop.py_interop_run.base_exception):
    __swig_setmethods__ = {}
    for _s in [interop.py_interop_run.base_exception]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, invalid_argument, name, value)
    __swig_getmethods__ = {}
    for _s in [interop.py_interop_run.base_exception]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, invalid_argument, name)
    __repr__ = _swig_repr

    def __init__(self, mesg):
        this = _py_interop_comm.new_invalid_argument(mesg)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def __str__(self):
        return _py_interop_comm.invalid_argument___str__(self)
    __swig_destroy__ = _py_interop_comm.delete_invalid_argument
    __del__ = lambda self: None
invalid_argument_swigregister = _py_interop_comm.invalid_argument_swigregister
invalid_argument_swigregister(invalid_argument)

class paths(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, paths, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, paths, name)
    __repr__ = _swig_repr
    __swig_getmethods__["run_info"] = lambda x: _py_interop_comm.paths_run_info
    if _newclass:
        run_info = staticmethod(_py_interop_comm.paths_run_info)
    __swig_getmethods__["run_parameters"] = lambda x: _py_interop_comm.paths_run_parameters
    if _newclass:
        run_parameters = staticmethod(_py_interop_comm.paths_run_parameters)
    __swig_getmethods__["rta_config"] = lambda x: _py_interop_comm.paths_rta_config
    if _newclass:
        rta_config = staticmethod(_py_interop_comm.paths_rta_config)
    __swig_getmethods__["interop_filename"] = lambda x: _py_interop_comm.paths_interop_filename
    if _newclass:
        interop_filename = staticmethod(_py_interop_comm.paths_interop_filename)

    def __init__(self):
        this = _py_interop_comm.new_paths()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _py_interop_comm.delete_paths
    __del__ = lambda self: None
paths_swigregister = _py_interop_comm.paths_swigregister
paths_swigregister(paths)

def paths_run_info(*args):
    return _py_interop_comm.paths_run_info(*args)
paths_run_info = _py_interop_comm.paths_run_info

def paths_run_parameters(*args):
    return _py_interop_comm.paths_run_parameters(*args)
paths_run_parameters = _py_interop_comm.paths_run_parameters

def paths_rta_config(*args):
    return _py_interop_comm.paths_rta_config(*args)
paths_rta_config = _py_interop_comm.paths_rta_config

def paths_interop_filename(run_directory, prefix, suffix, cycle, use_out=True):
    return _py_interop_comm.paths_interop_filename(run_directory, prefix, suffix, cycle, use_out)
paths_interop_filename = _py_interop_comm.paths_interop_filename


def is_corrected_intensity_metric_deprecated(version):
    return _py_interop_comm.is_corrected_intensity_metric_deprecated(version)
is_corrected_intensity_metric_deprecated = _py_interop_comm.is_corrected_intensity_metric_deprecated

def is_error_metric_deprecated(version):
    return _py_interop_comm.is_error_metric_deprecated(version)
is_error_metric_deprecated = _py_interop_comm.is_error_metric_deprecated

def is_extended_tile_metric_deprecated(version):
    return _py_interop_comm.is_extended_tile_metric_deprecated(version)
is_extended_tile_metric_deprecated = _py_interop_comm.is_extended_tile_metric_deprecated

def is_extraction_metric_deprecated(version):
    return _py_interop_comm.is_extraction_metric_deprecated(version)
is_extraction_metric_deprecated = _py_interop_comm.is_extraction_metric_deprecated

def is_image_metric_deprecated(version):
    return _py_interop_comm.is_image_metric_deprecated(version)
is_image_metric_deprecated = _py_interop_comm.is_image_metric_deprecated

def is_q_metric_deprecated(version):
    return _py_interop_comm.is_q_metric_deprecated(version)
is_q_metric_deprecated = _py_interop_comm.is_q_metric_deprecated

def is_tile_metric_deprecated(version):
    return _py_interop_comm.is_tile_metric_deprecated(version)
is_tile_metric_deprecated = _py_interop_comm.is_tile_metric_deprecated

def is_index_metric_deprecated(version):
    return _py_interop_comm.is_index_metric_deprecated(version)
is_index_metric_deprecated = _py_interop_comm.is_index_metric_deprecated

def is_q_collapsed_metric_deprecated(version):
    return _py_interop_comm.is_q_collapsed_metric_deprecated(version)
is_q_collapsed_metric_deprecated = _py_interop_comm.is_q_collapsed_metric_deprecated

def compute_buffer_size(*args):
    return _py_interop_comm.compute_buffer_size(*args)
compute_buffer_size = _py_interop_comm.compute_buffer_size

def write_interop_to_buffer(*args):
    return _py_interop_comm.write_interop_to_buffer(*args)
write_interop_to_buffer = _py_interop_comm.write_interop_to_buffer

def read_interop_from_buffer(*args):
    return _py_interop_comm.read_interop_from_buffer(*args)
read_interop_from_buffer = _py_interop_comm.read_interop_from_buffer

def read_interop(*args):
    return _py_interop_comm.read_interop(*args)
read_interop = _py_interop_comm.read_interop

def write_interop(*args):
    return _py_interop_comm.write_interop(*args)
write_interop = _py_interop_comm.write_interop

def read_interop_by_cycle(*args):
    return _py_interop_comm.read_interop_by_cycle(*args)
read_interop_by_cycle = _py_interop_comm.read_interop_by_cycle

def is_q_by_lane_metric_deprecated(version):
    return _py_interop_comm.is_q_by_lane_metric_deprecated(version)
is_q_by_lane_metric_deprecated = _py_interop_comm.is_q_by_lane_metric_deprecated
# This file is compatible with both classic and new-style classes.


