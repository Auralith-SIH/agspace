import json
import csv
import numpy as np
from pathlib import Path


def stats(arr, mask=None):
    """
    Compute basic stats for a 2D/3D numpy array. Works best for 2D indices.
    If mask is provided, mask=True means "keep".
    """
    a = np.asarray(arr, dtype=np.float32)

    if mask is not None:
        m = np.asarray(mask, dtype=bool)
        a = a[m]

    # remove NaNs/Infs
    a = a[np.isfinite(a)]

    if a.size == 0:
        return {
            "count": 0,
            "min": None,
            "max": None,
            "mean": None,
            "std": None,
        }

    return {
        "count": int(a.size),
        "min": float(np.min(a)),
        "max": float(np.max(a)),
        "mean": float(np.mean(a)),
        "std": float(np.std(a)),
    }


def threshold_coverage(arr, threshold, mask=None):
    """
    Percent of pixels >= threshold (useful for vegetation/water coverage).
    """
    a = np.asarray(arr, dtype=np.float32)
    if mask is not None:
        m = np.asarray(mask, dtype=bool)
        a = a[m]
    a = a[np.isfinite(a)]
    if a.size == 0:
        return 0.0
    return float((a >= threshold).mean() * 100.0)


def save_json(data, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def save_csv(flat_dict, path):
    """
    Saves a single-row CSV from a dict.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(flat_dict.keys()))
        writer.writeheader()
        writer.writerow(flat_dict)