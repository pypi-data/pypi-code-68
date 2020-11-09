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
    'GetAclTokenResult',
    'AwaitableGetAclTokenResult',
    'get_acl_token',
]

@pulumi.output_type
class GetAclTokenResult:
    """
    A collection of values returned by getAclToken.
    """
    def __init__(__self__, accessor_id=None, description=None, id=None, local=None, namespace=None, policies=None):
        if accessor_id and not isinstance(accessor_id, str):
            raise TypeError("Expected argument 'accessor_id' to be a str")
        pulumi.set(__self__, "accessor_id", accessor_id)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if local and not isinstance(local, bool):
            raise TypeError("Expected argument 'local' to be a bool")
        pulumi.set(__self__, "local", local)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)
        if policies and not isinstance(policies, list):
            raise TypeError("Expected argument 'policies' to be a list")
        pulumi.set(__self__, "policies", policies)

    @property
    @pulumi.getter(name="accessorId")
    def accessor_id(self) -> str:
        return pulumi.get(self, "accessor_id")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the ACL token.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def local(self) -> Optional[bool]:
        """
        Whether the ACL token is local to the datacenter it was created within.
        """
        return pulumi.get(self, "local")

    @property
    @pulumi.getter
    def namespace(self) -> Optional[str]:
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter
    def policies(self) -> Optional[Sequence['outputs.GetAclTokenPolicyResult']]:
        """
        A list of policies associated with the ACL token. Each entry has
        an `id` and a `name` attribute.
        """
        return pulumi.get(self, "policies")


class AwaitableGetAclTokenResult(GetAclTokenResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAclTokenResult(
            accessor_id=self.accessor_id,
            description=self.description,
            id=self.id,
            local=self.local,
            namespace=self.namespace,
            policies=self.policies)


def get_acl_token(accessor_id: Optional[str] = None,
                  description: Optional[str] = None,
                  local: Optional[bool] = None,
                  namespace: Optional[str] = None,
                  policies: Optional[Sequence[pulumi.InputType['GetAclTokenPolicyArgs']]] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAclTokenResult:
    """
    The `AclToken` data source returns the information related to the
    `AclToken` resource with the exception of its secret ID.

    If you want to get the secret ID associated with a token, use the
    [`getAclTokenSecretId` data source](https://www.terraform.io/docs/providers/consul/d/acl_token_secret_id.html).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_consul as consul

    test = consul.get_acl_token(accessor_id="00000000-0000-0000-0000-000000000002")
    pulumi.export("consulAclPolicies", test.policies)
    ```


    :param str accessor_id: The accessor ID of the ACL token.
    :param str description: The description of the ACL token.
    :param bool local: Whether the ACL token is local to the datacenter it was created within.
    :param str namespace: The namespace to lookup the ACL token.
    :param Sequence[pulumi.InputType['GetAclTokenPolicyArgs']] policies: A list of policies associated with the ACL token. Each entry has
           an `id` and a `name` attribute.
    """
    __args__ = dict()
    __args__['accessorId'] = accessor_id
    __args__['description'] = description
    __args__['local'] = local
    __args__['namespace'] = namespace
    __args__['policies'] = policies
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('consul:index/getAclToken:getAclToken', __args__, opts=opts, typ=GetAclTokenResult).value

    return AwaitableGetAclTokenResult(
        accessor_id=__ret__.accessor_id,
        description=__ret__.description,
        id=__ret__.id,
        local=__ret__.local,
        namespace=__ret__.namespace,
        policies=__ret__.policies)
