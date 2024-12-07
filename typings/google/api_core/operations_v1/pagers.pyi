"""
This type stub file was generated by pyright.
"""

from typing import Callable, Iterator, Sequence, Tuple
from google.longrunning import operations_pb2
from google.api_core.operations_v1.pagers_base import ListOperationsPagerBase

class ListOperationsPager(ListOperationsPagerBase):
    """A pager for iterating through ``list_operations`` requests.

    This class thinly wraps an initial
    :class:`google.longrunning.operations_pb2.ListOperationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``operations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListOperations`` requests and continue to iterate
    through the ``operations`` field on the
    corresponding responses.

    All the usual :class:`google.longrunning.operations_pb2.ListOperationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self, method: Callable[..., operations_pb2.ListOperationsResponse], request: operations_pb2.ListOperationsRequest, response: operations_pb2.ListOperationsResponse, *, metadata: Sequence[Tuple[str, str]] = ...) -> None:
        ...
    
    @property
    def pages(self) -> Iterator[operations_pb2.ListOperationsResponse]:
        ...
    
    def __iter__(self) -> Iterator[operations_pb2.Operation]:
        ...
    


