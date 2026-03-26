"""
src.data.preprocessing
-----------------------
Cleans and prepares raw biological sequences before feature extraction.
"""

import pandas as pd

# Standard 20 amino acids
STANDARD_AAS = set("ACDEFGHIKLMNPQRSTVWY")


def remove_invalid_sequences(df: pd.DataFrame, seq_col: str = "sequence") -> pd.DataFrame:
    """Drop sequences that contain non-standard amino acid characters.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame with a column of amino acid sequences.
    seq_col : str
        Name of the sequence column.

    Returns
    -------
    pd.DataFrame
        Filtered DataFrame.

    TODO
    ----
    - Filter rows where all characters in seq_col are in STANDARD_AAS
    - Log how many sequences were dropped
    """
    raise NotImplementedError


def truncate_sequences(df: pd.DataFrame, max_len: int, seq_col: str = "sequence") -> pd.DataFrame:
    """Truncate sequences to a maximum length.

    TODO
    ----
    - Slice each sequence to max_len characters
    - Optionally log a warning for sequences that were truncated
    """
    raise NotImplementedError


def encode_labels(df: pd.DataFrame, label_col: str = "label") -> tuple[pd.DataFrame, dict]:
    """Map string class labels to integer indices.

    Returns
    -------
    tuple of (updated DataFrame, label-to-index mapping dict)

    TODO
    ----
    - Build sorted unique label list
    - Create {label: idx} mapping
    - Add encoded column to DataFrame
    """
    raise NotImplementedError


def train_val_test_split(
    df: pd.DataFrame,
    val_size: float = 0.1,
    test_size: float = 0.1,
    random_state: int = 42,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Split DataFrame into train, validation, and test sets.

    TODO
    ----
    - Use sklearn.model_selection.train_test_split (stratified on label)
    - Return (train_df, val_df, test_df)
    """
    raise NotImplementedError
