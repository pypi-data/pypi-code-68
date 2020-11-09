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

__all__ = ['ReadOnlyInstance']


class ReadOnlyInstance(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 engine_version: Optional[pulumi.Input[str]] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 instance_storage: Optional[pulumi.Input[int]] = None,
                 instance_type: Optional[pulumi.Input[str]] = None,
                 master_db_instance_id: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ReadOnlyInstanceParameterArgs']]]]] = None,
                 resource_group_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 vswitch_id: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an RDS readonly instance resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        creation = config.get("creation")
        if creation is None:
            creation = "Rds"
        name = config.get("name")
        if name is None:
            name = "dbInstancevpc"
        default_zones = alicloud.get_zones(available_resource_creation=creation)
        default_network = alicloud.vpc.Network("defaultNetwork", cidr_block="172.16.0.0/16")
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vpc_id=default_network.id,
            cidr_block="172.16.0.0/24",
            availability_zone=default_zones.zones[0].id)
        default_instance = alicloud.rds.Instance("defaultInstance",
            engine="MySQL",
            engine_version="5.6",
            instance_type="rds.mysql.t1.small",
            instance_storage=20,
            instance_charge_type="Postpaid",
            instance_name=name,
            vswitch_id=default_switch.id,
            security_ips=[
                "10.168.1.12",
                "100.69.7.112",
            ])
        default_read_only_instance = alicloud.rds.ReadOnlyInstance("defaultReadOnlyInstance",
            master_db_instance_id=default_instance.id,
            zone_id=default_instance.zone_id,
            engine_version=default_instance.engine_version,
            instance_type=default_instance.instance_type,
            instance_storage=30,
            instance_name=f"{name}ro",
            vswitch_id=default_switch.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] engine_version: Database version. Value options can refer to the latest docs [CreateDBInstance](https://www.alibabacloud.com/help/doc-detail/26228.htm) `EngineVersion`.
        :param pulumi.Input[str] instance_name: The name of DB instance. It a string of 2 to 256 characters.
        :param pulumi.Input[int] instance_storage: User-defined DB instance storage space. Value range: [5, 2000] for MySQL/SQL Server HA dual node edition. Increase progressively at a rate of 5 GB. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
        :param pulumi.Input[str] instance_type: DB Instance type. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
        :param pulumi.Input[str] master_db_instance_id: ID of the master instance.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ReadOnlyInstanceParameterArgs']]]] parameters: Set of parameters needs to be set after DB instance was launched. Available parameters can refer to the latest docs [View database parameter templates](https://www.alibabacloud.com/help/doc-detail/26284.htm).
        :param pulumi.Input[str] resource_group_id: The ID of resource group which the DB read-only instance belongs.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
               - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
               - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
        :param pulumi.Input[str] vswitch_id: The virtual switch ID to launch DB instances in one VPC.
        :param pulumi.Input[str] zone_id: The Zone to launch the DB instance.
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

            if engine_version is None:
                raise TypeError("Missing required property 'engine_version'")
            __props__['engine_version'] = engine_version
            __props__['instance_name'] = instance_name
            if instance_storage is None:
                raise TypeError("Missing required property 'instance_storage'")
            __props__['instance_storage'] = instance_storage
            if instance_type is None:
                raise TypeError("Missing required property 'instance_type'")
            __props__['instance_type'] = instance_type
            if master_db_instance_id is None:
                raise TypeError("Missing required property 'master_db_instance_id'")
            __props__['master_db_instance_id'] = master_db_instance_id
            __props__['parameters'] = parameters
            __props__['resource_group_id'] = resource_group_id
            __props__['tags'] = tags
            __props__['vswitch_id'] = vswitch_id
            __props__['zone_id'] = zone_id
            __props__['connection_string'] = None
            __props__['engine'] = None
            __props__['port'] = None
        super(ReadOnlyInstance, __self__).__init__(
            'alicloud:rds/readOnlyInstance:ReadOnlyInstance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            connection_string: Optional[pulumi.Input[str]] = None,
            engine: Optional[pulumi.Input[str]] = None,
            engine_version: Optional[pulumi.Input[str]] = None,
            instance_name: Optional[pulumi.Input[str]] = None,
            instance_storage: Optional[pulumi.Input[int]] = None,
            instance_type: Optional[pulumi.Input[str]] = None,
            master_db_instance_id: Optional[pulumi.Input[str]] = None,
            parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ReadOnlyInstanceParameterArgs']]]]] = None,
            port: Optional[pulumi.Input[str]] = None,
            resource_group_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            vswitch_id: Optional[pulumi.Input[str]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'ReadOnlyInstance':
        """
        Get an existing ReadOnlyInstance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] connection_string: RDS database connection string.
        :param pulumi.Input[str] engine: Database type.
        :param pulumi.Input[str] engine_version: Database version. Value options can refer to the latest docs [CreateDBInstance](https://www.alibabacloud.com/help/doc-detail/26228.htm) `EngineVersion`.
        :param pulumi.Input[str] instance_name: The name of DB instance. It a string of 2 to 256 characters.
        :param pulumi.Input[int] instance_storage: User-defined DB instance storage space. Value range: [5, 2000] for MySQL/SQL Server HA dual node edition. Increase progressively at a rate of 5 GB. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
        :param pulumi.Input[str] instance_type: DB Instance type. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
        :param pulumi.Input[str] master_db_instance_id: ID of the master instance.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ReadOnlyInstanceParameterArgs']]]] parameters: Set of parameters needs to be set after DB instance was launched. Available parameters can refer to the latest docs [View database parameter templates](https://www.alibabacloud.com/help/doc-detail/26284.htm).
        :param pulumi.Input[str] port: RDS database connection port.
        :param pulumi.Input[str] resource_group_id: The ID of resource group which the DB read-only instance belongs.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
               - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
               - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
        :param pulumi.Input[str] vswitch_id: The virtual switch ID to launch DB instances in one VPC.
        :param pulumi.Input[str] zone_id: The Zone to launch the DB instance.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["connection_string"] = connection_string
        __props__["engine"] = engine
        __props__["engine_version"] = engine_version
        __props__["instance_name"] = instance_name
        __props__["instance_storage"] = instance_storage
        __props__["instance_type"] = instance_type
        __props__["master_db_instance_id"] = master_db_instance_id
        __props__["parameters"] = parameters
        __props__["port"] = port
        __props__["resource_group_id"] = resource_group_id
        __props__["tags"] = tags
        __props__["vswitch_id"] = vswitch_id
        __props__["zone_id"] = zone_id
        return ReadOnlyInstance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> pulumi.Output[str]:
        """
        RDS database connection string.
        """
        return pulumi.get(self, "connection_string")

    @property
    @pulumi.getter
    def engine(self) -> pulumi.Output[str]:
        """
        Database type.
        """
        return pulumi.get(self, "engine")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> pulumi.Output[str]:
        """
        Database version. Value options can refer to the latest docs [CreateDBInstance](https://www.alibabacloud.com/help/doc-detail/26228.htm) `EngineVersion`.
        """
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> pulumi.Output[str]:
        """
        The name of DB instance. It a string of 2 to 256 characters.
        """
        return pulumi.get(self, "instance_name")

    @property
    @pulumi.getter(name="instanceStorage")
    def instance_storage(self) -> pulumi.Output[int]:
        """
        User-defined DB instance storage space. Value range: [5, 2000] for MySQL/SQL Server HA dual node edition. Increase progressively at a rate of 5 GB. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
        """
        return pulumi.get(self, "instance_storage")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Output[str]:
        """
        DB Instance type. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
        """
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter(name="masterDbInstanceId")
    def master_db_instance_id(self) -> pulumi.Output[str]:
        """
        ID of the master instance.
        """
        return pulumi.get(self, "master_db_instance_id")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Sequence['outputs.ReadOnlyInstanceParameter']]:
        """
        Set of parameters needs to be set after DB instance was launched. Available parameters can refer to the latest docs [View database parameter templates](https://www.alibabacloud.com/help/doc-detail/26284.htm).
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[str]:
        """
        RDS database connection port.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> pulumi.Output[str]:
        """
        The ID of resource group which the DB read-only instance belongs.
        """
        return pulumi.get(self, "resource_group_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        A mapping of tags to assign to the resource.
        - Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
        - Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vswitchId")
    def vswitch_id(self) -> pulumi.Output[Optional[str]]:
        """
        The virtual switch ID to launch DB instances in one VPC.
        """
        return pulumi.get(self, "vswitch_id")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        The Zone to launch the DB instance.
        """
        return pulumi.get(self, "zone_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

