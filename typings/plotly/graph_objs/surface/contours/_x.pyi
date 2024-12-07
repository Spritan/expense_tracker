"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class X(_BaseTraceHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def color(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the color of the contour lines.

        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen

        Returns
        -------
        str
        """
        ...
    
    @color.setter
    def color(self, val): # -> None:
        ...
    
    @property
    def end(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the end contour level value. Must be more than
        `contours.start`

        The 'end' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        ...
    
    @end.setter
    def end(self, val): # -> None:
        ...
    
    @property
    def highlight(self): # -> tuple[Any, ...] | Self | None:
        """
        Determines whether or not contour lines about the x dimension
        are highlighted on hover.

        The 'highlight' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        ...
    
    @highlight.setter
    def highlight(self, val): # -> None:
        ...
    
    @property
    def highlightcolor(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the color of the highlighted contour lines.

        The 'highlightcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, rebeccapurple, saddlebrown, salmon,
                sandybrown, seagreen, seashell, sienna, silver,
                skyblue, slateblue, slategray, slategrey, snow,
                springgreen, steelblue, tan, teal, thistle, tomato,
                turquoise, violet, wheat, white, whitesmoke,
                yellow, yellowgreen

        Returns
        -------
        str
        """
        ...
    
    @highlightcolor.setter
    def highlightcolor(self, val): # -> None:
        ...
    
    @property
    def highlightwidth(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the width of the highlighted contour lines.

        The 'highlightwidth' property is a number and may be specified as:
          - An int or float in the interval [1, 16]

        Returns
        -------
        int|float
        """
        ...
    
    @highlightwidth.setter
    def highlightwidth(self, val): # -> None:
        ...
    
    @property
    def project(self): # -> tuple[Any, ...] | Self | None:
        """
        The 'project' property is an instance of Project
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.surface.contours.x.Project`
          - A dict of string/value properties that will be passed
            to the Project constructor

            Supported dict properties:

                x
                    Determines whether or not these contour lines
                    are projected on the x plane. If `highlight` is
                    set to True (the default), the projected lines
                    are shown on hover. If `show` is set to True,
                    the projected lines are shown in permanence.
                y
                    Determines whether or not these contour lines
                    are projected on the y plane. If `highlight` is
                    set to True (the default), the projected lines
                    are shown on hover. If `show` is set to True,
                    the projected lines are shown in permanence.
                z
                    Determines whether or not these contour lines
                    are projected on the z plane. If `highlight` is
                    set to True (the default), the projected lines
                    are shown on hover. If `show` is set to True,
                    the projected lines are shown in permanence.

        Returns
        -------
        plotly.graph_objs.surface.contours.x.Project
        """
        ...
    
    @project.setter
    def project(self, val): # -> None:
        ...
    
    @property
    def show(self): # -> tuple[Any, ...] | Self | None:
        """
        Determines whether or not contour lines about the x dimension
        are drawn.

        The 'show' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        ...
    
    @show.setter
    def show(self, val): # -> None:
        ...
    
    @property
    def size(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the step between each contour level. Must be positive.

        The 'size' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        ...
    
    @size.setter
    def size(self, val): # -> None:
        ...
    
    @property
    def start(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the starting contour level value. Must be less than
        `contours.end`

        The 'start' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        ...
    
    @start.setter
    def start(self, val): # -> None:
        ...
    
    @property
    def usecolormap(self): # -> tuple[Any, ...] | Self | None:
        """
        An alternate to "color". Determines whether or not the contour
        lines are colored using the trace "colorscale".

        The 'usecolormap' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        ...
    
    @usecolormap.setter
    def usecolormap(self, val): # -> None:
        ...
    
    @property
    def width(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the width of the contour lines.

        The 'width' property is a number and may be specified as:
          - An int or float in the interval [1, 16]

        Returns
        -------
        int|float
        """
        ...
    
    @width.setter
    def width(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., color=..., end=..., highlight=..., highlightcolor=..., highlightwidth=..., project=..., show=..., size=..., start=..., usecolormap=..., width=..., **kwargs) -> None:
        """
        Construct a new X object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.surface.contours.X`
        color
            Sets the color of the contour lines.
        end
            Sets the end contour level value. Must be more than
            `contours.start`
        highlight
            Determines whether or not contour lines about the x
            dimension are highlighted on hover.
        highlightcolor
            Sets the color of the highlighted contour lines.
        highlightwidth
            Sets the width of the highlighted contour lines.
        project
            :class:`plotly.graph_objects.surface.contours.x.Project
            ` instance or dict with compatible properties
        show
            Determines whether or not contour lines about the x
            dimension are drawn.
        size
            Sets the step between each contour level. Must be
            positive.
        start
            Sets the starting contour level value. Must be less
            than `contours.end`
        usecolormap
            An alternate to "color". Determines whether or not the
            contour lines are colored using the trace "colorscale".
        width
            Sets the width of the contour lines.

        Returns
        -------
        X
        """
        ...
    


