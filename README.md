# ESMFold Protein Structure Predictor

[![ESMFold Protein Structure Predictor](https://github.com/user-attachments/assets/a185fe09-338b-4cb1-90f3-b8055a2856c4)](https://esmfold-protein-structure-predictor.streamlit.app/)

## Overview
The ESMFold Protein Structure Predictor is a web application that uses the ESM-2 language model to predict the 3D structure of proteins based on their amino acid sequences. This tool allows users to input protein sequences in text format or upload a FASTA file and visualize the predicted protein structure in 3D. It also provides pLDDT scores, which are confidence measures for the predicted structure.

## Features
- **Protein Sequence Input**: Accepts protein sequences via text input or FASTA file upload.
- **Structure Prediction**: Predicts protein structures using the ESMFold API.
- **3D Visualization**: Visualizes the predicted protein structure using Py3Dmol.
- **pLDDT Scores**: Extracts and displays pLDDT scores, indicating the confidence of the predicted structure.
- **Download Option**: Allows users to download the predicted PDB file.

## Requirements
- Python 3.7 or higher
- Streamlit
- Requests
- Urllib3
- Py3Dmol

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/esmfold-predictor.git
    cd esmfold-predictor
    ```
2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the Streamlit application:
    ```bash
    streamlit run esm.py
    ```
2. Open your web browser and navigate to `http://localhost:8501`.
