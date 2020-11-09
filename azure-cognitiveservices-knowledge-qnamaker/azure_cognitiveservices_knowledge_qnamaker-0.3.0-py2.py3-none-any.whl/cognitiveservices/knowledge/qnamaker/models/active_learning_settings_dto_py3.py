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


class ActiveLearningSettingsDTO(Model):
    """Active Learning settings of the endpoint.

    :param enable: True/False string providing Active Learning
    :type enable: str
    """

    _attribute_map = {
        'enable': {'key': 'enable', 'type': 'str'},
    }

    def __init__(self, *, enable: str=None, **kwargs) -> None:
        super(ActiveLearningSettingsDTO, self).__init__(**kwargs)
        self.enable = enable
