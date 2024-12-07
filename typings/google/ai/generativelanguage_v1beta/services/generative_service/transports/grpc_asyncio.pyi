"""
This type stub file was generated by pyright.
"""

import grpc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple, Union
from google.api_core import gapic_v1
from google.auth import credentials as ga_credentials
from grpc.experimental import aio
from google.ai.generativelanguage_v1beta.types import generative_service
from .base import GenerativeServiceTransport

class GenerativeServiceGrpcAsyncIOTransport(GenerativeServiceTransport):
    """gRPC AsyncIO backend transport for GenerativeService.

    API for using Large Models that generate multimodal content
    and have additional capabilities beyond text generation.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """
    _grpc_channel: aio.Channel
    _stubs: Dict[str, Callable] = ...
    @classmethod
    def create_channel(cls, host: str = ..., credentials: Optional[ga_credentials.Credentials] = ..., credentials_file: Optional[str] = ..., scopes: Optional[Sequence[str]] = ..., quota_project_id: Optional[str] = ..., **kwargs) -> aio.Channel:
        """Create and return a gRPC AsyncIO channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            aio.Channel: A gRPC AsyncIO channel object.
        """
        ...
    
    def __init__(self, *, host: str = ..., credentials: Optional[ga_credentials.Credentials] = ..., credentials_file: Optional[str] = ..., scopes: Optional[Sequence[str]] = ..., channel: Optional[Union[aio.Channel, Callable[..., aio.Channel]]] = ..., api_mtls_endpoint: Optional[str] = ..., client_cert_source: Optional[Callable[[], Tuple[bytes, bytes]]] = ..., ssl_channel_credentials: Optional[grpc.ChannelCredentials] = ..., client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = ..., quota_project_id: Optional[str] = ..., client_info: gapic_v1.client_info.ClientInfo = ..., always_use_jwt_access: Optional[bool] = ..., api_audience: Optional[str] = ...) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'generativelanguage.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if a ``channel`` instance is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if a ``channel`` instance is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            channel (Optional[Union[aio.Channel, Callable[..., aio.Channel]]]):
                A ``Channel`` instance through which to make calls, or a Callable
                that constructs and returns one. If set to None, ``self.create_channel``
                is used to create the channel. If a Callable is given, it will be called
                with the same arguments as used in ``self.create_channel``.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or application default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for the grpc channel. It is ignored if a ``channel`` instance is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure a mutual TLS channel. It is
                ignored if a ``channel`` instance or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        ...
    
    @property
    def grpc_channel(self) -> aio.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        ...
    
    @property
    def generate_content(self) -> Callable[[generative_service.GenerateContentRequest], Awaitable[generative_service.GenerateContentResponse],]:
        r"""Return a callable for the generate content method over gRPC.

        Generates a model response given an input
        ``GenerateContentRequest``. Refer to the `text generation
        guide <https://ai.google.dev/gemini-api/docs/text-generation>`__
        for detailed usage information. Input capabilities differ
        between models, including tuned models. Refer to the `model
        guide <https://ai.google.dev/gemini-api/docs/models/gemini>`__
        and `tuning
        guide <https://ai.google.dev/gemini-api/docs/model-tuning>`__
        for details.

        Returns:
            Callable[[~.GenerateContentRequest],
                    Awaitable[~.GenerateContentResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        ...
    
    @property
    def generate_answer(self) -> Callable[[generative_service.GenerateAnswerRequest], Awaitable[generative_service.GenerateAnswerResponse],]:
        r"""Return a callable for the generate answer method over gRPC.

        Generates a grounded answer from the model given an input
        ``GenerateAnswerRequest``.

        Returns:
            Callable[[~.GenerateAnswerRequest],
                    Awaitable[~.GenerateAnswerResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        ...
    
    @property
    def stream_generate_content(self) -> Callable[[generative_service.GenerateContentRequest], Awaitable[generative_service.GenerateContentResponse],]:
        r"""Return a callable for the stream generate content method over gRPC.

        Generates a `streamed
        response <https://ai.google.dev/gemini-api/docs/text-generation?lang=python#generate-a-text-stream>`__
        from the model given an input ``GenerateContentRequest``.

        Returns:
            Callable[[~.GenerateContentRequest],
                    Awaitable[~.GenerateContentResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        ...
    
    @property
    def embed_content(self) -> Callable[[generative_service.EmbedContentRequest], Awaitable[generative_service.EmbedContentResponse],]:
        r"""Return a callable for the embed content method over gRPC.

        Generates a text embedding vector from the input ``Content``
        using the specified `Gemini Embedding
        model <https://ai.google.dev/gemini-api/docs/models/gemini#text-embedding>`__.

        Returns:
            Callable[[~.EmbedContentRequest],
                    Awaitable[~.EmbedContentResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        ...
    
    @property
    def batch_embed_contents(self) -> Callable[[generative_service.BatchEmbedContentsRequest], Awaitable[generative_service.BatchEmbedContentsResponse],]:
        r"""Return a callable for the batch embed contents method over gRPC.

        Generates multiple embedding vectors from the input ``Content``
        which consists of a batch of strings represented as
        ``EmbedContentRequest`` objects.

        Returns:
            Callable[[~.BatchEmbedContentsRequest],
                    Awaitable[~.BatchEmbedContentsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        ...
    
    @property
    def count_tokens(self) -> Callable[[generative_service.CountTokensRequest], Awaitable[generative_service.CountTokensResponse],]:
        r"""Return a callable for the count tokens method over gRPC.

        Runs a model's tokenizer on input ``Content`` and returns the
        token count. Refer to the `tokens
        guide <https://ai.google.dev/gemini-api/docs/tokens>`__ to learn
        more about tokens.

        Returns:
            Callable[[~.CountTokensRequest],
                    Awaitable[~.CountTokensResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        ...
    
    def close(self): # -> Coroutine[Any, Any, None]:
        ...
    


__all__ = ("GenerativeServiceGrpcAsyncIOTransport", )
