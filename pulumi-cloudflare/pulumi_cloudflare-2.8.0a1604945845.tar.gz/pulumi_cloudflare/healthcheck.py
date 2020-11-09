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

__all__ = ['Healthcheck']


class Healthcheck(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address: Optional[pulumi.Input[str]] = None,
                 allow_insecure: Optional[pulumi.Input[bool]] = None,
                 check_regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 consecutive_fails: Optional[pulumi.Input[int]] = None,
                 consecutive_successes: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expected_body: Optional[pulumi.Input[str]] = None,
                 expected_codes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 follow_redirects: Optional[pulumi.Input[bool]] = None,
                 headers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HealthcheckHeaderArgs']]]]] = None,
                 interval: Optional[pulumi.Input[int]] = None,
                 method: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 notification_email_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 notification_suspended: Optional[pulumi.Input[bool]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 retries: Optional[pulumi.Input[int]] = None,
                 suspended: Optional[pulumi.Input[bool]] = None,
                 timeout: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Standalone Health Checks provide a way to monitor origin servers without needing a Cloudflare Load Balancer.

        ## Example Usage

        The resource supports HTTP, HTTPS and TCP type health checks.
        ### HTTPS Health Check

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        http_health_check = cloudflare.Healthcheck("httpHealthCheck",
            zone_id=var["cloudflare_zone_id"],
            name="http-health-check",
            description="example http health check",
            address="example.com",
            suspended=False,
            check_regions=[
                "WEU",
                "EEU",
            ],
            notification_suspended=False,
            notification_email_addresses=["hostmaster@example.com"],
            type="HTTPS",
            port=443,
            method="GET",
            path="/health",
            expected_body="alive",
            expected_codes=[
                "2xx",
                "301",
            ],
            follow_redirects=True,
            allow_insecure=False,
            headers=[cloudflare.HealthcheckHeaderArgs(
                header="Host",
                values=["example.com"],
            )],
            timeout=10,
            retries=2,
            interval=60,
            consecutive_fails=3,
            consecutive_successes=2)
        ```
        ### TCP Monitor

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        tcp_health_check = cloudflare.Healthcheck("tcpHealthCheck",
            zone_id=var["cloudflare_zone_id"],
            name="tcp-health-check",
            description="example tcp health check",
            address="example.com",
            suspended=False,
            check_regions=[
                "WEU",
                "EEU",
            ],
            notification_suspended=False,
            notification_email_addresses=["hostmaster@example.com"],
            type="TCP",
            port=22,
            method="connection_established",
            timeout=10,
            retries=2,
            interval=60,
            consecutive_fails=3,
            consecutive_successes=2)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address: The hostname or IP address of the origin server to run health checks on.
        :param pulumi.Input[bool] allow_insecure: Do not validate the certificate when the health check uses HTTPS. Valid values: `true` or `false` (Default: `false`).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] check_regions: A list of regions from which to run health checks. If not set Cloudflare will pick a default region. Valid values: `WNAM`, `ENAM`, `WEU`, `EEU`, `NSAM`, `SSAM`, `OC`, `ME`, `NAF`, `SAF`, `IN`, `SEAS`, `NEAS`, `ALL_REGIONS`.
        :param pulumi.Input[int] consecutive_fails: The number of consecutive fails required from a health check before changing the health to unhealthy. (Default: `1`)
        :param pulumi.Input[int] consecutive_successes: The number of consecutive successes required from a health check before changing the health to healthy. (Default: `1`)
        :param pulumi.Input[str] description: A human-readable description of the health check.
        :param pulumi.Input[str] expected_body: A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] expected_codes: The expected HTTP response codes (e.g. "200") or code ranges (e.g. "2xx" for all codes starting with 2) of the health check. (Default: `["200"]`)
        :param pulumi.Input[bool] follow_redirects: Follow redirects if the origin returns a 3xx status code. Valid values: `true` or `false` (Default: `false`).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HealthcheckHeaderArgs']]]] headers: The header name.
        :param pulumi.Input[int] interval: The interval between each health check. Shorter intervals may give quicker notifications if the origin status changes, but will increase load on the origin as we check from multiple locations. (Default: `60`)
        :param pulumi.Input[str] method: The TCP connection method to use for the health check. Valid values: `connection_established` (Default: `connection_established`).
        :param pulumi.Input[str] name: A short name to identify the health check. Only alphanumeric characters, hyphens and underscores are allowed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] notification_email_addresses: A list of email addresses we want to send the notifications to.
        :param pulumi.Input[bool] notification_suspended: Whether the notifications are suspended or not. Useful for maintenance periods. Valid values: `true` or `false` (Default: `false`).
        :param pulumi.Input[str] path: The endpoint path to health check against. (Default: `/`)
        :param pulumi.Input[int] port: Port number to connect to for the health check.  Valid values are in the rage `0-65535` (Default: `80`).
        :param pulumi.Input[int] retries: The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. (Default: `2`)
        :param pulumi.Input[bool] suspended: If suspended, no health checks are sent to the origin. Valid values: `true` or `false` (Default: `false`).
        :param pulumi.Input[int] timeout: The timeout (in seconds) before marking the health check as failed. (Default: `5`)
        :param pulumi.Input[str] type: The protocol to use for the health check. Valid values: `HTTP`, `HTTPS`, `TCP`.
        :param pulumi.Input[str] zone_id: The DNS zone ID to which apply settings.
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

            if address is None:
                raise TypeError("Missing required property 'address'")
            __props__['address'] = address
            __props__['allow_insecure'] = allow_insecure
            __props__['check_regions'] = check_regions
            __props__['consecutive_fails'] = consecutive_fails
            __props__['consecutive_successes'] = consecutive_successes
            __props__['description'] = description
            __props__['expected_body'] = expected_body
            __props__['expected_codes'] = expected_codes
            __props__['follow_redirects'] = follow_redirects
            __props__['headers'] = headers
            __props__['interval'] = interval
            __props__['method'] = method
            if name is None:
                raise TypeError("Missing required property 'name'")
            __props__['name'] = name
            __props__['notification_email_addresses'] = notification_email_addresses
            __props__['notification_suspended'] = notification_suspended
            __props__['path'] = path
            __props__['port'] = port
            __props__['retries'] = retries
            __props__['suspended'] = suspended
            __props__['timeout'] = timeout
            if type is None:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
            if zone_id is None:
                raise TypeError("Missing required property 'zone_id'")
            __props__['zone_id'] = zone_id
            __props__['created_on'] = None
            __props__['modified_on'] = None
        super(Healthcheck, __self__).__init__(
            'cloudflare:index/healthcheck:Healthcheck',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            address: Optional[pulumi.Input[str]] = None,
            allow_insecure: Optional[pulumi.Input[bool]] = None,
            check_regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            consecutive_fails: Optional[pulumi.Input[int]] = None,
            consecutive_successes: Optional[pulumi.Input[int]] = None,
            created_on: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            expected_body: Optional[pulumi.Input[str]] = None,
            expected_codes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            follow_redirects: Optional[pulumi.Input[bool]] = None,
            headers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HealthcheckHeaderArgs']]]]] = None,
            interval: Optional[pulumi.Input[int]] = None,
            method: Optional[pulumi.Input[str]] = None,
            modified_on: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            notification_email_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            notification_suspended: Optional[pulumi.Input[bool]] = None,
            path: Optional[pulumi.Input[str]] = None,
            port: Optional[pulumi.Input[int]] = None,
            retries: Optional[pulumi.Input[int]] = None,
            suspended: Optional[pulumi.Input[bool]] = None,
            timeout: Optional[pulumi.Input[int]] = None,
            type: Optional[pulumi.Input[str]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'Healthcheck':
        """
        Get an existing Healthcheck resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address: The hostname or IP address of the origin server to run health checks on.
        :param pulumi.Input[bool] allow_insecure: Do not validate the certificate when the health check uses HTTPS. Valid values: `true` or `false` (Default: `false`).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] check_regions: A list of regions from which to run health checks. If not set Cloudflare will pick a default region. Valid values: `WNAM`, `ENAM`, `WEU`, `EEU`, `NSAM`, `SSAM`, `OC`, `ME`, `NAF`, `SAF`, `IN`, `SEAS`, `NEAS`, `ALL_REGIONS`.
        :param pulumi.Input[int] consecutive_fails: The number of consecutive fails required from a health check before changing the health to unhealthy. (Default: `1`)
        :param pulumi.Input[int] consecutive_successes: The number of consecutive successes required from a health check before changing the health to healthy. (Default: `1`)
        :param pulumi.Input[str] description: A human-readable description of the health check.
        :param pulumi.Input[str] expected_body: A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] expected_codes: The expected HTTP response codes (e.g. "200") or code ranges (e.g. "2xx" for all codes starting with 2) of the health check. (Default: `["200"]`)
        :param pulumi.Input[bool] follow_redirects: Follow redirects if the origin returns a 3xx status code. Valid values: `true` or `false` (Default: `false`).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HealthcheckHeaderArgs']]]] headers: The header name.
        :param pulumi.Input[int] interval: The interval between each health check. Shorter intervals may give quicker notifications if the origin status changes, but will increase load on the origin as we check from multiple locations. (Default: `60`)
        :param pulumi.Input[str] method: The TCP connection method to use for the health check. Valid values: `connection_established` (Default: `connection_established`).
        :param pulumi.Input[str] name: A short name to identify the health check. Only alphanumeric characters, hyphens and underscores are allowed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] notification_email_addresses: A list of email addresses we want to send the notifications to.
        :param pulumi.Input[bool] notification_suspended: Whether the notifications are suspended or not. Useful for maintenance periods. Valid values: `true` or `false` (Default: `false`).
        :param pulumi.Input[str] path: The endpoint path to health check against. (Default: `/`)
        :param pulumi.Input[int] port: Port number to connect to for the health check.  Valid values are in the rage `0-65535` (Default: `80`).
        :param pulumi.Input[int] retries: The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. (Default: `2`)
        :param pulumi.Input[bool] suspended: If suspended, no health checks are sent to the origin. Valid values: `true` or `false` (Default: `false`).
        :param pulumi.Input[int] timeout: The timeout (in seconds) before marking the health check as failed. (Default: `5`)
        :param pulumi.Input[str] type: The protocol to use for the health check. Valid values: `HTTP`, `HTTPS`, `TCP`.
        :param pulumi.Input[str] zone_id: The DNS zone ID to which apply settings.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["address"] = address
        __props__["allow_insecure"] = allow_insecure
        __props__["check_regions"] = check_regions
        __props__["consecutive_fails"] = consecutive_fails
        __props__["consecutive_successes"] = consecutive_successes
        __props__["created_on"] = created_on
        __props__["description"] = description
        __props__["expected_body"] = expected_body
        __props__["expected_codes"] = expected_codes
        __props__["follow_redirects"] = follow_redirects
        __props__["headers"] = headers
        __props__["interval"] = interval
        __props__["method"] = method
        __props__["modified_on"] = modified_on
        __props__["name"] = name
        __props__["notification_email_addresses"] = notification_email_addresses
        __props__["notification_suspended"] = notification_suspended
        __props__["path"] = path
        __props__["port"] = port
        __props__["retries"] = retries
        __props__["suspended"] = suspended
        __props__["timeout"] = timeout
        __props__["type"] = type
        __props__["zone_id"] = zone_id
        return Healthcheck(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def address(self) -> pulumi.Output[str]:
        """
        The hostname or IP address of the origin server to run health checks on.
        """
        return pulumi.get(self, "address")

    @property
    @pulumi.getter(name="allowInsecure")
    def allow_insecure(self) -> pulumi.Output[Optional[bool]]:
        """
        Do not validate the certificate when the health check uses HTTPS. Valid values: `true` or `false` (Default: `false`).
        """
        return pulumi.get(self, "allow_insecure")

    @property
    @pulumi.getter(name="checkRegions")
    def check_regions(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of regions from which to run health checks. If not set Cloudflare will pick a default region. Valid values: `WNAM`, `ENAM`, `WEU`, `EEU`, `NSAM`, `SSAM`, `OC`, `ME`, `NAF`, `SAF`, `IN`, `SEAS`, `NEAS`, `ALL_REGIONS`.
        """
        return pulumi.get(self, "check_regions")

    @property
    @pulumi.getter(name="consecutiveFails")
    def consecutive_fails(self) -> pulumi.Output[Optional[int]]:
        """
        The number of consecutive fails required from a health check before changing the health to unhealthy. (Default: `1`)
        """
        return pulumi.get(self, "consecutive_fails")

    @property
    @pulumi.getter(name="consecutiveSuccesses")
    def consecutive_successes(self) -> pulumi.Output[Optional[int]]:
        """
        The number of consecutive successes required from a health check before changing the health to healthy. (Default: `1`)
        """
        return pulumi.get(self, "consecutive_successes")

    @property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> pulumi.Output[str]:
        return pulumi.get(self, "created_on")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A human-readable description of the health check.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="expectedBody")
    def expected_body(self) -> pulumi.Output[Optional[str]]:
        """
        A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy.
        """
        return pulumi.get(self, "expected_body")

    @property
    @pulumi.getter(name="expectedCodes")
    def expected_codes(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The expected HTTP response codes (e.g. "200") or code ranges (e.g. "2xx" for all codes starting with 2) of the health check. (Default: `["200"]`)
        """
        return pulumi.get(self, "expected_codes")

    @property
    @pulumi.getter(name="followRedirects")
    def follow_redirects(self) -> pulumi.Output[Optional[bool]]:
        """
        Follow redirects if the origin returns a 3xx status code. Valid values: `true` or `false` (Default: `false`).
        """
        return pulumi.get(self, "follow_redirects")

    @property
    @pulumi.getter
    def headers(self) -> pulumi.Output[Optional[Sequence['outputs.HealthcheckHeader']]]:
        """
        The header name.
        """
        return pulumi.get(self, "headers")

    @property
    @pulumi.getter
    def interval(self) -> pulumi.Output[Optional[int]]:
        """
        The interval between each health check. Shorter intervals may give quicker notifications if the origin status changes, but will increase load on the origin as we check from multiple locations. (Default: `60`)
        """
        return pulumi.get(self, "interval")

    @property
    @pulumi.getter
    def method(self) -> pulumi.Output[str]:
        """
        The TCP connection method to use for the health check. Valid values: `connection_established` (Default: `connection_established`).
        """
        return pulumi.get(self, "method")

    @property
    @pulumi.getter(name="modifiedOn")
    def modified_on(self) -> pulumi.Output[str]:
        return pulumi.get(self, "modified_on")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A short name to identify the health check. Only alphanumeric characters, hyphens and underscores are allowed.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notificationEmailAddresses")
    def notification_email_addresses(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of email addresses we want to send the notifications to.
        """
        return pulumi.get(self, "notification_email_addresses")

    @property
    @pulumi.getter(name="notificationSuspended")
    def notification_suspended(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether the notifications are suspended or not. Useful for maintenance periods. Valid values: `true` or `false` (Default: `false`).
        """
        return pulumi.get(self, "notification_suspended")

    @property
    @pulumi.getter
    def path(self) -> pulumi.Output[Optional[str]]:
        """
        The endpoint path to health check against. (Default: `/`)
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[Optional[int]]:
        """
        Port number to connect to for the health check.  Valid values are in the rage `0-65535` (Default: `80`).
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def retries(self) -> pulumi.Output[Optional[int]]:
        """
        The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. (Default: `2`)
        """
        return pulumi.get(self, "retries")

    @property
    @pulumi.getter
    def suspended(self) -> pulumi.Output[Optional[bool]]:
        """
        If suspended, no health checks are sent to the origin. Valid values: `true` or `false` (Default: `false`).
        """
        return pulumi.get(self, "suspended")

    @property
    @pulumi.getter
    def timeout(self) -> pulumi.Output[Optional[int]]:
        """
        The timeout (in seconds) before marking the health check as failed. (Default: `5`)
        """
        return pulumi.get(self, "timeout")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The protocol to use for the health check. Valid values: `HTTP`, `HTTPS`, `TCP`.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        The DNS zone ID to which apply settings.
        """
        return pulumi.get(self, "zone_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

