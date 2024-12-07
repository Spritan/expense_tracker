"""
This type stub file was generated by pyright.
"""

from plotly import optional_imports
from ._imshow import imshow
from ._chart_types import area, bar, bar_polar, box, choropleth, choropleth_map, choropleth_mapbox, density_contour, density_heatmap, density_map, density_mapbox, ecdf, funnel, funnel_area, histogram, icicle, line, line_3d, line_geo, line_map, line_mapbox, line_polar, line_ternary, parallel_categories, parallel_coordinates, pie, scatter, scatter_3d, scatter_geo, scatter_map, scatter_mapbox, scatter_matrix, scatter_polar, scatter_ternary, strip, sunburst, timeline, treemap, violin
from ._core import NO_COLOR, defaults, get_trendline_results, set_mapbox_access_token
from ._special_inputs import Constant, IdentityMap, Range
from . import colors, data, trendline_functions

"""
`plotly.express` is a terse, consistent, high-level wrapper around `plotly.graph_objects`
for rapid data exploration and figure generation. Learn more at https://plotly.com/python/plotly-express/
"""
pd = ...
if pd is None:
    ...
__all__ = ["scatter", "scatter_3d", "scatter_polar", "scatter_ternary", "scatter_map", "scatter_mapbox", "scatter_geo", "scatter_matrix", "density_contour", "density_heatmap", "density_map", "density_mapbox", "line", "line_3d", "line_polar", "line_ternary", "line_map", "line_mapbox", "line_geo", "parallel_coordinates", "parallel_categories", "area", "bar", "timeline", "bar_polar", "violin", "box", "strip", "histogram", "ecdf", "choropleth", "choropleth_map", "choropleth_mapbox", "pie", "sunburst", "treemap", "icicle", "funnel", "funnel_area", "imshow", "data", "colors", "trendline_functions", "set_mapbox_access_token", "get_trendline_results", "IdentityMap", "Constant", "Range", "NO_COLOR"]