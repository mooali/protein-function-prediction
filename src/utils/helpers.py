"""
src.utils.helpers
------------------
Shared utility functions used across the pipeline:
configuration loading, reproducibility, logging setup, and path helpers.
"""

import random
from pathlib import Path

import numpy as np
import yaml


def load_config(path: str | Path) -> dict:
    """Load a YAML configuration file into a Python dictionary.

    Parameters
    ----------
    path : str or Path
        Path to the YAML config file.

    Returns
    -------
    dict

    TODO
    ----
    - Open path with yaml.safe_load
    - Validate required top-level keys (data, model, training)
    """
    with open(path, "r") as f:
        return yaml.safe_load(f)


def set_seed(seed: int) -> None:
    """Set random seeds for Python, NumPy, and PyTorch for reproducibility.

    TODO
    ----
    - random.seed(seed)
    - np.random.seed(seed)
    - torch.manual_seed(seed)
    - torch.cuda.manual_seed_all(seed) if cuda available
    """
    raise NotImplementedError


def get_device(prefer_gpu: bool = True) -> "torch.device":
    """Return the best available torch device.

    TODO
    ----
    - Return torch.device("cuda") if prefer_gpu and cuda available
    - Else return torch.device("cpu")
    """
    raise NotImplementedError


def ensure_dir(path: str | Path) -> Path:
    """Create a directory (and parents) if it does not yet exist.

    Returns the resolved Path object.
    """
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def get_project_root() -> Path:
    """Return the absolute path to the repository root.

    Relies on this file living at src/utils/helpers.py.
    """
    return Path(__file__).resolve().parents[2]
