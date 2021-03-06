# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import query_pb2 as query__pb2
import response_pb2 as response__pb2
import transaction_pb2 as transaction__pb2
import transaction_response_pb2 as transaction__response__pb2


class TokenServiceStub(object):
    """*
    Transactions and queries for the Token Service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.createToken = channel.unary_unary(
                '/proto.TokenService/createToken',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                )
        self.updateToken = channel.unary_unary(
                '/proto.TokenService/updateToken',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                )
        self.mintToken = channel.unary_unary(
                '/proto.TokenService/mintToken',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                )
        self.burnToken = channel.unary_unary(
                '/proto.TokenService/burnToken',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                )
        self.deleteToken = channel.unary_unary(
                '/proto.TokenService/deleteToken',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                )
        self.wipeTokenAccount = channel.unary_unary(
                '/proto.TokenService/wipeTokenAccount',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                )
        self.freezeTokenAccount = channel.unary_unary(
                '/proto.TokenService/freezeTokenAccount',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                )
        self.unfreezeTokenAccount = channel.unary_unary(
                '/proto.TokenService/unfreezeTokenAccount',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                )
        self.grantKycToTokenAccount = channel.unary_unary(
                '/proto.TokenService/grantKycToTokenAccount',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                )
        self.revokeKycFromTokenAccount = channel.unary_unary(
                '/proto.TokenService/revokeKycFromTokenAccount',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                )
        self.associateTokens = channel.unary_unary(
                '/proto.TokenService/associateTokens',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                )
        self.dissociateTokens = channel.unary_unary(
                '/proto.TokenService/dissociateTokens',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                )
        self.updateTokenFeeSchedule = channel.unary_unary(
                '/proto.TokenService/updateTokenFeeSchedule',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                )
        self.getTokenInfo = channel.unary_unary(
                '/proto.TokenService/getTokenInfo',
                request_serializer=query__pb2.Query.SerializeToString,
                response_deserializer=response__pb2.Response.FromString,
                )
        self.getAccountNftInfos = channel.unary_unary(
                '/proto.TokenService/getAccountNftInfos',
                request_serializer=query__pb2.Query.SerializeToString,
                response_deserializer=response__pb2.Response.FromString,
                )
        self.getTokenNftInfo = channel.unary_unary(
                '/proto.TokenService/getTokenNftInfo',
                request_serializer=query__pb2.Query.SerializeToString,
                response_deserializer=response__pb2.Response.FromString,
                )
        self.getTokenNftInfos = channel.unary_unary(
                '/proto.TokenService/getTokenNftInfos',
                request_serializer=query__pb2.Query.SerializeToString,
                response_deserializer=response__pb2.Response.FromString,
                )
        self.pauseToken = channel.unary_unary(
                '/proto.TokenService/pauseToken',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                )
        self.unpauseToken = channel.unary_unary(
                '/proto.TokenService/unpauseToken',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                )


class TokenServiceServicer(object):
    """*
    Transactions and queries for the Token Service
    """

    def createToken(self, request, context):
        """*
        Creates a new Token by submitting the transaction
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateToken(self, request, context):
        """*
        Updates the account by submitting the transaction
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def mintToken(self, request, context):
        """*
        Mints an amount of the token to the defined treasury account
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def burnToken(self, request, context):
        """*
        Burns an amount of the token from the defined treasury account
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteToken(self, request, context):
        """*
        Deletes a Token
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def wipeTokenAccount(self, request, context):
        """*
        Wipes the provided amount of tokens from the specified Account ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def freezeTokenAccount(self, request, context):
        """*
        Freezes the transfer of tokens to or from the specified Account ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def unfreezeTokenAccount(self, request, context):
        """*
        Unfreezes the transfer of tokens to or from the specified Account ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def grantKycToTokenAccount(self, request, context):
        """*
        Flags the provided Account ID as having gone through KYC
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def revokeKycFromTokenAccount(self, request, context):
        """*
        Removes the KYC flag of the provided Account ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def associateTokens(self, request, context):
        """*
        Associates tokens to an account
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def dissociateTokens(self, request, context):
        """*
        Dissociates tokens from an account
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateTokenFeeSchedule(self, request, context):
        """*
        Updates the custom fee schedule on a token
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getTokenInfo(self, request, context):
        """*
        Retrieves the metadata of a token
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getAccountNftInfos(self, request, context):
        """*
        (DEPRECATED) Gets info on NFTs N through M on the list of NFTs associated with a given account
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getTokenNftInfo(self, request, context):
        """*
        Retrieves the metadata of an NFT by TokenID and serial number
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getTokenNftInfos(self, request, context):
        """*
        (DEPRECATED) Gets info on NFTs N through M on the list of NFTs associated with a given Token of type NON_FUNGIBLE
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def pauseToken(self, request, context):
        """Pause the token
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def unpauseToken(self, request, context):
        """Unpause the token
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TokenServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'createToken': grpc.unary_unary_rpc_method_handler(
                    servicer.createToken,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'updateToken': grpc.unary_unary_rpc_method_handler(
                    servicer.updateToken,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'mintToken': grpc.unary_unary_rpc_method_handler(
                    servicer.mintToken,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'burnToken': grpc.unary_unary_rpc_method_handler(
                    servicer.burnToken,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'deleteToken': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteToken,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'wipeTokenAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.wipeTokenAccount,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'freezeTokenAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.freezeTokenAccount,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'unfreezeTokenAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.unfreezeTokenAccount,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'grantKycToTokenAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.grantKycToTokenAccount,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'revokeKycFromTokenAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.revokeKycFromTokenAccount,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'associateTokens': grpc.unary_unary_rpc_method_handler(
                    servicer.associateTokens,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'dissociateTokens': grpc.unary_unary_rpc_method_handler(
                    servicer.dissociateTokens,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'updateTokenFeeSchedule': grpc.unary_unary_rpc_method_handler(
                    servicer.updateTokenFeeSchedule,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'getTokenInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.getTokenInfo,
                    request_deserializer=query__pb2.Query.FromString,
                    response_serializer=response__pb2.Response.SerializeToString,
            ),
            'getAccountNftInfos': grpc.unary_unary_rpc_method_handler(
                    servicer.getAccountNftInfos,
                    request_deserializer=query__pb2.Query.FromString,
                    response_serializer=response__pb2.Response.SerializeToString,
            ),
            'getTokenNftInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.getTokenNftInfo,
                    request_deserializer=query__pb2.Query.FromString,
                    response_serializer=response__pb2.Response.SerializeToString,
            ),
            'getTokenNftInfos': grpc.unary_unary_rpc_method_handler(
                    servicer.getTokenNftInfos,
                    request_deserializer=query__pb2.Query.FromString,
                    response_serializer=response__pb2.Response.SerializeToString,
            ),
            'pauseToken': grpc.unary_unary_rpc_method_handler(
                    servicer.pauseToken,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
            'unpauseToken': grpc.unary_unary_rpc_method_handler(
                    servicer.unpauseToken,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.TokenService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TokenService(object):
    """*
    Transactions and queries for the Token Service
    """

    @staticmethod
    def createToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.TokenService/createToken',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.TokenService/updateToken',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def mintToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.TokenService/mintToken',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def burnToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.TokenService/burnToken',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.TokenService/deleteToken',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def wipeTokenAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.TokenService/wipeTokenAccount',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def freezeTokenAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.TokenService/freezeTokenAccount',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def unfreezeTokenAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.TokenService/unfreezeTokenAccount',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def grantKycToTokenAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.TokenService/grantKycToTokenAccount',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def revokeKycFromTokenAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.TokenService/revokeKycFromTokenAccount',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def associateTokens(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.TokenService/associateTokens',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def dissociateTokens(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.TokenService/dissociateTokens',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateTokenFeeSchedule(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.TokenService/updateTokenFeeSchedule',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getTokenInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.TokenService/getTokenInfo',
            query__pb2.Query.SerializeToString,
            response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getAccountNftInfos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.TokenService/getAccountNftInfos',
            query__pb2.Query.SerializeToString,
            response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getTokenNftInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.TokenService/getTokenNftInfo',
            query__pb2.Query.SerializeToString,
            response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getTokenNftInfos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.TokenService/getTokenNftInfos',
            query__pb2.Query.SerializeToString,
            response__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def pauseToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.TokenService/pauseToken',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def unpauseToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.TokenService/unpauseToken',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
