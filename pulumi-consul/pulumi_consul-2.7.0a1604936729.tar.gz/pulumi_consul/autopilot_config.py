# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['AutopilotConfig']


class AutopilotConfig(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cleanup_dead_servers: Optional[pulumi.Input[bool]] = None,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 disable_upgrade_migration: Optional[pulumi.Input[bool]] = None,
                 last_contact_threshold: Optional[pulumi.Input[str]] = None,
                 max_trailing_logs: Optional[pulumi.Input[int]] = None,
                 redundancy_zone_tag: Optional[pulumi.Input[str]] = None,
                 server_stabilization_time: Optional[pulumi.Input[str]] = None,
                 upgrade_version_tag: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides access to the [Autopilot Configuration](https://www.consul.io/docs/guides/autopilot.html)
        of Consul to automatically manage Consul servers.

        It includes to automatically cleanup dead servers, monitor the status of the Raft
        cluster and stable server introduction.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_consul as consul

        config = consul.AutopilotConfig("config",
            cleanup_dead_servers=False,
            last_contact_threshold="1s",
            max_trailing_logs=500)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] cleanup_dead_servers: Whether to remove failing servers when a
               replacement comes online. Defaults to true.
        :param pulumi.Input[str] datacenter: The datacenter to use. This overrides the agent's
               default datacenter and the datacenter in the provider setup.
        :param pulumi.Input[bool] disable_upgrade_migration: Whether to disable [upgrade migrations](https://www.consul.io/docs/guides/autopilot.html#redundancy-zones).
               Defaults to false.
        :param pulumi.Input[str] last_contact_threshold: The time after which a server is
               considered as unhealthy and will be removed. Defaults to `"200ms"`.
        :param pulumi.Input[int] max_trailing_logs: The maximum number of Raft log entries a
               server can trail the leader. Defaults to 250.
        :param pulumi.Input[str] redundancy_zone_tag: The [redundancy zone](https://www.consul.io/docs/guides/autopilot.html#redundancy-zones)
               tag to use. Consul will try to keep one voting server by zone to take advantage
               of isolated failure domains. Defaults to an empty string.
        :param pulumi.Input[str] server_stabilization_time: The period to wait for a server to be
               healthy and stable before being promoted to a full, voting member. Defaults to
               `"10s"`.
        :param pulumi.Input[str] upgrade_version_tag: The tag to override the version information
               used during a migration. Defaults to an empty string.
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

            __props__['cleanup_dead_servers'] = cleanup_dead_servers
            __props__['datacenter'] = datacenter
            __props__['disable_upgrade_migration'] = disable_upgrade_migration
            __props__['last_contact_threshold'] = last_contact_threshold
            __props__['max_trailing_logs'] = max_trailing_logs
            __props__['redundancy_zone_tag'] = redundancy_zone_tag
            __props__['server_stabilization_time'] = server_stabilization_time
            __props__['upgrade_version_tag'] = upgrade_version_tag
        super(AutopilotConfig, __self__).__init__(
            'consul:index/autopilotConfig:AutopilotConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cleanup_dead_servers: Optional[pulumi.Input[bool]] = None,
            datacenter: Optional[pulumi.Input[str]] = None,
            disable_upgrade_migration: Optional[pulumi.Input[bool]] = None,
            last_contact_threshold: Optional[pulumi.Input[str]] = None,
            max_trailing_logs: Optional[pulumi.Input[int]] = None,
            redundancy_zone_tag: Optional[pulumi.Input[str]] = None,
            server_stabilization_time: Optional[pulumi.Input[str]] = None,
            upgrade_version_tag: Optional[pulumi.Input[str]] = None) -> 'AutopilotConfig':
        """
        Get an existing AutopilotConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] cleanup_dead_servers: Whether to remove failing servers when a
               replacement comes online. Defaults to true.
        :param pulumi.Input[str] datacenter: The datacenter to use. This overrides the agent's
               default datacenter and the datacenter in the provider setup.
        :param pulumi.Input[bool] disable_upgrade_migration: Whether to disable [upgrade migrations](https://www.consul.io/docs/guides/autopilot.html#redundancy-zones).
               Defaults to false.
        :param pulumi.Input[str] last_contact_threshold: The time after which a server is
               considered as unhealthy and will be removed. Defaults to `"200ms"`.
        :param pulumi.Input[int] max_trailing_logs: The maximum number of Raft log entries a
               server can trail the leader. Defaults to 250.
        :param pulumi.Input[str] redundancy_zone_tag: The [redundancy zone](https://www.consul.io/docs/guides/autopilot.html#redundancy-zones)
               tag to use. Consul will try to keep one voting server by zone to take advantage
               of isolated failure domains. Defaults to an empty string.
        :param pulumi.Input[str] server_stabilization_time: The period to wait for a server to be
               healthy and stable before being promoted to a full, voting member. Defaults to
               `"10s"`.
        :param pulumi.Input[str] upgrade_version_tag: The tag to override the version information
               used during a migration. Defaults to an empty string.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cleanup_dead_servers"] = cleanup_dead_servers
        __props__["datacenter"] = datacenter
        __props__["disable_upgrade_migration"] = disable_upgrade_migration
        __props__["last_contact_threshold"] = last_contact_threshold
        __props__["max_trailing_logs"] = max_trailing_logs
        __props__["redundancy_zone_tag"] = redundancy_zone_tag
        __props__["server_stabilization_time"] = server_stabilization_time
        __props__["upgrade_version_tag"] = upgrade_version_tag
        return AutopilotConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cleanupDeadServers")
    def cleanup_dead_servers(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to remove failing servers when a
        replacement comes online. Defaults to true.
        """
        return pulumi.get(self, "cleanup_dead_servers")

    @property
    @pulumi.getter
    def datacenter(self) -> pulumi.Output[Optional[str]]:
        """
        The datacenter to use. This overrides the agent's
        default datacenter and the datacenter in the provider setup.
        """
        return pulumi.get(self, "datacenter")

    @property
    @pulumi.getter(name="disableUpgradeMigration")
    def disable_upgrade_migration(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to disable [upgrade migrations](https://www.consul.io/docs/guides/autopilot.html#redundancy-zones).
        Defaults to false.
        """
        return pulumi.get(self, "disable_upgrade_migration")

    @property
    @pulumi.getter(name="lastContactThreshold")
    def last_contact_threshold(self) -> pulumi.Output[Optional[str]]:
        """
        The time after which a server is
        considered as unhealthy and will be removed. Defaults to `"200ms"`.
        """
        return pulumi.get(self, "last_contact_threshold")

    @property
    @pulumi.getter(name="maxTrailingLogs")
    def max_trailing_logs(self) -> pulumi.Output[Optional[int]]:
        """
        The maximum number of Raft log entries a
        server can trail the leader. Defaults to 250.
        """
        return pulumi.get(self, "max_trailing_logs")

    @property
    @pulumi.getter(name="redundancyZoneTag")
    def redundancy_zone_tag(self) -> pulumi.Output[Optional[str]]:
        """
        The [redundancy zone](https://www.consul.io/docs/guides/autopilot.html#redundancy-zones)
        tag to use. Consul will try to keep one voting server by zone to take advantage
        of isolated failure domains. Defaults to an empty string.
        """
        return pulumi.get(self, "redundancy_zone_tag")

    @property
    @pulumi.getter(name="serverStabilizationTime")
    def server_stabilization_time(self) -> pulumi.Output[Optional[str]]:
        """
        The period to wait for a server to be
        healthy and stable before being promoted to a full, voting member. Defaults to
        `"10s"`.
        """
        return pulumi.get(self, "server_stabilization_time")

    @property
    @pulumi.getter(name="upgradeVersionTag")
    def upgrade_version_tag(self) -> pulumi.Output[Optional[str]]:
        """
        The tag to override the version information
        used during a migration. Defaults to an empty string.
        """
        return pulumi.get(self, "upgrade_version_tag")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

