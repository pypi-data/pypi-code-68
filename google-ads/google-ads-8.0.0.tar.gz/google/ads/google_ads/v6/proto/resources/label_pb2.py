# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v6/proto/resources/label.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v6.proto.common import text_label_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_common_dot_text__label__pb2
from google.ads.google_ads.v6.proto.enums import label_status_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_label__status__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v6/proto/resources/label.proto',
  package='google.ads.googleads.v6.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v6.resourcesB\nLabelProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V6.Resources\312\002!Google\\Ads\\GoogleAds\\V6\\Resources\352\002%Google::Ads::GoogleAds::V6::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n3google/ads/googleads_v6/proto/resources/label.proto\x12!google.ads.googleads.v6.resources\x1a\x35google/ads/googleads_v6/proto/common/text_label.proto\x1a\x36google/ads/googleads_v6/proto/enums/label_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xdf\x02\n\x05Label\x12=\n\rresource_name\x18\x01 \x01(\tB&\xe0\x41\x05\xfa\x41 \n\x1egoogleads.googleapis.com/Label\x12\x14\n\x02id\x18\x06 \x01(\x03\x42\x03\xe0\x41\x03H\x00\x88\x01\x01\x12\x11\n\x04name\x18\x07 \x01(\tH\x01\x88\x01\x01\x12O\n\x06status\x18\x04 \x01(\x0e\x32:.google.ads.googleads.v6.enums.LabelStatusEnum.LabelStatusB\x03\xe0\x41\x03\x12=\n\ntext_label\x18\x05 \x01(\x0b\x32).google.ads.googleads.v6.common.TextLabel:N\xea\x41K\n\x1egoogleads.googleapis.com/Label\x12)customers/{customer_id}/labels/{label_id}B\x05\n\x03_idB\x07\n\x05_nameB\xf7\x01\n%com.google.ads.googleads.v6.resourcesB\nLabelProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V6.Resources\xca\x02!Google\\Ads\\GoogleAds\\V6\\Resources\xea\x02%Google::Ads::GoogleAds::V6::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads__v6_dot_proto_dot_common_dot_text__label__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_label__status__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_LABEL = _descriptor.Descriptor(
  name='Label',
  full_name='google.ads.googleads.v6.resources.Label',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.resources.Label.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\372A \n\036googleads.googleapis.com/Label', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v6.resources.Label.id', index=1,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.ads.googleads.v6.resources.Label.name', index=2,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v6.resources.Label.status', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text_label', full_name='google.ads.googleads.v6.resources.Label.text_label', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_options=b'\352AK\n\036googleads.googleapis.com/Label\022)customers/{customer_id}/labels/{label_id}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_id', full_name='google.ads.googleads.v6.resources.Label._id',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_name', full_name='google.ads.googleads.v6.resources.Label._name',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=292,
  serialized_end=643,
)

_LABEL.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_enums_dot_label__status__pb2._LABELSTATUSENUM_LABELSTATUS
_LABEL.fields_by_name['text_label'].message_type = google_dot_ads_dot_googleads__v6_dot_proto_dot_common_dot_text__label__pb2._TEXTLABEL
_LABEL.oneofs_by_name['_id'].fields.append(
  _LABEL.fields_by_name['id'])
_LABEL.fields_by_name['id'].containing_oneof = _LABEL.oneofs_by_name['_id']
_LABEL.oneofs_by_name['_name'].fields.append(
  _LABEL.fields_by_name['name'])
_LABEL.fields_by_name['name'].containing_oneof = _LABEL.oneofs_by_name['_name']
DESCRIPTOR.message_types_by_name['Label'] = _LABEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Label = _reflection.GeneratedProtocolMessageType('Label', (_message.Message,), {
  'DESCRIPTOR' : _LABEL,
  '__module__' : 'google.ads.googleads_v6.proto.resources.label_pb2'
  ,
  '__doc__': """A label.
  
  Attributes:
      resource_name:
          Immutable. Name of the resource. Label resource names have the
          form: ``customers/{customer_id}/labels/{label_id}``
      id:
          Output only. Id of the label. Read only.
      name:
          The name of the label.  This field is required and should not
          be empty when creating a new label.  The length of this string
          should be between 1 and 80, inclusive.
      status:
          Output only. Status of the label. Read only.
      text_label:
          A type of label displaying text on a colored background.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.resources.Label)
  })
_sym_db.RegisterMessage(Label)


DESCRIPTOR._options = None
_LABEL.fields_by_name['resource_name']._options = None
_LABEL.fields_by_name['id']._options = None
_LABEL.fields_by_name['status']._options = None
_LABEL._options = None
# @@protoc_insertion_point(module_scope)
