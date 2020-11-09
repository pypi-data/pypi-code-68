# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['PipelineSchedule']


class PipelineSchedule(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active: Optional[pulumi.Input[bool]] = None,
                 cron: Optional[pulumi.Input[str]] = None,
                 cron_timezone: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 ref: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## # gitlab\_pipeline\_schedule

        This resource allows you to create and manage pipeline schedules.
        For further information on clusters, consult the [gitlab
        documentation](https://docs.gitlab.com/ce/user/project/pipelines/schedules.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gitlab as gitlab

        example = gitlab.PipelineSchedule("example",
            cron="0 1 * * *",
            description="Used to schedule builds",
            project="12345",
            ref="master")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] active: The activation of pipeline schedule. If false is set, the pipeline schedule will deactivated initially.
        :param pulumi.Input[str] cron: The cron (e.g. `0 1 * * *`).
        :param pulumi.Input[str] cron_timezone: The timezone.
        :param pulumi.Input[str] description: The description of the pipeline schedule.
        :param pulumi.Input[str] project: The name or id of the project to add the schedule to.
        :param pulumi.Input[str] ref: The branch/tag name to be triggered.
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

            __props__['active'] = active
            if cron is None:
                raise TypeError("Missing required property 'cron'")
            __props__['cron'] = cron
            __props__['cron_timezone'] = cron_timezone
            if description is None:
                raise TypeError("Missing required property 'description'")
            __props__['description'] = description
            if project is None:
                raise TypeError("Missing required property 'project'")
            __props__['project'] = project
            if ref is None:
                raise TypeError("Missing required property 'ref'")
            __props__['ref'] = ref
        super(PipelineSchedule, __self__).__init__(
            'gitlab:index/pipelineSchedule:PipelineSchedule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            active: Optional[pulumi.Input[bool]] = None,
            cron: Optional[pulumi.Input[str]] = None,
            cron_timezone: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            ref: Optional[pulumi.Input[str]] = None) -> 'PipelineSchedule':
        """
        Get an existing PipelineSchedule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] active: The activation of pipeline schedule. If false is set, the pipeline schedule will deactivated initially.
        :param pulumi.Input[str] cron: The cron (e.g. `0 1 * * *`).
        :param pulumi.Input[str] cron_timezone: The timezone.
        :param pulumi.Input[str] description: The description of the pipeline schedule.
        :param pulumi.Input[str] project: The name or id of the project to add the schedule to.
        :param pulumi.Input[str] ref: The branch/tag name to be triggered.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["active"] = active
        __props__["cron"] = cron
        __props__["cron_timezone"] = cron_timezone
        __props__["description"] = description
        __props__["project"] = project
        __props__["ref"] = ref
        return PipelineSchedule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def active(self) -> pulumi.Output[Optional[bool]]:
        """
        The activation of pipeline schedule. If false is set, the pipeline schedule will deactivated initially.
        """
        return pulumi.get(self, "active")

    @property
    @pulumi.getter
    def cron(self) -> pulumi.Output[str]:
        """
        The cron (e.g. `0 1 * * *`).
        """
        return pulumi.get(self, "cron")

    @property
    @pulumi.getter(name="cronTimezone")
    def cron_timezone(self) -> pulumi.Output[Optional[str]]:
        """
        The timezone.
        """
        return pulumi.get(self, "cron_timezone")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the pipeline schedule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The name or id of the project to add the schedule to.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def ref(self) -> pulumi.Output[str]:
        """
        The branch/tag name to be triggered.
        """
        return pulumi.get(self, "ref")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

