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
from agilicus_api.models.whoami_response import WhoamiResponse  # noqa: E501
from agilicus_api.rest import ApiException

class TestWhoamiResponse(unittest.TestCase):
    """WhoamiResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test WhoamiResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.whoami_response.WhoamiResponse()  # noqa: E501
        if include_optional :
            return WhoamiResponse(
                token = '2ashiferjh56guwegbiwueh23867923', 
                orgs = [
                    agilicus_api.models.organisation.Organisation(
                        id = '123', 
                        all_users_group_id = '123', 
                        all_users_all_suborgs_group_id = '123', 
                        all_users_direct_suborgs_group_id = '123', 
                        auto_created_users_group_id = '123', 
                        external_id = '123', 
                        organisation = 'some name', 
                        issuer = 'app1', 
                        issuer_id = '123', 
                        subdomain = 'app1.example.com', 
                        created = '2015-07-07T15:49:51.230+02:00', 
                        updated = '2015-07-07T15:49:51.230+02:00', 
                        contact_id = '123', 
                        contact_email = 'contact@agilicus.com', 
                        parent_id = '123', 
                        root_org_id = 'aB29sdkD3jlaAbl7', 
                        auto_create = False, 
                        trust_on_first_use_duration = 0, 
                        feature_flags = [
                            agilicus_api.models.feature_flag.FeatureFlag(
                                feature = 'saml_auth', 
                                enabled = True, 
                                setting = '0', )
                            ], )
                    ]
            )
        else :
            return WhoamiResponse(
        )

    def testWhoamiResponse(self):
        """Test WhoamiResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
