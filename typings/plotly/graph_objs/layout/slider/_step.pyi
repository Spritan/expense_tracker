"""
This type stub file was generated by pyright.
"""

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType

class Step(_BaseLayoutHierarchyType):
    _parent_path_str = ...
    _path_str = ...
    _valid_props = ...
    @property
    def args(self): # -> tuple[Any, ...] | Self | None:
        """
            Sets the arguments values to be passed to the Plotly method set
            in `method` on slide.

            The 'args' property is an info array that may be specified as:

            * a list or tuple of up to 3 elements where:
        (0) The 'args[0]' property accepts values of any type
        (1) The 'args[1]' property accepts values of any type
        (2) The 'args[2]' property accepts values of any type

            Returns
            -------
            list
        """
        ...
    
    @args.setter
    def args(self, val): # -> None:
        ...
    
    @property
    def execute(self): # -> tuple[Any, ...] | Self | None:
        """
        When true, the API method is executed. When false, all other
        behaviors are the same and command execution is skipped. This
        may be useful when hooking into, for example, the
        `plotly_sliderchange` method and executing the API command
        manually without losing the benefit of the slider automatically
        binding to the state of the plot through the specification of
        `method` and `args`.

        The 'execute' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        ...
    
    @execute.setter
    def execute(self, val): # -> None:
        ...
    
    @property
    def label(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the text label to appear on the slider

        The 'label' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        ...
    
    @label.setter
    def label(self, val): # -> None:
        ...
    
    @property
    def method(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the Plotly method to be called when the slider value is
        changed. If the `skip` method is used, the API slider will
        function as normal but will perform no API calls and will not
        bind automatically to state updates. This may be used to create
        a component interface and attach to slider events manually via
        JavaScript.

        The 'method' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['restyle', 'relayout', 'animate', 'update', 'skip']

        Returns
        -------
        Any
        """
        ...
    
    @method.setter
    def method(self, val): # -> None:
        ...
    
    @property
    def name(self): # -> tuple[Any, ...] | Self | None:
        """
        When used in a template, named items are created in the output
        figure in addition to any items the figure already has in this
        array. You can modify these items in the output figure by
        making your own item with `templateitemname` matching this
        `name` alongside your modifications (including `visible: false`
        or `enabled: false` to hide it). Has no effect outside of a
        template.

        The 'name' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        ...
    
    @name.setter
    def name(self, val): # -> None:
        ...
    
    @property
    def templateitemname(self): # -> tuple[Any, ...] | Self | None:
        """
        Used to refer to a named item in this array in the template.
        Named items from the template will be created even without a
        matching item in the input figure, but you can modify one by
        making an item with `templateitemname` matching its `name`,
        alongside your modifications (including `visible: false` or
        `enabled: false` to hide it). If there is no template or no
        matching item, this item will be hidden unless you explicitly
        show it with `visible: true`.

        The 'templateitemname' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        ...
    
    @templateitemname.setter
    def templateitemname(self, val): # -> None:
        ...
    
    @property
    def value(self): # -> tuple[Any, ...] | Self | None:
        """
        Sets the value of the slider step, used to refer to the step
        programatically. Defaults to the slider label if not provided.

        The 'value' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        ...
    
    @value.setter
    def value(self, val): # -> None:
        ...
    
    @property
    def visible(self): # -> tuple[Any, ...] | Self | None:
        """
        Determines whether or not this step is included in the slider.

        The 'visible' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        ...
    
    @visible.setter
    def visible(self, val): # -> None:
        ...
    
    def __init__(self, arg=..., args=..., execute=..., label=..., method=..., name=..., templateitemname=..., value=..., visible=..., **kwargs) -> None:
        """
        Construct a new Step object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.slider.Step`
        args
            Sets the arguments values to be passed to the Plotly
            method set in `method` on slide.
        execute
            When true, the API method is executed. When false, all
            other behaviors are the same and command execution is
            skipped. This may be useful when hooking into, for
            example, the `plotly_sliderchange` method and executing
            the API command manually without losing the benefit of
            the slider automatically binding to the state of the
            plot through the specification of `method` and `args`.
        label
            Sets the text label to appear on the slider
        method
            Sets the Plotly method to be called when the slider
            value is changed. If the `skip` method is used, the API
            slider will function as normal but will perform no API
            calls and will not bind automatically to state updates.
            This may be used to create a component interface and
            attach to slider events manually via JavaScript.
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        value
            Sets the value of the slider step, used to refer to the
            step programatically. Defaults to the slider label if
            not provided.
        visible
            Determines whether or not this step is included in the
            slider.

        Returns
        -------
        Step
        """
        ...
    


