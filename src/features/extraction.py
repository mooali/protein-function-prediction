"""
src.features.extraction
------------------------
Converts raw amino acid sequences into numerical feature representations
suitable for downstream ML models.

Supported strategies
--------------------
- One-hot encoding
- k-mer frequency vectors
- Physicochemical property profiles
- Pretrained protein language model embeddings (e.g., ESM-2)
"""

import numpy as np
from typing import List


def one_hot_encode(sequence: str, max_len: int) -> np.ndarray:
    """Encode a sequence as a 2-D one-hot matrix (max_len × 20).

    Parameters
    ----------
    sequence : str
        Amino acid sequence using single-letter codes.
    max_len : int
        Fixed length to pad / truncate to.

    Returns
    -------
    np.ndarray of shape (max_len, 20)

    TODO
    ----
    - Build amino acid → index mapping from STANDARD_AAS
    - Iterate characters, set the appropriate column to 1
    - Zero-pad shorter sequences; truncate longer ones
    """
    raise NotImplementedError


def kmer_frequencies(sequence: str, k: int = 3) -> dict:
    """Compute normalised k-mer frequency dictionary for a sequence.

    TODO
    ----
    - Slide a window of size k across sequence
    - Count occurrences, normalise by total k-mer count
    - Return {kmer: frequency} dict
    """
    raise NotImplementedError


def physicochemical_profile(sequence: str) -> np.ndarray:
    """Return a feature vector of global physicochemical properties.

    Properties to include (TODO):
    - Molecular weight
    - Isoelectric point
    - GRAVY hydrophobicity score
    - Amino acid composition fractions

    TODO
    ----
    - Use Bio.SeqUtils.ProtParam.ProteinAnalysis
    - Return numpy array of scalar features
    """
    raise NotImplementedError


def get_esm_embeddings(sequences: List[str], model_name: str = "esm2_t6_8M_UR50D") -> np.ndarray:
    """Extract per-sequence mean embeddings from a pretrained ESM-2 model.

    Parameters
    ----------
    sequences : list of str
    model_name : str
        Identifier for the ESM model variant to load.

    Returns
    -------
    np.ndarray of shape (len(sequences), embedding_dim)

    TODO
    ----
    - Load model and alphabet with esm.pretrained.<model_name>()
    - Batch sequences through the model
    - Average over token dimension to get per-sequence vectors
    """
    raise NotImplementedError
