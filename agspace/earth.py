from pathlib import Path
import numpy as np

from .indices import INDEX_FUNCS
from .report import stats, threshold_coverage, save_json, save_csv
from .viz import save_index_png


def _load_geotiff(path):
    """
    Optional GeoTIFF loader. Requires rasterio.
    Returns: (bands, meta)
    bands: numpy array shape (count, height, width)
    """
    try:
        import rasterio
    except ImportError as e:
        raise ImportError(
            "GeoTIFF support requires rasterio. Install with: pip install rasterio"
        ) from e

    with rasterio.open(path) as src:
        bands = src.read()  # (count, h, w) 1-based bands
        meta = src.meta.copy()
    return bands, meta


def _get_band(bands, band_index_1based):
    """
    bands shape: (count, h, w)
    band_index_1based: 1..count
    """
    i = int(band_index_1based) - 1
    if i < 0 or i >= bands.shape[0]:
        raise ValueError(f"Band index {band_index_1based} out of range. Available: 1..{bands.shape[0]}")
    return bands[i]


def compute_index_from_bands(index_name, *, red=None, nir=None, green=None, swir=None):
    """
    Compute an index using numpy arrays directly.
    """
    idx = index_name.lower().strip()
    if idx not in INDEX_FUNCS:
        raise ValueError(f"Unknown index '{index_name}'. Choose from: {list(INDEX_FUNCS.keys())}")

    if idx == "ndvi":
        if nir is None or red is None:
            raise ValueError("NDVI needs nir and red arrays.")
        return INDEX_FUNCS[idx](nir, red)

    if idx == "ndwi":
        if green is None or nir is None:
            raise ValueError("NDWI needs green and nir arrays.")
        return INDEX_FUNCS[idx](green, nir)

    if idx == "ndbi":
        if swir is None or nir is None:
            raise ValueError("NDBI needs swir and nir arrays.")
        return INDEX_FUNCS[idx](swir, nir)

    # unreachable, but safe
    raise ValueError(f"Index '{index_name}' not wired correctly.")


def index_report(
    raster_path=None,
    *,
    index="ndvi",
    # band numbers are 1-based (GeoTIFF convention)
    red_band=None,
    nir_band=None,
    green_band=None,
    swir_band=None,
    # OR pass arrays directly:
    red=None,
    nir=None,
    green=None,
    swir=None,
    # outputs:
    out_dir="outputs",
    save_png=True,
    threshold=None,
):
    """
    Create a beginner-friendly report for an Earth index.

    Use either:
    - raster_path + band numbers (requires rasterio), OR
    - pass arrays directly (red/nir/green/swir)

    Returns: dict report
    """
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    meta = None

    if raster_path is not None:
        bands, meta = _load_geotiff(raster_path)

        # map requested band numbers to arrays if not provided
        if red is None and red_band is not None:
            red = _get_band(bands, red_band)
        if nir is None and nir_band is not None:
            nir = _get_band(bands, nir_band)
        if green is None and green_band is not None:
            green = _get_band(bands, green_band)
        if swir is None and swir_band is not None:
            swir = _get_band(bands, swir_band)

    # compute index
    idx_arr = compute_index_from_bands(index, red=red, nir=nir, green=green, swir=swir)

    # basic stats
    s = stats(idx_arr)

    # optional coverage threshold
    coverage = None
    if threshold is not None:
        coverage = threshold_coverage(idx_arr, float(threshold))

    report = {
        "tool": "agspace",
        "index": index.lower(),
        "stats": s,
        "threshold": threshold,
        "coverage_percent": coverage,
        "notes": {
            "geotiff_used": bool(raster_path),
            "meta_present": bool(meta),
        },
    }

    # save outputs
    save_json(report, out_dir / f"{index.lower()}_report.json")
    save_csv(
        {
            "index": report["index"],
            "count": report["stats"]["count"],
            "min": report["stats"]["min"],
            "max": report["stats"]["max"],
            "mean": report["stats"]["mean"],
            "std": report["stats"]["std"],
            "threshold": report["threshold"],
            "coverage_percent": report["coverage_percent"],
        },
        out_dir / f"{index.lower()}_report.csv",
    )

    if save_png:
        save_index_png(idx_arr, out_dir / f"{index.lower()}.png")

    return report