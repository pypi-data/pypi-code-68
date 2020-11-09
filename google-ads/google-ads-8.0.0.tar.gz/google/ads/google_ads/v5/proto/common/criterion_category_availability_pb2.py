# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v5/proto/common/criterion_category_availability.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v5.proto.enums import advertising_channel_sub_type_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_advertising__channel__sub__type__pb2
from google.ads.google_ads.v5.proto.enums import advertising_channel_type_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_advertising__channel__type__pb2
from google.ads.google_ads.v5.proto.enums import criterion_category_channel_availability_mode_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_criterion__category__channel__availability__mode__pb2
from google.ads.google_ads.v5.proto.enums import criterion_category_locale_availability_mode_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_criterion__category__locale__availability__mode__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v5/proto/common/criterion_category_availability.proto',
  package='google.ads.googleads.v5.common',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v5.commonB\"CriterionCategoryAvailabilityProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v5/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V5.Common\312\002\036Google\\Ads\\GoogleAds\\V5\\Common\352\002\"Google::Ads::GoogleAds::V5::Common',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nJgoogle/ads/googleads_v5/proto/common/criterion_category_availability.proto\x12\x1egoogle.ads.googleads.v5.common\x1a\x46google/ads/googleads_v5/proto/enums/advertising_channel_sub_type.proto\x1a\x42google/ads/googleads_v5/proto/enums/advertising_channel_type.proto\x1aVgoogle/ads/googleads_v5/proto/enums/criterion_category_channel_availability_mode.proto\x1aUgoogle/ads/googleads_v5/proto/enums/criterion_category_locale_availability_mode.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xcb\x01\n\x1d\x43riterionCategoryAvailability\x12U\n\x07\x63hannel\x18\x01 \x01(\x0b\x32\x44.google.ads.googleads.v5.common.CriterionCategoryChannelAvailability\x12S\n\x06locale\x18\x02 \x03(\x0b\x32\x43.google.ads.googleads.v5.common.CriterionCategoryLocaleAvailability\"\xf0\x03\n$CriterionCategoryChannelAvailability\x12\x8f\x01\n\x11\x61vailability_mode\x18\x01 \x01(\x0e\x32t.google.ads.googleads.v5.enums.CriterionCategoryChannelAvailabilityModeEnum.CriterionCategoryChannelAvailabilityMode\x12r\n\x18\x61\x64vertising_channel_type\x18\x02 \x01(\x0e\x32P.google.ads.googleads.v5.enums.AdvertisingChannelTypeEnum.AdvertisingChannelType\x12|\n\x1c\x61\x64vertising_channel_sub_type\x18\x03 \x03(\x0e\x32V.google.ads.googleads.v5.enums.AdvertisingChannelSubTypeEnum.AdvertisingChannelSubType\x12\x44\n include_default_channel_sub_type\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"\x9e\x02\n#CriterionCategoryLocaleAvailability\x12\x8d\x01\n\x11\x61vailability_mode\x18\x01 \x01(\x0e\x32r.google.ads.googleads.v5.enums.CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityMode\x12\x32\n\x0c\x63ountry_code\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rlanguage_code\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\xfd\x01\n\"com.google.ads.googleads.v5.commonB\"CriterionCategoryAvailabilityProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v5/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V5.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V5\\Common\xea\x02\"Google::Ads::GoogleAds::V5::Commonb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_advertising__channel__sub__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_advertising__channel__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_criterion__category__channel__availability__mode__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_criterion__category__locale__availability__mode__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CRITERIONCATEGORYAVAILABILITY = _descriptor.Descriptor(
  name='CriterionCategoryAvailability',
  full_name='google.ads.googleads.v5.common.CriterionCategoryAvailability',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='google.ads.googleads.v5.common.CriterionCategoryAvailability.channel', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='locale', full_name='google.ads.googleads.v5.common.CriterionCategoryAvailability.locale', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=488,
  serialized_end=691,
)


_CRITERIONCATEGORYCHANNELAVAILABILITY = _descriptor.Descriptor(
  name='CriterionCategoryChannelAvailability',
  full_name='google.ads.googleads.v5.common.CriterionCategoryChannelAvailability',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='availability_mode', full_name='google.ads.googleads.v5.common.CriterionCategoryChannelAvailability.availability_mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='advertising_channel_type', full_name='google.ads.googleads.v5.common.CriterionCategoryChannelAvailability.advertising_channel_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='advertising_channel_sub_type', full_name='google.ads.googleads.v5.common.CriterionCategoryChannelAvailability.advertising_channel_sub_type', index=2,
      number=3, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='include_default_channel_sub_type', full_name='google.ads.googleads.v5.common.CriterionCategoryChannelAvailability.include_default_channel_sub_type', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=694,
  serialized_end=1190,
)


_CRITERIONCATEGORYLOCALEAVAILABILITY = _descriptor.Descriptor(
  name='CriterionCategoryLocaleAvailability',
  full_name='google.ads.googleads.v5.common.CriterionCategoryLocaleAvailability',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='availability_mode', full_name='google.ads.googleads.v5.common.CriterionCategoryLocaleAvailability.availability_mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='country_code', full_name='google.ads.googleads.v5.common.CriterionCategoryLocaleAvailability.country_code', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='language_code', full_name='google.ads.googleads.v5.common.CriterionCategoryLocaleAvailability.language_code', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1193,
  serialized_end=1479,
)

