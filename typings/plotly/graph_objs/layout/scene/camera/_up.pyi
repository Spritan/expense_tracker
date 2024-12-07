"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType

class Up(_BaseLayoutHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def x(self): # -> tuple[Any, ...] | Self | None:
        """
        The 'x' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        ...
    
    @x.setter
    def x(self, val): # -> None:
        ...
    
    @property
    def y(self): # -> tuple[Any, ...] | Self | None:
        """
        The 'y' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        ...
    
    @y.setter
    def y(self, val): # -> None:
        ...
    
    @property
    def z(self): # -> tuple[Any, ...] | Self | None:
        """
        The 'z' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        ...
    
    @z.setter
    def z(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., x=..., y=..., z=..., **kwargs) -> None:
        """
        Construct a new Up object

        Sets the (x,y,z) components of the 'up' camera vector. This
        vector determines the up direction of this scene with respect
        to the page. The default is *{x: 0, y: 0, z: 1}* which means
        that the z axis points up.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.scene.camera.Up`
        x

        y

        z


        Returns
        -------
        Up
        """
        ...
    

