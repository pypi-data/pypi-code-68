# coding: utf-8

"""
    Agilicus API

    Agilicus API endpoints  # noqa: E501

    The version of the OpenAPI document: 2020.11.06
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from agilicus_api.configuration import Configuration


class UserIdentityUpdateSpec(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'primary_email': 'str',
        'first_name': 'str',
        'last_name': 'str'
    }

    attribute_map = {
        'primary_email': 'primary_email',
        'first_name': 'first_name',
        'last_name': 'last_name'
    }

    def __init__(self, primary_email=None, first_name=None, last_name=None, local_vars_configuration=None):  # noqa: E501
        """UserIdentityUpdateSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._primary_email = None
        self._first_name = None
        self._last_name = None
        self.discriminator = None

        if primary_email is not None:
            self.primary_email = primary_email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name

    @property
    def primary_email(self):
        """Gets the primary_email of this UserIdentityUpdateSpec.  # noqa: E501

        User's email address  # noqa: E501

        :return: The primary_email of this UserIdentityUpdateSpec.  # noqa: E501
        :rtype: str
        """
        return self._primary_email

    @primary_email.setter
    def primary_email(self, primary_email):
        """Sets the primary_email of this UserIdentityUpdateSpec.

        User's email address  # noqa: E501

        :param primary_email: The primary_email of this UserIdentityUpdateSpec.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                primary_email is not None and len(primary_email) > 100):
            raise ValueError("Invalid value for `primary_email`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                primary_email is not None and len(primary_email) < 0):
            raise ValueError("Invalid value for `primary_email`, length must be greater than or equal to `0`")  # noqa: E501

        self._primary_email = primary_email

    @property
    def first_name(self):
        """Gets the first_name of this UserIdentityUpdateSpec.  # noqa: E501

        User's first name  # noqa: E501

        :return: The first_name of this UserIdentityUpdateSpec.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserIdentityUpdateSpec.

        User's first name  # noqa: E501

        :param first_name: The first_name of this UserIdentityUpdateSpec.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                first_name is not None and len(first_name) > 100):
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                first_name is not None and len(first_name) < 1):
            raise ValueError("Invalid value for `first_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UserIdentityUpdateSpec.  # noqa: E501

        User's last name  # noqa: E501

        :return: The last_name of this UserIdentityUpdateSpec.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserIdentityUpdateSpec.

        User's last name  # noqa: E501

        :param last_name: The last_name of this UserIdentityUpdateSpec.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                last_name is not None and len(last_name) > 100):
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                last_name is not None and len(last_name) < 0):
            raise ValueError("Invalid value for `last_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._last_name = last_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserIdentityUpdateSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserIdentityUpdateSpec):
            return True

        return self.to_dict() != other.to_dict()
