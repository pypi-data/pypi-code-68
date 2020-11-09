# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v6.proto.resources import feed_item_set_link_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_feed__item__set__link__pb2
from google.ads.google_ads.v6.proto.services import feed_item_set_link_service_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_feed__item__set__link__service__pb2


class FeedItemSetLinkServiceStub(object):
    """Proto file describing the FeedItemSetLink service.

    Service to manage feed item set links.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetFeedItemSetLink = channel.unary_unary(
                '/google.ads.googleads.v6.services.FeedItemSetLinkService/GetFeedItemSetLink',
                request_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_feed__item__set__link__service__pb2.GetFeedItemSetLinkRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_feed__item__set__link__pb2.FeedItemSetLink.FromString,
                )
        self.MutateFeedItemSetLinks = channel.unary_unary(
                '/google.ads.googleads.v6.services.FeedItemSetLinkService/MutateFeedItemSetLinks',
                request_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_feed__item__set__link__service__pb2.MutateFeedItemSetLinksRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_feed__item__set__link__service__pb2.MutateFeedItemSetLinksResponse.FromString,
                )


class FeedItemSetLinkServiceServicer(object):
    """Proto file describing the FeedItemSetLink service.

    Service to manage feed item set links.
    """

    def GetFeedItemSetLink(self, request, context):
        """Returns the requested feed item set link in full detail.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MutateFeedItemSetLinks(self, request, context):
        """Creates, updates, or removes feed item set links.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FeedItemSetLinkServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetFeedItemSetLink': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFeedItemSetLink,
                    request_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_feed__item__set__link__service__pb2.GetFeedItemSetLinkRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_feed__item__set__link__pb2.FeedItemSetLink.SerializeToString,
            ),
            'MutateFeedItemSetLinks': grpc.unary_unary_rpc_method_handler(
                    servicer.MutateFeedItemSetLinks,
                    request_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_feed__item__set__link__service__pb2.MutateFeedItemSetLinksRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_feed__item__set__link__service__pb2.MutateFeedItemSetLinksResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v6.services.FeedItemSetLinkService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FeedItemSetLinkService(object):
    """Proto file describing the FeedItemSetLink service.

    Service to manage feed item set links.
    """

    @staticmethod
    def GetFeedItemSetLink(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.FeedItemSetLinkService/GetFeedItemSetLink',
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_feed__item__set__link__service__pb2.GetFeedItemSetLinkRequest.SerializeToString,
            google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_feed__item__set__link__pb2.FeedItemSetLink.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MutateFeedItemSetLinks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.FeedItemSetLinkService/MutateFeedItemSetLinks',
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_feed__item__set__link__service__pb2.MutateFeedItemSetLinksRequest.SerializeToString,
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_feed__item__set__link__service__pb2.MutateFeedItemSetLinksResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
