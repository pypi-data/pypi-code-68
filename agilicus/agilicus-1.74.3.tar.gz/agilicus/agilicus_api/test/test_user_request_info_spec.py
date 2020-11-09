# coding: utf-8

"""
    Agilicus API

    Agilicus API endpoints  # noqa: E501

    The version of the OpenAPI document: 2020.11.06
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import agilicus_api
from agilicus_api.models.user_request_info_spec import UserRequestInfoSpec  # noqa: E501
from agilicus_api.rest import ApiException

class TestUserRequestInfoSpec(unittest.TestCase):
    """UserRequestInfoSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserRequestInfoSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.user_request_info_spec.UserRequestInfoSpec()  # noqa: E501
        if include_optional :
            return UserRequestInfoSpec(
                user_id = 'tuU7smH86zAXMl76sua6xQ', 
                org_id = 'IAsl3dl40aSsfLKiU76', 
                requested_resource = 'phone', 
                requested_sub_resource = 'self', 
                requested_resource_type = 'application_access', 
                request_information = 'I need this to do my job', 
                state = 'pending'
            )
        else :
            return UserRequestInfoSpec(
                user_id = 'tuU7smH86zAXMl76sua6xQ',
                org_id = 'IAsl3dl40aSsfLKiU76',
                requested_resource = 'phone',
                requested_resource_type = 'application_access',
        )

    def testUserRequestInfoSpec(self):
        """Test UserRequestInfoSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
