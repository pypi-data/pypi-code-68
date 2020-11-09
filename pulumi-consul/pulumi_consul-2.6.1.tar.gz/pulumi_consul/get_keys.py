# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = [
    'GetKeysResult',
    'AwaitableGetKeysResult',
    'get_keys',
]

@pulumi.output_type
class GetKeysResult:
    """
    A collection of values returned by getKeys.
    """
    def __init__(__self__, datacenter=None, id=None, keys=None, namespace=None, token=None, var=None):
        if datacenter and not isinstance(datacenter, str):
            raise TypeError("Expected argument 'datacenter' to be a str")
        pulumi.set(__self__, "datacenter", datacenter)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if keys and not isinstance(keys, list):
            raise TypeError("Expected argument 'keys' to be a list")
        pulumi.set(__self__, "keys", keys)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)
        if token and not isinstance(token, str):
            raise TypeError("Expected argument 'token' to be a str")
        pulumi.set(__self__, "token", token)
        if var and not isinstance(var, dict):
            raise TypeError("Expected argument 'var' to be a dict")
        pulumi.set(__self__, "var", var)

    @property
    @pulumi.getter
    def datacenter(self) -> str:
        """
        The datacenter the keys are being read from.
        * `var.<name>` - For each name given, the corresponding attribute
        has the value of the key.
        """
        return pulumi.get(self, "datacenter")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def keys(self) -> Optional[Sequence['outputs.GetKeysKeyResult']]:
        return pulumi.get(self, "keys")

    @property
    @pulumi.getter
    def namespace(self) -> Optional[str]:
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter
    def token(self) -> Optional[str]:
        return pulumi.get(self, "token")

    @property
    @pulumi.getter
    def var(self) -> Mapping[str, str]:
        return pulumi.get(self, "var")


class AwaitableGetKeysResult(GetKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKeysResult(
            datacenter=self.datacenter,
            id=self.id,
            keys=self.keys,
            namespace=self.namespace,
            token=self.token,
            var=self.var)


def get_keys(datacenter: Optional[str] = None,
             keys: Optional[Sequence[pulumi.InputType['GetKeysKeyArgs']]] = None,
             namespace: Optional[str] = None,
             token: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKeysResult:
    """
    The `Keys` resource reads values from the Consul key/value store.
    This is a powerful way dynamically set values in templates.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws
    import pulumi_consul as consul

    app_keys = consul.get_keys(datacenter="nyc1",
        keys=[consul.GetKeysKeyArgs(
            default="ami-1234",
            name="ami",
            path="service/app/launch_ami",
        )],
        token="abcd")
    # Start our instance with the dynamic ami value
    app_instance = aws.ec2.Instance("appInstance", ami=app_keys.var["ami"])
    ```


    :param str datacenter: The datacenter to use. This overrides the
           agent's default datacenter and the datacenter in the provider setup.
    :param Sequence[pulumi.InputType['GetKeysKeyArgs']] keys: Specifies a key in Consul to be read. Supported
           values documented below. Multiple blocks supported.
    :param str namespace: The namespace to lookup the keys.
    :param str token: The ACL token to use. This overrides the
           token that the agent provides by default.
    """
    __args__ = dict()
    __args__['datacenter'] = datacenter
    __args__['keys'] = keys
    __args__['namespace'] = namespace
    __args__['token'] = token
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('consul:index/getKeys:getKeys', __args__, opts=opts, typ=GetKeysResult).value

    return AwaitableGetKeysResult(
        datacenter=__ret__.datacenter,
        id=__ret__.id,
        keys=__ret__.keys,
        namespace=__ret__.namespace,
        token=__ret__.token,
        var=__ret__.var)
