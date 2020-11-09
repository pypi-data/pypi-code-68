# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v5/proto/common/asset_types.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v5.proto.enums import mime_type_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_mime__type__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v5/proto/common/asset_types.proto',
  package='google.ads.googleads.v5.common',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v5.commonB\017AssetTypesProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v5/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V5.Common\312\002\036Google\\Ads\\GoogleAds\\V5\\Common\352\002\"Google::Ads::GoogleAds::V5::Common',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n6google/ads/googleads_v5/proto/common/asset_types.proto\x12\x1egoogle.ads.googleads.v5.common\x1a\x33google/ads/googleads_v5/proto/enums/mime_type.proto\x1a\x1cgoogle/api/annotations.proto\"G\n\x11YoutubeVideoAsset\x12\x1d\n\x10youtube_video_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x13\n\x11_youtube_video_id\".\n\x10MediaBundleAsset\x12\x11\n\x04\x64\x61ta\x18\x02 \x01(\x0cH\x00\x88\x01\x01\x42\x07\n\x05_data\"\xda\x01\n\nImageAsset\x12\x11\n\x04\x64\x61ta\x18\x05 \x01(\x0cH\x00\x88\x01\x01\x12\x16\n\tfile_size\x18\x06 \x01(\x03H\x01\x88\x01\x01\x12G\n\tmime_type\x18\x03 \x01(\x0e\x32\x34.google.ads.googleads.v5.enums.MimeTypeEnum.MimeType\x12\x41\n\tfull_size\x18\x04 \x01(\x0b\x32..google.ads.googleads.v5.common.ImageDimensionB\x07\n\x05_dataB\x0c\n\n_file_size\"\x84\x01\n\x0eImageDimension\x12\x1a\n\rheight_pixels\x18\x04 \x01(\x03H\x00\x88\x01\x01\x12\x19\n\x0cwidth_pixels\x18\x05 \x01(\x03H\x01\x88\x01\x01\x12\x10\n\x03url\x18\x06 \x01(\tH\x02\x88\x01\x01\x42\x10\n\x0e_height_pixelsB\x0f\n\r_width_pixelsB\x06\n\x04_url\"\'\n\tTextAsset\x12\x11\n\x04text\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_text\"\x13\n\x11\x42ookOnGoogleAssetB\xea\x01\n\"com.google.ads.googleads.v5.commonB\x0f\x41ssetTypesProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v5/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V5.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V5\\Common\xea\x02\"Google::Ads::GoogleAds::V5::Commonb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_mime__type__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_YOUTUBEVIDEOASSET = _descriptor.Descriptor(
  name='YoutubeVideoAsset',
  full_name='google.ads.googleads.v5.common.YoutubeVideoAsset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='youtube_video_id', full_name='google.ads.googleads.v5.common.YoutubeVideoAsset.youtube_video_id', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
      name='_youtube_video_id', full_name='google.ads.googleads.v5.common.YoutubeVideoAsset._youtube_video_id',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=173,
  serialized_end=244,
)


_MEDIABUNDLEASSET = _descriptor.Descriptor(
  name='MediaBundleAsset',
  full_name='google.ads.googleads.v5.common.MediaBundleAsset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='google.ads.googleads.v5.common.MediaBundleAsset.data', index=0,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
      name='_data', full_name='google.ads.googleads.v5.common.MediaBundleAsset._data',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=246,
  serialized_end=292,
)


