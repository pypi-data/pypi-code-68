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

__all__ = ['DedicatedHost']


class DedicatedHost(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action_on_maintenance: Optional[pulumi.Input[str]] = None,
                 auto_placement: Optional[pulumi.Input[str]] = None,
                 auto_release_time: Optional[pulumi.Input[str]] = None,
                 auto_renew: Optional[pulumi.Input[bool]] = None,
                 auto_renew_period: Optional[pulumi.Input[int]] = None,
                 dedicated_host_name: Optional[pulumi.Input[str]] = None,
                 dedicated_host_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 detail_fee: Optional[pulumi.Input[bool]] = None,
                 dry_run: Optional[pulumi.Input[bool]] = None,
                 expired_time: Optional[pulumi.Input[str]] = None,
                 network_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DedicatedHostNetworkAttributeArgs']]]]] = None,
                 payment_type: Optional[pulumi.Input[str]] = None,
                 resource_group_id: Optional[pulumi.Input[str]] = None,
                 sale_cycle: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        This resouce used to create a dedicated host and store its initial version. For information about Aliecs Dedicated Host and how to use it, see [What is Resource Aliecs Dedicated Host](https://www.alibabacloud.com/help/doc-detail/134238.htm).

        > **NOTE:** Available in 1.91.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default = alicloud.ecs.DedicatedHost("default",
            dedicated_host_name="dedicated_host_name",
            dedicated_host_type="ddh.g5",
            description="From_Terraform",
            tags={
                "Create": "Terraform",
                "For": "DDH",
            })
        ```

        Create Prepaid DDH

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default = alicloud.ecs.DedicatedHost("default",
            dedicated_host_name="dedicated_host_name",
            dedicated_host_type="ddh.g5",
            description="From_Terraform",
            expired_time="1",
            payment_type="PrePaid",
            sale_cycle="Month",
            tags={
                "Create": "Terraform",
                "For": "DDH",
            })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action_on_maintenance: The policy used to migrate the instances from the dedicated host when the dedicated host fails or needs to be repaired online. Valid values: `Migrate`, `Stop`.
        :param pulumi.Input[str] auto_placement: Specifies whether to add the dedicated host to the resource pool for automatic deployment. If you do not specify the DedicatedHostId parameter when you create an instance on a dedicated host, Alibaba Cloud automatically selects a dedicated host from the resource pool to host the instance. Valid values: `on`, `off`. Default: `on`.
        :param pulumi.Input[str] auto_release_time: The automatic release time of the dedicated host. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC+0.
        :param pulumi.Input[bool] auto_renew: Specifies whether to automatically renew the subscription dedicated host.
        :param pulumi.Input[int] auto_renew_period: The auto-renewal period of the dedicated host. Unit: months. Valid values: `1`, `2`, `3`, `6`, and `12`. takes effect and is required only when the AutoRenew parameter is set to true.
        :param pulumi.Input[str] dedicated_host_name: The name of the dedicated host. The name must be 2 to 128 characters in length. It must start with a letter but cannot start with http:// or https://. It can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        :param pulumi.Input[str] dedicated_host_type: The type of the dedicated host. You can call the [DescribeDedicatedHostTypes](https://www.alibabacloud.com/help/doc-detail/134240.htm) operation to obtain the most recent list of dedicated host types.
        :param pulumi.Input[str] description: The description of the dedicated host. The description must be 2 to 256 characters in length and cannot start with http:// or https://.
        :param pulumi.Input[bool] detail_fee: Specifies whether to return the billing details of the order when the billing method is changed from subscription to pay-as-you-go. Default: `false`.
        :param pulumi.Input[bool] dry_run: Specifies whether to only validate the request. Default: `false`.
        :param pulumi.Input[str] expired_time: The subscription period of the dedicated host. The Period parameter takes effect and is required only when the ChargeType parameter is set to PrePaid.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DedicatedHostNetworkAttributeArgs']]]] network_attributes: dedicated host network parameters. contains the following attributes:
        :param pulumi.Input[str] payment_type: The billing method of the dedicated host. Valid values: `PrePaid`, `PostPaid`. Default: `PostPaid`.
        :param pulumi.Input[str] resource_group_id: The ID of the resource group to which the dedicated host belongs.
        :param pulumi.Input[str] sale_cycle: The unit of the subscription period of the dedicated host.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] zone_id: The zone ID of the dedicated host. This parameter is empty by default. If you do not specify this parameter, the system automatically selects a zone.
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

            __props__['action_on_maintenance'] = action_on_maintenance
            __props__['auto_placement'] = auto_placement
            __props__['auto_release_time'] = auto_release_time
            __props__['auto_renew'] = auto_renew
            __props__['auto_renew_period'] = auto_renew_period
            __props__['dedicated_host_name'] = dedicated_host_name
            if dedicated_host_type is None:
                raise TypeError("Missing required property 'dedicated_host_type'")
            __props__['dedicated_host_type'] = dedicated_host_type
            __props__['description'] = description
            __props__['detail_fee'] = detail_fee
            __props__['dry_run'] = dry_run
            __props__['expired_time'] = expired_time
            __props__['network_attributes'] = network_attributes
            __props__['payment_type'] = payment_type
            __props__['resource_group_id'] = resource_group_id
            __props__['sale_cycle'] = sale_cycle
            __props__['tags'] = tags
            __props__['zone_id'] = zone_id
            __props__['status'] = None
        super(DedicatedHost, __self__).__init__(
            'alicloud:ecs/dedicatedHost:DedicatedHost',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            action_on_maintenance: Optional[pulumi.Input[str]] = None,
            auto_placement: Optional[pulumi.Input[str]] = None,
            auto_release_time: Optional[pulumi.Input[str]] = None,
            auto_renew: Optional[pulumi.Input[bool]] = None,
            auto_renew_period: Optional[pulumi.Input[int]] = None,
            dedicated_host_name: Optional[pulumi.Input[str]] = None,
            dedicated_host_type: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            detail_fee: Optional[pulumi.Input[bool]] = None,
            dry_run: Optional[pulumi.Input[bool]] = None,
            expired_time: Optional[pulumi.Input[str]] = None,
            network_attributes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DedicatedHostNetworkAttributeArgs']]]]] = None,
            payment_type: Optional[pulumi.Input[str]] = None,
            resource_group_id: Optional[pulumi.Input[str]] = None,
            sale_cycle: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'DedicatedHost':
        """
        Get an existing DedicatedHost resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action_on_maintenance: The policy used to migrate the instances from the dedicated host when the dedicated host fails or needs to be repaired online. Valid values: `Migrate`, `Stop`.
        :param pulumi.Input[str] auto_placement: Specifies whether to add the dedicated host to the resource pool for automatic deployment. If you do not specify the DedicatedHostId parameter when you create an instance on a dedicated host, Alibaba Cloud automatically selects a dedicated host from the resource pool to host the instance. Valid values: `on`, `off`. Default: `on`.
        :param pulumi.Input[str] auto_release_time: The automatic release time of the dedicated host. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC+0.
        :param pulumi.Input[bool] auto_renew: Specifies whether to automatically renew the subscription dedicated host.
        :param pulumi.Input[int] auto_renew_period: The auto-renewal period of the dedicated host. Unit: months. Valid values: `1`, `2`, `3`, `6`, and `12`. takes effect and is required only when the AutoRenew parameter is set to true.
        :param pulumi.Input[str] dedicated_host_name: The name of the dedicated host. The name must be 2 to 128 characters in length. It must start with a letter but cannot start with http:// or https://. It can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        :param pulumi.Input[str] dedicated_host_type: The type of the dedicated host. You can call the [DescribeDedicatedHostTypes](https://www.alibabacloud.com/help/doc-detail/134240.htm) operation to obtain the most recent list of dedicated host types.
        :param pulumi.Input[str] description: The description of the dedicated host. The description must be 2 to 256 characters in length and cannot start with http:// or https://.
        :param pulumi.Input[bool] detail_fee: Specifies whether to return the billing details of the order when the billing method is changed from subscription to pay-as-you-go. Default: `false`.
        :param pulumi.Input[bool] dry_run: Specifies whether to only validate the request. Default: `false`.
        :param pulumi.Input[str] expired_time: The subscription period of the dedicated host. The Period parameter takes effect and is required only when the ChargeType parameter is set to PrePaid.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DedicatedHostNetworkAttributeArgs']]]] network_attributes: dedicated host network parameters. contains the following attributes:
        :param pulumi.Input[str] payment_type: The billing method of the dedicated host. Valid values: `PrePaid`, `PostPaid`. Default: `PostPaid`.
        :param pulumi.Input[str] resource_group_id: The ID of the resource group to which the dedicated host belongs.
        :param pulumi.Input[str] sale_cycle: The unit of the subscription period of the dedicated host.
        :param pulumi.Input[str] status: The status of the dedicated host.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[str] zone_id: The zone ID of the dedicated host. This parameter is empty by default. If you do not specify this parameter, the system automatically selects a zone.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["action_on_maintenance"] = action_on_maintenance
        __props__["auto_placement"] = auto_placement
        __props__["auto_release_time"] = auto_release_time
        __props__["auto_renew"] = auto_renew
        __props__["auto_renew_period"] = auto_renew_period
        __props__["dedicated_host_name"] = dedicated_host_name
        __props__["dedicated_host_type"] = dedicated_host_type
        __props__["description"] = description
        __props__["detail_fee"] = detail_fee
        __props__["dry_run"] = dry_run
        __props__["expired_time"] = expired_time
        __props__["network_attributes"] = network_attributes
        __props__["payment_type"] = payment_type
        __props__["resource_group_id"] = resource_group_id
        __props__["sale_cycle"] = sale_cycle
        __props__["status"] = status
        __props__["tags"] = tags
        __props__["zone_id"] = zone_id
        return DedicatedHost(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="actionOnMaintenance")
    def action_on_maintenance(self) -> pulumi.Output[Optional[str]]:
        """
        The policy used to migrate the instances from the dedicated host when the dedicated host fails or needs to be repaired online. Valid values: `Migrate`, `Stop`.
        """
        return pulumi.get(self, "action_on_maintenance")

    @property
    @pulumi.getter(name="autoPlacement")
    def auto_placement(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies whether to add the dedicated host to the resource pool for automatic deployment. If you do not specify the DedicatedHostId parameter when you create an instance on a dedicated host, Alibaba Cloud automatically selects a dedicated host from the resource pool to host the instance. Valid values: `on`, `off`. Default: `on`.
        """
        return pulumi.get(self, "auto_placement")

    @property
    @pulumi.getter(name="autoReleaseTime")
    def auto_release_time(self) -> pulumi.Output[Optional[str]]:
        """
        The automatic release time of the dedicated host. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC+0.
        """
        return pulumi.get(self, "auto_release_time")

    @property
    @pulumi.getter(name="autoRenew")
    def auto_renew(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether to automatically renew the subscription dedicated host.
        """
        return pulumi.get(self, "auto_renew")

    @property
    @pulumi.getter(name="autoRenewPeriod")
    def auto_renew_period(self) -> pulumi.Output[Optional[int]]:
        """
        The auto-renewal period of the dedicated host. Unit: months. Valid values: `1`, `2`, `3`, `6`, and `12`. takes effect and is required only when the AutoRenew parameter is set to true.
        """
        return pulumi.get(self, "auto_renew_period")

    @property
    @pulumi.getter(name="dedicatedHostName")
    def dedicated_host_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the dedicated host. The name must be 2 to 128 characters in length. It must start with a letter but cannot start with http:// or https://. It can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        """
        return pulumi.get(self, "dedicated_host_name")

    @property
    @pulumi.getter(name="dedicatedHostType")
    def dedicated_host_type(self) -> pulumi.Output[str]:
        """
        The type of the dedicated host. You can call the [DescribeDedicatedHostTypes](https://www.alibabacloud.com/help/doc-detail/134240.htm) operation to obtain the most recent list of dedicated host types.
        """
        return pulumi.get(self, "dedicated_host_type")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the dedicated host. The description must be 2 to 256 characters in length and cannot start with http:// or https://.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="detailFee")
    def detail_fee(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether to return the billing details of the order when the billing method is changed from subscription to pay-as-you-go. Default: `false`.
        """
        return pulumi.get(self, "detail_fee")

    @property
    @pulumi.getter(name="dryRun")
    def dry_run(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether to only validate the request. Default: `false`.
        """
        return pulumi.get(self, "dry_run")

    @property
    @pulumi.getter(name="expiredTime")
    def expired_time(self) -> pulumi.Output[str]:
        """
        The subscription period of the dedicated host. The Period parameter takes effect and is required only when the ChargeType parameter is set to PrePaid.
        """
        return pulumi.get(self, "expired_time")

    @property
    @pulumi.getter(name="networkAttributes")
    def network_attributes(self) -> pulumi.Output[Optional[Sequence['outputs.DedicatedHostNetworkAttribute']]]:
        """
        dedicated host network parameters. contains the following attributes:
        """
        return pulumi.get(self, "network_attributes")

    @property
    @pulumi.getter(name="paymentType")
    def payment_type(self) -> pulumi.Output[Optional[str]]:
        """
        The billing method of the dedicated host. Valid values: `PrePaid`, `PostPaid`. Default: `PostPaid`.
        """
        return pulumi.get(self, "payment_type")

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> pulumi.Output[str]:
        """
        The ID of the resource group to which the dedicated host belongs.
        """
        return pulumi.get(self, "resource_group_id")

    @property
    @pulumi.getter(name="saleCycle")
    def sale_cycle(self) -> pulumi.Output[str]:
        """
        The unit of the subscription period of the dedicated host.
        """
        return pulumi.get(self, "sale_cycle")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the dedicated host.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        The zone ID of the dedicated host. This parameter is empty by default. If you do not specify this parameter, the system automatically selects a zone.
        """
        return pulumi.get(self, "zone_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

