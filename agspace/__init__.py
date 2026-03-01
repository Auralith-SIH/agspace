"""
agspace - Beginner-friendly Earth & space data toolkit.
Maintained by ARUSHIGULBHILE.

Core focus:
- Earth observation indices (NDVI/NDWI/NDBI) + reports
- NASA APOD helpers (extra utilities)
"""

from .nasa import get_apod, get_apod_safe, get_space_weather
from .astronomy import satellite_position

# Earth Index Toolkit (new)
from .earth import index_report, compute_index_from_bands
from .indices import ndvi, ndwi, ndbi

__version__ = "0.2.0"

__all__ = [
    # NASA / general utilities
    "get_apod",
    "get_apod_safe",
    "get_space_weather",
    "satellite_position",
    # Earth Index Toolkit
    "index_report",
    "compute_index_from_bands",
    "ndvi",
    "ndwi",
    "ndbi",
]