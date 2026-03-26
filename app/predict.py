"""
app/predict.py
--------------
Lightweight inference script. Loads a trained model checkpoint and
runs predictions on a provided FASTA file.

Usage
-----
    python app/predict.py --input data/raw/sequences.fasta \\
                          --checkpoint artifacts/models/best.pt \\
                          --config configs/default.yaml \\
                          --output predictions.csv
"""

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run protein function predictions.")
    parser.add_argument("--input",      type=Path, required=True,  help="Path to input FASTA file.")
    parser.add_argument("--checkpoint", type=Path, required=True,  help="Path to model checkpoint (.pt).")
    parser.add_argument("--config",     type=Path, default=Path("configs/default.yaml"))
    parser.add_argument("--output",     type=Path, default=Path("predictions.csv"))
    return parser.parse_args()


def load_model(checkpoint_path: Path, config: dict):
    """Load model architecture and weights from a checkpoint.

    TODO
    ----
    - Call src.models.classifier.build_model(config)
    - Load state dict with torch.load and model.load_state_dict
    - Set model to eval mode and move to device
    """
    raise NotImplementedError


def predict(sequences, model, config: dict):
    """Run inference on a list of sequences.

    Returns
    -------
    list of (sequence_id, predicted_label, confidence_score)

    TODO
    ----
    - Extract features matching the strategy used during training
    - Batch and forward through model
    - Apply softmax, pick argmax label, map back to label name
    """
    raise NotImplementedError


def save_predictions(predictions, output_path: Path) -> None:
    """Write predictions to a CSV file.

    TODO
    ----
    - Build pandas DataFrame from predictions list
    - Save with df.to_csv(output_path, index=False)
    """
    raise NotImplementedError


if __name__ == "__main__":
    from src.utils.helpers import load_config
    from src.data.loader import load_fasta

    args = parse_args()
    cfg = load_config(args.config)

    sequences = load_fasta(args.input)
    model = load_model(args.checkpoint, cfg)
    predictions = predict(sequences, model, cfg)
    save_predictions(predictions, args.output)

    print(f"Predictions saved to {args.output}")
