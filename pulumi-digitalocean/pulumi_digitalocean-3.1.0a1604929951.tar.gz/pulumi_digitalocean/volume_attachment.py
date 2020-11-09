# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['VolumeAttachment']


class VolumeAttachment(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 droplet_id: Optional[pulumi.Input[int]] = None,
                 volume_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages attaching a Volume to a Droplet.

        > **NOTE:** Volumes can be attached either directly on the `Droplet` resource, or using the `VolumeAttachment` resource - but the two cannot be used together. If both are used against the same Droplet, the volume attachments will constantly drift.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_digitalocean as digitalocean

        foobar_volume = digitalocean.Volume("foobarVolume",
            region="nyc1",
            size=100,
            initial_filesystem_type="ext4",
            description="an example volume")
        foobar_droplet = digitalocean.Droplet("foobarDroplet",
            size="s-1vcpu-1gb",
            image="ubuntu-18-04-x64",
            region="nyc1")
        foobar_volume_attachment = digitalocean.VolumeAttachment("foobarVolumeAttachment",
            droplet_id=foobar_droplet.id,
            volume_id=foobar_volume.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] droplet_id: ID of the Droplet to attach the volume to.
        :param pulumi.Input[str] volume_id: ID of the Volume to be attached to the Droplet.
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

            if droplet_id is None:
                raise TypeError("Missing required property 'droplet_id'")
            __props__['droplet_id'] = droplet_id
            if volume_id is None:
                raise TypeError("Missing required property 'volume_id'")
            __props__['volume_id'] = volume_id
        super(VolumeAttachment, __self__).__init__(
            'digitalocean:index/volumeAttachment:VolumeAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            droplet_id: Optional[pulumi.Input[int]] = None,
            volume_id: Optional[pulumi.Input[str]] = None) -> 'VolumeAttachment':
        """
        Get an existing VolumeAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] droplet_id: ID of the Droplet to attach the volume to.
        :param pulumi.Input[str] volume_id: ID of the Volume to be attached to the Droplet.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["droplet_id"] = droplet_id
        __props__["volume_id"] = volume_id
        return VolumeAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dropletId")
    def droplet_id(self) -> pulumi.Output[int]:
        """
        ID of the Droplet to attach the volume to.
        """
        return pulumi.get(self, "droplet_id")

    @property
    @pulumi.getter(name="volumeId")
    def volume_id(self) -> pulumi.Output[str]:
        """
        ID of the Volume to be attached to the Droplet.
        """
        return pulumi.get(self, "volume_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

