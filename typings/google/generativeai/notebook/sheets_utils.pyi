"""
This type stub file was generated by pyright.
"""

from google.generativeai.notebook import sheets_id
from google.generativeai.notebook.lib import llmfn_inputs_source, llmfn_outputs

"""SheetsInputs."""
def get_sheets_id_from_str(value: str) -> sheets_id.SheetsIdentifier:
    ...

class SheetsInputs(llmfn_inputs_source.LLMFnInputsSource):
    """Inputs to an LLMFunction from Google Sheets."""
    def __init__(self, sid: sheets_id.SheetsIdentifier, worksheet_id: int = ...) -> None:
        ...
    


class SheetsOutputs(llmfn_outputs.LLMFnOutputsSink):
    """Writes outputs from an LLMFunction to Google Sheets."""
    def __init__(self, sid: sheets_id.SheetsIdentifier) -> None:
        ...
    
    def write_outputs(self, outputs: llmfn_outputs.LLMFnOutputsBase) -> None:
        ...
    


