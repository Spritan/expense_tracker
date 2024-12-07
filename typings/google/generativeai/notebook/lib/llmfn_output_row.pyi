"""
This type stub file was generated by pyright.
"""

import abc
from typing import Any, Iterator, Mapping

"""LLMFnOutputRow."""
_CELLVALUETYPE = Any
class LLMFnOutputRowView(Mapping[str, _CELLVALUETYPE], metaclass=abc.ABCMeta):
    """Immutable view of LLMFnOutputRow."""
    @abc.abstractmethod
    def __contains__(self, k: str) -> bool:
        """For expressions like: x in this_instance."""
        ...
    
    @abc.abstractmethod
    def __str__(self) -> str:
        """For expressions like: str(this_instance)."""
        ...
    
    @abc.abstractmethod
    def result_type(self) -> type[Any]:
        """Returns the type enforced for the result cell."""
        ...
    
    @abc.abstractmethod
    def result_value(self) -> Any:
        """Get the value of the result cell."""
        ...
    
    @abc.abstractmethod
    def result_key(self) -> str:
        """Get the key of the result cell."""
        ...
    


class LLMFnOutputRow(LLMFnOutputRowView):
    """Container that represents a single row in a table of outputs.

    We represent outputs as a table. This class represents a single row in the
    table like a dictionary, where the key is the column name and the value is the
    cell value.

    A single cell is designated the "result". This contains the output of the LLM
    model after running any post-processing functions specified by the user.

    In addition to behaving like a dictionary, this class provides additional
    methods, including:
    - Getting the value of the "result" cell
    - Setting the value (and optionally the key) of the "result" cell.
    - Add a new non-result cell

    Notes: As an implementation detail, the result-cell is always kept as the
    rightmost cell.
    """
    def __init__(self, data: Mapping[str, _CELLVALUETYPE], result_type: type[Any]) -> None:
        """Constructor.

        Args:
          data: The initial value of the row. The last entry will be treated as the
            result. Cannot be empty. The value of the last entry must be `str`.
          result_type: The type of the result cell. This will be enforced at
            runtime.
        """
        ...
    
    def __iter__(self) -> Iterator[str]:
        ...
    
    def __len__(self) -> int:
        ...
    
    def __getitem__(self, k: str) -> _CELLVALUETYPE:
        ...
    
    def __contains__(self, k: str) -> bool:
        ...
    
    def __str__(self) -> str:
        ...
    
    def result_type(self) -> type[Any]:
        ...
    
    def result_value(self) -> Any:
        ...
    
    def result_key(self) -> str:
        ...
    
    def set_result_value(self, value: Any, key: str | None = ...) -> None:
        """Set the value of the result cell.

        Sets the value (and optionally the key) of the result cell.

        Args:
          value: The value to set the result cell today.
          key: Optionally change the key as well.
        """
        ...
    
    def add(self, key: str, value: _CELLVALUETYPE) -> None:
        """Add a non-result cell.

        Adds a new non-result cell. This does not affect the result cell.

        Args:
          key: The key of the new cell to add.
          value: The value of the new cell to add.
        """
        ...
    

