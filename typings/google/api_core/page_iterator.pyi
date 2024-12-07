"""
This type stub file was generated by pyright.
"""

import abc

"""Iterators for paging through paged API methods.

These iterators simplify the process of paging through API responses
where the request takes a page token and the response is a list of results with
a token for the next page. See `list pagination`_ in the Google API Style Guide
for more details.

.. _list pagination:
    https://cloud.google.com/apis/design/design_patterns#list_pagination

API clients that have methods that follow the list pagination pattern can
return an :class:`.Iterator`. You can use this iterator to get **all** of
the results across all pages::

    >>> results_iterator = client.list_resources()
    >>> list(results_iterator)  # Convert to a list (consumes all values).

Or you can walk your way through items and call off the search early if
you find what you're looking for (resulting in possibly fewer requests)::

    >>> for resource in results_iterator:
    ...     print(resource.name)
    ...     if not resource.is_valid:
    ...         break

At any point, you may check the number of items consumed by referencing the
``num_results`` property of the iterator::

    >>> for my_item in results_iterator:
    ...     if results_iterator.num_results >= 10:
    ...         break

When iterating, not every new item will send a request to the server.
To iterate based on each page of items (where a page corresponds to
a request)::

    >>> for page in results_iterator.pages:
    ...     print('=' * 20)
    ...     print('    Page number: {:d}'.format(iterator.page_number))
    ...     print('  Items in page: {:d}'.format(page.num_items))
    ...     print('     First item: {!r}'.format(next(page)))
    ...     print('Items remaining: {:d}'.format(page.remaining))
    ...     print('Next page token: {}'.format(iterator.next_page_token))
    ====================
        Page number: 1
      Items in page: 1
         First item: <MyItemClass at 0x7f1d3cccf690>
    Items remaining: 0
    Next page token: eav1OzQB0OM8rLdGXOEsyQWSG
    ====================
        Page number: 2
      Items in page: 19
         First item: <MyItemClass at 0x7f1d3cccffd0>
    Items remaining: 18
    Next page token: None

Then, for each page you can get all the resources on that page by iterating
through it or using :func:`list`::

    >>> list(page)
    [
        <MyItemClass at 0x7fd64a098ad0>,
        <MyItemClass at 0x7fd64a098ed0>,
        <MyItemClass at 0x7fd64a098e90>,
    ]
"""
class Page:
    """Single page of results in an iterator.

    Args:
        parent (google.api_core.page_iterator.Iterator): The iterator that owns
            the current page.
        items (Sequence[Any]): An iterable (that also defines __len__) of items
            from a raw API response.
        item_to_value (Callable[google.api_core.page_iterator.Iterator, Any]):
            Callable to convert an item from the type in the raw API response
            into the native object. Will be called with the iterator and a
            single item.
        raw_page Optional[google.protobuf.message.Message]:
            The raw page response.
    """
    def __init__(self, parent, items, item_to_value, raw_page=...) -> None:
        ...
    
    @property
    def raw_page(self): # -> None:
        """google.protobuf.message.Message"""
        ...
    
    @property
    def num_items(self): # -> int:
        """int: Total items in the page."""
        ...
    
    @property
    def remaining(self): # -> int:
        """int: Remaining items in the page."""
        ...
    
    def __iter__(self): # -> Self:
        """The :class:`Page` is an iterator of items."""
        ...
    
    def __next__(self):
        """Get the next value in the page."""
        ...
    


class Iterator(metaclass=abc.ABCMeta):
    """A generic class for iterating through API list responses.

    Args:
        client(google.cloud.client.Client): The API client.
        item_to_value (Callable[google.api_core.page_iterator.Iterator, Any]):
            Callable to convert an item from the type in the raw API response
            into the native object. Will be called with the iterator and a
            single item.
        page_token (str): A token identifying a page in a result set to start
            fetching results from.
        max_results (int): The maximum number of results to fetch.
    """
    def __init__(self, client, item_to_value=..., page_token=..., max_results=...) -> None:
        ...
    
    @property
    def pages(self): # -> Generator[Any, Any, None]:
        """Iterator of pages in the response.

        returns:
            types.GeneratorType[google.api_core.page_iterator.Page]: A
                generator of page instances.

        raises:
            ValueError: If the iterator has already been started.
        """
        ...
    
    def __iter__(self): # -> Generator[Any, Any, None]:
        """Iterator for each item returned.

        Returns:
            types.GeneratorType[Any]: A generator of items from the API.

        Raises:
            ValueError: If the iterator has already been started.
        """
        ...
    
    def __next__(self):
        ...
    


