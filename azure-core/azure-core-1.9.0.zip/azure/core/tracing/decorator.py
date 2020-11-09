# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# --------------------------------------------------------------------------
"""The decorator to apply if you want the given function traced."""

import functools

from typing import overload

from .common import change_context, get_function_and_class_name
from ..settings import settings

try:
    from typing import TYPE_CHECKING
except ImportError:
    TYPE_CHECKING = False

if TYPE_CHECKING:
    from typing import Callable, Dict, Optional, Any, TypeVar

    T = TypeVar("T")


@overload
def distributed_trace(__func):
    # type: (Callable[..., T]) -> Callable[..., T]
    pass


@overload
def distributed_trace(**kwargs):  # pylint:disable=function-redefined,unused-argument
    # type: (**Any) -> Callable[[Callable[..., T]], Callable[..., T]]
    pass


def distributed_trace(  # pylint:disable=function-redefined
    __func=None,  # type: Callable[..., T]
    **kwargs  # type: Any
):
    """Decorator to apply to function to get traced automatically.

    Span will use the func name or "name_of_span".

    :param callable func: A function to decorate
    :param str name_of_span: The span name to replace func name if necessary
    """
    name_of_span = kwargs.pop("name_of_span", None)
    tracing_attributes = kwargs.pop("tracing_attributes", {})

    def decorator(func):
        # type: (Callable[..., T]) -> Callable[..., T]

        @functools.wraps(func)
        def wrapper_use_tracer(*args, **kwargs):
            # type: (*Any, **Any) -> T
            merge_span = kwargs.pop("merge_span", False)
            passed_in_parent = kwargs.pop("parent_span", None)

            span_impl_type = settings.tracing_implementation()
            if span_impl_type is None:
                return func(*args, **kwargs)

            # Merge span is parameter is set, but only if no explicit parent are passed
            if merge_span and not passed_in_parent:
                return func(*args, **kwargs)

            with change_context(passed_in_parent):
                name = name_of_span or get_function_and_class_name(func, *args)
                with span_impl_type(name=name) as span:
                    for key, value in tracing_attributes.items():
                        span.add_attribute(key, value)
                    return func(*args, **kwargs)

        return wrapper_use_tracer

    return decorator if __func is None else decorator(__func)
