# Multi-Omics Data Integration for Breast Cancer Survival Prediction

This repository contains a machine learning (ML) pipeline for the integration of large-scale omics data to predict survival outcomes in breast cancer patients. The pipeline utilizes multi-omics data, including gene expression, miRNA expression, DNA methylation, and copy number variation, from 302 female patients available in The Cancer Genome Atlas (TCGA) dataset.

## Table of Contents

- [Usage](#Usage)
- [Repository Structure](#Repository-Structure)
- [Background](#Background)
- [Objective](#Objective)
- [Model Architecture](#Model-Architecture)

## Usage
### for Linux 
To use the ML model and run the Flask application locally, follow these steps:

1. Download and unpack the zip file/ Clone the GitHub library.
2. Change the working directory to the downloaded repository.
3. Create and Activate a new python environment using terminal.
   * `pip install virtualenv`
   * `virtualenv ConnectOME`
   * `virtualenv -p /usr/bin/python3 virtualenv_name`
   * `source virtualenv_name/bin/activate`
4. Run command.
    * `pip install -r requirements.txt`
    * `export FLASK_APP="ConnectOME.py"`
    * `flask run`
5. Open the provided link in your preferred web browser.

## Repository Structure

This GitHub repository contains the following files and directories:

1. ConnetOME.py: The Flask application file to run the ML model.
1. models/: Directory containing the model pickle files.
1. example/: Directory containing sample example files for testing the application.


## Background
Integration of diverse omics data is crucial for extracting biologically relevant information and gaining a better understanding of the complex biological processes associated with different disease phenotypes. Machine learning approaches have shown great potential for systematic multi-omics data integration.

## Objective
The main objective of this study is to predict the survival outcomes of breast cancer patients by leveraging multi-omics data. By developing a computational ML pipeline using Support Vector Machine (SVM) and Partial Least Squares (PLS) algorithms, we aim to overcome the limitations of univariate feature selection criteria. The pipeline incorporates latent variables obtained through multivariate dimension reduction methods, allowing us to investigate background genetic networks and identify potential hub genes.

## Model Architecture
![Alt text](https://github.com/Kunaltembhare003/ConnectOME/blob/main/image/Model_Architecture.jpg)



## Results
The analysis of the results obtained revealed that the SVM with PLS-DA method, integrated with gene expression, DNA methylation, and miRNA expression modalities, outperformed other models. It achieved an area under the curve (AUC) of 89% and an accuracy of 82% for survival prediction. Additionally, this study validated previously reported breast cancer-specific prognostic biomarkers while also predicting new biomarkers.


