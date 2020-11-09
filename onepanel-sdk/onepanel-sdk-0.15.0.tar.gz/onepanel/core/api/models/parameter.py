# coding: utf-8

"""
    Onepanel

    Onepanel API  # noqa: E501

    The version of the OpenAPI document: 0.15.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from onepanel.core.api.configuration import Configuration


class Parameter(object):
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
        'name': 'str',
        'value': 'str',
        'type': 'str',
        'display_name': 'str',
        'hint': 'str',
        'required': 'bool',
        'visibility': 'str',
        'options': 'list[ParameterOption]'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'type': 'type',
        'display_name': 'displayName',
        'hint': 'hint',
        'required': 'required',
        'visibility': 'visibility',
        'options': 'options'
    }

    def __init__(self, name=None, value=None, type=None, display_name=None, hint=None, required=None, visibility=None, options=None, local_vars_configuration=None):  # noqa: E501
        """Parameter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._value = None
        self._type = None
        self._display_name = None
        self._hint = None
        self._required = None
        self._visibility = None
        self._options = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if type is not None:
            self.type = type
        if display_name is not None:
            self.display_name = display_name
        if hint is not None:
            self.hint = hint
        if required is not None:
            self.required = required
        if visibility is not None:
            self.visibility = visibility
        if options is not None:
            self.options = options

    @property
    def name(self):
        """Gets the name of this Parameter.  # noqa: E501


        :return: The name of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Parameter.


        :param name: The name of this Parameter.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this Parameter.  # noqa: E501


        :return: The value of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Parameter.


        :param value: The value of this Parameter.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def type(self):
        """Gets the type of this Parameter.  # noqa: E501


        :return: The type of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Parameter.


        :param type: The type of this Parameter.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def display_name(self):
        """Gets the display_name of this Parameter.  # noqa: E501


        :return: The display_name of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Parameter.


        :param display_name: The display_name of this Parameter.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def hint(self):
        """Gets the hint of this Parameter.  # noqa: E501


        :return: The hint of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._hint

    @hint.setter
    def hint(self, hint):
        """Sets the hint of this Parameter.


        :param hint: The hint of this Parameter.  # noqa: E501
        :type: str
        """

        self._hint = hint

    @property
    def required(self):
        """Gets the required of this Parameter.  # noqa: E501


        :return: The required of this Parameter.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this Parameter.


        :param required: The required of this Parameter.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def visibility(self):
        """Gets the visibility of this Parameter.  # noqa: E501


        :return: The visibility of this Parameter.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this Parameter.


        :param visibility: The visibility of this Parameter.  # noqa: E501
        :type: str
        """

        self._visibility = visibility

    @property
    def options(self):
        """Gets the options of this Parameter.  # noqa: E501


        :return: The options of this Parameter.  # noqa: E501
        :rtype: list[ParameterOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this Parameter.


        :param options: The options of this Parameter.  # noqa: E501
        :type: list[ParameterOption]
        """

        self._options = options

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
        if not isinstance(other, Parameter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Parameter):
            return True

        return self.to_dict() != other.to_dict()
