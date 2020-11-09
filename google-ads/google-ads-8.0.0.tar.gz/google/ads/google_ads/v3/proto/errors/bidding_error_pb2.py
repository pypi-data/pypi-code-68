# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/errors/bidding_error.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v3/proto/errors/bidding_error.proto',
  package='google.ads.googleads.v3.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v3.errorsB\021BiddingErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v3/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V3.Errors\312\002\036Google\\Ads\\GoogleAds\\V3\\Errors\352\002\"Google::Ads::GoogleAds::V3::Errors'),
  serialized_pb=_b('\n8google/ads/googleads_v3/proto/errors/bidding_error.proto\x12\x1egoogle.ads.googleads.v3.errors\x1a\x1cgoogle/api/annotations.proto\"\xee\x08\n\x10\x42iddingErrorEnum\"\xd9\x08\n\x0c\x42iddingError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12+\n\'BIDDING_STRATEGY_TRANSITION_NOT_ALLOWED\x10\x02\x12.\n*CANNOT_ATTACH_BIDDING_STRATEGY_TO_CAMPAIGN\x10\x07\x12+\n\'INVALID_ANONYMOUS_BIDDING_STRATEGY_TYPE\x10\n\x12!\n\x1dINVALID_BIDDING_STRATEGY_TYPE\x10\x0e\x12\x0f\n\x0bINVALID_BID\x10\x11\x12\x33\n/BIDDING_STRATEGY_NOT_AVAILABLE_FOR_ACCOUNT_TYPE\x10\x12\x12#\n\x1f\x43ONVERSION_TRACKING_NOT_ENABLED\x10\x13\x12\x1a\n\x16NOT_ENOUGH_CONVERSIONS\x10\x14\x12\x30\n,CANNOT_CREATE_CAMPAIGN_WITH_BIDDING_STRATEGY\x10\x15\x12O\nKCANNOT_TARGET_CONTENT_NETWORK_ONLY_WITH_CAMPAIGN_LEVEL_POP_BIDDING_STRATEGY\x10\x17\x12\x33\n/BIDDING_STRATEGY_NOT_SUPPORTED_WITH_AD_SCHEDULE\x10\x18\x12\x31\n-PAY_PER_CONVERSION_NOT_AVAILABLE_FOR_CUSTOMER\x10\x19\x12\x32\n.PAY_PER_CONVERSION_NOT_ALLOWED_WITH_TARGET_CPA\x10\x1a\x12:\n6BIDDING_STRATEGY_NOT_ALLOWED_FOR_SEARCH_ONLY_CAMPAIGNS\x10\x1b\x12;\n7BIDDING_STRATEGY_NOT_SUPPORTED_IN_DRAFTS_OR_EXPERIMENTS\x10\x1c\x12I\nEBIDDING_STRATEGY_TYPE_DOES_NOT_SUPPORT_PRODUCT_TYPE_ADGROUP_CRITERION\x10\x1d\x12\x11\n\rBID_TOO_SMALL\x10\x1e\x12\x0f\n\x0b\x42ID_TOO_BIG\x10\x1f\x12\"\n\x1e\x42ID_TOO_MANY_FRACTIONAL_DIGITS\x10 \x12\x17\n\x13INVALID_DOMAIN_NAME\x10!\x12$\n NOT_COMPATIBLE_WITH_PAYMENT_MODE\x10\"\x12#\n\x1fNOT_COMPATIBLE_WITH_BUDGET_TYPE\x10#\x12-\n)NOT_COMPATIBLE_WITH_BIDDING_STRATEGY_TYPE\x10$\x12\x39\n5BIDDING_STRATEGY_TYPE_INCOMPATIBLE_WITH_SHARED_BUDGET\x10%B\xec\x01\n\"com.google.ads.googleads.v3.errorsB\x11\x42iddingErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v3/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V3.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V3\\Errors\xea\x02\"Google::Ads::GoogleAds::V3::Errorsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_BIDDINGERRORENUM_BIDDINGERROR = _descriptor.EnumDescriptor(
  name='BiddingError',
  full_name='google.ads.googleads.v3.errors.BiddingErrorEnum.BiddingError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BIDDING_STRATEGY_TRANSITION_NOT_ALLOWED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_ATTACH_BIDDING_STRATEGY_TO_CAMPAIGN', index=3, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_ANONYMOUS_BIDDING_STRATEGY_TYPE', index=4, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_BIDDING_STRATEGY_TYPE', index=5, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_BID', index=6, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BIDDING_STRATEGY_NOT_AVAILABLE_FOR_ACCOUNT_TYPE', index=7, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONVERSION_TRACKING_NOT_ENABLED', index=8, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_ENOUGH_CONVERSIONS', index=9, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_CREATE_CAMPAIGN_WITH_BIDDING_STRATEGY', index=10, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_TARGET_CONTENT_NETWORK_ONLY_WITH_CAMPAIGN_LEVEL_POP_BIDDING_STRATEGY', index=11, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BIDDING_STRATEGY_NOT_SUPPORTED_WITH_AD_SCHEDULE', index=12, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAY_PER_CONVERSION_NOT_AVAILABLE_FOR_CUSTOMER', index=13, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAY_PER_CONVERSION_NOT_ALLOWED_WITH_TARGET_CPA', index=14, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BIDDING_STRATEGY_NOT_ALLOWED_FOR_SEARCH_ONLY_CAMPAIGNS', index=15, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BIDDING_STRATEGY_NOT_SUPPORTED_IN_DRAFTS_OR_EXPERIMENTS', index=16, number=28,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BIDDING_STRATEGY_TYPE_DOES_NOT_SUPPORT_PRODUCT_TYPE_ADGROUP_CRITERION', index=17, number=29,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BID_TOO_SMALL', index=18, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BID_TOO_BIG', index=19, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BID_TOO_MANY_FRACTIONAL_DIGITS', index=20, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_DOMAIN_NAME', index=21, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_COMPATIBLE_WITH_PAYMENT_MODE', index=22, number=34,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_COMPATIBLE_WITH_BUDGET_TYPE', index=23, number=35,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_COMPATIBLE_WITH_BIDDING_STRATEGY_TYPE', index=24, number=36,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BIDDING_STRATEGY_TYPE_INCOMPATIBLE_WITH_SHARED_BUDGET', index=25, number=37,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=144,
  serialized_end=1257,
)
_sym_db.RegisterEnumDescriptor(_BIDDINGERRORENUM_BIDDINGERROR)


_BIDDINGERRORENUM = _descriptor.Descriptor(
  name='BiddingErrorEnum',
  full_name='google.ads.googleads.v3.errors.BiddingErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BIDDINGERRORENUM_BIDDINGERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=123,
  serialized_end=1257,
)

_BIDDINGERRORENUM_BIDDINGERROR.containing_type = _BIDDINGERRORENUM
DESCRIPTOR.message_types_by_name['BiddingErrorEnum'] = _BIDDINGERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BiddingErrorEnum = _reflection.GeneratedProtocolMessageType('BiddingErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _BIDDINGERRORENUM,
  __module__ = 'google.ads.googleads_v3.proto.errors.bidding_error_pb2'
  ,
  __doc__ = """Container for enum describing possible bidding errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.errors.BiddingErrorEnum)
  ))
_sym_db.RegisterMessage(BiddingErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
