# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['DomainGroup']


class DomainGroup(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_group_name: Optional[pulumi.Input[str]] = None,
                 group_name: Optional[pulumi.Input[str]] = None,
                 lang: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Alidns Domain Group resource. For information about Alidns Domain Group and how to use it, see [What is Resource Alidns Domain Group](https://www.alibabacloud.com/help/en/doc-detail/29762.htm).

        > **NOTE:** Available in v1.84.0+.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        # Add a new Alinds Domain Group.
        example = alicloud.dns.DomainGroup("example", domain_group_name="tf-testDG")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_group_name: Name of the domain group.
        :param pulumi.Input[str] group_name: Replaced by `domain_group_name` after version 1.97.0.
        :param pulumi.Input[str] lang: User language.
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

            __props__['domain_group_name'] = domain_group_name
            if group_name is not None:
                warnings.warn("Field 'group_name' has been deprecated from version 1.97.0. Use 'domain_group_name' instead.", DeprecationWarning)
                pulumi.log.warn("group_name is deprecated: Field 'group_name' has been deprecated from version 1.97.0. Use 'domain_group_name' instead.")
            __props__['group_name'] = group_name
            __props__['lang'] = lang
        super(DomainGroup, __self__).__init__(
            'alicloud:dns/domainGroup:DomainGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            domain_group_name: Optional[pulumi.Input[str]] = None,
            group_name: Optional[pulumi.Input[str]] = None,
            lang: Optional[pulumi.Input[str]] = None) -> 'DomainGroup':
        """
        Get an existing DomainGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_group_name: Name of the domain group.
        :param pulumi.Input[str] group_name: Replaced by `domain_group_name` after version 1.97.0.
        :param pulumi.Input[str] lang: User language.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["domain_group_name"] = domain_group_name
        __props__["group_name"] = group_name
        __props__["lang"] = lang
        return DomainGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="domainGroupName")
    def domain_group_name(self) -> pulumi.Output[str]:
        """
        Name of the domain group.
        """
        return pulumi.get(self, "domain_group_name")

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> pulumi.Output[str]:
        """
        Replaced by `domain_group_name` after version 1.97.0.
        """
        return pulumi.get(self, "group_name")

    @property
    @pulumi.getter
    def lang(self) -> pulumi.Output[Optional[str]]:
        """
        User language.
        """
        return pulumi.get(self, "lang")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

