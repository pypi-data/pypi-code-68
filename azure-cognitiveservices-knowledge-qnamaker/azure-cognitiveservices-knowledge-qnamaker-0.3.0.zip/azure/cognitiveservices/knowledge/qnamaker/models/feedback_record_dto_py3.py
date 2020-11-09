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


class FeedbackRecordDTO(Model):
    """Active learning feedback record.

    :param user_id: Unique identifier for the user.
    :type user_id: str
    :param user_question: The suggested question being provided as feedback.
    :type user_question: str
    :param qna_id: The qnaId for which the suggested question is provided as
     feedback.
    :type qna_id: int
    """

    _validation = {
        'user_question': {'max_length': 1000},
    }

    _attribute_map = {
        'user_id': {'key': 'userId', 'type': 'str'},
        'user_question': {'key': 'userQuestion', 'type': 'str'},
        'qna_id': {'key': 'qnaId', 'type': 'int'},
    }

    def __init__(self, *, user_id: str=None, user_question: str=None, qna_id: int=None, **kwargs) -> None:
        super(FeedbackRecordDTO, self).__init__(**kwargs)
        self.user_id = user_id
        self.user_question = user_question
        self.qna_id = qna_id
