# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v4/proto/resources/remarketing_action.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v4.proto.common import tag_snippet_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_common_dot_tag__snippet__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v4/proto/resources/remarketing_action.proto',
  package='google.ads.googleads.v4.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v4.resourcesB\026RemarketingActionProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v4/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V4.Resources\312\002!Google\\Ads\\GoogleAds\\V4\\Resources\352\002%Google::Ads::GoogleAds::V4::Resources'),
  serialized_pb=_b('\n@google/ads/googleads_v4/proto/resources/remarketing_action.proto\x12!google.ads.googleads.v4.resources\x1a\x36google/ads/googleads_v4/proto/common/tag_snippet.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xee\x02\n\x11RemarketingAction\x12I\n\rresource_name\x18\x01 \x01(\tB2\xe0\x41\x05\xfa\x41,\n*googleads.googleapis.com/RemarketingAction\x12,\n\x02id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x03\xe0\x41\x03\x12*\n\x04name\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x45\n\x0ctag_snippets\x18\x04 \x03(\x0b\x32*.google.ads.googleads.v4.common.TagSnippetB\x03\xe0\x41\x03:m\xea\x41j\n*googleads.googleapis.com/RemarketingAction\x12<customers/{customer}/remarketingActions/{remarketing_action}B\x83\x02\n%com.google.ads.googleads.v4.resourcesB\x16RemarketingActionProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v4/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V4.Resources\xca\x02!Google\\Ads\\GoogleAds\\V4\\Resources\xea\x02%Google::Ads::GoogleAds::V4::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v4_dot_proto_dot_common_dot_tag__snippet__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_REMARKETINGACTION = _descriptor.Descriptor(
  name='RemarketingAction',
  full_name='google.ads.googleads.v4.resources.RemarketingAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v4.resources.RemarketingAction.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\005\372A,\n*googleads.googleapis.com/RemarketingAction'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v4.resources.RemarketingAction.id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.ads.googleads.v4.resources.RemarketingAction.name', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag_snippets', full_name='google.ads.googleads.v4.resources.RemarketingAction.tag_snippets', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\352Aj\n*googleads.googleapis.com/RemarketingAction\022<customers/{customer}/remarketingActions/{remarketing_action}'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=282,
  serialized_end=648,
)

_REMARKETINGACTION.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_REMARKETINGACTION.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_REMARKETINGACTION.fields_by_name['tag_snippets'].message_type = google_dot_ads_dot_googleads__v4_dot_proto_dot_common_dot_tag__snippet__pb2._TAGSNIPPET
DESCRIPTOR.message_types_by_name['RemarketingAction'] = _REMARKETINGACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RemarketingAction = _reflection.GeneratedProtocolMessageType('RemarketingAction', (_message.Message,), dict(
  DESCRIPTOR = _REMARKETINGACTION,
  __module__ = 'google.ads.googleads_v4.proto.resources.remarketing_action_pb2'
  ,
  __doc__ = """A remarketing action. A snippet of JavaScript code that will collect the
  product id and the type of page people visited (product page, shopping
  cart page, purchase page, general site visit) on an advertiser's
  website.
  
  
  Attributes:
      resource_name:
          Immutable. The resource name of the remarketing action.
          Remarketing action resource names have the form:  ``customers/
          {customer_id}/remarketingActions/{remarketing_action_id}``
      id:
          Output only. Id of the remarketing action.
      name:
          The name of the remarketing action.  This field is required
          and should not be empty when creating new remarketing actions.
      tag_snippets:
          Output only. The snippets used for tracking remarketing
          actions.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.resources.RemarketingAction)
  ))
_sym_db.RegisterMessage(RemarketingAction)


DESCRIPTOR._options = None
_REMARKETINGACTION.fields_by_name['resource_name']._options = None
_REMARKETINGACTION.fields_by_name['id']._options = None
_REMARKETINGACTION.fields_by_name['tag_snippets']._options = None
_REMARKETINGACTION._options = None
# @@protoc_insertion_point(module_scope)
