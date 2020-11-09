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


class V1alpha1BioProject(object):
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
        'accession': 'str',
        'parent_accession': 'str',
        'title': 'str'
    }

    attribute_map = {
        'accession': 'accession',
        'parent_accession': 'parent_accession',
        'title': 'title'
    }

    def __init__(self, accession=None, parent_accession=None, title=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1BioProject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._accession = None
        self._parent_accession = None
        self._title = None
        self.discriminator = None

        if accession is not None:
            self.accession = accession
        if parent_accession is not None:
            self.parent_accession = parent_accession
        if title is not None:
            self.title = title

    @property
    def accession(self):
        """Gets the accession of this V1alpha1BioProject.  # noqa: E501


        :return: The accession of this V1alpha1BioProject.  # noqa: E501
        :rtype: str
        """
        return self._accession

    @accession.setter
    def accession(self, accession):
        """Sets the accession of this V1alpha1BioProject.


        :param accession: The accession of this V1alpha1BioProject.  # noqa: E501
        :type: str
        """

        self._accession = accession

    @property
    def parent_accession(self):
        """Gets the parent_accession of this V1alpha1BioProject.  # noqa: E501


        :return: The parent_accession of this V1alpha1BioProject.  # noqa: E501
        :rtype: str
        """
        return self._parent_accession

    @parent_accession.setter
    def parent_accession(self, parent_accession):
        """Sets the parent_accession of this V1alpha1BioProject.


        :param parent_accession: The parent_accession of this V1alpha1BioProject.  # noqa: E501
        :type: str
        """

        self._parent_accession = parent_accession

    @property
    def title(self):
        """Gets the title of this V1alpha1BioProject.  # noqa: E501


        :return: The title of this V1alpha1BioProject.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this V1alpha1BioProject.


        :param title: The title of this V1alpha1BioProject.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if not isinstance(other, V1alpha1BioProject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1BioProject):
            return True

        return self.to_dict() != other.to_dict()
