# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.asset_v1beta1.proto import asset_service_pb2 as google_dot_cloud_dot_asset__v1beta1_dot_proto_dot_asset__service__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2


class AssetServiceStub(object):
  """Asset service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ExportAssets = channel.unary_unary(
        '/google.cloud.asset.v1beta1.AssetService/ExportAssets',
        request_serializer=google_dot_cloud_dot_asset__v1beta1_dot_proto_dot_asset__service__pb2.ExportAssetsRequest.SerializeToString,
        response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
        )
    self.BatchGetAssetsHistory = channel.unary_unary(
        '/google.cloud.asset.v1beta1.AssetService/BatchGetAssetsHistory',
        request_serializer=google_dot_cloud_dot_asset__v1beta1_dot_proto_dot_asset__service__pb2.BatchGetAssetsHistoryRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_asset__v1beta1_dot_proto_dot_asset__service__pb2.BatchGetAssetsHistoryResponse.FromString,
        )


class AssetServiceServicer(object):
  """Asset service definition.
  """

  def ExportAssets(self, request, context):
    """Exports assets with time and resource types to a given Cloud Storage
    location. The output format is newline-delimited JSON.
    This API implements the [google.longrunning.Operation][google.longrunning.Operation] API allowing you
    to keep track of the export.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def BatchGetAssetsHistory(self, request, context):
    """Batch gets the update history of assets that overlap a time window.
    For RESOURCE content, this API outputs history with asset in both
    non-delete or deleted status.
    For IAM_POLICY content, this API outputs history when the asset and its
    attached IAM POLICY both exist. This can create gaps in the output history.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AssetServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ExportAssets': grpc.unary_unary_rpc_method_handler(
          servicer.ExportAssets,
          request_deserializer=google_dot_cloud_dot_asset__v1beta1_dot_proto_dot_asset__service__pb2.ExportAssetsRequest.FromString,
          response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
      ),
      'BatchGetAssetsHistory': grpc.unary_unary_rpc_method_handler(
          servicer.BatchGetAssetsHistory,
          request_deserializer=google_dot_cloud_dot_asset__v1beta1_dot_proto_dot_asset__service__pb2.BatchGetAssetsHistoryRequest.FromString,
          response_serializer=google_dot_cloud_dot_asset__v1beta1_dot_proto_dot_asset__service__pb2.BatchGetAssetsHistoryResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.cloud.asset.v1beta1.AssetService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
