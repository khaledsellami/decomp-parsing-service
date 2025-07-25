# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import parse_pb2 as parse_dot_v2_dot_parse__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in parse/v2/parse_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ParserStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.parseAll = channel.unary_unary(
                '/parsing.Parser/parseAll',
                request_serializer=parse_dot_v2_dot_parse__pb2.ParseRequest.SerializeToString,
                response_deserializer=parse_dot_v2_dot_parse__pb2.ParseReply.FromString,
                _registered_method=True)
        self.getNames = channel.unary_unary(
                '/parsing.Parser/getNames',
                request_serializer=parse_dot_v2_dot_parse__pb2.NamesRequest.SerializeToString,
                response_deserializer=parse_dot_v2_dot_parse__pb2.Names.FromString,
                _registered_method=True)
        self.getInteractions = channel.unary_stream(
                '/parsing.Parser/getInteractions',
                request_serializer=parse_dot_v2_dot_parse__pb2.ParseRequest.SerializeToString,
                response_deserializer=parse_dot_v2_dot_parse__pb2.ParseDataResponse.FromString,
                _registered_method=True)
        self.getCalls = channel.unary_stream(
                '/parsing.Parser/getCalls',
                request_serializer=parse_dot_v2_dot_parse__pb2.ParseRequest.SerializeToString,
                response_deserializer=parse_dot_v2_dot_parse__pb2.ParseDataResponse.FromString,
                _registered_method=True)
        self.getTFIDF = channel.unary_stream(
                '/parsing.Parser/getTFIDF',
                request_serializer=parse_dot_v2_dot_parse__pb2.ParseRequest.SerializeToString,
                response_deserializer=parse_dot_v2_dot_parse__pb2.ParseDataResponse.FromString,
                _registered_method=True)
        self.getWordCounts = channel.unary_stream(
                '/parsing.Parser/getWordCounts',
                request_serializer=parse_dot_v2_dot_parse__pb2.ParseRequest.SerializeToString,
                response_deserializer=parse_dot_v2_dot_parse__pb2.ParseDataResponse.FromString,
                _registered_method=True)


class ParserServicer(object):
    """Missing associated documentation comment in .proto file."""

    def parseAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getNames(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getInteractions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getCalls(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getTFIDF(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getWordCounts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ParserServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'parseAll': grpc.unary_unary_rpc_method_handler(
                    servicer.parseAll,
                    request_deserializer=parse_dot_v2_dot_parse__pb2.ParseRequest.FromString,
                    response_serializer=parse_dot_v2_dot_parse__pb2.ParseReply.SerializeToString,
            ),
            'getNames': grpc.unary_unary_rpc_method_handler(
                    servicer.getNames,
                    request_deserializer=parse_dot_v2_dot_parse__pb2.NamesRequest.FromString,
                    response_serializer=parse_dot_v2_dot_parse__pb2.Names.SerializeToString,
            ),
            'getInteractions': grpc.unary_stream_rpc_method_handler(
                    servicer.getInteractions,
                    request_deserializer=parse_dot_v2_dot_parse__pb2.ParseRequest.FromString,
                    response_serializer=parse_dot_v2_dot_parse__pb2.ParseDataResponse.SerializeToString,
            ),
            'getCalls': grpc.unary_stream_rpc_method_handler(
                    servicer.getCalls,
                    request_deserializer=parse_dot_v2_dot_parse__pb2.ParseRequest.FromString,
                    response_serializer=parse_dot_v2_dot_parse__pb2.ParseDataResponse.SerializeToString,
            ),
            'getTFIDF': grpc.unary_stream_rpc_method_handler(
                    servicer.getTFIDF,
                    request_deserializer=parse_dot_v2_dot_parse__pb2.ParseRequest.FromString,
                    response_serializer=parse_dot_v2_dot_parse__pb2.ParseDataResponse.SerializeToString,
            ),
            'getWordCounts': grpc.unary_stream_rpc_method_handler(
                    servicer.getWordCounts,
                    request_deserializer=parse_dot_v2_dot_parse__pb2.ParseRequest.FromString,
                    response_serializer=parse_dot_v2_dot_parse__pb2.ParseDataResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'parsing.Parser', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('parsing.Parser', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Parser(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def parseAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/parsing.Parser/parseAll',
            parse_dot_v2_dot_parse__pb2.ParseRequest.SerializeToString,
            parse_dot_v2_dot_parse__pb2.ParseReply.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def getNames(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/parsing.Parser/getNames',
            parse_dot_v2_dot_parse__pb2.NamesRequest.SerializeToString,
            parse_dot_v2_dot_parse__pb2.Names.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def getInteractions(request,
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
            '/parsing.Parser/getInteractions',
            parse_dot_v2_dot_parse__pb2.ParseRequest.SerializeToString,
            parse_dot_v2_dot_parse__pb2.ParseDataResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def getCalls(request,
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
            '/parsing.Parser/getCalls',
            parse_dot_v2_dot_parse__pb2.ParseRequest.SerializeToString,
            parse_dot_v2_dot_parse__pb2.ParseDataResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def getTFIDF(request,
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
            '/parsing.Parser/getTFIDF',
            parse_dot_v2_dot_parse__pb2.ParseRequest.SerializeToString,
            parse_dot_v2_dot_parse__pb2.ParseDataResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def getWordCounts(request,
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
            '/parsing.Parser/getWordCounts',
            parse_dot_v2_dot_parse__pb2.ParseRequest.SerializeToString,
            parse_dot_v2_dot_parse__pb2.ParseDataResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
