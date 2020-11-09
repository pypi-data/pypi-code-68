# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'MfaDuo',
    'MfaFidoU2f',
    'MfaFidoWebauthn',
    'MfaGoogleOtp',
    'MfaOktaCall',
    'MfaOktaOtp',
    'MfaOktaPassword',
    'MfaOktaPush',
    'MfaOktaQuestion',
    'MfaOktaSms',
    'MfaRsaToken',
    'MfaSymantecVip',
    'MfaYubikeyToken',
    'RuleIdpDiscoveryAppExclude',
    'RuleIdpDiscoveryAppInclude',
    'RuleIdpDiscoveryPlatformInclude',
    'RuleIdpDiscoveryUserIdentifierPattern',
]

@pulumi.output_type
class MfaDuo(dict):
    def __init__(__self__, *,
                 consent_type: Optional[str] = None,
                 enroll: Optional[str] = None):
        """
        :param str consent_type: User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
        :param str enroll: Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
        """
        if consent_type is not None:
            pulumi.set(__self__, "consent_type", consent_type)
        if enroll is not None:
            pulumi.set(__self__, "enroll", enroll)

    @property
    @pulumi.getter(name="consentType")
    def consent_type(self) -> Optional[str]:
        """
        User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
        """
        return pulumi.get(self, "consent_type")

    @property
    @pulumi.getter
    def enroll(self) -> Optional[str]:
        """
        Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
        """
        return pulumi.get(self, "enroll")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MfaFidoU2f(dict):
    def __init__(__self__, *,
                 consent_type: Optional[str] = None,
                 enroll: Optional[str] = None):
        """
        :param str consent_type: User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
        :param str enroll: Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
        """
        if consent_type is not None:
            pulumi.set(__self__, "consent_type", consent_type)
        if enroll is not None:
            pulumi.set(__self__, "enroll", enroll)

    @property
    @pulumi.getter(name="consentType")
    def consent_type(self) -> Optional[str]:
        """
        User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
        """
        return pulumi.get(self, "consent_type")

    @property
    @pulumi.getter
    def enroll(self) -> Optional[str]:
        """
        Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
        """
        return pulumi.get(self, "enroll")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MfaFidoWebauthn(dict):
    def __init__(__self__, *,
                 consent_type: Optional[str] = None,
                 enroll: Optional[str] = None):
        """
        :param str consent_type: User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
        :param str enroll: Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
        """
        if consent_type is not None:
            pulumi.set(__self__, "consent_type", consent_type)
        if enroll is not None:
            pulumi.set(__self__, "enroll", enroll)

    @property
    @pulumi.getter(name="consentType")
    def consent_type(self) -> Optional[str]:
        """
        User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
        """
        return pulumi.get(self, "consent_type")

    @property
    @pulumi.getter
    def enroll(self) -> Optional[str]:
        """
        Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
        """
        return pulumi.get(self, "enroll")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MfaGoogleOtp(dict):
    def __init__(__self__, *,
                 consent_type: Optional[str] = None,
                 enroll: Optional[str] = None):
        """
        :param str consent_type: User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
        :param str enroll: Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
        """
        if consent_type is not None:
            pulumi.set(__self__, "consent_type", consent_type)
        if enroll is not None:
            pulumi.set(__self__, "enroll", enroll)

    @property
    @pulumi.getter(name="consentType")
    def consent_type(self) -> Optional[str]:
        """
        User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
        """
        return pulumi.get(self, "consent_type")

    @property
    @pulumi.getter
    def enroll(self) -> Optional[str]:
        """
        Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
        """
        return pulumi.get(self, "enroll")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MfaOktaCall(dict):
    def __init__(__self__, *,
                 consent_type: Optional[str] = None,
                 enroll: Optional[str] = None):
        """
        :param str consent_type: User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
        :param str enroll: Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
        """
        if consent_type is not None:
            pulumi.set(__self__, "consent_type", consent_type)
        if enroll is not None:
            pulumi.set(__self__, "enroll", enroll)

    @property
    @pulumi.getter(name="consentType")
    def consent_type(self) -> Optional[str]:
        """
        User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
        """
        return pulumi.get(self, "consent_type")

    @property
    @pulumi.getter
    def enroll(self) -> Optional[str]:
        """
        Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
        """
        return pulumi.get(self, "enroll")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MfaOktaOtp(dict):
    def __init__(__self__, *,
                 consent_type: Optional[str] = None,
                 enroll: Optional[str] = None):
        """
        :param str consent_type: User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
        :param str enroll: Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
        """
        if consent_type is not None:
            pulumi.set(__self__, "consent_type", consent_type)
        if enroll is not None:
            pulumi.set(__self__, "enroll", enroll)

    @property
    @pulumi.getter(name="consentType")
    def consent_type(self) -> Optional[str]:
        """
        User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
        """
        return pulumi.get(self, "consent_type")

    @property
    @pulumi.getter
    def enroll(self) -> Optional[str]:
        """
        Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
        """
        return pulumi.get(self, "enroll")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MfaOktaPassword(dict):
    def __init__(__self__, *,
                 consent_type: Optional[str] = None,
                 enroll: Optional[str] = None):
        """
        :param str consent_type: User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
        :param str enroll: Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
        """
        if consent_type is not None:
            pulumi.set(__self__, "consent_type", consent_type)
        if enroll is not None:
            pulumi.set(__self__, "enroll", enroll)

    @property
    @pulumi.getter(name="consentType")
    def consent_type(self) -> Optional[str]:
        """
        User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
        """
        return pulumi.get(self, "consent_type")

    @property
    @pulumi.getter
    def enroll(self) -> Optional[str]:
        """
        Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
        """
        return pulumi.get(self, "enroll")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MfaOktaPush(dict):
    def __init__(__self__, *,
                 consent_type: Optional[str] = None,
                 enroll: Optional[str] = None):
        """
        :param str consent_type: User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
        :param str enroll: Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
        """
        if consent_type is not None:
            pulumi.set(__self__, "consent_type", consent_type)
        if enroll is not None:
            pulumi.set(__self__, "enroll", enroll)

    @property
    @pulumi.getter(name="consentType")
    def consent_type(self) -> Optional[str]:
        """
        User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
        """
        return pulumi.get(self, "consent_type")

    @property
    @pulumi.getter
    def enroll(self) -> Optional[str]:
        """
        Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
        """
        return pulumi.get(self, "enroll")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MfaOktaQuestion(dict):
    def __init__(__self__, *,
                 consent_type: Optional[str] = None,
                 enroll: Optional[str] = None):
        """
        :param str consent_type: User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
        :param str enroll: Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
        """
        if consent_type is not None:
            pulumi.set(__self__, "consent_type", consent_type)
        if enroll is not None:
            pulumi.set(__self__, "enroll", enroll)

    @property
    @pulumi.getter(name="consentType")
    def consent_type(self) -> Optional[str]:
        """
        User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
        """
        return pulumi.get(self, "consent_type")

    @property
    @pulumi.getter
    def enroll(self) -> Optional[str]:
        """
        Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
        """
        return pulumi.get(self, "enroll")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MfaOktaSms(dict):
    def __init__(__self__, *,
                 consent_type: Optional[str] = None,
                 enroll: Optional[str] = None):
        """
        :param str consent_type: User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
        :param str enroll: Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
        """
        if consent_type is not None:
            pulumi.set(__self__, "consent_type", consent_type)
        if enroll is not None:
            pulumi.set(__self__, "enroll", enroll)

    @property
    @pulumi.getter(name="consentType")
    def consent_type(self) -> Optional[str]:
        """
        User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
        """
        return pulumi.get(self, "consent_type")

    @property
    @pulumi.getter
    def enroll(self) -> Optional[str]:
        """
        Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
        """
        return pulumi.get(self, "enroll")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MfaRsaToken(dict):
    def __init__(__self__, *,
                 consent_type: Optional[str] = None,
                 enroll: Optional[str] = None):
        """
        :param str consent_type: User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
        :param str enroll: Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
        """
        if consent_type is not None:
            pulumi.set(__self__, "consent_type", consent_type)
        if enroll is not None:
            pulumi.set(__self__, "enroll", enroll)

    @property
    @pulumi.getter(name="consentType")
    def consent_type(self) -> Optional[str]:
        """
        User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
        """
        return pulumi.get(self, "consent_type")

    @property
    @pulumi.getter
    def enroll(self) -> Optional[str]:
        """
        Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
        """
        return pulumi.get(self, "enroll")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MfaSymantecVip(dict):
    def __init__(__self__, *,
                 consent_type: Optional[str] = None,
                 enroll: Optional[str] = None):
        """
        :param str consent_type: User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
        :param str enroll: Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
        """
        if consent_type is not None:
            pulumi.set(__self__, "consent_type", consent_type)
        if enroll is not None:
            pulumi.set(__self__, "enroll", enroll)

    @property
    @pulumi.getter(name="consentType")
    def consent_type(self) -> Optional[str]:
        """
        User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
        """
        return pulumi.get(self, "consent_type")

    @property
    @pulumi.getter
    def enroll(self) -> Optional[str]:
        """
        Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
        """
        return pulumi.get(self, "enroll")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MfaYubikeyToken(dict):
    def __init__(__self__, *,
                 consent_type: Optional[str] = None,
                 enroll: Optional[str] = None):
        """
        :param str consent_type: User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
        :param str enroll: Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
        """
        if consent_type is not None:
            pulumi.set(__self__, "consent_type", consent_type)
        if enroll is not None:
            pulumi.set(__self__, "enroll", enroll)

    @property
    @pulumi.getter(name="consentType")
    def consent_type(self) -> Optional[str]:
        """
        User consent type required before enrolling in the factor: `"NONE"` or `"TERMS_OF_SERVICE"`. By default it is `"NONE"`.
        """
        return pulumi.get(self, "consent_type")

    @property
    @pulumi.getter
    def enroll(self) -> Optional[str]:
        """
        Requirements for user initiated enrollment. Can be `"NOT_ALLOWED"`, `"OPTIONAL"`, or `"REQUIRED"`. By default it is `"OPTIONAL"`.
        """
        return pulumi.get(self, "enroll")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class RuleIdpDiscoveryAppExclude(dict):
    def __init__(__self__, *,
                 id: Optional[str] = None,
                 name: Optional[str] = None,
                 type: Optional[str] = None):
        """
        :param str id: ID of the Rule.
        :param str name: Policy Rule Name.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        ID of the Rule.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Policy Rule Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        return pulumi.get(self, "type")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class RuleIdpDiscoveryAppInclude(dict):
    def __init__(__self__, *,
                 id: Optional[str] = None,
                 name: Optional[str] = None,
                 type: Optional[str] = None):
        """
        :param str id: ID of the Rule.
        :param str name: Policy Rule Name.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        ID of the Rule.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Policy Rule Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        return pulumi.get(self, "type")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class RuleIdpDiscoveryPlatformInclude(dict):
    def __init__(__self__, *,
                 os_expression: Optional[str] = None,
                 os_type: Optional[str] = None,
                 type: Optional[str] = None):
        if os_expression is not None:
            pulumi.set(__self__, "os_expression", os_expression)
        if os_type is not None:
            pulumi.set(__self__, "os_type", os_type)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="osExpression")
    def os_expression(self) -> Optional[str]:
        return pulumi.get(self, "os_expression")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[str]:
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        return pulumi.get(self, "type")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class RuleIdpDiscoveryUserIdentifierPattern(dict):
    def __init__(__self__, *,
                 match_type: Optional[str] = None,
                 value: Optional[str] = None):
        if match_type is not None:
            pulumi.set(__self__, "match_type", match_type)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="matchType")
    def match_type(self) -> Optional[str]:
        return pulumi.get(self, "match_type")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        return pulumi.get(self, "value")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


