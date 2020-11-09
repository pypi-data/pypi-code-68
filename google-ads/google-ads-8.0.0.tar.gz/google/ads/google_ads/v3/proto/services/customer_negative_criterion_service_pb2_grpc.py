# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v3.proto.resources import customer_negative_criterion_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_customer__negative__criterion__pb2
from google.ads.google_ads.v3.proto.services import customer_negative_criterion_service_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_customer__negative__criterion__service__pb2


class CustomerNegativeCriterionServiceStub(object):
  """Proto file describing the Customer Negative Criterion service.

  Service to manage customer negative criteria.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetCustomerNegativeCriterion = channel.unary_unary(
        '/google.ads.googleads.v3.services.CustomerNegativeCriterionService/GetCustomerNegativeCriterion',
        request_serializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_customer__negative__criterion__service__pb2.GetCustomerNegativeCriterionRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_customer__negative__criterion__pb2.CustomerNegativeCriterion.FromString,
        )
    self.MutateCustomerNegativeCriteria = channel.unary_unary(
        '/google.ads.googleads.v3.services.CustomerNegativeCriterionService/MutateCustomerNegativeCriteria',
        request_serializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_customer__negative__criterion__service__pb2.MutateCustomerNegativeCriteriaRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_customer__negative__criterion__service__pb2.MutateCustomerNegativeCriteriaResponse.FromString,
        )


class CustomerNegativeCriterionServiceServicer(object):
  """Proto file describing the Customer Negative Criterion service.

  Service to manage customer negative criteria.
  """

  def GetCustomerNegativeCriterion(self, request, context):
    """Returns the requested criterion in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateCustomerNegativeCriteria(self, request, context):
    """Creates or removes criteria. Operation statuses are returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CustomerNegativeCriterionServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetCustomerNegativeCriterion': grpc.unary_unary_rpc_method_handler(
          servicer.GetCustomerNegativeCriterion,
          request_deserializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_customer__negative__criterion__service__pb2.GetCustomerNegativeCriterionRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_customer__negative__criterion__pb2.CustomerNegativeCriterion.SerializeToString,
      ),
      'MutateCustomerNegativeCriteria': grpc.unary_unary_rpc_method_handler(
          servicer.MutateCustomerNegativeCriteria,
          request_deserializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_customer__negative__criterion__service__pb2.MutateCustomerNegativeCriteriaRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_customer__negative__criterion__service__pb2.MutateCustomerNegativeCriteriaResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v3.services.CustomerNegativeCriterionService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
