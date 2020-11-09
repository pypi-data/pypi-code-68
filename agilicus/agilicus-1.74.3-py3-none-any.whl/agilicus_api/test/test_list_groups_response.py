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
from agilicus_api.models.list_groups_response import ListGroupsResponse  # noqa: E501
from agilicus_api.rest import ApiException

class TestListGroupsResponse(unittest.TestCase):
    """ListGroupsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListGroupsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.list_groups_response.ListGroupsResponse()  # noqa: E501
        if include_optional :
            return ListGroupsResponse(
                groups = [
                    ], 
                limit = 56, 
                previous_page_email = 'foo@example.com', 
                next_page_email = 'foo@example.com'
            )
        else :
            return ListGroupsResponse(
                limit = 56,
        )

    def testListGroupsResponse(self):
        """Test ListGroupsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
