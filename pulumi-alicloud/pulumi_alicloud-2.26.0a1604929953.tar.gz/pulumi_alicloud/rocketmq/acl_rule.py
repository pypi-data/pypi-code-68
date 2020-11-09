# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['AclRule']


class AclRule(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 acl_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dest_cidr: Optional[pulumi.Input[str]] = None,
                 dest_port_range: Optional[pulumi.Input[str]] = None,
                 direction: Optional[pulumi.Input[str]] = None,
                 ip_protocol: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 source_cidr: Optional[pulumi.Input[str]] = None,
                 source_port_range: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Sag Acl Rule resource. This topic describes how to configure an access control list (ACL) rule for a target Smart Access Gateway instance to permit or deny access to or from specified IP addresses in the ACL rule.

        For information about Sag Acl Rule and how to use it, see [What is access control list (ACL) rule](https://www.alibabacloud.com/help/doc-detail/111483.htm).

        > **NOTE:** Available in 1.60.0+

        > **NOTE:** Only the following regions support create Cloud Connect Network. [`cn-shanghai`, `cn-shanghai-finance-1`, `cn-hongkong`, `ap-southeast-1`, `ap-southeast-2`, `ap-southeast-3`, `ap-southeast-5`, `ap-northeast-1`, `eu-central-1`]

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] acl_id: The ID of the ACL.
        :param pulumi.Input[str] description: The description of the ACL rule. It must be 1 to 512 characters in length.
        :param pulumi.Input[str] dest_cidr: The destination address. It is an IPv4 address range in CIDR format. Default value: 0.0.0.0/0.
        :param pulumi.Input[str] dest_port_range: The range of the destination port. Valid value: 80/80.
        :param pulumi.Input[str] direction: The direction of the ACL rule. Valid values: in|out.
        :param pulumi.Input[str] ip_protocol: The protocol used by the ACL rule. The value is not case sensitive.
        :param pulumi.Input[str] policy: The policy used by the ACL rule. Valid values: accept|drop.
        :param pulumi.Input[int] priority: The priority of the ACL rule. Value range: 1 to 100.
        :param pulumi.Input[str] source_cidr: The source address. It is an IPv4 address range in the CIDR format. Default value: 0.0.0.0/0.
        :param pulumi.Input[str] source_port_range: The range of the source port. Valid value: 80/80.
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

            if acl_id is None:
                raise TypeError("Missing required property 'acl_id'")
            __props__['acl_id'] = acl_id
            __props__['description'] = description
            if dest_cidr is None:
                raise TypeError("Missing required property 'dest_cidr'")
            __props__['dest_cidr'] = dest_cidr
            if dest_port_range is None:
                raise TypeError("Missing required property 'dest_port_range'")
            __props__['dest_port_range'] = dest_port_range
            if direction is None:
                raise TypeError("Missing required property 'direction'")
            __props__['direction'] = direction
            if ip_protocol is None:
                raise TypeError("Missing required property 'ip_protocol'")
            __props__['ip_protocol'] = ip_protocol
            if policy is None:
                raise TypeError("Missing required property 'policy'")
            __props__['policy'] = policy
            __props__['priority'] = priority
            if source_cidr is None:
                raise TypeError("Missing required property 'source_cidr'")
            __props__['source_cidr'] = source_cidr
            if source_port_range is None:
                raise TypeError("Missing required property 'source_port_range'")
            __props__['source_port_range'] = source_port_range
        super(AclRule, __self__).__init__(
            'alicloud:rocketmq/aclRule:AclRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            acl_id: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            dest_cidr: Optional[pulumi.Input[str]] = None,
            dest_port_range: Optional[pulumi.Input[str]] = None,
            direction: Optional[pulumi.Input[str]] = None,
            ip_protocol: Optional[pulumi.Input[str]] = None,
            policy: Optional[pulumi.Input[str]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            source_cidr: Optional[pulumi.Input[str]] = None,
            source_port_range: Optional[pulumi.Input[str]] = None) -> 'AclRule':
        """
        Get an existing AclRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] acl_id: The ID of the ACL.
        :param pulumi.Input[str] description: The description of the ACL rule. It must be 1 to 512 characters in length.
        :param pulumi.Input[str] dest_cidr: The destination address. It is an IPv4 address range in CIDR format. Default value: 0.0.0.0/0.
        :param pulumi.Input[str] dest_port_range: The range of the destination port. Valid value: 80/80.
        :param pulumi.Input[str] direction: The direction of the ACL rule. Valid values: in|out.
        :param pulumi.Input[str] ip_protocol: The protocol used by the ACL rule. The value is not case sensitive.
        :param pulumi.Input[str] policy: The policy used by the ACL rule. Valid values: accept|drop.
        :param pulumi.Input[int] priority: The priority of the ACL rule. Value range: 1 to 100.
        :param pulumi.Input[str] source_cidr: The source address. It is an IPv4 address range in the CIDR format. Default value: 0.0.0.0/0.
        :param pulumi.Input[str] source_port_range: The range of the source port. Valid value: 80/80.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["acl_id"] = acl_id
        __props__["description"] = description
        __props__["dest_cidr"] = dest_cidr
        __props__["dest_port_range"] = dest_port_range
        __props__["direction"] = direction
        __props__["ip_protocol"] = ip_protocol
        __props__["policy"] = policy
        __props__["priority"] = priority
        __props__["source_cidr"] = source_cidr
        __props__["source_port_range"] = source_port_range
        return AclRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="aclId")
    def acl_id(self) -> pulumi.Output[str]:
        """
        The ID of the ACL.
        """
        return pulumi.get(self, "acl_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the ACL rule. It must be 1 to 512 characters in length.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="destCidr")
    def dest_cidr(self) -> pulumi.Output[str]:
        """
        The destination address. It is an IPv4 address range in CIDR format. Default value: 0.0.0.0/0.
        """
        return pulumi.get(self, "dest_cidr")

    @property
    @pulumi.getter(name="destPortRange")
    def dest_port_range(self) -> pulumi.Output[str]:
        """
        The range of the destination port. Valid value: 80/80.
        """
        return pulumi.get(self, "dest_port_range")

    @property
    @pulumi.getter
    def direction(self) -> pulumi.Output[str]:
        """
        The direction of the ACL rule. Valid values: in|out.
        """
        return pulumi.get(self, "direction")

    @property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> pulumi.Output[str]:
        """
        The protocol used by the ACL rule. The value is not case sensitive.
        """
        return pulumi.get(self, "ip_protocol")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output[str]:
        """
        The policy used by the ACL rule. Valid values: accept|drop.
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[int]]:
        """
        The priority of the ACL rule. Value range: 1 to 100.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="sourceCidr")
    def source_cidr(self) -> pulumi.Output[str]:
        """
        The source address. It is an IPv4 address range in the CIDR format. Default value: 0.0.0.0/0.
        """
        return pulumi.get(self, "source_cidr")

    @property
    @pulumi.getter(name="sourcePortRange")
    def source_port_range(self) -> pulumi.Output[str]:
        """
        The range of the source port. Valid value: 80/80.
        """
        return pulumi.get(self, "source_port_range")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

