"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Stream(_BaseTraceHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def maxpoints(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the maximum number of points to keep on the plots from an
        incoming stream. If `maxpoints` is set to 50, only the newest
        50 points will be displayed on the plot.

        The 'maxpoints' property is a number and may be specified as:
          - An int or float in the interval [0, 10000]

        Returns
        -------
        int|float
        """
        ...
    
    @maxpoints.setter
    def maxpoints(self, val): # -> None:
        ...
    
    @property
    def token(self): # -> tuple[Any, ...] | Self | None:
        """
        The stream id number links a data trace on a plot with a
        stream. See https://chart-studio.plotly.com/settings for more
        details.

        The 'token' property is a string and must be specified as:
          - A non-empty string

        Returns
        -------
        str
        """
        ...
    
    @token.setter
    def token(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., maxpoints=..., token=..., **kwargs) -> None:
        """
        Construct a new Stream object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.carpet.Stream`
        maxpoints
            Sets the maximum number of points to keep on the plots
            from an incoming stream. If `maxpoints` is set to 50,
            only the newest 50 points will be displayed on the
            plot.
        token
            The stream id number links a data trace on a plot with
            a stream. See https://chart-studio.plotly.com/settings
            for more details.

        Returns
        -------
        Stream
        """
        ...
    


