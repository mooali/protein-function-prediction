"""
src.data.loader
---------------
Handles loading of biological sequence datasets from common formats
(FASTA, CSV, TSV, HDF5) into in-memory data structures.
"""

from pathlib import Path
from typing import List, Tuple

# TODO: import BioPython SeqIO or pandas as needed


def load_fasta(path: str | Path) -> List[Tuple[str, str]]:
    """Load sequences from a FASTA file.

    Parameters
    ----------
    path : str or Path
        Path to the .fasta / .fa file.

    Returns
    -------
    list of (id, sequence) tuples
        Protein identifiers and their amino acid sequences.

    TODO
    ----
    - Parse records with Bio.SeqIO.parse(path, "fasta")
    - Return list of (record.id, str(record.seq)) tuples
    """
    raise NotImplementedError


def load_labels(path: str | Path) -> dict:
    """Load sequence-to-label mapping from a CSV/TSV file.

    Parameters
    ----------
    path : str or Path
        Path to a tabular file with columns [sequence_id, label].

    Returns
    -------
    dict
        Mapping from sequence_id to label string or integer.

    TODO
    ----
    - Read with pandas.read_csv
    - Build and return {id: label} dict
    """
    raise NotImplementedError


def load_dataset(sequences_path: str | Path, labels_path: str | Path):
    """Convenience wrapper that loads sequences and labels together.

    TODO
    ----
    - Call load_fasta and load_labels
    - Align on shared IDs
    - Return a pandas DataFrame with columns [id, sequence, label]
    """
    raise NotImplementedError
