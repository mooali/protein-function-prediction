# Protein Function Prediction

A machine learning pipeline for biological sequence classification, focusing on predicting protein function from amino acid sequences.

## Project Structure

```
protein-function-prediction/
├── configs/            # YAML configuration files
├── data/               # Raw, processed, and split datasets (not tracked by git)
├── notebooks/          # Exploratory and analysis notebooks
├── artifacts/          # Saved models and evaluation results (not tracked by git)
├── app/                # Lightweight inference/serving interface
└── src/                # Core source code
    ├── data/           # Data loading and preprocessing
    ├── features/       # Feature extraction from sequences
    ├── models/         # Model architectures
    ├── training/       # Training loops and callbacks
    ├── evaluation/     # Metrics and evaluation utilities
    └── utils/          # Shared helpers
```

## Setup

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Train a model
python -m src.training.trainer --config configs/default.yaml

# Run inference
python app/predict.py --input data/raw/sequences.fasta
```

## Dataset

> TODO: Describe the dataset source (e.g., UniProt, PDB, Gene Ontology annotations).

## Model

> TODO: Describe the model architecture used (e.g., ESM embeddings + MLP, CNN, Transformer).

## Results

> TODO: Add benchmark results and evaluation metrics.

## License

See [LICENSE](LICENSE).
