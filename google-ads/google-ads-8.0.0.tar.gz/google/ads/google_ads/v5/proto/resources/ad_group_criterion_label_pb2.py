# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v5/proto/resources/ad_group_criterion_label.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v5/proto/resources/ad_group_criterion_label.proto',
  package='google.ads.googleads.v5.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v5.resourcesB\032AdGroupCriterionLabelProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v5/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V5.Resources\312\002!Google\\Ads\\GoogleAds\\V5\\Resources\352\002%Google::Ads::GoogleAds::V5::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nFgoogle/ads/googleads_v5/proto/resources/ad_group_criterion_label.proto\x12!google.ads.googleads.v5.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xa5\x03\n\x15\x41\x64GroupCriterionLabel\x12M\n\rresource_name\x18\x01 \x01(\tB6\xe0\x41\x05\xfa\x41\x30\n.googleads.googleapis.com/AdGroupCriterionLabel\x12k\n\x12\x61\x64_group_criterion\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueB1\xe0\x41\x05\xfa\x41+\n)googleads.googleapis.com/AdGroupCriterion\x12S\n\x05label\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValueB&\xe0\x41\x05\xfa\x41 \n\x1egoogleads.googleapis.com/Label:{\xea\x41x\n.googleads.googleapis.com/AdGroupCriterionLabel\x12\x46\x63ustomers/{customer}/adGroupCriterionLabels/{ad_group_criterion_label}B\x87\x02\n%com.google.ads.googleads.v5.resourcesB\x1a\x41\x64GroupCriterionLabelProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v5/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V5.Resources\xca\x02!Google\\Ads\\GoogleAds\\V5\\Resources\xea\x02%Google::Ads::GoogleAds::V5::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_ADGROUPCRITERIONLABEL = _descriptor.Descriptor(
  name='AdGroupCriterionLabel',
  full_name='google.ads.googleads.v5.resources.AdGroupCriterionLabel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v5.resources.AdGroupCriterionLabel.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\372A0\n.googleads.googleapis.com/AdGroupCriterionLabel', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ad_group_criterion', full_name='google.ads.googleads.v5.resources.AdGroupCriterionLabel.ad_group_criterion', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\372A+\n)googleads.googleapis.com/AdGroupCriterion', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='google.ads.googleads.v5.resources.AdGroupCriterionLabel.label', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\372A \n\036googleads.googleapis.com/Label', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352Ax\n.googleads.googleapis.com/AdGroupCriterionLabel\022Fcustomers/{customer}/adGroupCriterionLabels/{ad_group_criterion_label}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=232,
  serialized_end=653,
)

_ADGROUPCRITERIONLABEL.fields_by_name['ad_group_criterion'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_ADGROUPCRITERIONLABEL.fields_by_name['label'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['AdGroupCriterionLabel'] = _ADGROUPCRITERIONLABEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdGroupCriterionLabel = _reflection.GeneratedProtocolMessageType('AdGroupCriterionLabel', (_message.Message,), {
  'DESCRIPTOR' : _ADGROUPCRITERIONLABEL,
  '__module__' : 'google.ads.googleads_v5.proto.resources.ad_group_criterion_label_pb2'
  ,
  '__doc__': """A relationship between an ad group criterion and a label.
  
  Attributes:
      resource_name:
          Immutable. The resource name of the ad group criterion label.
          Ad group criterion label resource names have the form: ``custo
          mers/{customer_id}/adGroupCriterionLabels/{ad_group_id}~{crite
          rion_id}~{label_id}``
      ad_group_criterion:
          Immutable. The ad group criterion to which the label is
          attached.
      label:
          Immutable. The label assigned to the ad group criterion.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.resources.AdGroupCriterionLabel)
  })
_sym_db.RegisterMessage(AdGroupCriterionLabel)


DESCRIPTOR._options = None
_ADGROUPCRITERIONLABEL.fields_by_name['resource_name']._options = None
_ADGROUPCRITERIONLABEL.fields_by_name['ad_group_criterion']._options = None
_ADGROUPCRITERIONLABEL.fields_by_name['label']._options = None
_ADGROUPCRITERIONLABEL._options = None
# @@protoc_insertion_point(module_scope)
