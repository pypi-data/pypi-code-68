# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/services/carrier_constant_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v3.proto.resources import carrier_constant_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_carrier__constant__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v3/proto/services/carrier_constant_service.proto',
  package='google.ads.googleads.v3.services',
  syntax='proto3',
  serialized_options=_b('\n$com.google.ads.googleads.v3.servicesB\033CarrierConstantServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v3/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V3.Services\312\002 Google\\Ads\\GoogleAds\\V3\\Services\352\002$Google::Ads::GoogleAds::V3::Services'),
  serialized_pb=_b('\nEgoogle/ads/googleads_v3/proto/services/carrier_constant_service.proto\x12 google.ads.googleads.v3.services\x1a>google/ads/googleads_v3/proto/resources/carrier_constant.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\"d\n\x19GetCarrierConstantRequest\x12G\n\rresource_name\x18\x01 \x01(\tB0\xe0\x41\x02\xfa\x41*\n(googleads.googleapis.com/CarrierConstant2\xfd\x01\n\x16\x43\x61rrierConstantService\x12\xc5\x01\n\x12GetCarrierConstant\x12;.google.ads.googleads.v3.services.GetCarrierConstantRequest\x1a\x32.google.ads.googleads.v3.resources.CarrierConstant\">\x82\xd3\xe4\x93\x02(\x12&/v3/{resource_name=carrierConstants/*}\xda\x41\rresource_name\x1a\x1b\xca\x41\x18googleads.googleapis.comB\x82\x02\n$com.google.ads.googleads.v3.servicesB\x1b\x43\x61rrierConstantServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v3/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V3.Services\xca\x02 Google\\Ads\\GoogleAds\\V3\\Services\xea\x02$Google::Ads::GoogleAds::V3::Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_carrier__constant__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,])




_GETCARRIERCONSTANTREQUEST = _descriptor.Descriptor(
  name='GetCarrierConstantRequest',
  full_name='google.ads.googleads.v3.services.GetCarrierConstantRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v3.services.GetCarrierConstantRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002\372A*\n(googleads.googleapis.com/CarrierConstant'), file=DESCRIPTOR),
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
  serialized_start=286,
  serialized_end=386,
)

DESCRIPTOR.message_types_by_name['GetCarrierConstantRequest'] = _GETCARRIERCONSTANTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCarrierConstantRequest = _reflection.GeneratedProtocolMessageType('GetCarrierConstantRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCARRIERCONSTANTREQUEST,
  __module__ = 'google.ads.googleads_v3.proto.services.carrier_constant_service_pb2'
  ,
  __doc__ = """Request message for
  [CarrierConstantService.GetCarrierConstant][google.ads.googleads.v3.services.CarrierConstantService.GetCarrierConstant].
  
  
  Attributes:
      resource_name:
          Required. Resource name of the carrier constant to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.services.GetCarrierConstantRequest)
  ))
_sym_db.RegisterMessage(GetCarrierConstantRequest)


DESCRIPTOR._options = None
_GETCARRIERCONSTANTREQUEST.fields_by_name['resource_name']._options = None

_CARRIERCONSTANTSERVICE = _descriptor.ServiceDescriptor(
  name='CarrierConstantService',
  full_name='google.ads.googleads.v3.services.CarrierConstantService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=_b('\312A\030googleads.googleapis.com'),
  serialized_start=389,
  serialized_end=642,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCarrierConstant',
    full_name='google.ads.googleads.v3.services.CarrierConstantService.GetCarrierConstant',
    index=0,
    containing_service=None,
    input_type=_GETCARRIERCONSTANTREQUEST,
    output_type=google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_carrier__constant__pb2._CARRIERCONSTANT,
    serialized_options=_b('\202\323\344\223\002(\022&/v3/{resource_name=carrierConstants/*}\332A\rresource_name'),
  ),
])
_sym_db.RegisterServiceDescriptor(_CARRIERCONSTANTSERVICE)

DESCRIPTOR.services_by_name['CarrierConstantService'] = _CARRIERCONSTANTSERVICE

# @@protoc_insertion_point(module_scope)
