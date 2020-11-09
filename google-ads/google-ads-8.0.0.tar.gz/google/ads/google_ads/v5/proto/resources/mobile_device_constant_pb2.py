# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v5/proto/resources/mobile_device_constant.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v5.proto.enums import mobile_device_type_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_mobile__device__type__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v5/proto/resources/mobile_device_constant.proto',
  package='google.ads.googleads.v5.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v5.resourcesB\031MobileDeviceConstantProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v5/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V5.Resources\312\002!Google\\Ads\\GoogleAds\\V5\\Resources\352\002%Google::Ads::GoogleAds::V5::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nDgoogle/ads/googleads_v5/proto/resources/mobile_device_constant.proto\x12!google.ads.googleads.v5.resources\x1a<google/ads/googleads_v5/proto/enums/mobile_device_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xdd\x03\n\x14MobileDeviceConstant\x12L\n\rresource_name\x18\x01 \x01(\tB5\xe0\x41\x03\xfa\x41/\n-googleads.googleapis.com/MobileDeviceConstant\x12\x14\n\x02id\x18\x07 \x01(\x03\x42\x03\xe0\x41\x03H\x00\x88\x01\x01\x12\x16\n\x04name\x18\x08 \x01(\tB\x03\xe0\x41\x03H\x01\x88\x01\x01\x12#\n\x11manufacturer_name\x18\t \x01(\tB\x03\xe0\x41\x03H\x02\x88\x01\x01\x12\'\n\x15operating_system_name\x18\n \x01(\tB\x03\xe0\x41\x03H\x03\x88\x01\x01\x12W\n\x04type\x18\x06 \x01(\x0e\x32\x44.google.ads.googleads.v5.enums.MobileDeviceTypeEnum.MobileDeviceTypeB\x03\xe0\x41\x03:b\xea\x41_\n-googleads.googleapis.com/MobileDeviceConstant\x12.mobileDeviceConstants/{mobile_device_constant}B\x05\n\x03_idB\x07\n\x05_nameB\x14\n\x12_manufacturer_nameB\x18\n\x16_operating_system_nameB\x86\x02\n%com.google.ads.googleads.v5.resourcesB\x19MobileDeviceConstantProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v5/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V5.Resources\xca\x02!Google\\Ads\\GoogleAds\\V5\\Resources\xea\x02%Google::Ads::GoogleAds::V5::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_mobile__device__type__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_MOBILEDEVICECONSTANT = _descriptor.Descriptor(
  name='MobileDeviceConstant',
  full_name='google.ads.googleads.v5.resources.MobileDeviceConstant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v5.resources.MobileDeviceConstant.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003\372A/\n-googleads.googleapis.com/MobileDeviceConstant', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v5.resources.MobileDeviceConstant.id', index=1,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.ads.googleads.v5.resources.MobileDeviceConstant.name', index=2,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='manufacturer_name', full_name='google.ads.googleads.v5.resources.MobileDeviceConstant.manufacturer_name', index=3,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operating_system_name', full_name='google.ads.googleads.v5.resources.MobileDeviceConstant.operating_system_name', index=4,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.ads.googleads.v5.resources.MobileDeviceConstant.type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352A_\n-googleads.googleapis.com/MobileDeviceConstant\022.mobileDeviceConstants/{mobile_device_constant}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_id', full_name='google.ads.googleads.v5.resources.MobileDeviceConstant._id',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_name', full_name='google.ads.googleads.v5.resources.MobileDeviceConstant._name',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_manufacturer_name', full_name='google.ads.googleads.v5.resources.MobileDeviceConstant._manufacturer_name',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_operating_system_name', full_name='google.ads.googleads.v5.resources.MobileDeviceConstant._operating_system_name',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=260,
  serialized_end=737,
)

_MOBILEDEVICECONSTANT.fields_by_name['type'].enum_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_mobile__device__type__pb2._MOBILEDEVICETYPEENUM_MOBILEDEVICETYPE
_MOBILEDEVICECONSTANT.oneofs_by_name['_id'].fields.append(
  _MOBILEDEVICECONSTANT.fields_by_name['id'])
_MOBILEDEVICECONSTANT.fields_by_name['id'].containing_oneof = _MOBILEDEVICECONSTANT.oneofs_by_name['_id']
_MOBILEDEVICECONSTANT.oneofs_by_name['_name'].fields.append(
  _MOBILEDEVICECONSTANT.fields_by_name['name'])
_MOBILEDEVICECONSTANT.fields_by_name['name'].containing_oneof = _MOBILEDEVICECONSTANT.oneofs_by_name['_name']
_MOBILEDEVICECONSTANT.oneofs_by_name['_manufacturer_name'].fields.append(
  _MOBILEDEVICECONSTANT.fields_by_name['manufacturer_name'])
_MOBILEDEVICECONSTANT.fields_by_name['manufacturer_name'].containing_oneof = _MOBILEDEVICECONSTANT.oneofs_by_name['_manufacturer_name']
_MOBILEDEVICECONSTANT.oneofs_by_name['_operating_system_name'].fields.append(
  _MOBILEDEVICECONSTANT.fields_by_name['operating_system_name'])
_MOBILEDEVICECONSTANT.fields_by_name['operating_system_name'].containing_oneof = _MOBILEDEVICECONSTANT.oneofs_by_name['_operating_system_name']
DESCRIPTOR.message_types_by_name['MobileDeviceConstant'] = _MOBILEDEVICECONSTANT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MobileDeviceConstant = _reflection.GeneratedProtocolMessageType('MobileDeviceConstant', (_message.Message,), {
  'DESCRIPTOR' : _MOBILEDEVICECONSTANT,
  '__module__' : 'google.ads.googleads_v5.proto.resources.mobile_device_constant_pb2'
  ,
  '__doc__': """A mobile device constant.
  
  Attributes:
      resource_name:
          Output only. The resource name of the mobile device constant.
          Mobile device constant resource names have the form:
          ``mobileDeviceConstants/{criterion_id}``
      id:
          Output only. The ID of the mobile device constant.
      name:
          Output only. The name of the mobile device.
      manufacturer_name:
          Output only. The manufacturer of the mobile device.
      operating_system_name:
          Output only. The operating system of the mobile device.
      type:
          Output only. The type of mobile device.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.resources.MobileDeviceConstant)
  })
_sym_db.RegisterMessage(MobileDeviceConstant)


DESCRIPTOR._options = None
_MOBILEDEVICECONSTANT.fields_by_name['resource_name']._options = None
_MOBILEDEVICECONSTANT.fields_by_name['id']._options = None
_MOBILEDEVICECONSTANT.fields_by_name['name']._options = None
_MOBILEDEVICECONSTANT.fields_by_name['manufacturer_name']._options = None
_MOBILEDEVICECONSTANT.fields_by_name['operating_system_name']._options = None
_MOBILEDEVICECONSTANT.fields_by_name['type']._options = None
_MOBILEDEVICECONSTANT._options = None
# @@protoc_insertion_point(module_scope)
