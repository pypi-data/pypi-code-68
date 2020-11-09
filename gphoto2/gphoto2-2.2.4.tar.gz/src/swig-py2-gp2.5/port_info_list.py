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
    from . import _port_info_list
else:
    import _port_info_list

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _port_info_list.SWIG_PyInstanceMethod_New
_swig_new_static_method = _port_info_list.SWIG_PyStaticMethod_New

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
import gphoto2.port_log
import gphoto2.result
import gphoto2.version
import gphoto2.widget
class _GPPortInfo(object):
    r"""Proxy of C _GPPortInfo struct."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    get_name = _swig_new_instance_method(_port_info_list._GPPortInfo_get_name)
    get_path = _swig_new_instance_method(_port_info_list._GPPortInfo_get_path)
    get_type = _swig_new_instance_method(_port_info_list._GPPortInfo_get_type)
    __swig_destroy__ = _port_info_list.delete__GPPortInfo

# Register _GPPortInfo in _port_info_list:
_port_info_list._GPPortInfo_swigregister(_GPPortInfo)

class PortInfoList(object):
    r"""Proxy of C _GPPortInfoList struct."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __len__ = _swig_new_instance_method(_port_info_list.PortInfoList___len__)
    __getitem__ = _swig_new_instance_method(_port_info_list.PortInfoList___getitem__)
    append = _swig_new_instance_method(_port_info_list.PortInfoList_append)
    load = _swig_new_instance_method(_port_info_list.PortInfoList_load)
    count = _swig_new_instance_method(_port_info_list.PortInfoList_count)
    lookup_path = _swig_new_instance_method(_port_info_list.PortInfoList_lookup_path)
    lookup_name = _swig_new_instance_method(_port_info_list.PortInfoList_lookup_name)
    get_info = _swig_new_instance_method(_port_info_list.PortInfoList_get_info)

    def __init__(self):
        r"""__init__(self) -> PortInfoList"""
        _port_info_list.PortInfoList_swiginit(self, _port_info_list.new_PortInfoList())
    __swig_destroy__ = _port_info_list.delete_PortInfoList

# Register PortInfoList in _port_info_list:
_port_info_list.PortInfoList_swigregister(PortInfoList)

GP_PORT_NONE = _port_info_list.GP_PORT_NONE

GP_PORT_SERIAL = _port_info_list.GP_PORT_SERIAL

GP_PORT_USB = _port_info_list.GP_PORT_USB

GP_PORT_DISK = _port_info_list.GP_PORT_DISK

GP_PORT_PTPIP = _port_info_list.GP_PORT_PTPIP

GP_PORT_USB_DISK_DIRECT = _port_info_list.GP_PORT_USB_DISK_DIRECT

GP_PORT_USB_SCSI = _port_info_list.GP_PORT_USB_SCSI

GP_PORT_IP = _port_info_list.GP_PORT_IP

gp_port_info_get_name = _port_info_list.gp_port_info_get_name
gp_port_info_get_path = _port_info_list.gp_port_info_get_path
gp_port_info_get_type = _port_info_list.gp_port_info_get_type
gp_port_info_list_new = _port_info_list.gp_port_info_list_new
gp_port_info_list_append = _port_info_list.gp_port_info_list_append
gp_port_info_list_load = _port_info_list.gp_port_info_list_load
gp_port_info_list_count = _port_info_list.gp_port_info_list_count
gp_port_info_list_lookup_path = _port_info_list.gp_port_info_list_lookup_path
gp_port_info_list_lookup_name = _port_info_list.gp_port_info_list_lookup_name
gp_port_info_list_get_info = _port_info_list.gp_port_info_list_get_info
gp_port_message_codeset = _port_info_list.gp_port_message_codeset


