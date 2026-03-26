"""
src.training.trainer
---------------------
Main training entry point. Loads config, builds data loaders, instantiates
the model, and runs the training / validation loop.

Usage
-----
    python -m src.training.trainer --config configs/default.yaml
"""

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Train a protein function classifier.")
    parser.add_argument("--config", type=Path, default="configs/default.yaml")
    # TODO: add --resume, --device, --seed overrides
    return parser.parse_args()


def build_dataloaders(config: dict):
    """Construct PyTorch DataLoader objects for train / val / test splits.

    TODO
    ----
    - Call src.data.loader.load_dataset
    - Apply src.data.preprocessing pipeline
    - Extract features with src.features.extraction
    - Wrap in torch.utils.data.TensorDataset and DataLoader
    - Return (train_loader, val_loader, test_loader)
    """
    raise NotImplementedError


def train_one_epoch(model, loader, optimizer, criterion, device):
    """Run a single training epoch.

    TODO
    ----
    - Set model to train mode
    - Iterate batches: forward → loss → backward → optimizer step
    - Accumulate and return average loss and accuracy
    """
    raise NotImplementedError


def evaluate(model, loader, criterion, device):
    """Evaluate the model on a data loader without gradient updates.

    TODO
    ----
    - Set model to eval mode
    - Collect predictions and targets
    - Return average loss and accuracy
    """
    raise NotImplementedError


def train(config: dict) -> None:
    """Full training pipeline driven by a config dictionary.

    TODO
    ----
    - Set random seeds for reproducibility
    - Call build_dataloaders
    - Call src.models.classifier.build_model
    - Instantiate optimizer (Adam) and criterion (CrossEntropyLoss)
    - Loop for config['training']['epochs']:
        - train_one_epoch → log train metrics
        - evaluate on val set → log val metrics
        - checkpoint best model to artifacts/models/
    - Final evaluation on test set
    - Save results to artifacts/results/
    """
    raise NotImplementedError


if __name__ == "__main__":
    from src.utils.helpers import load_config

    args = parse_args()
    cfg = load_config(args.config)
    train(cfg)
