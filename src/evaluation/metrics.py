"""
src.evaluation.metrics
-----------------------
Evaluation metrics suited for multi-class protein function prediction.
Supports both sklearn-compatible arrays and PyTorch tensors.
"""

import numpy as np
from typing import List


def compute_classification_report(y_true, y_pred, label_names: List[str] | None = None) -> dict:
    """Compute per-class precision, recall, F1, and macro / weighted averages.

    TODO
    ----
    - Use sklearn.metrics.classification_report(output_dict=True)
    - Return the resulting dict
    """
    raise NotImplementedError


def compute_confusion_matrix(y_true, y_pred) -> np.ndarray:
    """Return the confusion matrix as a numpy array.

    TODO
    ----
    - Use sklearn.metrics.confusion_matrix
    """
    raise NotImplementedError


def compute_top_k_accuracy(y_true, y_proba, k: int = 5) -> float:
    """Compute top-k accuracy for multi-class predictions.

    Parameters
    ----------
    y_proba : array-like of shape (n_samples, n_classes)
        Class probability scores.
    k : int
        Number of top predictions to consider.

    TODO
    ----
    - Use sklearn.metrics.top_k_accuracy_score
    """
    raise NotImplementedError


def save_metrics(metrics: dict, path: str) -> None:
    """Persist a metrics dictionary to a JSON file.

    TODO
    ----
    - Serialise with json.dump (indent=2)
    - Create parent directories if they don't exist
    """
    raise NotImplementedError


def plot_confusion_matrix(cm: np.ndarray, label_names: List[str], output_path: str) -> None:
    """Render and save a confusion matrix heatmap.

    TODO
    ----
    - Use seaborn.heatmap with annot=True
    - Save figure to output_path with matplotlib.pyplot.savefig
    """
    raise NotImplementedError
