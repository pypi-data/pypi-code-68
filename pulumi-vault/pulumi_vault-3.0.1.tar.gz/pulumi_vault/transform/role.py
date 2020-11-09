# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Role']


class Role(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 transformations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        This resource supports the "/transform/role/{name}" Vault endpoint.

        It creates or updates the role with the given name. If a role with the name does not exist, it will be created.
        If the role exists, it will be updated with the new attributes.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_vault as vault

        mount_transform = vault.Mount("mountTransform",
            path="transform",
            type="transform")
        test = vault.transform.Role("test",
            path=mount_transform.path,
            transformations=["ccn-fpe"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the role.
        :param pulumi.Input[str] path: Path to where the back-end is mounted within Vault.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] transformations: A comma separated string or slice of transformations to use.
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

            __props__['name'] = name
            if path is None:
                raise TypeError("Missing required property 'path'")
            __props__['path'] = path
            __props__['transformations'] = transformations
        super(Role, __self__).__init__(
            'vault:transform/role:Role',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            path: Optional[pulumi.Input[str]] = None,
            transformations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'Role':
        """
        Get an existing Role resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the role.
        :param pulumi.Input[str] path: Path to where the back-end is mounted within Vault.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] transformations: A comma separated string or slice of transformations to use.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["name"] = name
        __props__["path"] = path
        __props__["transformations"] = transformations
        return Role(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the role.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def path(self) -> pulumi.Output[str]:
        """
        Path to where the back-end is mounted within Vault.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def transformations(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A comma separated string or slice of transformations to use.
        """
        return pulumi.get(self, "transformations")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

