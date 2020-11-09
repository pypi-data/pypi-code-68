# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _port_log
else:
    import _port_log

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _port_log.SWIG_PyInstanceMethod_New
_swig_new_static_method = _port_log.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import gphoto2.abilities_list
import gphoto2.camera
import gphoto2.context
import gphoto2.file
import gphoto2.filesys
import gphoto2.list
import gphoto2.port_info_list
import gphoto2.result
import gphoto2.version
import gphoto2.widget
class LogFuncItem(object):
    r"""Proxy of C LogFuncItem struct."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _port_log.delete_LogFuncItem

# Register LogFuncItem in _port_log:
_port_log.LogFuncItem_swigregister(LogFuncItem)


import logging
import sys

def _gphoto2_logger_cb(level, domain, msg, data):
    log_func, mapping = data
    if sys.version_info[0] >= 3:
# decode bytes to str
        if domain:
            domain = domain.decode(errors='replace')
        if msg:
            msg = msg.decode(errors='replace')
    if level in mapping:
        log_func(mapping[level], '(%s) %s', domain, msg)
    else:
        log_func(logging.ERROR, '%d (%s) %s', level, domain, msg)

def use_python_logging(mapping={}):
    """Install a callback to receive gphoto2 errors and forward them
    to Python's logging system.

    The return value is a tuple containing an error code and a Python object
    containing details of the callback. Deleting this object will uninstall
    the callback.

    Parameters
    ----------
    * `mapping` :
        a dictionary mapping any of the four gphoto2 logging severity
        levels to a Python logging level. Note that anything below Python
        DEBUG level will not be forwarded.

    Returns
    -------
    a tuple containing an id or error code and a callback reference object.

    """
    full_mapping = {
        GP_LOG_ERROR   : logging.WARNING,
        GP_LOG_VERBOSE : logging.INFO,
        GP_LOG_DEBUG   : logging.DEBUG,
        GP_LOG_DATA    : logging.DEBUG - 5,
        }
    full_mapping.update(mapping)
    log_func = logging.getLogger('gphoto2').log
    for level in (GP_LOG_DATA, GP_LOG_DEBUG, GP_LOG_VERBOSE, GP_LOG_ERROR):
        if full_mapping[level] >= logging.DEBUG:
            break
    return gp_log_add_func(level, _gphoto2_logger_cb, (log_func, full_mapping))

GP_LOG_ERROR = _port_log.GP_LOG_ERROR

GP_LOG_VERBOSE = _port_log.GP_LOG_VERBOSE

GP_LOG_DEBUG = _port_log.GP_LOG_DEBUG

GP_LOG_DATA = _port_log.GP_LOG_DATA

gp_log_add_func = _port_log.gp_log_add_func
gp_log = _port_log.gp_log


