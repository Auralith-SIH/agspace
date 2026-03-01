import numpy as np
from pathlib import Path


def save_index_png(index_arr, out_path, vmin=-1.0, vmax=1.0):
    """
    Save a quicklook PNG of an index array using matplotlib (if available).
    """
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    a = np.asarray(index_arr, dtype=np.float32)
    a = np.clip(a, vmin, vmax)

    try:
        import matplotlib.pyplot as plt
    except ImportError as e:
        raise ImportError("matplotlib is required for save_index_png(). Install with: pip install matplotlib") from e

    plt.figure()
    plt.imshow(a, vmin=vmin, vmax=vmax)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(out_path, dpi=200, bbox_inches="tight", pad_inches=0)
    plt.close()