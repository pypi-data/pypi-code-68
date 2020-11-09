# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'GetInstancesResult',
    'AwaitableGetInstancesResult',
    'get_instances',
]

@pulumi.output_type
class GetInstancesResult:
    """
    A collection of values returned by getInstances.
    """
    def __init__(__self__, id=None, ids=None, instance_source=None, instances=None, output_file=None, resource_group_id=None, status=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if instance_source and not isinstance(instance_source, str):
            raise TypeError("Expected argument 'instance_source' to be a str")
        pulumi.set(__self__, "instance_source", instance_source)
        if instances and not isinstance(instances, list):
            raise TypeError("Expected argument 'instances' to be a list")
        pulumi.set(__self__, "instances", instances)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if resource_group_id and not isinstance(resource_group_id, str):
            raise TypeError("Expected argument 'resource_group_id' to be a str")
        pulumi.set(__self__, "resource_group_id", resource_group_id)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        """
        (Optional) A list of WAF instance IDs.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="instanceSource")
    def instance_source(self) -> Optional[str]:
        return pulumi.get(self, "instance_source")

    @property
    @pulumi.getter
    def instances(self) -> Sequence['outputs.GetInstancesInstanceResult']:
        """
        A list of WAF instances. Each element contains the following attributes:
        """
        return pulumi.get(self, "instances")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> Optional[str]:
        return pulumi.get(self, "resource_group_id")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Indicates whether the WAF instance has expired.
        """
        return pulumi.get(self, "status")


class AwaitableGetInstancesResult(GetInstancesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInstancesResult(
            id=self.id,
            ids=self.ids,
            instance_source=self.instance_source,
            instances=self.instances,
            output_file=self.output_file,
            resource_group_id=self.resource_group_id,
            status=self.status)


def get_instances(ids: Optional[Sequence[str]] = None,
                  instance_source: Optional[str] = None,
                  output_file: Optional[str] = None,
                  resource_group_id: Optional[str] = None,
                  status: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInstancesResult:
    """
    Provides a WAF datasource to retrieve instances.

    For information about WAF and how to use it, see [What is Alibaba Cloud WAF](https://www.alibabacloud.com/help/doc-detail/28517.htm).

    > **NOTE:** Available in 1.90.0+ .

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.waf.get_instances(ids=["waf-cn-09k********"],
        status="1",
        resource_group_id="rg-acfmwvv********",
        instance_source="waf-cloud")
    pulumi.export("theFirstWafInstanceId", default.instances[0].id)
    ```


    :param Sequence[str] ids: A list of WAF instance IDs.
    :param str instance_source: The source of the WAF instance.
    :param str resource_group_id: The ID of resource group to which WAF instance belongs.
    :param str status: The status of WAF instance to filter results. Optional value: `0`: The instance has expired, `1` : The instance has not expired and is working properly.
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['instanceSource'] = instance_source
    __args__['outputFile'] = output_file
    __args__['resourceGroupId'] = resource_group_id
    __args__['status'] = status
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:waf/getInstances:getInstances', __args__, opts=opts, typ=GetInstancesResult).value

    return AwaitableGetInstancesResult(
        id=__ret__.id,
        ids=__ret__.ids,
        instance_source=__ret__.instance_source,
        instances=__ret__.instances,
        output_file=__ret__.output_file,
        resource_group_id=__ret__.resource_group_id,
        status=__ret__.status)
