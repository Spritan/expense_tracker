"""
This type stub file was generated by pyright.
"""

from .basedatatypes import BaseFigure

class FigureWidget(BaseFigure):
    """
    FigureWidget stand-in for use when ipywidgets is not installed. The only purpose
    of this class is to provide something to import as
    `plotly.graph_objs.FigureWidget` when ipywidgets is not installed. This class
    simply raises an informative error message when the constructor is called
    """
    def __init__(self, *args, **kwargs) -> None:
        ...
    


