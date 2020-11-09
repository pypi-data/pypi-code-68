# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v6/proto/common/frequency_cap.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v6.proto.enums import frequency_cap_event_type_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_frequency__cap__event__type__pb2
from google.ads.google_ads.v6.proto.enums import frequency_cap_level_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_frequency__cap__level__pb2
from google.ads.google_ads.v6.proto.enums import frequency_cap_time_unit_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_frequency__cap__time__unit__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v6/proto/common/frequency_cap.proto',
  package='google.ads.googleads.v6.common',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v6.commonB\021FrequencyCapProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v6/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V6.Common\312\002\036Google\\Ads\\GoogleAds\\V6\\Common\352\002\"Google::Ads::GoogleAds::V6::Common',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n8google/ads/googleads_v6/proto/common/frequency_cap.proto\x12\x1egoogle.ads.googleads.v6.common\x1a\x42google/ads/googleads_v6/proto/enums/frequency_cap_event_type.proto\x1a=google/ads/googleads_v6/proto/enums/frequency_cap_level.proto\x1a\x41google/ads/googleads_v6/proto/enums/frequency_cap_time_unit.proto\x1a\x1cgoogle/api/annotations.proto\"k\n\x11\x46requencyCapEntry\x12<\n\x03key\x18\x01 \x01(\x0b\x32/.google.ads.googleads.v6.common.FrequencyCapKey\x12\x10\n\x03\x63\x61p\x18\x03 \x01(\x05H\x00\x88\x01\x01\x42\x06\n\x04_cap\"\xd7\x02\n\x0f\x46requencyCapKey\x12U\n\x05level\x18\x01 \x01(\x0e\x32\x46.google.ads.googleads.v6.enums.FrequencyCapLevelEnum.FrequencyCapLevel\x12\x62\n\nevent_type\x18\x03 \x01(\x0e\x32N.google.ads.googleads.v6.enums.FrequencyCapEventTypeEnum.FrequencyCapEventType\x12_\n\ttime_unit\x18\x02 \x01(\x0e\x32L.google.ads.googleads.v6.enums.FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit\x12\x18\n\x0btime_length\x18\x05 \x01(\x05H\x00\x88\x01\x01\x42\x0e\n\x0c_time_lengthB\xec\x01\n\"com.google.ads.googleads.v6.commonB\x11\x46requencyCapProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v6/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V6.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V6\\Common\xea\x02\"Google::Ads::GoogleAds::V6::Commonb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_frequency__cap__event__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_frequency__cap__level__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_frequency__cap__time__unit__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_FREQUENCYCAPENTRY = _descriptor.Descriptor(
  name='FrequencyCapEntry',
  full_name='google.ads.googleads.v6.common.FrequencyCapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.ads.googleads.v6.common.FrequencyCapEntry.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cap', full_name='google.ads.googleads.v6.common.FrequencyCapEntry.cap', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
    _descriptor.OneofDescriptor(
      name='_cap', full_name='google.ads.googleads.v6.common.FrequencyCapEntry._cap',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=320,
  serialized_end=427,
)


_FREQUENCYCAPKEY = _descriptor.Descriptor(
  name='FrequencyCapKey',
  full_name='google.ads.googleads.v6.common.FrequencyCapKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='google.ads.googleads.v6.common.FrequencyCapKey.level', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='event_type', full_name='google.ads.googleads.v6.common.FrequencyCapKey.event_type', index=1,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_unit', full_name='google.ads.googleads.v6.common.FrequencyCapKey.time_unit', index=2,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_length', full_name='google.ads.googleads.v6.common.FrequencyCapKey.time_length', index=3,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
    _descriptor.OneofDescriptor(
      name='_time_length', full_name='google.ads.googleads.v6.common.FrequencyCapKey._time_length',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=430,
  serialized_end=773,
)

_FREQUENCYCAPENTRY.fields_by_name['key'].message_type = _FREQUENCYCAPKEY
_FREQUENCYCAPENTRY.oneofs_by_name['_cap'].fields.append(
  _FREQUENCYCAPENTRY.fields_by_name['cap'])
_FREQUENCYCAPENTRY.fields_by_name['cap'].containing_oneof = _FREQUENCYCAPENTRY.oneofs_by_name['_cap']
_FREQUENCYCAPKEY.fields_by_name['level'].enum_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_frequency__cap__level__pb2._FREQUENCYCAPLEVELENUM_FREQUENCYCAPLEVEL
_FREQUENCYCAPKEY.fields_by_name['event_type'].enum_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_frequency__cap__event__type__pb2._FREQUENCYCAPEVENTTYPEENUM_FREQUENCYCAPEVENTTYPE
_FREQUENCYCAPKEY.fields_by_name['time_unit'].enum_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_frequency__cap__time__unit__pb2._FREQUENCYCAPTIMEUNITENUM_FREQUENCYCAPTIMEUNIT
_FREQUENCYCAPKEY.oneofs_by_name['_time_length'].fields.append(
  _FREQUENCYCAPKEY.fields_by_name['time_length'])
_FREQUENCYCAPKEY.fields_by_name['time_length'].containing_oneof = _FREQUENCYCAPKEY.oneofs_by_name['_time_length']
DESCRIPTOR.message_types_by_name['FrequencyCapEntry'] = _FREQUENCYCAPENTRY
DESCRIPTOR.message_types_by_name['FrequencyCapKey'] = _FREQUENCYCAPKEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FrequencyCapEntry = _reflection.GeneratedProtocolMessageType('FrequencyCapEntry', (_message.Message,), {
  'DESCRIPTOR' : _FREQUENCYCAPENTRY,
  '__module__' : 'google.ads.googleads_v6.proto.common.frequency_cap_pb2'
  ,
  '__doc__': """A rule specifying the maximum number of times an ad (or some set of
  ads) can be shown to a user over a particular time period.
  
  Attributes:
      key:
          The key of a particular frequency cap. There can be no more
          than one frequency cap with the same key.
      cap:
          Maximum number of events allowed during the time range by this
          cap.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.common.FrequencyCapEntry)
  })
_sym_db.RegisterMessage(FrequencyCapEntry)

FrequencyCapKey = _reflection.GeneratedProtocolMessageType('FrequencyCapKey', (_message.Message,), {
  'DESCRIPTOR' : _FREQUENCYCAPKEY,
  '__module__' : 'google.ads.googleads_v6.proto.common.frequency_cap_pb2'
  ,
  '__doc__': """A group of fields used as keys for a frequency cap. There can be no
  more than one frequency cap with the same key.
  
  Attributes:
      level:
          The level on which the cap is to be applied (e.g. ad group ad,
          ad group). The cap is applied to all the entities of this
          level.
      event_type:
          The type of event that the cap applies to (e.g. impression).
      time_unit:
          Unit of time the cap is defined at (e.g. day, week).
      time_length:
          Number of time units the cap lasts.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.common.FrequencyCapKey)
  })
_sym_db.RegisterMessage(FrequencyCapKey)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
