# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Order']


class Order(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 components: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 coupon_id: Optional[pulumi.Input[str]] = None,
                 duration: Optional[pulumi.Input[int]] = None,
                 package_version: Optional[pulumi.Input[str]] = None,
                 pay_type: Optional[pulumi.Input[str]] = None,
                 pricing_cycle: Optional[pulumi.Input[str]] = None,
                 product_code: Optional[pulumi.Input[str]] = None,
                 quantity: Optional[pulumi.Input[int]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Create a Order resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] components: Service providers customize additional components.
        :param pulumi.Input[str] coupon_id: The coupon id of the market product.
        :param pulumi.Input[int] duration: The number of purchase cycles.
        :param pulumi.Input[str] package_version: The package version of the market product.
        :param pulumi.Input[str] pay_type: Valid values are `PrePaid`, `PostPaid`,System default to `PostPaid`.
        :param pulumi.Input[str] pricing_cycle: The purchase cycle of the product, valid values are `Day`, `Month` and `Year`.
        :param pulumi.Input[str] product_code: The product_code of market place product.
        :param pulumi.Input[int] quantity: The quantity of the market product will be purchased.
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

            __props__['components'] = components
            __props__['coupon_id'] = coupon_id
            __props__['duration'] = duration
            if package_version is None:
                raise TypeError("Missing required property 'package_version'")
            __props__['package_version'] = package_version
            __props__['pay_type'] = pay_type
            if pricing_cycle is None:
                raise TypeError("Missing required property 'pricing_cycle'")
            __props__['pricing_cycle'] = pricing_cycle
            if product_code is None:
                raise TypeError("Missing required property 'product_code'")
            __props__['product_code'] = product_code
            __props__['quantity'] = quantity
        super(Order, __self__).__init__(
            'alicloud:marketplace/order:Order',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            components: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            coupon_id: Optional[pulumi.Input[str]] = None,
            duration: Optional[pulumi.Input[int]] = None,
            package_version: Optional[pulumi.Input[str]] = None,
            pay_type: Optional[pulumi.Input[str]] = None,
            pricing_cycle: Optional[pulumi.Input[str]] = None,
            product_code: Optional[pulumi.Input[str]] = None,
            quantity: Optional[pulumi.Input[int]] = None) -> 'Order':
        """
        Get an existing Order resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] components: Service providers customize additional components.
        :param pulumi.Input[str] coupon_id: The coupon id of the market product.
        :param pulumi.Input[int] duration: The number of purchase cycles.
        :param pulumi.Input[str] package_version: The package version of the market product.
        :param pulumi.Input[str] pay_type: Valid values are `PrePaid`, `PostPaid`,System default to `PostPaid`.
        :param pulumi.Input[str] pricing_cycle: The purchase cycle of the product, valid values are `Day`, `Month` and `Year`.
        :param pulumi.Input[str] product_code: The product_code of market place product.
        :param pulumi.Input[int] quantity: The quantity of the market product will be purchased.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["components"] = components
        __props__["coupon_id"] = coupon_id
        __props__["duration"] = duration
        __props__["package_version"] = package_version
        __props__["pay_type"] = pay_type
        __props__["pricing_cycle"] = pricing_cycle
        __props__["product_code"] = product_code
        __props__["quantity"] = quantity
        return Order(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def components(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        Service providers customize additional components.
        """
        return pulumi.get(self, "components")

    @property
    @pulumi.getter(name="couponId")
    def coupon_id(self) -> pulumi.Output[Optional[str]]:
        """
        The coupon id of the market product.
        """
        return pulumi.get(self, "coupon_id")

    @property
    @pulumi.getter
    def duration(self) -> pulumi.Output[Optional[int]]:
        """
        The number of purchase cycles.
        """
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter(name="packageVersion")
    def package_version(self) -> pulumi.Output[str]:
        """
        The package version of the market product.
        """
        return pulumi.get(self, "package_version")

    @property
    @pulumi.getter(name="payType")
    def pay_type(self) -> pulumi.Output[Optional[str]]:
        """
        Valid values are `PrePaid`, `PostPaid`,System default to `PostPaid`.
        """
        return pulumi.get(self, "pay_type")

    @property
    @pulumi.getter(name="pricingCycle")
    def pricing_cycle(self) -> pulumi.Output[str]:
        """
        The purchase cycle of the product, valid values are `Day`, `Month` and `Year`.
        """
        return pulumi.get(self, "pricing_cycle")

    @property
    @pulumi.getter(name="productCode")
    def product_code(self) -> pulumi.Output[str]:
        """
        The product_code of market place product.
        """
        return pulumi.get(self, "product_code")

    @property
    @pulumi.getter
    def quantity(self) -> pulumi.Output[Optional[int]]:
        """
        The quantity of the market product will be purchased.
        """
        return pulumi.get(self, "quantity")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

