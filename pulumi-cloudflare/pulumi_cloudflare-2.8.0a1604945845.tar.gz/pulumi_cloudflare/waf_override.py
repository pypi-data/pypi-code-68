# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['WafOverride']


class WafOverride(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 groups: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 paused: Optional[pulumi.Input[bool]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 rewrite_action: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 rules: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 urls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Cloudflare WAF override resource. This enables the ability to toggle
        WAF rules and groups on or off based on URIs.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        shop_ecxample = cloudflare.WafOverride("shopEcxample",
            zone_id="1d5fdc9e88c8a8c4518b068cd94331fe",
            urls=[
                "example.com/no-waf-here",
                "example.com/another/path/*",
            ],
            rules={
                "100015": "disable",
            },
            groups={
                "ea8687e59929c1fd05ba97574ad43f77": "default",
            },
            rewrite_action={
                "default": "block",
                "challenge": "block",
            })
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of what the WAF override does.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] groups: Similar to `rules`; which WAF groups you want to alter.
        :param pulumi.Input[bool] paused: Whether this package is currently paused.
        :param pulumi.Input[int] priority: Relative priority of this configuration when multiple configurations match a single URL.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] rewrite_action: When a WAF rule matches, substitute its configured action for a different action specified by this definition.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] rules: A list of WAF rule ID to rule action you intend to apply.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] urls: An array of URLs to apply the WAF override to.
        :param pulumi.Input[str] zone_id: The DNS zone to which the WAF override condition should be added.
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

            __props__['description'] = description
            __props__['groups'] = groups
            __props__['paused'] = paused
            __props__['priority'] = priority
            __props__['rewrite_action'] = rewrite_action
            if rules is None:
                raise TypeError("Missing required property 'rules'")
            __props__['rules'] = rules
            if urls is None:
                raise TypeError("Missing required property 'urls'")
            __props__['urls'] = urls
            if zone_id is None:
                raise TypeError("Missing required property 'zone_id'")
            __props__['zone_id'] = zone_id
            __props__['override_id'] = None
        super(WafOverride, __self__).__init__(
            'cloudflare:index/wafOverride:WafOverride',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            groups: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            override_id: Optional[pulumi.Input[str]] = None,
            paused: Optional[pulumi.Input[bool]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            rewrite_action: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            rules: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            urls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'WafOverride':
        """
        Get an existing WafOverride resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of what the WAF override does.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] groups: Similar to `rules`; which WAF groups you want to alter.
        :param pulumi.Input[bool] paused: Whether this package is currently paused.
        :param pulumi.Input[int] priority: Relative priority of this configuration when multiple configurations match a single URL.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] rewrite_action: When a WAF rule matches, substitute its configured action for a different action specified by this definition.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] rules: A list of WAF rule ID to rule action you intend to apply.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] urls: An array of URLs to apply the WAF override to.
        :param pulumi.Input[str] zone_id: The DNS zone to which the WAF override condition should be added.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["description"] = description
        __props__["groups"] = groups
        __props__["override_id"] = override_id
        __props__["paused"] = paused
        __props__["priority"] = priority
        __props__["rewrite_action"] = rewrite_action
        __props__["rules"] = rules
        __props__["urls"] = urls
        __props__["zone_id"] = zone_id
        return WafOverride(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of what the WAF override does.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def groups(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Similar to `rules`; which WAF groups you want to alter.
        """
        return pulumi.get(self, "groups")

    @property
    @pulumi.getter(name="overrideId")
    def override_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "override_id")

    @property
    @pulumi.getter
    def paused(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether this package is currently paused.
        """
        return pulumi.get(self, "paused")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[int]]:
        """
        Relative priority of this configuration when multiple configurations match a single URL.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="rewriteAction")
    def rewrite_action(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        When a WAF rule matches, substitute its configured action for a different action specified by this definition.
        """
        return pulumi.get(self, "rewrite_action")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A list of WAF rule ID to rule action you intend to apply.
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter
    def urls(self) -> pulumi.Output[Sequence[str]]:
        """
        An array of URLs to apply the WAF override to.
        """
        return pulumi.get(self, "urls")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        The DNS zone to which the WAF override condition should be added.
        """
        return pulumi.get(self, "zone_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