class HTTPIterator(Iterator):
    """A generic class for iterating through HTTP/JSON API list responses.

    To make an iterator work, you'll need to provide a way to convert a JSON
    item returned from the API into the object of your choice (via
    ``item_to_value``). You also may need to specify a custom ``items_key`` so
    that a given response (containing a page of results) can be parsed into an
    iterable page of the actual objects you want.

    Args:
        client (google.cloud.client.Client): The API client.
        api_request (Callable): The function to use to make API requests.
            Generally, this will be
            :meth:`google.cloud._http.JSONConnection.api_request`.
        path (str): The method path to query for the list of items.
        item_to_value (Callable[google.api_core.page_iterator.Iterator, Any]):
            Callable to convert an item from the type in the JSON response into
            a native object. Will be called with the iterator and a single
            item.
        items_key (str): The key in the API response where the list of items
            can be found.
        page_token (str): A token identifying a page in a result set to start
            fetching results from.
        page_size (int): The maximum number of results to fetch per page
        max_results (int): The maximum number of results to fetch
        extra_params (dict): Extra query string parameters for the
            API call.
        page_start (Callable[
            google.api_core.page_iterator.Iterator,
            google.api_core.page_iterator.Page, dict]): Callable to provide
            any special behavior after a new page has been created. Assumed
            signature takes the :class:`.Iterator` that started the page,
            the :class:`.Page` that was started and the dictionary containing
            the page response.
        next_token (str): The name of the field used in the response for page
            tokens.

    .. autoattribute:: pages
    """
    _DEFAULT_ITEMS_KEY = ...
    _PAGE_TOKEN = ...
    _MAX_RESULTS = ...
    _NEXT_TOKEN = ...
    _RESERVED_PARAMS = ...
    _HTTP_METHOD = ...
    def __init__(self, client, api_request, path, item_to_value, items_key=..., page_token=..., page_size=..., max_results=..., extra_params=..., page_start=..., next_token=...) -> None:
        ...
    


class _GAXIterator(Iterator):
    """A generic class for iterating through Cloud gRPC APIs list responses.

    Any:
        client (google.cloud.client.Client): The API client.
        page_iter (google.gax.PageIterator): A GAX page iterator to be wrapped
            to conform to the :class:`Iterator` interface.
        item_to_value (Callable[Iterator, Any]): Callable to convert an item
            from the protobuf response into a native object. Will
            be called with the iterator and a single item.
        max_results (int): The maximum number of results to fetch.

    .. autoattribute:: pages
    """
    def __init__(self, client, page_iter, item_to_value, max_results=...) -> None:
        ...
    


class GRPCIterator(Iterator):
    """A generic class for iterating through gRPC list responses.

    .. note:: The class does not take a ``page_token`` argument because it can
        just be specified in the ``request``.

    Args:
        client (google.cloud.client.Client): The API client. This unused by
            this class, but kept to satisfy the :class:`Iterator` interface.
        method (Callable[protobuf.Message]): A bound gRPC method that should
            take a single message for the request.
        request (protobuf.Message): The request message.
        items_field (str): The field in the response message that has the
            items for the page.
        item_to_value (Callable[GRPCIterator, Any]): Callable to convert an
            item from the type in the JSON response into a native object. Will
            be called with the iterator and a single item.
        request_token_field (str): The field in the request message used to
            specify the page token.
        response_token_field (str): The field in the response message that has
            the token for the next page.
        max_results (int): The maximum number of results to fetch.

    .. autoattribute:: pages
    """
    _DEFAULT_REQUEST_TOKEN_FIELD = ...
    _DEFAULT_RESPONSE_TOKEN_FIELD = ...
    def __init__(self, client, method, request, items_field, item_to_value=..., request_token_field=..., response_token_field=..., max_results=...) -> None:
        ...
    


