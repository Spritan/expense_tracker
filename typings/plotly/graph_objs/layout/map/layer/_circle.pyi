"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType

class Circle(_BaseLayoutHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def radius(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the circle radius (map.layer.paint.circle-radius). Has an
        effect only when `type` is set to "circle".

        The 'radius' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        ...
    
    @radius.setter
    def radius(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., radius=..., **kwargs) -> None:
        """
        Construct a new Circle object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.map.layer.Circle`
        radius
            Sets the circle radius (map.layer.paint.circle-radius).
            Has an effect only when `type` is set to "circle".

        Returns
        -------
        Circle
        """
        ...
    


