# coding: utf-8

"""
    NCBI Datasets API

    NCBI service to query and download biological sequence data across all domains of life from NCBI databases.  # noqa: E501

    The version of the OpenAPI document: v1alpha
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ncbi.datasets.configuration import Configuration


class V1alpha1GeneMatch(object):
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
        'gene': 'V1alpha1GeneDescriptor',
        'messages': 'list[V1alpha1Message]'
    }

    attribute_map = {
        'gene': 'gene',
        'messages': 'messages'
    }

    def __init__(self, gene=None, messages=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1GeneMatch - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._gene = None
        self._messages = None
        self.discriminator = None

        if gene is not None:
            self.gene = gene
        if messages is not None:
            self.messages = messages

    @property
    def gene(self):
        """Gets the gene of this V1alpha1GeneMatch.  # noqa: E501


        :return: The gene of this V1alpha1GeneMatch.  # noqa: E501
        :rtype: V1alpha1GeneDescriptor
        """
        return self._gene

    @gene.setter
    def gene(self, gene):
        """Sets the gene of this V1alpha1GeneMatch.


        :param gene: The gene of this V1alpha1GeneMatch.  # noqa: E501
        :type: V1alpha1GeneDescriptor
        """

        self._gene = gene

    @property
    def messages(self):
        """Gets the messages of this V1alpha1GeneMatch.  # noqa: E501


        :return: The messages of this V1alpha1GeneMatch.  # noqa: E501
        :rtype: list[V1alpha1Message]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this V1alpha1GeneMatch.


        :param messages: The messages of this V1alpha1GeneMatch.  # noqa: E501
        :type: list[V1alpha1Message]
        """

        self._messages = messages

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
        if not isinstance(other, V1alpha1GeneMatch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1GeneMatch):
            return True

        return self.to_dict() != other.to_dict()
