# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import basic_types_pb2 as basic__types__pb2
import mirror_network_service_pb2 as mirror__network__service__pb2

GRPC_GENERATED_VERSION = '1.63.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in mirror_network_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class NetworkServiceStub(object):
    """*
    Provides cross network APIs like address book queries
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getNodes = channel.unary_stream(
                '/com.hedera.mirror.api.proto.NetworkService/getNodes',
                request_serializer=mirror__network__service__pb2.AddressBookQuery.SerializeToString,
                response_deserializer=basic__types__pb2.NodeAddress.FromString,
                _registered_method=True)


class NetworkServiceServicer(object):
    """*
    Provides cross network APIs like address book queries
    """

    def getNodes(self, request, context):
        """
        Query for an address book and return its nodes. The nodes are returned in ascending order by node ID. The
        response is not guaranteed to be a byte-for-byte equivalent to the NodeAddress in the Hedera file on
        the network since it is reconstructed from a normalized database table.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NetworkServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getNodes': grpc.unary_stream_rpc_method_handler(
                    servicer.getNodes,
                    request_deserializer=mirror__network__service__pb2.AddressBookQuery.FromString,
                    response_serializer=basic__types__pb2.NodeAddress.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.hedera.mirror.api.proto.NetworkService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NetworkService(object):
    """*
    Provides cross network APIs like address book queries
    """

    @staticmethod
    def getNodes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/com.hedera.mirror.api.proto.NetworkService/getNodes',
            mirror__network__service__pb2.AddressBookQuery.SerializeToString,
            basic__types__pb2.NodeAddress.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