_IMAGEASSET = _descriptor.Descriptor(
  name='ImageAsset',
  full_name='google.ads.googleads.v5.common.ImageAsset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='google.ads.googleads.v5.common.ImageAsset.data', index=0,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_size', full_name='google.ads.googleads.v5.common.ImageAsset.file_size', index=1,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mime_type', full_name='google.ads.googleads.v5.common.ImageAsset.mime_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='full_size', full_name='google.ads.googleads.v5.common.ImageAsset.full_size', index=3,
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
    _descriptor.OneofDescriptor(
      name='_data', full_name='google.ads.googleads.v5.common.ImageAsset._data',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_file_size', full_name='google.ads.googleads.v5.common.ImageAsset._file_size',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=295,
  serialized_end=513,
)


_IMAGEDIMENSION = _descriptor.Descriptor(
  name='ImageDimension',
  full_name='google.ads.googleads.v5.common.ImageDimension',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='height_pixels', full_name='google.ads.googleads.v5.common.ImageDimension.height_pixels', index=0,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width_pixels', full_name='google.ads.googleads.v5.common.ImageDimension.width_pixels', index=1,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='url', full_name='google.ads.googleads.v5.common.ImageDimension.url', index=2,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
      name='_height_pixels', full_name='google.ads.googleads.v5.common.ImageDimension._height_pixels',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_width_pixels', full_name='google.ads.googleads.v5.common.ImageDimension._width_pixels',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_url', full_name='google.ads.googleads.v5.common.ImageDimension._url',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=516,
  serialized_end=648,
)


_TEXTASSET = _descriptor.Descriptor(
  name='TextAsset',
  full_name='google.ads.googleads.v5.common.TextAsset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='google.ads.googleads.v5.common.TextAsset.text', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
      name='_text', full_name='google.ads.googleads.v5.common.TextAsset._text',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=650,
  serialized_end=689,
)


_BOOKONGOOGLEASSET = _descriptor.Descriptor(
  name='BookOnGoogleAsset',
  full_name='google.ads.googleads.v5.common.BookOnGoogleAsset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=691,
  serialized_end=710,
)

_YOUTUBEVIDEOASSET.oneofs_by_name['_youtube_video_id'].fields.append(
  _YOUTUBEVIDEOASSET.fields_by_name['youtube_video_id'])
_YOUTUBEVIDEOASSET.fields_by_name['youtube_video_id'].containing_oneof = _YOUTUBEVIDEOASSET.oneofs_by_name['_youtube_video_id']
_MEDIABUNDLEASSET.oneofs_by_name['_data'].fields.append(
  _MEDIABUNDLEASSET.fields_by_name['data'])
_MEDIABUNDLEASSET.fields_by_name['data'].containing_oneof = _MEDIABUNDLEASSET.oneofs_by_name['_data']
_IMAGEASSET.fields_by_name['mime_type'].enum_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_mime__type__pb2._MIMETYPEENUM_MIMETYPE
_IMAGEASSET.fields_by_name['full_size'].message_type = _IMAGEDIMENSION
_IMAGEASSET.oneofs_by_name['_data'].fields.append(
  _IMAGEASSET.fields_by_name['data'])
_IMAGEASSET.fields_by_name['data'].containing_oneof = _IMAGEASSET.oneofs_by_name['_data']
_IMAGEASSET.oneofs_by_name['_file_size'].fields.append(
  _IMAGEASSET.fields_by_name['file_size'])
_IMAGEASSET.fields_by_name['file_size'].containing_oneof = _IMAGEASSET.oneofs_by_name['_file_size']
_IMAGEDIMENSION.oneofs_by_name['_height_pixels'].fields.append(
  _IMAGEDIMENSION.fields_by_name['height_pixels'])
_IMAGEDIMENSION.fields_by_name['height_pixels'].containing_oneof = _IMAGEDIMENSION.oneofs_by_name['_height_pixels']
_IMAGEDIMENSION.oneofs_by_name['_width_pixels'].fields.append(
  _IMAGEDIMENSION.fields_by_name['width_pixels'])
_IMAGEDIMENSION.fields_by_name['width_pixels'].containing_oneof = _IMAGEDIMENSION.oneofs_by_name['_width_pixels']
_IMAGEDIMENSION.oneofs_by_name['_url'].fields.append(
  _IMAGEDIMENSION.fields_by_name['url'])
_IMAGEDIMENSION.fields_by_name['url'].containing_oneof = _IMAGEDIMENSION.oneofs_by_name['_url']
_TEXTASSET.oneofs_by_name['_text'].fields.append(
  _TEXTASSET.fields_by_name['text'])
_TEXTASSET.fields_by_name['text'].containing_oneof = _TEXTASSET.oneofs_by_name['_text']
DESCRIPTOR.message_types_by_name['YoutubeVideoAsset'] = _YOUTUBEVIDEOASSET
DESCRIPTOR.message_types_by_name['MediaBundleAsset'] = _MEDIABUNDLEASSET
DESCRIPTOR.message_types_by_name['ImageAsset'] = _IMAGEASSET
DESCRIPTOR.message_types_by_name['ImageDimension'] = _IMAGEDIMENSION
DESCRIPTOR.message_types_by_name['TextAsset'] = _TEXTASSET
DESCRIPTOR.message_types_by_name['BookOnGoogleAsset'] = _BOOKONGOOGLEASSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

YoutubeVideoAsset = _reflection.GeneratedProtocolMessageType('YoutubeVideoAsset', (_message.Message,), {
  'DESCRIPTOR' : _YOUTUBEVIDEOASSET,
  '__module__' : 'google.ads.googleads_v5.proto.common.asset_types_pb2'
  ,
  '__doc__': """A YouTube asset.
  
  Attributes:
      youtube_video_id:
          YouTube video id. This is the 11 character string value used
          in the YouTube video URL.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.common.YoutubeVideoAsset)
  })
_sym_db.RegisterMessage(YoutubeVideoAsset)

MediaBundleAsset = _reflection.GeneratedProtocolMessageType('MediaBundleAsset', (_message.Message,), {
  'DESCRIPTOR' : _MEDIABUNDLEASSET,
  '__module__' : 'google.ads.googleads_v5.proto.common.asset_types_pb2'
  ,
  '__doc__': """A MediaBundle asset.
  
  Attributes:
      data:
          Media bundle (ZIP file) asset data. The format of the uploaded
          ZIP file depends on the ad field where it will be used. For
          more information on the format, see the documentation of the
          ad field where you plan on using the MediaBundleAsset. This
          field is mutate only.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.common.MediaBundleAsset)
  })
