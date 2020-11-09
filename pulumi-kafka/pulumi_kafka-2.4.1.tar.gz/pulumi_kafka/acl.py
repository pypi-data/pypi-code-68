# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['Acl']


class Acl(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 acl_host: Optional[pulumi.Input[str]] = None,
                 acl_operation: Optional[pulumi.Input[str]] = None,
                 acl_permission_type: Optional[pulumi.Input[str]] = None,
                 acl_principal: Optional[pulumi.Input[str]] = None,
                 acl_resource_name: Optional[pulumi.Input[str]] = None,
                 acl_resource_type: Optional[pulumi.Input[str]] = None,
                 resource_pattern_type_filter: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Create a Acl resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] acl_resource_name: The name of the resource
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

            if acl_host is None:
                raise TypeError("Missing required property 'acl_host'")
            __props__['acl_host'] = acl_host
            if acl_operation is None:
                raise TypeError("Missing required property 'acl_operation'")
            __props__['acl_operation'] = acl_operation
            if acl_permission_type is None:
                raise TypeError("Missing required property 'acl_permission_type'")
            __props__['acl_permission_type'] = acl_permission_type
            if acl_principal is None:
                raise TypeError("Missing required property 'acl_principal'")
            __props__['acl_principal'] = acl_principal
            if acl_resource_name is None:
                raise TypeError("Missing required property 'acl_resource_name'")
            __props__['acl_resource_name'] = acl_resource_name
            if acl_resource_type is None:
                raise TypeError("Missing required property 'acl_resource_type'")
            __props__['acl_resource_type'] = acl_resource_type
            __props__['resource_pattern_type_filter'] = resource_pattern_type_filter
        super(Acl, __self__).__init__(
            'kafka:index/acl:Acl',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            acl_host: Optional[pulumi.Input[str]] = None,
            acl_operation: Optional[pulumi.Input[str]] = None,
            acl_permission_type: Optional[pulumi.Input[str]] = None,
            acl_principal: Optional[pulumi.Input[str]] = None,
            acl_resource_name: Optional[pulumi.Input[str]] = None,
            acl_resource_type: Optional[pulumi.Input[str]] = None,
            resource_pattern_type_filter: Optional[pulumi.Input[str]] = None) -> 'Acl':
        """
        Get an existing Acl resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] acl_resource_name: The name of the resource
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["acl_host"] = acl_host
        __props__["acl_operation"] = acl_operation
        __props__["acl_permission_type"] = acl_permission_type
        __props__["acl_principal"] = acl_principal
        __props__["acl_resource_name"] = acl_resource_name
        __props__["acl_resource_type"] = acl_resource_type
        __props__["resource_pattern_type_filter"] = resource_pattern_type_filter
        return Acl(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="aclHost")
    def acl_host(self) -> pulumi.Output[str]:
        return pulumi.get(self, "acl_host")

    @property
    @pulumi.getter(name="aclOperation")
    def acl_operation(self) -> pulumi.Output[str]:
        return pulumi.get(self, "acl_operation")

    @property
    @pulumi.getter(name="aclPermissionType")
    def acl_permission_type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "acl_permission_type")

    @property
    @pulumi.getter(name="aclPrincipal")
    def acl_principal(self) -> pulumi.Output[str]:
        return pulumi.get(self, "acl_principal")

    @property
    @pulumi.getter(name="aclResourceName")
    def acl_resource_name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "acl_resource_name")

    @property
    @pulumi.getter(name="aclResourceType")
    def acl_resource_type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "acl_resource_type")

    @property
    @pulumi.getter(name="resourcePatternTypeFilter")
    def resource_pattern_type_filter(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "resource_pattern_type_filter")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

