"""
This type stub file was generated by pyright.
"""

import abc
import argparse
from typing import Sequence
from google.generativeai.notebook import ipython_env

"""Customized ArgumentParser.

The default behvaior of argparse.ArgumentParser's parse_args() method  is to
exit with a SystemExit exception in the following cases:
1. When the user requests a help message (with the --help or -h flags), or
2. When there's a parsing error (e.g. missing required flags or mistyped flags)

To make the errors more user-friendly, this class customizes
argparse.ArgumentParser and raises either ParserNormalExit for (1) or
ParserError for (2); this way the caller has control over how to display them
to the user.
"""
class _ParserBaseException(RuntimeError, metaclass=abc.ABCMeta):
    """Base class for parser exceptions including normal exit."""
    def __init__(self, msgs: Sequence[str], *args, **kwargs) -> None:
        ...
    
    def set_ipython_env(self, env: ipython_env.IPythonEnv) -> None:
        ...
    
    def msgs(self) -> Sequence[str]:
        ...
    
    @abc.abstractmethod
    def display(self, env: ipython_env.IPythonEnv | None) -> None:
        """Display this exception on an IPython console."""
        ...
    


class ParserNormalExit(_ParserBaseException):
    """Exception thrown when the parser exits normally.

    This is usually thrown when the user requests the help message.
    """
    def display(self, env: ipython_env.IPythonEnv | None) -> None:
        ...
    


class ParserError(_ParserBaseException):
    """Exception thrown when there is an error."""
    def display(self, env: ipython_env.IPythonEnv | None) -> None:
        ...
    


class ArgumentParser(argparse.ArgumentParser):
    """Customized ArgumentParser for LLM Magics.

    This class overrides the parent argparse.ArgumentParser's error-handling
    methods to avoid side-effects like printing to stderr. The messages are
    accumulated and passed into the raised exceptions for the caller to
    handle them.
    """
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def exit(self, status=..., message=...):
        """Override ArgumentParser's exit() method."""
        ...
    


