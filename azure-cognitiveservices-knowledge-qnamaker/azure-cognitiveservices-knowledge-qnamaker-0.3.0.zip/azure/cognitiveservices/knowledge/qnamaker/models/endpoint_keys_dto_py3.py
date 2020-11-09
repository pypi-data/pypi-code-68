# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EndpointKeysDTO(Model):
    """Schema for EndpointKeys generate/refresh operations.

    :param primary_endpoint_key: Primary Access Key.
    :type primary_endpoint_key: str
    :param secondary_endpoint_key: Secondary Access Key.
    :type secondary_endpoint_key: str
    :param installed_version: Current version of runtime.
    :type installed_version: str
    :param last_stable_version: Latest version of runtime.
    :type last_stable_version: str
    :param language: Language setting of runtime.
    :type language: str
    """

    _attribute_map = {
        'primary_endpoint_key': {'key': 'primaryEndpointKey', 'type': 'str'},
        'secondary_endpoint_key': {'key': 'secondaryEndpointKey', 'type': 'str'},
        'installed_version': {'key': 'installedVersion', 'type': 'str'},
        'last_stable_version': {'key': 'lastStableVersion', 'type': 'str'},
        'language': {'key': 'language', 'type': 'str'},
    }

    def __init__(self, *, primary_endpoint_key: str=None, secondary_endpoint_key: str=None, installed_version: str=None, last_stable_version: str=None, language: str=None, **kwargs) -> None:
        super(EndpointKeysDTO, self).__init__(**kwargs)
        self.primary_endpoint_key = primary_endpoint_key
        self.secondary_endpoint_key = secondary_endpoint_key
        self.installed_version = installed_version
        self.last_stable_version = last_stable_version
        self.language = language
