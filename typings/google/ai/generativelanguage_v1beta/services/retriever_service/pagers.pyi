"""
This type stub file was generated by pyright.
"""

from typing import Any, AsyncIterator, Awaitable, Callable, Iterator, Sequence, Tuple, Union
from google.ai.generativelanguage_v1beta.types import retriever, retriever_service

"""
This type stub file was generated by pyright.
"""
OptionalRetry = ...
OptionalAsyncRetry = ...
class ListCorporaPager:
    """A pager for iterating through ``list_corpora`` requests.

    This class thinly wraps an initial
    :class:`google.ai.generativelanguage_v1beta.types.ListCorporaResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``corpora`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCorpora`` requests and continue to iterate
    through the ``corpora`` field on the
    corresponding responses.

    All the usual :class:`google.ai.generativelanguage_v1beta.types.ListCorporaResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self, method: Callable[..., retriever_service.ListCorporaResponse], request: retriever_service.ListCorporaRequest, response: retriever_service.ListCorporaResponse, *, retry: OptionalRetry = ..., timeout: Union[float, object] = ..., metadata: Sequence[Tuple[str, str]] = ...) -> None:
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.ai.generativelanguage_v1beta.types.ListCorporaRequest):
                The initial request object.
            response (google.ai.generativelanguage_v1beta.types.ListCorporaResponse):
                The initial response object.
            retry (google.api_core.retry.Retry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        ...
    
    def __getattr__(self, name: str) -> Any:
        ...
    
    @property
    def pages(self) -> Iterator[retriever_service.ListCorporaResponse]:
        ...
    
    def __iter__(self) -> Iterator[retriever.Corpus]:
        ...
    
    def __repr__(self) -> str:
        ...
    


class ListCorporaAsyncPager:
    """A pager for iterating through ``list_corpora`` requests.

    This class thinly wraps an initial
    :class:`google.ai.generativelanguage_v1beta.types.ListCorporaResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``corpora`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCorpora`` requests and continue to iterate
    through the ``corpora`` field on the
    corresponding responses.

    All the usual :class:`google.ai.generativelanguage_v1beta.types.ListCorporaResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self, method: Callable[..., Awaitable[retriever_service.ListCorporaResponse]], request: retriever_service.ListCorporaRequest, response: retriever_service.ListCorporaResponse, *, retry: OptionalAsyncRetry = ..., timeout: Union[float, object] = ..., metadata: Sequence[Tuple[str, str]] = ...) -> None:
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.ai.generativelanguage_v1beta.types.ListCorporaRequest):
                The initial request object.
            response (google.ai.generativelanguage_v1beta.types.ListCorporaResponse):
                The initial response object.
            retry (google.api_core.retry.AsyncRetry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        ...
    
    def __getattr__(self, name: str) -> Any:
        ...
    
    @property
    async def pages(self) -> AsyncIterator[retriever_service.ListCorporaResponse]:
        ...
    
    def __aiter__(self) -> AsyncIterator[retriever.Corpus]:
        ...
    
    def __repr__(self) -> str:
        ...
    


class ListDocumentsPager:
    """A pager for iterating through ``list_documents`` requests.

    This class thinly wraps an initial
    :class:`google.ai.generativelanguage_v1beta.types.ListDocumentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``documents`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDocuments`` requests and continue to iterate
    through the ``documents`` field on the
    corresponding responses.

    All the usual :class:`google.ai.generativelanguage_v1beta.types.ListDocumentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self, method: Callable[..., retriever_service.ListDocumentsResponse], request: retriever_service.ListDocumentsRequest, response: retriever_service.ListDocumentsResponse, *, retry: OptionalRetry = ..., timeout: Union[float, object] = ..., metadata: Sequence[Tuple[str, str]] = ...) -> None:
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.ai.generativelanguage_v1beta.types.ListDocumentsRequest):
                The initial request object.
            response (google.ai.generativelanguage_v1beta.types.ListDocumentsResponse):
                The initial response object.
            retry (google.api_core.retry.Retry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        ...
    
    def __getattr__(self, name: str) -> Any:
        ...
    
    @property
    def pages(self) -> Iterator[retriever_service.ListDocumentsResponse]:
        ...
    
    def __iter__(self) -> Iterator[retriever.Document]:
        ...
    
    def __repr__(self) -> str:
        ...
    


class ListDocumentsAsyncPager:
    """A pager for iterating through ``list_documents`` requests.

    This class thinly wraps an initial
    :class:`google.ai.generativelanguage_v1beta.types.ListDocumentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``documents`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDocuments`` requests and continue to iterate
    through the ``documents`` field on the
    corresponding responses.

    All the usual :class:`google.ai.generativelanguage_v1beta.types.ListDocumentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self, method: Callable[..., Awaitable[retriever_service.ListDocumentsResponse]], request: retriever_service.ListDocumentsRequest, response: retriever_service.ListDocumentsResponse, *, retry: OptionalAsyncRetry = ..., timeout: Union[float, object] = ..., metadata: Sequence[Tuple[str, str]] = ...) -> None:
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.ai.generativelanguage_v1beta.types.ListDocumentsRequest):
                The initial request object.
            response (google.ai.generativelanguage_v1beta.types.ListDocumentsResponse):
                The initial response object.
            retry (google.api_core.retry.AsyncRetry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        ...
    
    def __getattr__(self, name: str) -> Any:
        ...
    
    @property
    async def pages(self) -> AsyncIterator[retriever_service.ListDocumentsResponse]:
        ...
    
    def __aiter__(self) -> AsyncIterator[retriever.Document]:
        ...
    
    def __repr__(self) -> str:
        ...
    


class ListChunksPager:
    """A pager for iterating through ``list_chunks`` requests.

    This class thinly wraps an initial
    :class:`google.ai.generativelanguage_v1beta.types.ListChunksResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``chunks`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListChunks`` requests and continue to iterate
    through the ``chunks`` field on the
    corresponding responses.

    All the usual :class:`google.ai.generativelanguage_v1beta.types.ListChunksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self, method: Callable[..., retriever_service.ListChunksResponse], request: retriever_service.ListChunksRequest, response: retriever_service.ListChunksResponse, *, retry: OptionalRetry = ..., timeout: Union[float, object] = ..., metadata: Sequence[Tuple[str, str]] = ...) -> None:
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.ai.generativelanguage_v1beta.types.ListChunksRequest):
                The initial request object.
            response (google.ai.generativelanguage_v1beta.types.ListChunksResponse):
                The initial response object.
            retry (google.api_core.retry.Retry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        ...
    
    def __getattr__(self, name: str) -> Any:
        ...
    
    @property
    def pages(self) -> Iterator[retriever_service.ListChunksResponse]:
        ...
    
    def __iter__(self) -> Iterator[retriever.Chunk]:
        ...
    
    def __repr__(self) -> str:
        ...
    


class ListChunksAsyncPager:
    """A pager for iterating through ``list_chunks`` requests.

    This class thinly wraps an initial
    :class:`google.ai.generativelanguage_v1beta.types.ListChunksResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``chunks`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListChunks`` requests and continue to iterate
    through the ``chunks`` field on the
    corresponding responses.

    All the usual :class:`google.ai.generativelanguage_v1beta.types.ListChunksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self, method: Callable[..., Awaitable[retriever_service.ListChunksResponse]], request: retriever_service.ListChunksRequest, response: retriever_service.ListChunksResponse, *, retry: OptionalAsyncRetry = ..., timeout: Union[float, object] = ..., metadata: Sequence[Tuple[str, str]] = ...) -> None:
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.ai.generativelanguage_v1beta.types.ListChunksRequest):
                The initial request object.
            response (google.ai.generativelanguage_v1beta.types.ListChunksResponse):
                The initial response object.
            retry (google.api_core.retry.AsyncRetry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        ...
    
    def __getattr__(self, name: str) -> Any:
        ...
    
    @property
    async def pages(self) -> AsyncIterator[retriever_service.ListChunksResponse]:
        ...
    
    def __aiter__(self) -> AsyncIterator[retriever.Chunk]:
        ...
    
    def __repr__(self) -> str:
        ...
    


