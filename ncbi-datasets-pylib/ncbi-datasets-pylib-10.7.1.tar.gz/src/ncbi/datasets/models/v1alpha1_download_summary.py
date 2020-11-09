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


class V1alpha1DownloadSummary(object):
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
        'assembly_count': 'int',
        'dehydrated': 'DownloadSummaryDehydrated',
        'errors': 'list[Datasetsv1alpha1Error]',
        'hydrated': 'DownloadSummaryHydrated',
        'messages': 'list[V1alpha1Message]',
        'record_count': 'int',
        'resource_updated_on': 'datetime'
    }

    attribute_map = {
        'assembly_count': 'assembly_count',
        'dehydrated': 'dehydrated',
        'errors': 'errors',
        'hydrated': 'hydrated',
        'messages': 'messages',
        'record_count': 'record_count',
        'resource_updated_on': 'resource_updated_on'
    }

    def __init__(self, assembly_count=None, dehydrated=None, errors=None, hydrated=None, messages=None, record_count=None, resource_updated_on=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1DownloadSummary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._assembly_count = None
        self._dehydrated = None
        self._errors = None
        self._hydrated = None
        self._messages = None
        self._record_count = None
        self._resource_updated_on = None
        self.discriminator = None

        if assembly_count is not None:
            self.assembly_count = assembly_count
        if dehydrated is not None:
            self.dehydrated = dehydrated
        if errors is not None:
            self.errors = errors
        if hydrated is not None:
            self.hydrated = hydrated
        if messages is not None:
            self.messages = messages
        if record_count is not None:
            self.record_count = record_count
        if resource_updated_on is not None:
            self.resource_updated_on = resource_updated_on

    @property
    def assembly_count(self):
        """Gets the assembly_count of this V1alpha1DownloadSummary.  # noqa: E501


        :return: The assembly_count of this V1alpha1DownloadSummary.  # noqa: E501
        :rtype: int
        """
        return self._assembly_count

    @assembly_count.setter
    def assembly_count(self, assembly_count):
        """Sets the assembly_count of this V1alpha1DownloadSummary.


        :param assembly_count: The assembly_count of this V1alpha1DownloadSummary.  # noqa: E501
        :type: int
        """

        self._assembly_count = assembly_count

    @property
    def dehydrated(self):
        """Gets the dehydrated of this V1alpha1DownloadSummary.  # noqa: E501


        :return: The dehydrated of this V1alpha1DownloadSummary.  # noqa: E501
        :rtype: DownloadSummaryDehydrated
        """
        return self._dehydrated

    @dehydrated.setter
    def dehydrated(self, dehydrated):
        """Sets the dehydrated of this V1alpha1DownloadSummary.


        :param dehydrated: The dehydrated of this V1alpha1DownloadSummary.  # noqa: E501
        :type: DownloadSummaryDehydrated
        """

        self._dehydrated = dehydrated

    @property
    def errors(self):
        """Gets the errors of this V1alpha1DownloadSummary.  # noqa: E501


        :return: The errors of this V1alpha1DownloadSummary.  # noqa: E501
        :rtype: list[Datasetsv1alpha1Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this V1alpha1DownloadSummary.


        :param errors: The errors of this V1alpha1DownloadSummary.  # noqa: E501
        :type: list[Datasetsv1alpha1Error]
        """

        self._errors = errors

    @property
    def hydrated(self):
        """Gets the hydrated of this V1alpha1DownloadSummary.  # noqa: E501


        :return: The hydrated of this V1alpha1DownloadSummary.  # noqa: E501
        :rtype: DownloadSummaryHydrated
        """
        return self._hydrated

    @hydrated.setter
    def hydrated(self, hydrated):
        """Sets the hydrated of this V1alpha1DownloadSummary.


        :param hydrated: The hydrated of this V1alpha1DownloadSummary.  # noqa: E501
        :type: DownloadSummaryHydrated
        """

        self._hydrated = hydrated

    @property
    def messages(self):
        """Gets the messages of this V1alpha1DownloadSummary.  # noqa: E501


        :return: The messages of this V1alpha1DownloadSummary.  # noqa: E501
        :rtype: list[V1alpha1Message]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this V1alpha1DownloadSummary.


        :param messages: The messages of this V1alpha1DownloadSummary.  # noqa: E501
        :type: list[V1alpha1Message]
        """

        self._messages = messages

    @property
    def record_count(self):
        """Gets the record_count of this V1alpha1DownloadSummary.  # noqa: E501

        The number of records for the requested filter.  # noqa: E501

        :return: The record_count of this V1alpha1DownloadSummary.  # noqa: E501
        :rtype: int
        """
        return self._record_count

    @record_count.setter
    def record_count(self, record_count):
        """Sets the record_count of this V1alpha1DownloadSummary.

        The number of records for the requested filter.  # noqa: E501

        :param record_count: The record_count of this V1alpha1DownloadSummary.  # noqa: E501
        :type: int
        """

        self._record_count = record_count

    @property
    def resource_updated_on(self):
        """Gets the resource_updated_on of this V1alpha1DownloadSummary.  # noqa: E501

        The latest date on which the resource was updated.  # noqa: E501

        :return: The resource_updated_on of this V1alpha1DownloadSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._resource_updated_on

    @resource_updated_on.setter
    def resource_updated_on(self, resource_updated_on):
        """Sets the resource_updated_on of this V1alpha1DownloadSummary.

        The latest date on which the resource was updated.  # noqa: E501

        :param resource_updated_on: The resource_updated_on of this V1alpha1DownloadSummary.  # noqa: E501
        :type: datetime
        """

        self._resource_updated_on = resource_updated_on

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
        if not isinstance(other, V1alpha1DownloadSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1DownloadSummary):
            return True

        return self.to_dict() != other.to_dict()
