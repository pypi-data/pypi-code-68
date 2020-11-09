# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['GroupPolicies']


class GroupPolicies(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 exclusive: Optional[pulumi.Input[bool]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages policies for an Identity Group for Vault. The [Identity secrets engine](https://www.vaultproject.io/docs/secrets/identity/index.html) is the identity management solution for Vault.

        ## Example Usage
        ### Exclusive Policies

        ```python
        import pulumi
        import pulumi_vault as vault

        internal = vault.identity.Group("internal",
            type="internal",
            external_policies=True,
            metadata={
                "version": "2",
            })
        policies = vault.identity.GroupPolicies("policies",
            policies=[
                "default",
                "test",
            ],
            exclusive=True,
            group_id=internal.id)
        ```
        ### Non-exclusive Policies

        ```python
        import pulumi
        import pulumi_vault as vault

        internal = vault.identity.Group("internal",
            type="internal",
            external_policies=True,
            metadata={
                "version": "2",
            })
        default = vault.identity.GroupPolicies("default",
            policies=[
                "default",
                "test",
            ],
            exclusive=False,
            group_id=internal.id)
        others = vault.identity.GroupPolicies("others",
            policies=["others"],
            exclusive=False,
            group_id=internal.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] exclusive: Defaults to `true`.
        :param pulumi.Input[str] group_id: Group ID to assign policies to.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policies: List of policies to assign to the group
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

            __props__['exclusive'] = exclusive
            if group_id is None:
                raise TypeError("Missing required property 'group_id'")
            __props__['group_id'] = group_id
            if policies is None:
                raise TypeError("Missing required property 'policies'")
            __props__['policies'] = policies
            __props__['group_name'] = None
        super(GroupPolicies, __self__).__init__(
            'vault:identity/groupPolicies:GroupPolicies',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            exclusive: Optional[pulumi.Input[bool]] = None,
            group_id: Optional[pulumi.Input[str]] = None,
            group_name: Optional[pulumi.Input[str]] = None,
            policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'GroupPolicies':
        """
        Get an existing GroupPolicies resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] exclusive: Defaults to `true`.
        :param pulumi.Input[str] group_id: Group ID to assign policies to.
        :param pulumi.Input[str] group_name: The name of the group that are assigned the policies.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policies: List of policies to assign to the group
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["exclusive"] = exclusive
        __props__["group_id"] = group_id
        __props__["group_name"] = group_name
        __props__["policies"] = policies
        return GroupPolicies(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def exclusive(self) -> pulumi.Output[Optional[bool]]:
        """
        Defaults to `true`.
        """
        return pulumi.get(self, "exclusive")

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Output[str]:
        """
        Group ID to assign policies to.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter(name="groupName")
    def group_name(self) -> pulumi.Output[str]:
        """
        The name of the group that are assigned the policies.
        """
        return pulumi.get(self, "group_name")

    @property
    @pulumi.getter
    def policies(self) -> pulumi.Output[Sequence[str]]:
        """
        List of policies to assign to the group
        """
        return pulumi.get(self, "policies")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

