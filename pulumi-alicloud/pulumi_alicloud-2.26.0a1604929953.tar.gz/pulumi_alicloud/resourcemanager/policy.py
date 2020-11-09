# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Policy']


class Policy(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_version: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 policy_document: Optional[pulumi.Input[str]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Resource Manager Policy resource.\
        For information about Resource Manager Policy and how to use it, see [What is Resource Manager Policy](https://www.alibabacloud.com/help/en/doc-detail/93732.htm).

        > **NOTE:** Available in v1.83.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example = alicloud.resourcemanager.Policy("example",
            policy_document=\"\"\"		{
        			"Statement": [{
        				"Action": ["oss:*"],
        				"Effect": "Allow",
        				"Resource": ["acs:oss:*:*:*"]
        			}],
        			"Version": "1"
        		}
            
        \"\"\",
            policy_name="abc12345")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_version: The version of the policy. Default to v1.
        :param pulumi.Input[str] description: The description of the policy. The description must be 1 to 1,024 characters in length.
        :param pulumi.Input[str] policy_document: The content of the policy. The content must be 1 to 2,048 characters in length.
        :param pulumi.Input[str] policy_name: The name of the policy. name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
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

            if default_version is not None:
                warnings.warn("Field 'default_version' has been deprecated from provider version 1.90.0", DeprecationWarning)
                pulumi.log.warn("default_version is deprecated: Field 'default_version' has been deprecated from provider version 1.90.0")
            __props__['default_version'] = default_version
            __props__['description'] = description
            if policy_document is None:
                raise TypeError("Missing required property 'policy_document'")
            __props__['policy_document'] = policy_document
            if policy_name is None:
                raise TypeError("Missing required property 'policy_name'")
            __props__['policy_name'] = policy_name
            __props__['policy_type'] = None
        super(Policy, __self__).__init__(
            'alicloud:resourcemanager/policy:Policy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            default_version: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            policy_document: Optional[pulumi.Input[str]] = None,
            policy_name: Optional[pulumi.Input[str]] = None,
            policy_type: Optional[pulumi.Input[str]] = None) -> 'Policy':
        """
        Get an existing Policy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_version: The version of the policy. Default to v1.
        :param pulumi.Input[str] description: The description of the policy. The description must be 1 to 1,024 characters in length.
        :param pulumi.Input[str] policy_document: The content of the policy. The content must be 1 to 2,048 characters in length.
        :param pulumi.Input[str] policy_name: The name of the policy. name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        :param pulumi.Input[str] policy_type: The type of the policy. Valid values: `Custom`, `System`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["default_version"] = default_version
        __props__["description"] = description
        __props__["policy_document"] = policy_document
        __props__["policy_name"] = policy_name
        __props__["policy_type"] = policy_type
        return Policy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="defaultVersion")
    def default_version(self) -> pulumi.Output[str]:
        """
        The version of the policy. Default to v1.
        """
        return pulumi.get(self, "default_version")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the policy. The description must be 1 to 1,024 characters in length.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> pulumi.Output[str]:
        """
        The content of the policy. The content must be 1 to 2,048 characters in length.
        """
        return pulumi.get(self, "policy_document")

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> pulumi.Output[str]:
        """
        The name of the policy. name must be 1 to 128 characters in length and can contain letters, digits, and hyphens (-).
        """
        return pulumi.get(self, "policy_name")

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Output[str]:
        """
        The type of the policy. Valid values: `Custom`, `System`.
        """
        return pulumi.get(self, "policy_type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

