# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['CertificateAuthority']


class CertificateAuthority(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 connect_provider: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The `CertificateAuthority` resource can be used to manage the configuration of
        the Certificate Authority used by [Consul Connect](https://www.consul.io/docs/connect/ca).

        ## Example Usage

        Use the built-in CA with specific TTL:

        ```python
        import pulumi
        import pulumi_consul as consul

        connect = consul.CertificateAuthority("connect",
            config={
                "IntermediateCertTTL": "8760h",
                "LeafCertTTL": "24h",
                "RotationPeriod": "2160h",
            },
            connect_provider="consul")
        ```

        Use Vault to manage and sign certificates:

        ```python
        import pulumi
        import pulumi_consul as consul

        connect = consul.CertificateAuthority("connect",
            config={
                "address": "http://localhost:8200",
                "intermediate_pki_path": "connect-intermediate",
                "root_pki_path": "connect-root",
                "token": "...",
            },
            connect_provider="vault")
        ```

        Use the [AWS Certificate Manager Private Certificate Authority](https://aws.amazon.com/certificate-manager/private-certificate-authority/):

        ```python
        import pulumi
        import pulumi_consul as consul

        connect = consul.CertificateAuthority("connect",
            config={
                "existing_arn": "arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-123456789012",
            },
            connect_provider="aws-pca")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] config: The raw configuration to use for the chosen provider.
        :param pulumi.Input[str] connect_provider: Specifies the CA provider type to use.
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

            if config is None:
                raise TypeError("Missing required property 'config'")
            __props__['config'] = config
            if connect_provider is None:
                raise TypeError("Missing required property 'connect_provider'")
            __props__['connect_provider'] = connect_provider
        super(CertificateAuthority, __self__).__init__(
            'consul:index/certificateAuthority:CertificateAuthority',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            config: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            connect_provider: Optional[pulumi.Input[str]] = None) -> 'CertificateAuthority':
        """
        Get an existing CertificateAuthority resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] config: The raw configuration to use for the chosen provider.
        :param pulumi.Input[str] connect_provider: Specifies the CA provider type to use.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["config"] = config
        __props__["connect_provider"] = connect_provider
        return CertificateAuthority(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def config(self) -> pulumi.Output[Mapping[str, str]]:
        """
        The raw configuration to use for the chosen provider.
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter(name="connectProvider")
    def connect_provider(self) -> pulumi.Output[str]:
        """
        Specifies the CA provider type to use.
        """
        return pulumi.get(self, "connect_provider")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

