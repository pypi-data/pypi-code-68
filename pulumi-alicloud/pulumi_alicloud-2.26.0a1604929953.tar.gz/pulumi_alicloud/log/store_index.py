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

__all__ = ['StoreIndex']


class StoreIndex(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 field_searches: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StoreIndexFieldSearchArgs']]]]] = None,
                 full_text: Optional[pulumi.Input[pulumi.InputType['StoreIndexFullTextArgs']]] = None,
                 logstore: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Create a StoreIndex resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StoreIndexFieldSearchArgs']]]] field_searches: List configurations of field search index. Valid item as follows:
        :param pulumi.Input[pulumi.InputType['StoreIndexFullTextArgs']] full_text: The configuration of full text index. Valid item as follows:
        :param pulumi.Input[str] logstore: The log store name to the query index belongs.
        :param pulumi.Input[str] project: The project name to the log store belongs.
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

            __props__['field_searches'] = field_searches
            __props__['full_text'] = full_text
            if logstore is None:
                raise TypeError("Missing required property 'logstore'")
            __props__['logstore'] = logstore
            if project is None:
                raise TypeError("Missing required property 'project'")
            __props__['project'] = project
        super(StoreIndex, __self__).__init__(
            'alicloud:log/storeIndex:StoreIndex',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            field_searches: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StoreIndexFieldSearchArgs']]]]] = None,
            full_text: Optional[pulumi.Input[pulumi.InputType['StoreIndexFullTextArgs']]] = None,
            logstore: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None) -> 'StoreIndex':
        """
        Get an existing StoreIndex resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['StoreIndexFieldSearchArgs']]]] field_searches: List configurations of field search index. Valid item as follows:
        :param pulumi.Input[pulumi.InputType['StoreIndexFullTextArgs']] full_text: The configuration of full text index. Valid item as follows:
        :param pulumi.Input[str] logstore: The log store name to the query index belongs.
        :param pulumi.Input[str] project: The project name to the log store belongs.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["field_searches"] = field_searches
        __props__["full_text"] = full_text
        __props__["logstore"] = logstore
        __props__["project"] = project
        return StoreIndex(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="fieldSearches")
    def field_searches(self) -> pulumi.Output[Optional[Sequence['outputs.StoreIndexFieldSearch']]]:
        """
        List configurations of field search index. Valid item as follows:
        """
        return pulumi.get(self, "field_searches")

    @property
    @pulumi.getter(name="fullText")
    def full_text(self) -> pulumi.Output[Optional['outputs.StoreIndexFullText']]:
        """
        The configuration of full text index. Valid item as follows:
        """
        return pulumi.get(self, "full_text")

    @property
    @pulumi.getter
    def logstore(self) -> pulumi.Output[str]:
        """
        The log store name to the query index belongs.
        """
        return pulumi.get(self, "logstore")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The project name to the log store belongs.
        """
        return pulumi.get(self, "project")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

