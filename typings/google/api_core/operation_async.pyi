"""
This type stub file was generated by pyright.
"""

from google.api_core.future import async_future

"""
This type stub file was generated by pyright.
"""
class AsyncOperation(async_future.AsyncFuture):
    """A Future for interacting with a Google API Long-Running Operation.

    Args:
        operation (google.longrunning.operations_pb2.Operation): The
            initial operation.
        refresh (Callable[[], ~.api_core.operation.Operation]): A callable that
            returns the latest state of the operation.
        cancel (Callable[[], None]): A callable that tries to cancel
            the operation.
        result_type (func:`type`): The protobuf type for the operation's
            result.
        metadata_type (func:`type`): The protobuf type for the operation's
            metadata.
        retry (google.api_core.retry.Retry): The retry configuration used
            when polling. This can be used to control how often :meth:`done`
            is polled. Regardless of the retry's ``deadline``, it will be
            overridden by the ``timeout`` argument to :meth:`result`.
    """
    def __init__(self, operation, refresh, cancel, result_type, metadata_type=..., retry=...) -> None:
        ...
    
    @property
    def operation(self):
        """google.longrunning.Operation: The current long-running operation."""
        ...
    
    @property
    def metadata(self):
        """google.protobuf.Message: the current operation metadata."""
        ...
    
    @classmethod
    def deserialize(cls, payload):
        """Deserialize a ``google.longrunning.Operation`` protocol buffer.

        Args:
            payload (bytes): A serialized operation protocol buffer.

        Returns:
            ~.operations_pb2.Operation: An Operation protobuf object.
        """
        ...
    
    async def done(self, retry=...):
        """Checks to see if the operation is complete.

        Args:
            retry (google.api_core.retry.Retry): (Optional) How to retry the RPC.

        Returns:
            bool: True if the operation is complete, False otherwise.
        """
        ...
    
    async def cancel(self):
        """Attempt to cancel the operation.

        Returns:
            bool: True if the cancel RPC was made, False if the operation is
                already complete.
        """
        ...
    
    async def cancelled(self):
        """True if the operation was cancelled."""
        ...
    


def from_gapic(operation, operations_client, result_type, grpc_metadata=..., **kwargs):
    """Create an operation future from a gapic client.

    This interacts with the long-running operations `service`_ (specific
    to a given API) via a gapic client.

    .. _service: https://github.com/googleapis/googleapis/blob/\
                 050400df0fdb16f63b63e9dee53819044bffc857/\
                 google/longrunning/operations.proto#L38

    Args:
        operation (google.longrunning.operations_pb2.Operation): The operation.
        operations_client (google.api_core.operations_v1.OperationsClient):
            The operations client.
        result_type (:func:`type`): The protobuf result type.
        grpc_metadata (Optional[List[Tuple[str, str]]]): Additional metadata to pass
            to the rpc.
        kwargs: Keyword args passed into the :class:`Operation` constructor.

    Returns:
        ~.api_core.operation.Operation: The operation future to track the given
            operation.
    """
    ...