_CRITERIONCATEGORYAVAILABILITY.fields_by_name['channel'].message_type = _CRITERIONCATEGORYCHANNELAVAILABILITY
_CRITERIONCATEGORYAVAILABILITY.fields_by_name['locale'].message_type = _CRITERIONCATEGORYLOCALEAVAILABILITY
_CRITERIONCATEGORYCHANNELAVAILABILITY.fields_by_name['availability_mode'].enum_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_criterion__category__channel__availability__mode__pb2._CRITERIONCATEGORYCHANNELAVAILABILITYMODEENUM_CRITERIONCATEGORYCHANNELAVAILABILITYMODE
_CRITERIONCATEGORYCHANNELAVAILABILITY.fields_by_name['advertising_channel_type'].enum_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_advertising__channel__type__pb2._ADVERTISINGCHANNELTYPEENUM_ADVERTISINGCHANNELTYPE
_CRITERIONCATEGORYCHANNELAVAILABILITY.fields_by_name['advertising_channel_sub_type'].enum_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_advertising__channel__sub__type__pb2._ADVERTISINGCHANNELSUBTYPEENUM_ADVERTISINGCHANNELSUBTYPE
_CRITERIONCATEGORYCHANNELAVAILABILITY.fields_by_name['include_default_channel_sub_type'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_CRITERIONCATEGORYLOCALEAVAILABILITY.fields_by_name['availability_mode'].enum_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_criterion__category__locale__availability__mode__pb2._CRITERIONCATEGORYLOCALEAVAILABILITYMODEENUM_CRITERIONCATEGORYLOCALEAVAILABILITYMODE
_CRITERIONCATEGORYLOCALEAVAILABILITY.fields_by_name['country_code'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CRITERIONCATEGORYLOCALEAVAILABILITY.fields_by_name['language_code'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['CriterionCategoryAvailability'] = _CRITERIONCATEGORYAVAILABILITY
DESCRIPTOR.message_types_by_name['CriterionCategoryChannelAvailability'] = _CRITERIONCATEGORYCHANNELAVAILABILITY
DESCRIPTOR.message_types_by_name['CriterionCategoryLocaleAvailability'] = _CRITERIONCATEGORYLOCALEAVAILABILITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CriterionCategoryAvailability = _reflection.GeneratedProtocolMessageType('CriterionCategoryAvailability', (_message.Message,), {
  'DESCRIPTOR' : _CRITERIONCATEGORYAVAILABILITY,
  '__module__' : 'google.ads.googleads_v5.proto.common.criterion_category_availability_pb2'
  ,
  '__doc__': """Information of category availability, per advertising channel.
  
  Attributes:
      channel:
          Channel types and subtypes that are available to the category.
      locale:
          Locales that are available to the category for the channel.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.common.CriterionCategoryAvailability)
  })
_sym_db.RegisterMessage(CriterionCategoryAvailability)

CriterionCategoryChannelAvailability = _reflection.GeneratedProtocolMessageType('CriterionCategoryChannelAvailability', (_message.Message,), {
  'DESCRIPTOR' : _CRITERIONCATEGORYCHANNELAVAILABILITY,
  '__module__' : 'google.ads.googleads_v5.proto.common.criterion_category_availability_pb2'
  ,
  '__doc__': """Information of advertising channel type and subtypes a category is
  available in.
  
  Attributes:
      availability_mode:
          Format of the channel availability. Can be ALL\_CHANNELS (the
          rest of the fields will not be set), CHANNEL\_TYPE (only
          advertising\_channel\_type type will be set, the category is
          available to all sub types under it) or
          CHANNEL\_TYPE\_AND\_SUBTYPES (advertising\_channel\_type,
          advertising\_channel\_sub\_type, and
          include\_default\_channel\_sub\_type will all be set).
      advertising_channel_type:
          Channel type the category is available to.
      advertising_channel_sub_type:
          Channel subtypes under the channel type the category is
          available to.
      include_default_channel_sub_type:
          Whether default channel sub type is included. For example,
          advertising\_channel\_type being DISPLAY and
          include\_default\_channel\_sub\_type being false means that
          the default display campaign where channel sub type is not set
          is not included in this availability configuration.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.common.CriterionCategoryChannelAvailability)
  })
_sym_db.RegisterMessage(CriterionCategoryChannelAvailability)

CriterionCategoryLocaleAvailability = _reflection.GeneratedProtocolMessageType('CriterionCategoryLocaleAvailability', (_message.Message,), {
  'DESCRIPTOR' : _CRITERIONCATEGORYLOCALEAVAILABILITY,
  '__module__' : 'google.ads.googleads_v5.proto.common.criterion_category_availability_pb2'
  ,
  '__doc__': """Information about which locales a category is available in.
  
  Attributes:
      availability_mode:
          Format of the locale availability. Can be LAUNCHED\_TO\_ALL
          (both country and language will be empty), COUNTRY (only
          country will be set), LANGUAGE (only language wil be set),
          COUNTRY\_AND\_LANGUAGE (both country and language will be
          set).
      country_code:
          Code of the country.
      language_code:
          Code of the language.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.common.CriterionCategoryLocaleAvailability)
  })
_sym_db.RegisterMessage(CriterionCategoryLocaleAvailability)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
