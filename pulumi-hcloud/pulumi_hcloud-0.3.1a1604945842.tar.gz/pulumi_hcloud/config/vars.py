# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'endpoint',
    'token',
]

__config__ = pulumi.Config('hcloud')

endpoint = __config__.get('endpoint')

token = __config__.get('token')
"""
The API token to access the Hetzner cloud.
"""

