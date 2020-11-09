# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['Hook']


class Hook(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth: Optional[pulumi.Input[pulumi.InputType['HookAuthArgs']]] = None,
                 channel: Optional[pulumi.Input[pulumi.InputType['HookChannelArgs']]] = None,
                 headers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HookHeaderArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates an inline hook.

        This resource allows you to create and configure an inline hook.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.inline.Hook("example",
            auth=okta.inline.HookAuthArgs(
                key="Authorization",
                type="HEADER",
                value="secret",
            ),
            channel=okta.inline.HookChannelArgs(
                method="POST",
                uri="https://example.com/test",
                version="1.0.0",
            ),
            type="com.okta.oauth2.tokens.transform",
            version="1.0.0")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['HookAuthArgs']] auth: Authentication required for inline hook request.
        :param pulumi.Input[pulumi.InputType['HookChannelArgs']] channel: Details of the endpoint the inline hook will hit.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HookHeaderArgs']]]] headers: Map of headers to send along in inline hook request.
        :param pulumi.Input[str] name: The inline hook display name.
        :param pulumi.Input[str] type: The type of hook to trigger. Currently only `"HTTP"` is supported.
        :param pulumi.Input[str] version: The version of the endpoint.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['auth'] = auth
            __props__['channel'] = channel
            __props__['headers'] = headers
            __props__['name'] = name
            __props__['status'] = status
            if type is None:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
            if version is None:
                raise TypeError("Missing required property 'version'")
            __props__['version'] = version
        super(Hook, __self__).__init__(
            'okta:inline/hook:Hook',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            auth: Optional[pulumi.Input[pulumi.InputType['HookAuthArgs']]] = None,
            channel: Optional[pulumi.Input[pulumi.InputType['HookChannelArgs']]] = None,
            headers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HookHeaderArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[str]] = None) -> 'Hook':
        """
        Get an existing Hook resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['HookAuthArgs']] auth: Authentication required for inline hook request.
        :param pulumi.Input[pulumi.InputType['HookChannelArgs']] channel: Details of the endpoint the inline hook will hit.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HookHeaderArgs']]]] headers: Map of headers to send along in inline hook request.
        :param pulumi.Input[str] name: The inline hook display name.
        :param pulumi.Input[str] type: The type of hook to trigger. Currently only `"HTTP"` is supported.
        :param pulumi.Input[str] version: The version of the endpoint.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["auth"] = auth
        __props__["channel"] = channel
        __props__["headers"] = headers
        __props__["name"] = name
        __props__["status"] = status
        __props__["type"] = type
        __props__["version"] = version
        return Hook(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def auth(self) -> pulumi.Output[Optional['outputs.HookAuth']]:
        """
        Authentication required for inline hook request.
        """
        return pulumi.get(self, "auth")

    @property
    @pulumi.getter
    def channel(self) -> pulumi.Output[Optional['outputs.HookChannel']]:
        """
        Details of the endpoint the inline hook will hit.
        """
        return pulumi.get(self, "channel")

    @property
    @pulumi.getter
    def headers(self) -> pulumi.Output[Optional[Sequence['outputs.HookHeader']]]:
        """
        Map of headers to send along in inline hook request.
        """
        return pulumi.get(self, "headers")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The inline hook display name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of hook to trigger. Currently only `"HTTP"` is supported.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        The version of the endpoint.
        """
        return pulumi.get(self, "version")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

