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


class OIDCProxyConfig(object):
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
        'headers': 'OIDCProxyHeader',
        'domain_mapping': 'OIDCProxyDomainMapping',
        'auth': 'OIDCAuthConfig',
        'content_manipulation': 'OIDCProxyContentManipulation'
    }

    attribute_map = {
        'headers': 'headers',
        'domain_mapping': 'domain_mapping',
        'auth': 'auth',
        'content_manipulation': 'content_manipulation'
    }

    def __init__(self, headers=None, domain_mapping=None, auth=None, content_manipulation=None, local_vars_configuration=None):  # noqa: E501
        """OIDCProxyConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._headers = None
        self._domain_mapping = None
        self._auth = None
        self._content_manipulation = None
        self.discriminator = None

        self.headers = headers
        self.domain_mapping = domain_mapping
        if auth is not None:
            self.auth = auth
        self.content_manipulation = content_manipulation

    @property
    def headers(self):
        """Gets the headers of this OIDCProxyConfig.  # noqa: E501


        :return: The headers of this OIDCProxyConfig.  # noqa: E501
        :rtype: OIDCProxyHeader
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this OIDCProxyConfig.


        :param headers: The headers of this OIDCProxyConfig.  # noqa: E501
        :type: OIDCProxyHeader
        """
        if self.local_vars_configuration.client_side_validation and headers is None:  # noqa: E501
            raise ValueError("Invalid value for `headers`, must not be `None`")  # noqa: E501

        self._headers = headers

    @property
    def domain_mapping(self):
        """Gets the domain_mapping of this OIDCProxyConfig.  # noqa: E501


        :return: The domain_mapping of this OIDCProxyConfig.  # noqa: E501
        :rtype: OIDCProxyDomainMapping
        """
        return self._domain_mapping

    @domain_mapping.setter
    def domain_mapping(self, domain_mapping):
        """Sets the domain_mapping of this OIDCProxyConfig.


        :param domain_mapping: The domain_mapping of this OIDCProxyConfig.  # noqa: E501
        :type: OIDCProxyDomainMapping
        """
        if self.local_vars_configuration.client_side_validation and domain_mapping is None:  # noqa: E501
            raise ValueError("Invalid value for `domain_mapping`, must not be `None`")  # noqa: E501

        self._domain_mapping = domain_mapping

    @property
    def auth(self):
        """Gets the auth of this OIDCProxyConfig.  # noqa: E501


        :return: The auth of this OIDCProxyConfig.  # noqa: E501
        :rtype: OIDCAuthConfig
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this OIDCProxyConfig.


        :param auth: The auth of this OIDCProxyConfig.  # noqa: E501
        :type: OIDCAuthConfig
        """

        self._auth = auth

    @property
    def content_manipulation(self):
        """Gets the content_manipulation of this OIDCProxyConfig.  # noqa: E501


        :return: The content_manipulation of this OIDCProxyConfig.  # noqa: E501
        :rtype: OIDCProxyContentManipulation
        """
        return self._content_manipulation

    @content_manipulation.setter
    def content_manipulation(self, content_manipulation):
        """Sets the content_manipulation of this OIDCProxyConfig.


        :param content_manipulation: The content_manipulation of this OIDCProxyConfig.  # noqa: E501
        :type: OIDCProxyContentManipulation
        """
        if self.local_vars_configuration.client_side_validation and content_manipulation is None:  # noqa: E501
            raise ValueError("Invalid value for `content_manipulation`, must not be `None`")  # noqa: E501

        self._content_manipulation = content_manipulation

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
        if not isinstance(other, OIDCProxyConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OIDCProxyConfig):
            return True

        return self.to_dict() != other.to_dict()
