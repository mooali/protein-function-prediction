from setuptools import setup, find_packages

setup(
    name="protein-function-prediction",
    version="0.1.0",
    description="Machine learning pipeline for biological sequence classification",
    author="TODO: Your Name",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
    install_requires=[
        "numpy>=1.24",
        "pandas>=2.0",
        "scikit-learn>=1.3",
        "torch>=2.0",
        "biopython>=1.81",
        "pyyaml>=6.0",
        "tqdm>=4.65",
        "loguru>=0.7",
    ],
)
