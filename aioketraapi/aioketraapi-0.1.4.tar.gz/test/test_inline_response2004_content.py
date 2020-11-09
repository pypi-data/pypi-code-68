# coding: utf-8

"""
    Ketra Lighting API

    Control your Ketra lights  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import aioketraapi
from aioketraapi.models.inline_response2004_content import InlineResponse2004Content  # noqa: E501
from aioketraapi.rest import ApiException

class TestInlineResponse2004Content(unittest.TestCase):
    """InlineResponse2004Content unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2004Content
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = aioketraapi.models.inline_response2004_content.InlineResponse2004Content()  # noqa: E501
        if include_optional :
            return InlineResponse2004Content(
                api_schema = 56, 
                cpu_version = '0', 
                radio_version = '0', 
                serial_number = '0', 
                model_name = '0', 
                id = '0', 
                installation_id = '0', 
                installation_name = '0', 
                network_id = '0', 
                name = '0', 
                ethernet_mac = '0', 
                i_pv4_address = '0', 
                ethernet_link_status = [
                    True
                    ], 
                up_time_seconds = 56, 
                local_time = '0', 
                utc_time = '0', 
                last_reboot_reason = 'Power Cycle', 
                has_internet_connectivity = True, 
                last_time_update_was_successful = True, 
                remote_connection_enabled = True, 
                remote_connection_established = True, 
                supports_zone_keypads = True
            )
        else :
            return InlineResponse2004Content(
        )

    def testInlineResponse2004Content(self):
        """Test InlineResponse2004Content"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
