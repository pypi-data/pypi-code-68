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
    from . import _widget
else:
    import _widget

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _widget.SWIG_PyInstanceMethod_New
_swig_new_static_method = _widget.SWIG_PyStaticMethod_New

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
import gphoto2.port_log
import gphoto2.result
import gphoto2.version
gp_widget_set_value = _widget.gp_widget_set_value
gp_widget_get_value = _widget.gp_widget_get_value
class CameraWidgetChildIter(object):
    r"""Proxy of C CameraWidgetChildIter struct."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __iter__(self):
        return self
    def next(self):
        return self.__next__()

    __next__ = _swig_new_instance_method(_widget.CameraWidgetChildIter___next__)
    __swig_destroy__ = _widget.delete_CameraWidgetChildIter

# Register CameraWidgetChildIter in _widget:
_widget.CameraWidgetChildIter_swigregister(CameraWidgetChildIter)

gp_widget_get_children = _widget.gp_widget_get_children
class CameraWidgetChoiceIter(object):
    r"""Proxy of C CameraWidgetChoiceIter struct."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __iter__(self):
        return self
    def next(self):
        return self.__next__()

    __next__ = _swig_new_instance_method(_widget.CameraWidgetChoiceIter___next__)
    __swig_destroy__ = _widget.delete_CameraWidgetChoiceIter

# Register CameraWidgetChoiceIter in _widget:
_widget.CameraWidgetChoiceIter_swigregister(CameraWidgetChoiceIter)

gp_widget_get_choices = _widget.gp_widget_get_choices
class CameraWidget(object):
    r"""
    CameraWidget:  

    The internals of the CameraWidget are only visible to gphoto2. You can
    only access them using the functions provided by gphoto2.
    """

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    count_children = _swig_new_instance_method(_widget.CameraWidget_count_children)
    get_child = _swig_new_instance_method(_widget.CameraWidget_get_child)
    get_children = _swig_new_instance_method(_widget.CameraWidget_get_children)
    get_child_by_label = _swig_new_instance_method(_widget.CameraWidget_get_child_by_label)
    get_child_by_id = _swig_new_instance_method(_widget.CameraWidget_get_child_by_id)
    get_child_by_name = _swig_new_instance_method(_widget.CameraWidget_get_child_by_name)
    get_root = _swig_new_instance_method(_widget.CameraWidget_get_root)
    get_parent = _swig_new_instance_method(_widget.CameraWidget_get_parent)
    set_value = _swig_new_instance_method(_widget.CameraWidget_set_value)
    get_value = _swig_new_instance_method(_widget.CameraWidget_get_value)
    set_name = _swig_new_instance_method(_widget.CameraWidget_set_name)
    get_name = _swig_new_instance_method(_widget.CameraWidget_get_name)
    set_info = _swig_new_instance_method(_widget.CameraWidget_set_info)
    get_info = _swig_new_instance_method(_widget.CameraWidget_get_info)
    get_id = _swig_new_instance_method(_widget.CameraWidget_get_id)
    get_type = _swig_new_instance_method(_widget.CameraWidget_get_type)
    get_label = _swig_new_instance_method(_widget.CameraWidget_get_label)
    set_range = _swig_new_instance_method(_widget.CameraWidget_set_range)
    get_range = _swig_new_instance_method(_widget.CameraWidget_get_range)
    add_choice = _swig_new_instance_method(_widget.CameraWidget_add_choice)
    count_choices = _swig_new_instance_method(_widget.CameraWidget_count_choices)
    get_choices = _swig_new_instance_method(_widget.CameraWidget_get_choices)
    get_choice = _swig_new_instance_method(_widget.CameraWidget_get_choice)
    changed = _swig_new_instance_method(_widget.CameraWidget_changed)
    set_changed = _swig_new_instance_method(_widget.CameraWidget_set_changed)
    set_readonly = _swig_new_instance_method(_widget.CameraWidget_set_readonly)
    get_readonly = _swig_new_instance_method(_widget.CameraWidget_get_readonly)
    __swig_destroy__ = _widget.delete_CameraWidget

# Register CameraWidget in _widget:
_widget.CameraWidget_swigregister(CameraWidget)

GP_WIDGET_WINDOW = _widget.GP_WIDGET_WINDOW

GP_WIDGET_SECTION = _widget.GP_WIDGET_SECTION

GP_WIDGET_TEXT = _widget.GP_WIDGET_TEXT

GP_WIDGET_RANGE = _widget.GP_WIDGET_RANGE

GP_WIDGET_TOGGLE = _widget.GP_WIDGET_TOGGLE

GP_WIDGET_RADIO = _widget.GP_WIDGET_RADIO

GP_WIDGET_MENU = _widget.GP_WIDGET_MENU

GP_WIDGET_BUTTON = _widget.GP_WIDGET_BUTTON

GP_WIDGET_DATE = _widget.GP_WIDGET_DATE

gp_widget_append = _widget.gp_widget_append
gp_widget_prepend = _widget.gp_widget_prepend
gp_widget_count_children = _widget.gp_widget_count_children
gp_widget_get_child = _widget.gp_widget_get_child
gp_widget_get_child_by_label = _widget.gp_widget_get_child_by_label
gp_widget_get_child_by_id = _widget.gp_widget_get_child_by_id
gp_widget_get_child_by_name = _widget.gp_widget_get_child_by_name
gp_widget_get_root = _widget.gp_widget_get_root
gp_widget_get_parent = _widget.gp_widget_get_parent
gp_widget_set_name = _widget.gp_widget_set_name
gp_widget_get_name = _widget.gp_widget_get_name
gp_widget_set_info = _widget.gp_widget_set_info
gp_widget_get_info = _widget.gp_widget_get_info
gp_widget_get_id = _widget.gp_widget_get_id
gp_widget_get_type = _widget.gp_widget_get_type
gp_widget_get_label = _widget.gp_widget_get_label
gp_widget_set_range = _widget.gp_widget_set_range
gp_widget_get_range = _widget.gp_widget_get_range
gp_widget_add_choice = _widget.gp_widget_add_choice
gp_widget_count_choices = _widget.gp_widget_count_choices
gp_widget_get_choice = _widget.gp_widget_get_choice
gp_widget_changed = _widget.gp_widget_changed
gp_widget_set_changed = _widget.gp_widget_set_changed
gp_widget_set_readonly = _widget.gp_widget_set_readonly
gp_widget_get_readonly = _widget.gp_widget_get_readonly


