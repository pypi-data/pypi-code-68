# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['OidcKey']


class OidcKey(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 algorithm: Optional[pulumi.Input[str]] = None,
                 allowed_client_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rotation_period: Optional[pulumi.Input[int]] = None,
                 verification_ttl: Optional[pulumi.Input[int]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Create a OidcKey resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] algorithm: Signing algorithm to use. Signing algorithm to use.
               Allowed values are: RS256 (default), RS384, RS512, ES256, ES384, ES512, EdDSA.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_client_ids: Array of role client ids allowed to use this key for signing. If empty, no roles are allowed. If "*", all roles are
               allowed.
        :param pulumi.Input[str] name: Name of the OIDC Key to create.
        :param pulumi.Input[int] rotation_period: How often to generate a new signing key in number of seconds
        :param pulumi.Input[int] verification_ttl: "Controls how long the public portion of a signing key will be
               available for verification after being rotated in seconds.
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

            __props__['algorithm'] = algorithm
            __props__['allowed_client_ids'] = allowed_client_ids
            __props__['name'] = name
            __props__['rotation_period'] = rotation_period
            __props__['verification_ttl'] = verification_ttl
        super(OidcKey, __self__).__init__(
            'vault:identity/oidcKey:OidcKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            algorithm: Optional[pulumi.Input[str]] = None,
            allowed_client_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            rotation_period: Optional[pulumi.Input[int]] = None,
            verification_ttl: Optional[pulumi.Input[int]] = None) -> 'OidcKey':
        """
        Get an existing OidcKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] algorithm: Signing algorithm to use. Signing algorithm to use.
               Allowed values are: RS256 (default), RS384, RS512, ES256, ES384, ES512, EdDSA.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_client_ids: Array of role client ids allowed to use this key for signing. If empty, no roles are allowed. If "*", all roles are
               allowed.
        :param pulumi.Input[str] name: Name of the OIDC Key to create.
        :param pulumi.Input[int] rotation_period: How often to generate a new signing key in number of seconds
        :param pulumi.Input[int] verification_ttl: "Controls how long the public portion of a signing key will be
               available for verification after being rotated in seconds.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["algorithm"] = algorithm
        __props__["allowed_client_ids"] = allowed_client_ids
        __props__["name"] = name
        __props__["rotation_period"] = rotation_period
        __props__["verification_ttl"] = verification_ttl
        return OidcKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def algorithm(self) -> pulumi.Output[Optional[str]]:
        """
        Signing algorithm to use. Signing algorithm to use.
        Allowed values are: RS256 (default), RS384, RS512, ES256, ES384, ES512, EdDSA.
        """
        return pulumi.get(self, "algorithm")

    @property
    @pulumi.getter(name="allowedClientIds")
    def allowed_client_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        Array of role client ids allowed to use this key for signing. If empty, no roles are allowed. If "*", all roles are
        allowed.
        """
        return pulumi.get(self, "allowed_client_ids")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the OIDC Key to create.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="rotationPeriod")
    def rotation_period(self) -> pulumi.Output[Optional[int]]:
        """
        How often to generate a new signing key in number of seconds
        """
        return pulumi.get(self, "rotation_period")

    @property
    @pulumi.getter(name="verificationTtl")
    def verification_ttl(self) -> pulumi.Output[Optional[int]]:
        """
        "Controls how long the public portion of a signing key will be
        available for verification after being rotated in seconds.
        """
        return pulumi.get(self, "verification_ttl")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