_sym_db.RegisterMessage(MediaBundleAsset)

ImageAsset = _reflection.GeneratedProtocolMessageType('ImageAsset', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEASSET,
  '__module__' : 'google.ads.googleads_v5.proto.common.asset_types_pb2'
  ,
  '__doc__': """An Image asset.
  
  Attributes:
      data:
          The raw bytes data of an image. This field is mutate only.
      file_size:
          File size of the image asset in bytes.
      mime_type:
          MIME type of the image asset.
      full_size:
          Metadata for this image at its original size.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.common.ImageAsset)
  })
_sym_db.RegisterMessage(ImageAsset)

ImageDimension = _reflection.GeneratedProtocolMessageType('ImageDimension', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEDIMENSION,
  '__module__' : 'google.ads.googleads_v5.proto.common.asset_types_pb2'
  ,
  '__doc__': """Metadata for an image at a certain size, either original or resized.
  
  Attributes:
      height_pixels:
          Height of the image.
      width_pixels:
          Width of the image.
      url:
          A URL that returns the image with this height and width.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.common.ImageDimension)
  })
_sym_db.RegisterMessage(ImageDimension)

TextAsset = _reflection.GeneratedProtocolMessageType('TextAsset', (_message.Message,), {
  'DESCRIPTOR' : _TEXTASSET,
  '__module__' : 'google.ads.googleads_v5.proto.common.asset_types_pb2'
  ,
  '__doc__': """A Text asset.
  
  Attributes:
      text:
          Text content of the text asset.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.common.TextAsset)
  })
_sym_db.RegisterMessage(TextAsset)

BookOnGoogleAsset = _reflection.GeneratedProtocolMessageType('BookOnGoogleAsset', (_message.Message,), {
  'DESCRIPTOR' : _BOOKONGOOGLEASSET,
  '__module__' : 'google.ads.googleads_v5.proto.common.asset_types_pb2'
  ,
  '__doc__': """A Book on Google asset. Used to redirect user to book through Google.
  Book on Google will change the redirect url to book directly through
  Google.""",
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.common.BookOnGoogleAsset)
  })
_sym_db.RegisterMessage(BookOnGoogleAsset)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
