# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['User']


class User(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 can_create_group: Optional[pulumi.Input[bool]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 is_admin: Optional[pulumi.Input[bool]] = None,
                 is_external: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 projects_limit: Optional[pulumi.Input[int]] = None,
                 reset_password: Optional[pulumi.Input[bool]] = None,
                 skip_confirmation: Optional[pulumi.Input[bool]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Create a User resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] can_create_group: Boolean, defaults to false. Whether to allow the user to create groups.
        :param pulumi.Input[str] email: The e-mail address of the user.
        :param pulumi.Input[bool] is_admin: Boolean, defaults to false.  Whether to enable administrative priviledges
               for the user.
        :param pulumi.Input[bool] is_external: Boolean, defaults to false. Whether a user has access only to some internal or private projects. External users can only access projects to which they are explicitly granted access.
        :param pulumi.Input[str] name: The name of the user.
        :param pulumi.Input[str] password: The password of the user.
        :param pulumi.Input[int] projects_limit: Integer, defaults to 0.  Number of projects user can create.
        :param pulumi.Input[bool] reset_password: Boolean, defaults to false. Send user password reset link.
        :param pulumi.Input[bool] skip_confirmation: Boolean, defaults to true. Whether to skip confirmation.
        :param pulumi.Input[str] username: The username of the user.
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

            __props__['can_create_group'] = can_create_group
            if email is None:
                raise TypeError("Missing required property 'email'")
            __props__['email'] = email
            __props__['is_admin'] = is_admin
            __props__['is_external'] = is_external
            __props__['name'] = name
            __props__['password'] = password
            __props__['projects_limit'] = projects_limit
            __props__['reset_password'] = reset_password
            __props__['skip_confirmation'] = skip_confirmation
            if username is None:
                raise TypeError("Missing required property 'username'")
            __props__['username'] = username
        super(User, __self__).__init__(
            'gitlab:index/user:User',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            can_create_group: Optional[pulumi.Input[bool]] = None,
            email: Optional[pulumi.Input[str]] = None,
            is_admin: Optional[pulumi.Input[bool]] = None,
            is_external: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            password: Optional[pulumi.Input[str]] = None,
            projects_limit: Optional[pulumi.Input[int]] = None,
            reset_password: Optional[pulumi.Input[bool]] = None,
            skip_confirmation: Optional[pulumi.Input[bool]] = None,
            username: Optional[pulumi.Input[str]] = None) -> 'User':
        """
        Get an existing User resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] can_create_group: Boolean, defaults to false. Whether to allow the user to create groups.
        :param pulumi.Input[str] email: The e-mail address of the user.
        :param pulumi.Input[bool] is_admin: Boolean, defaults to false.  Whether to enable administrative priviledges
               for the user.
        :param pulumi.Input[bool] is_external: Boolean, defaults to false. Whether a user has access only to some internal or private projects. External users can only access projects to which they are explicitly granted access.
        :param pulumi.Input[str] name: The name of the user.
        :param pulumi.Input[str] password: The password of the user.
        :param pulumi.Input[int] projects_limit: Integer, defaults to 0.  Number of projects user can create.
        :param pulumi.Input[bool] reset_password: Boolean, defaults to false. Send user password reset link.
        :param pulumi.Input[bool] skip_confirmation: Boolean, defaults to true. Whether to skip confirmation.
        :param pulumi.Input[str] username: The username of the user.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["can_create_group"] = can_create_group
        __props__["email"] = email
        __props__["is_admin"] = is_admin
        __props__["is_external"] = is_external
        __props__["name"] = name
        __props__["password"] = password
        __props__["projects_limit"] = projects_limit
        __props__["reset_password"] = reset_password
        __props__["skip_confirmation"] = skip_confirmation
        __props__["username"] = username
        return User(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="canCreateGroup")
    def can_create_group(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean, defaults to false. Whether to allow the user to create groups.
        """
        return pulumi.get(self, "can_create_group")

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[str]:
        """
        The e-mail address of the user.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="isAdmin")
    def is_admin(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean, defaults to false.  Whether to enable administrative priviledges
        for the user.
        """
        return pulumi.get(self, "is_admin")

    @property
    @pulumi.getter(name="isExternal")
    def is_external(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean, defaults to false. Whether a user has access only to some internal or private projects. External users can only access projects to which they are explicitly granted access.
        """
        return pulumi.get(self, "is_external")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the user.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[str]]:
        """
        The password of the user.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="projectsLimit")
    def projects_limit(self) -> pulumi.Output[Optional[int]]:
        """
        Integer, defaults to 0.  Number of projects user can create.
        """
        return pulumi.get(self, "projects_limit")

    @property
    @pulumi.getter(name="resetPassword")
    def reset_password(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean, defaults to false. Send user password reset link.
        """
        return pulumi.get(self, "reset_password")

    @property
    @pulumi.getter(name="skipConfirmation")
    def skip_confirmation(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean, defaults to true. Whether to skip confirmation.
        """
        return pulumi.get(self, "skip_confirmation")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[str]:
        """
        The username of the user.
        """
        return pulumi.get(self, "username")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

