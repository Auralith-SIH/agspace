import numpy as np


def _as_float(a):
    return np.asarray(a, dtype=np.float32)


def _safe_div(num, den, eps=1e-6):
    den = _as_float(den)
    num = _as_float(num)
    return num / (den + eps)


def ndvi(nir, red):
    """
    NDVI = (NIR - RED) / (NIR + RED)
    """
    nir = _as_float(nir)
    red = _as_float(red)
    return _safe_div(nir - red, nir + red)


def ndwi(green, nir):
    """
    NDWI (McFeeters) = (GREEN - NIR) / (GREEN + NIR)
    """
    green = _as_float(green)
    nir = _as_float(nir)
    return _safe_div(green - nir, green + nir)


def ndbi(swir, nir):
    """
    NDBI = (SWIR - NIR) / (SWIR + NIR)
    """
    swir = _as_float(swir)
    nir = _as_float(nir)
    return _safe_div(swir - nir, swir + nir)


INDEX_FUNCS = {
    "ndvi": ndvi,
    "ndwi": ndwi,
    "ndbi": ndbi,
}