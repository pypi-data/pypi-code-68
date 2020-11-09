# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['DeployKeyEnable']


class DeployKeyEnable(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 can_push: Optional[pulumi.Input[bool]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 key_id: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## # gitlab\_deploy\_key\_enable

        This resource allows you to enable pre-existing deploy keys for your GitLab projects.

        **the GITLAB KEY_ID for the deploy key must be known**

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gitlab as gitlab

        # A repo to host the deployment key
        parent_project = gitlab.Project("parentProject")
        # A second repo to use the deployment key from the parent project
        foo_project = gitlab.Project("fooProject")
        # Upload a deployment key for the parent repo
        parent_deploy_key = gitlab.DeployKey("parentDeployKey",
            key="ssh-rsa AAAA...",
            project=parent_project.id,
            title="Example deploy key")
        # Enable the deployment key on the second repo
        foo_deploy_key_enable = gitlab.DeployKeyEnable("fooDeployKeyEnable",
            key_id=parent_deploy_key.id,
            project=foo_project.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key_id: The Gitlab key id for the pre-existing deploy key
        :param pulumi.Input[str] project: The name or id of the project to add the deploy key to.
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

            __props__['can_push'] = can_push
            __props__['key'] = key
            if key_id is None:
                raise TypeError("Missing required property 'key_id'")
            __props__['key_id'] = key_id
            if project is None:
                raise TypeError("Missing required property 'project'")
            __props__['project'] = project
            __props__['title'] = title
        super(DeployKeyEnable, __self__).__init__(
            'gitlab:index/deployKeyEnable:DeployKeyEnable',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            can_push: Optional[pulumi.Input[bool]] = None,
            key: Optional[pulumi.Input[str]] = None,
            key_id: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            title: Optional[pulumi.Input[str]] = None) -> 'DeployKeyEnable':
        """
        Get an existing DeployKeyEnable resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key_id: The Gitlab key id for the pre-existing deploy key
        :param pulumi.Input[str] project: The name or id of the project to add the deploy key to.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["can_push"] = can_push
        __props__["key"] = key
        __props__["key_id"] = key_id
        __props__["project"] = project
        __props__["title"] = title
        return DeployKeyEnable(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="canPush")
    def can_push(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "can_push")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Output[str]:
        """
        The Gitlab key id for the pre-existing deploy key
        """
        return pulumi.get(self, "key_id")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The name or id of the project to add the deploy key to.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[str]:
        return pulumi.get(self, "title")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

