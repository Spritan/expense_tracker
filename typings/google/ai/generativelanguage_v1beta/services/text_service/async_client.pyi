"""
This type stub file was generated by pyright.
"""

from typing import Callable, MutableSequence, Optional, Sequence, Tuple, Union
from google.api_core import gapic_v1
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials
from google.ai.generativelanguage_v1beta.types import text_service
from .client import TextServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, TextServiceTransport

"""
This type stub file was generated by pyright.
"""
OptionalRetry = ...
class TextServiceAsyncClient:
    """API for using Generative Language Models (GLMs) trained to
    generate text.
    Also known as Large Language Models (LLM)s, these generate text
    given an input prompt from the user.
    """
    _client: TextServiceClient
    DEFAULT_ENDPOINT = ...
    DEFAULT_MTLS_ENDPOINT = ...
    _DEFAULT_ENDPOINT_TEMPLATE = ...
    _DEFAULT_UNIVERSE = ...
    model_path = ...
    parse_model_path = ...
    common_billing_account_path = ...
    parse_common_billing_account_path = ...
    common_folder_path = ...
    parse_common_folder_path = ...
    common_organization_path = ...
    parse_common_organization_path = ...
    common_project_path = ...
    parse_common_project_path = ...
    common_location_path = ...
    parse_common_location_path = ...
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            TextServiceAsyncClient: The constructed client.
        """
        ...
    
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            TextServiceAsyncClient: The constructed client.
        """
        ...
    
    from_service_account_json = ...
    @classmethod
    def get_mtls_endpoint_and_cert_source(cls, client_options: Optional[ClientOptions] = ...):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variable is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        ...
    
    @property
    def transport(self) -> TextServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            TextServiceTransport: The transport used by the client instance.
        """
        ...
    
    @property
    def api_endpoint(self):
        """Return the API endpoint used by the client instance.

        Returns:
            str: The API endpoint used by the client instance.
        """
        ...
    
    @property
    def universe_domain(self) -> str:
        """Return the universe domain used by the client instance.

        Returns:
            str: The universe domain used
                by the client instance.
        """
        ...
    
    get_transport_class = ...
    def __init__(self, *, credentials: Optional[ga_credentials.Credentials] = ..., transport: Optional[Union[str, TextServiceTransport, Callable[..., TextServiceTransport]]] = ..., client_options: Optional[ClientOptions] = ..., client_info: gapic_v1.client_info.ClientInfo = ...) -> None:
        """Instantiates the text service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,TextServiceTransport,Callable[..., TextServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the TextServiceTransport constructor.
                If set to None, a transport is chosen automatically.
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]):
                Custom options for the client.

                1. The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client when ``transport`` is
                not explicitly provided. Only if this property is not set and
                ``transport`` was not explicitly provided, the endpoint is
                determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment
                variable, which have one of the following values:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto-switch to the
                default mTLS endpoint if client certificate is present; this is
                the default value).

                2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide a client certificate for mTLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

                3. The ``universe_domain`` property can be used to override the
                default "googleapis.com" universe. Note that ``api_endpoint``
                property still takes precedence; and ``universe_domain`` is
                currently not supported for mTLS.

            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        ...
    
    async def generate_text(self, request: Optional[Union[text_service.GenerateTextRequest, dict]] = ..., *, model: Optional[str] = ..., prompt: Optional[text_service.TextPrompt] = ..., temperature: Optional[float] = ..., candidate_count: Optional[int] = ..., max_output_tokens: Optional[int] = ..., top_p: Optional[float] = ..., top_k: Optional[int] = ..., retry: OptionalRetry = ..., timeout: Union[float, object] = ..., metadata: Sequence[Tuple[str, str]] = ...) -> text_service.GenerateTextResponse:
        r"""Generates a response from the model given an input
        message.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            async def sample_generate_text():
                # Create a client
                client = generativelanguage_v1beta.TextServiceAsyncClient()

                # Initialize request argument(s)
                prompt = generativelanguage_v1beta.TextPrompt()
                prompt.text = "text_value"

                request = generativelanguage_v1beta.GenerateTextRequest(
                    model="model_value",
                    prompt=prompt,
                )

                # Make the request
                response = await client.generate_text(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ai.generativelanguage_v1beta.types.GenerateTextRequest, dict]]):
                The request object. Request to generate a text completion
                response from the model.
            model (:class:`str`):
                Required. The name of the ``Model`` or ``TunedModel`` to
                use for generating the completion. Examples:
                models/text-bison-001
                tunedModels/sentence-translator-u3b7m

                This corresponds to the ``model`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            prompt (:class:`google.ai.generativelanguage_v1beta.types.TextPrompt`):
                Required. The free-form input text
                given to the model as a prompt.
                Given a prompt, the model will generate
                a TextCompletion response it predicts as
                the completion of the input text.

                This corresponds to the ``prompt`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            temperature (:class:`float`):
                Optional. Controls the randomness of the output. Note:
                The default value varies by model, see the
                ``Model.temperature`` attribute of the ``Model``
                returned the ``getModel`` function.

                Values can range from [0.0,1.0], inclusive. A value
                closer to 1.0 will produce responses that are more
                varied and creative, while a value closer to 0.0 will
                typically result in more straightforward responses from
                the model.

                This corresponds to the ``temperature`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            candidate_count (:class:`int`):
                Optional. Number of generated responses to return.

                This value must be between [1, 8], inclusive. If unset,
                this will default to 1.

                This corresponds to the ``candidate_count`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            max_output_tokens (:class:`int`):
                Optional. The maximum number of tokens to include in a
                candidate.

                If unset, this will default to output_token_limit
                specified in the ``Model`` specification.

                This corresponds to the ``max_output_tokens`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            top_p (:class:`float`):
                Optional. The maximum cumulative probability of tokens
                to consider when sampling.

                The model uses combined Top-k and nucleus sampling.

                Tokens are sorted based on their assigned probabilities
                so that only the most likely tokens are considered.
                Top-k sampling directly limits the maximum number of
                tokens to consider, while Nucleus sampling limits number
                of tokens based on the cumulative probability.

                Note: The default value varies by model, see the
                ``Model.top_p`` attribute of the ``Model`` returned the
                ``getModel`` function.

                This corresponds to the ``top_p`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            top_k (:class:`int`):
                Optional. The maximum number of tokens to consider when
                sampling.

                The model uses combined Top-k and nucleus sampling.

                Top-k sampling considers the set of ``top_k`` most
                probable tokens. Defaults to 40.

                Note: The default value varies by model, see the
                ``Model.top_k`` attribute of the ``Model`` returned the
                ``getModel`` function.

                This corresponds to the ``top_k`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.ai.generativelanguage_v1beta.types.GenerateTextResponse:
                The response from the model,
                including candidate completions.

        """
        ...
    
    async def embed_text(self, request: Optional[Union[text_service.EmbedTextRequest, dict]] = ..., *, model: Optional[str] = ..., text: Optional[str] = ..., retry: OptionalRetry = ..., timeout: Union[float, object] = ..., metadata: Sequence[Tuple[str, str]] = ...) -> text_service.EmbedTextResponse:
        r"""Generates an embedding from the model given an input
        message.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            async def sample_embed_text():
                # Create a client
                client = generativelanguage_v1beta.TextServiceAsyncClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.EmbedTextRequest(
                    model="model_value",
                )

                # Make the request
                response = await client.embed_text(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ai.generativelanguage_v1beta.types.EmbedTextRequest, dict]]):
                The request object. Request to get a text embedding from
                the model.
            model (:class:`str`):
                Required. The model name to use with
                the format model=models/{model}.

                This corresponds to the ``model`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            text (:class:`str`):
                Optional. The free-form input text
                that the model will turn into an
                embedding.

                This corresponds to the ``text`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.ai.generativelanguage_v1beta.types.EmbedTextResponse:
                The response to a EmbedTextRequest.
        """
        ...
    
    async def batch_embed_text(self, request: Optional[Union[text_service.BatchEmbedTextRequest, dict]] = ..., *, model: Optional[str] = ..., texts: Optional[MutableSequence[str]] = ..., retry: OptionalRetry = ..., timeout: Union[float, object] = ..., metadata: Sequence[Tuple[str, str]] = ...) -> text_service.BatchEmbedTextResponse:
        r"""Generates multiple embeddings from the model given
        input text in a synchronous call.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            async def sample_batch_embed_text():
                # Create a client
                client = generativelanguage_v1beta.TextServiceAsyncClient()

                # Initialize request argument(s)
                request = generativelanguage_v1beta.BatchEmbedTextRequest(
                    model="model_value",
                )

                # Make the request
                response = await client.batch_embed_text(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ai.generativelanguage_v1beta.types.BatchEmbedTextRequest, dict]]):
                The request object. Batch request to get a text embedding
                from the model.
            model (:class:`str`):
                Required. The name of the ``Model`` to use for
                generating the embedding. Examples:
                models/embedding-gecko-001

                This corresponds to the ``model`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            texts (:class:`MutableSequence[str]`):
                Optional. The free-form input texts
                that the model will turn into an
                embedding. The current limit is 100
                texts, over which an error will be
                thrown.

                This corresponds to the ``texts`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.ai.generativelanguage_v1beta.types.BatchEmbedTextResponse:
                The response to a EmbedTextRequest.
        """
        ...
    
    async def count_text_tokens(self, request: Optional[Union[text_service.CountTextTokensRequest, dict]] = ..., *, model: Optional[str] = ..., prompt: Optional[text_service.TextPrompt] = ..., retry: OptionalRetry = ..., timeout: Union[float, object] = ..., metadata: Sequence[Tuple[str, str]] = ...) -> text_service.CountTextTokensResponse:
        r"""Runs a model's tokenizer on a text and returns the
        token count.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.ai import generativelanguage_v1beta

            async def sample_count_text_tokens():
                # Create a client
                client = generativelanguage_v1beta.TextServiceAsyncClient()

                # Initialize request argument(s)
                prompt = generativelanguage_v1beta.TextPrompt()
                prompt.text = "text_value"

                request = generativelanguage_v1beta.CountTextTokensRequest(
                    model="model_value",
                    prompt=prompt,
                )

                # Make the request
                response = await client.count_text_tokens(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.ai.generativelanguage_v1beta.types.CountTextTokensRequest, dict]]):
                The request object. Counts the number of tokens in the ``prompt`` sent to a
                model.

                Models may tokenize text differently, so each model may
                return a different ``token_count``.
            model (:class:`str`):
                Required. The model's resource name. This serves as an
                ID for the Model to use.

                This name should match a model name returned by the
                ``ListModels`` method.

                Format: ``models/{model}``

                This corresponds to the ``model`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            prompt (:class:`google.ai.generativelanguage_v1beta.types.TextPrompt`):
                Required. The free-form input text
                given to the model as a prompt.

                This corresponds to the ``prompt`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.ai.generativelanguage_v1beta.types.CountTextTokensResponse:
                A response from CountTextTokens.

                   It returns the model's token_count for the prompt.

        """
        ...
    
    async def __aenter__(self) -> TextServiceAsyncClient:
        ...
    
    async def __aexit__(self, exc_type, exc, tb):
        ...
    


DEFAULT_CLIENT_INFO = ...
__all__ = ("TextServiceAsyncClient", )
