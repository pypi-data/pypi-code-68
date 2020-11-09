# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulp_rpm.configuration import Configuration


class RpmRpmRepositoryResponse(object):
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
        'pulp_href': 'str',
        'pulp_created': 'datetime',
        'versions_href': 'str',
        'latest_version_href': 'str',
        'name': 'str',
        'description': 'str',
        'remote': 'str',
        'metadata_signing_service': 'str',
        'retain_package_versions': 'int'
    }

    attribute_map = {
        'pulp_href': 'pulp_href',
        'pulp_created': 'pulp_created',
        'versions_href': 'versions_href',
        'latest_version_href': 'latest_version_href',
        'name': 'name',
        'description': 'description',
        'remote': 'remote',
        'metadata_signing_service': 'metadata_signing_service',
        'retain_package_versions': 'retain_package_versions'
    }

    def __init__(self, pulp_href=None, pulp_created=None, versions_href=None, latest_version_href=None, name=None, description=None, remote=None, metadata_signing_service=None, retain_package_versions=None, local_vars_configuration=None):  # noqa: E501
        """RpmRpmRepositoryResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pulp_href = None
        self._pulp_created = None
        self._versions_href = None
        self._latest_version_href = None
        self._name = None
        self._description = None
        self._remote = None
        self._metadata_signing_service = None
        self._retain_package_versions = None
        self.discriminator = None

        if pulp_href is not None:
            self.pulp_href = pulp_href
        if pulp_created is not None:
            self.pulp_created = pulp_created
        if versions_href is not None:
            self.versions_href = versions_href
        if latest_version_href is not None:
            self.latest_version_href = latest_version_href
        self.name = name
        self.description = description
        self.remote = remote
        self.metadata_signing_service = metadata_signing_service
        if retain_package_versions is not None:
            self.retain_package_versions = retain_package_versions

    @property
    def pulp_href(self):
        """Gets the pulp_href of this RpmRpmRepositoryResponse.  # noqa: E501


        :return: The pulp_href of this RpmRpmRepositoryResponse.  # noqa: E501
        :rtype: str
        """
        return self._pulp_href

    @pulp_href.setter
    def pulp_href(self, pulp_href):
        """Sets the pulp_href of this RpmRpmRepositoryResponse.


        :param pulp_href: The pulp_href of this RpmRpmRepositoryResponse.  # noqa: E501
        :type: str
        """

        self._pulp_href = pulp_href

    @property
    def pulp_created(self):
        """Gets the pulp_created of this RpmRpmRepositoryResponse.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The pulp_created of this RpmRpmRepositoryResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_created

    @pulp_created.setter
    def pulp_created(self, pulp_created):
        """Sets the pulp_created of this RpmRpmRepositoryResponse.

        Timestamp of creation.  # noqa: E501

        :param pulp_created: The pulp_created of this RpmRpmRepositoryResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_created = pulp_created

    @property
    def versions_href(self):
        """Gets the versions_href of this RpmRpmRepositoryResponse.  # noqa: E501


        :return: The versions_href of this RpmRpmRepositoryResponse.  # noqa: E501
        :rtype: str
        """
        return self._versions_href

    @versions_href.setter
    def versions_href(self, versions_href):
        """Sets the versions_href of this RpmRpmRepositoryResponse.


        :param versions_href: The versions_href of this RpmRpmRepositoryResponse.  # noqa: E501
        :type: str
        """

        self._versions_href = versions_href

    @property
    def latest_version_href(self):
        """Gets the latest_version_href of this RpmRpmRepositoryResponse.  # noqa: E501


        :return: The latest_version_href of this RpmRpmRepositoryResponse.  # noqa: E501
        :rtype: str
        """
        return self._latest_version_href

    @latest_version_href.setter
    def latest_version_href(self, latest_version_href):
        """Sets the latest_version_href of this RpmRpmRepositoryResponse.


        :param latest_version_href: The latest_version_href of this RpmRpmRepositoryResponse.  # noqa: E501
        :type: str
        """

        self._latest_version_href = latest_version_href

    @property
    def name(self):
        """Gets the name of this RpmRpmRepositoryResponse.  # noqa: E501

        A unique name for this repository.  # noqa: E501

        :return: The name of this RpmRpmRepositoryResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RpmRpmRepositoryResponse.

        A unique name for this repository.  # noqa: E501

        :param name: The name of this RpmRpmRepositoryResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this RpmRpmRepositoryResponse.  # noqa: E501

        An optional description.  # noqa: E501

        :return: The description of this RpmRpmRepositoryResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RpmRpmRepositoryResponse.

        An optional description.  # noqa: E501

        :param description: The description of this RpmRpmRepositoryResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def remote(self):
        """Gets the remote of this RpmRpmRepositoryResponse.  # noqa: E501


        :return: The remote of this RpmRpmRepositoryResponse.  # noqa: E501
        :rtype: str
        """
        return self._remote

    @remote.setter
    def remote(self, remote):
        """Sets the remote of this RpmRpmRepositoryResponse.


        :param remote: The remote of this RpmRpmRepositoryResponse.  # noqa: E501
        :type: str
        """

        self._remote = remote

    @property
    def metadata_signing_service(self):
        """Gets the metadata_signing_service of this RpmRpmRepositoryResponse.  # noqa: E501

        A reference to an associated signing service.  # noqa: E501

        :return: The metadata_signing_service of this RpmRpmRepositoryResponse.  # noqa: E501
        :rtype: str
        """
        return self._metadata_signing_service

    @metadata_signing_service.setter
    def metadata_signing_service(self, metadata_signing_service):
        """Sets the metadata_signing_service of this RpmRpmRepositoryResponse.

        A reference to an associated signing service.  # noqa: E501

        :param metadata_signing_service: The metadata_signing_service of this RpmRpmRepositoryResponse.  # noqa: E501
        :type: str
        """

        self._metadata_signing_service = metadata_signing_service

    @property
    def retain_package_versions(self):
        """Gets the retain_package_versions of this RpmRpmRepositoryResponse.  # noqa: E501

        The number of versions of each package to keep in the repository; older versions will be purged. The default is '0', which will disable this feature and keep all versions of each package.  # noqa: E501

        :return: The retain_package_versions of this RpmRpmRepositoryResponse.  # noqa: E501
        :rtype: int
        """
        return self._retain_package_versions

    @retain_package_versions.setter
    def retain_package_versions(self, retain_package_versions):
        """Sets the retain_package_versions of this RpmRpmRepositoryResponse.

        The number of versions of each package to keep in the repository; older versions will be purged. The default is '0', which will disable this feature and keep all versions of each package.  # noqa: E501

        :param retain_package_versions: The retain_package_versions of this RpmRpmRepositoryResponse.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                retain_package_versions is not None and retain_package_versions < 0):  # noqa: E501
            raise ValueError("Invalid value for `retain_package_versions`, must be a value greater than or equal to `0`")  # noqa: E501

        self._retain_package_versions = retain_package_versions

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
        if not isinstance(other, RpmRpmRepositoryResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RpmRpmRepositoryResponse):
            return True

        return self.to_dict() != other.to_dict()
