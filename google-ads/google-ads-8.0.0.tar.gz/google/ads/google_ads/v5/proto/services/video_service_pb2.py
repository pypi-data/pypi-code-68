# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v5/proto/services/video_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v5.proto.resources import video_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_video__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v5/proto/services/video_service.proto',
  package='google.ads.googleads.v5.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v5.servicesB\021VideoServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v5/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V5.Services\312\002 Google\\Ads\\GoogleAds\\V5\\Services\352\002$Google::Ads::GoogleAds::V5::Services',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n:google/ads/googleads_v5/proto/services/video_service.proto\x12 google.ads.googleads.v5.services\x1a\x33google/ads/googleads_v5/proto/resources/video.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\"P\n\x0fGetVideoRequest\x12=\n\rresource_name\x18\x01 \x01(\tB&\xe0\x41\x02\xfa\x41 \n\x1egoogleads.googleapis.com/Video2\xd7\x01\n\x0cVideoService\x12\xa9\x01\n\x08GetVideo\x12\x31.google.ads.googleads.v5.services.GetVideoRequest\x1a(.google.ads.googleads.v5.resources.Video\"@\x82\xd3\xe4\x93\x02*\x12(/v5/{resource_name=customers/*/videos/*}\xda\x41\rresource_name\x1a\x1b\xca\x41\x18googleads.googleapis.comB\xf8\x01\n$com.google.ads.googleads.v5.servicesB\x11VideoServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v5/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V5.Services\xca\x02 Google\\Ads\\GoogleAds\\V5\\Services\xea\x02$Google::Ads::GoogleAds::V5::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_video__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,])




_GETVIDEOREQUEST = _descriptor.Descriptor(
  name='GetVideoRequest',
  full_name='google.ads.googleads.v5.services.GetVideoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v5.services.GetVideoRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A \n\036googleads.googleapis.com/Video', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=264,
  serialized_end=344,
)

DESCRIPTOR.message_types_by_name['GetVideoRequest'] = _GETVIDEOREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetVideoRequest = _reflection.GeneratedProtocolMessageType('GetVideoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETVIDEOREQUEST,
  '__module__' : 'google.ads.googleads_v5.proto.services.video_service_pb2'
  ,
  '__doc__': """Request message for [VideoService.GetVideo][google.ads.googleads.v5.se
  rvices.VideoService.GetVideo].
  
  Attributes:
      resource_name:
          Required. The resource name of the video to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.services.GetVideoRequest)
  })
_sym_db.RegisterMessage(GetVideoRequest)


DESCRIPTOR._options = None
_GETVIDEOREQUEST.fields_by_name['resource_name']._options = None

_VIDEOSERVICE = _descriptor.ServiceDescriptor(
  name='VideoService',
  full_name='google.ads.googleads.v5.services.VideoService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com',
  create_key=_descriptor._internal_create_key,
  serialized_start=347,
  serialized_end=562,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetVideo',
    full_name='google.ads.googleads.v5.services.VideoService.GetVideo',
    index=0,
    containing_service=None,
    input_type=_GETVIDEOREQUEST,
    output_type=google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_video__pb2._VIDEO,
    serialized_options=b'\202\323\344\223\002*\022(/v5/{resource_name=customers/*/videos/*}\332A\rresource_name',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_VIDEOSERVICE)

DESCRIPTOR.services_by_name['VideoService'] = _VIDEOSERVICE

# @@protoc_insertion_point(module_scope)
