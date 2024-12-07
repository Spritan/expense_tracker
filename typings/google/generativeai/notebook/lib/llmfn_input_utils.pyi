"""
This type stub file was generated by pyright.
"""

from typing import Mapping, Sequence, Union
from google.generativeai.notebook.lib import llmfn_inputs_source

"""Utilities for handling input variables."""
_NormalizedInputsList = llmfn_inputs_source.NormalizedInputsList
_ColumnOrderValuesList = Mapping[str, Sequence[str]]
LLMFunctionInputs = Union[_ColumnOrderValuesList, llmfn_inputs_source.LLMFnInputsSource]
def to_normalized_inputs(inputs: LLMFunctionInputs) -> _NormalizedInputsList:
    """Handles the different types of `inputs` and returns a normalized form."""
    ...

