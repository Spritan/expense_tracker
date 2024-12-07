"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType

class Textfont(_BaseTraceHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def color(self): # -> tuple[Any, ...] | Self | None:
        """
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
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        ...
    
    @color.setter
    def color(self, val): # -> None:
        ...
    
    @property
    def colorsrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for `color`.

        The 'colorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @colorsrc.setter
    def colorsrc(self, val): # -> None:
        ...
    
    @property
    def family(self): # -> tuple[Any, ...] | Self | None:
        """
        HTML font family - the typeface that will be applied by the web
        browser. The web browser will only be able to apply a font if
        it is available on the system which it operates. Provide
        multiple font families, separated by commas, to indicate the
        preference in which to apply fonts if they aren't available on
        the system. The Chart Studio Cloud (at https://chart-
        studio.plotly.com or on-premise) generates images on a server,
        where only a select number of fonts are installed and
        supported. These include "Arial", "Balto", "Courier New",
        "Droid Sans", "Droid Serif", "Droid Sans Mono", "Gravitas One",
        "Old Standard TT", "Open Sans", "Overpass", "PT Sans Narrow",
        "Raleway", "Times New Roman".

        The 'family' property is a string and must be specified as:
          - A non-empty string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        ...
    
    @family.setter
    def family(self, val): # -> None:
        ...
    
    @property
    def familysrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for `family`.

        The 'familysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @familysrc.setter
    def familysrc(self, val): # -> None:
        ...
    
    @property
    def size(self): # -> tuple[Any, ...] | Self | None:
        """
        The 'size' property is a number and may be specified as:
          - An int or float in the interval [1, inf]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        ...
    
    @size.setter
    def size(self, val): # -> None:
        ...
    
    @property
    def sizesrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for `size`.

        The 'sizesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @sizesrc.setter
    def sizesrc(self, val): # -> None:
        ...
    
    @property
    def style(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets whether a font should be styled with a normal or italic
        face from its family.

        The 'style' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['normal', 'italic']
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        ...
    
    @style.setter
    def style(self, val): # -> None:
        ...
    
    @property
    def stylesrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for `style`.

        The 'stylesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @stylesrc.setter
    def stylesrc(self, val): # -> None:
        ...
    
    @property
    def variant(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the variant of the font.

        The 'variant' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['normal', 'small-caps']
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        ...
    
    @variant.setter
    def variant(self, val): # -> None:
        ...
    
    @property
    def variantsrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for `variant`.

        The 'variantsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @variantsrc.setter
    def variantsrc(self, val): # -> None:
        ...
    
    @property
    def weight(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the weight (or boldness) of the font.

        The 'weight' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['normal', 'bold']
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        ...
    
    @weight.setter
    def weight(self, val): # -> None:
        ...
    
    @property
    def weightsrc(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the source reference on Chart Studio Cloud for `weight`.

        The 'weightsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        ...
    
    @weightsrc.setter
    def weightsrc(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., color=..., colorsrc=..., family=..., familysrc=..., size=..., sizesrc=..., style=..., stylesrc=..., variant=..., variantsrc=..., weight=..., weightsrc=..., **kwargs) -> None:
        """
        Construct a new Textfont object

        Sets the text font.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.scatterpolargl.Textfont`
        color

        colorsrc
            Sets the source reference on Chart Studio Cloud for
            `color`.
        family
            HTML font family - the typeface that will be applied by
            the web browser. The web browser will only be able to
            apply a font if it is available on the system which it
            operates. Provide multiple font families, separated by
            commas, to indicate the preference in which to apply
            fonts if they aren't available on the system. The Chart
            Studio Cloud (at https://chart-studio.plotly.com or on-
            premise) generates images on a server, where only a
            select number of fonts are installed and supported.
            These include "Arial", "Balto", "Courier New", "Droid
            Sans", "Droid Serif", "Droid Sans Mono", "Gravitas
            One", "Old Standard TT", "Open Sans", "Overpass", "PT
            Sans Narrow", "Raleway", "Times New Roman".
        familysrc
            Sets the source reference on Chart Studio Cloud for
            `family`.
        size

        sizesrc
            Sets the source reference on Chart Studio Cloud for
            `size`.
        style
            Sets whether a font should be styled with a normal or
            italic face from its family.
        stylesrc
            Sets the source reference on Chart Studio Cloud for
            `style`.
        variant
            Sets the variant of the font.
        variantsrc
            Sets the source reference on Chart Studio Cloud for
            `variant`.
        weight
            Sets the weight (or boldness) of the font.
        weightsrc
            Sets the source reference on Chart Studio Cloud for
            `weight`.

        Returns
        -------
        Textfont
        """
        ...
    


