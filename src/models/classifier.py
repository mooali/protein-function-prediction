"""
src.models.classifier
----------------------
Model architectures for biological sequence classification.

Includes both a simple baseline (MLP) and a 1-D CNN suitable for
direct sequence input.  Swap in a transformer encoder or fine-tuned
protein language model head as needed.
"""

import torch
import torch.nn as nn


class MLPClassifier(nn.Module):
    """Fully-connected baseline classifier operating on fixed-size feature vectors.

    Parameters
    ----------
    input_dim : int
        Dimensionality of the input feature vector.
    hidden_dim : int
        Width of the hidden layer.
    num_classes : int
        Number of output classes.
    dropout : float
        Dropout probability applied after each hidden activation.

    TODO
    ----
    - Add a configurable number of hidden layers
    - Add batch normalisation option
    """

    def __init__(
        self,
        input_dim: int,
        hidden_dim: int,
        num_classes: int,
        dropout: float = 0.3,
    ) -> None:
        super().__init__()
        # TODO: define self.network as nn.Sequential with Linear → ReLU → Dropout → Linear
        raise NotImplementedError

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # TODO: return self.network(x)
        raise NotImplementedError


class CNNClassifier(nn.Module):
    """1-D convolutional classifier for raw one-hot encoded sequences.

    Parameters
    ----------
    seq_len : int
        Fixed input sequence length (after padding/truncation).
    in_channels : int
        Number of input channels (20 for one-hot encoded amino acids).
    num_filters : int
        Number of convolutional filters per layer.
    kernel_size : int
        Convolution kernel size.
    num_classes : int
        Number of output classes.

    TODO
    ----
    - Stack multiple Conv1d → BatchNorm1d → ReLU blocks
    - Apply global average pooling before the classification head
    """

    def __init__(
        self,
        seq_len: int,
        in_channels: int = 20,
        num_filters: int = 64,
        kernel_size: int = 7,
        num_classes: int = 10,
    ) -> None:
        super().__init__()
        # TODO: build convolutional backbone and linear head
        raise NotImplementedError

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # TODO: pass through conv blocks, pool, classify
        raise NotImplementedError


def build_model(config: dict) -> nn.Module:
    """Instantiate a model from a configuration dictionary.

    Parameters
    ----------
    config : dict
        Must contain key 'model_type' ('mlp' or 'cnn') and
        the corresponding architecture hyperparameters.

    TODO
    ----
    - Dispatch on config['model_type']
    - Pass remaining keys as kwargs
    - Raise ValueError for unknown model types
    """
    raise NotImplementedError
