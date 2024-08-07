# Credit Card Fraud Prediction

## Introduction
Credit card fraud prediction is a very important area of research and application in the financial industry, having objectives such as recognition and reduction of fraudulent transactions for safeguarding consumers and financial institutions. Resulting from their growing reliance on digital methods of payment, so is also the increase in fraud attempts in terms of frequency and sophistication, thus requiring building up robust predictive models. These models make use of sophisticated machine learning algorithms that crunch a good deal of transaction data to identify patterns and anomalies indicative of fraudulent behavior. Business enterprises can reduce potential or actual losses considerably by putting in place effective fraud prediction systems and regain customer confidence in their services.

## Objective
The objective of this project is to create an accurate credit card fraud prediction by using Support Vector Machine (SVM), K-Nearest Neighbor (KNN), Random Forest, Decision Tree, and Boosting model.

Deployment: [Click Here!](https://huggingface.co/spaces/RidwanMS/Prediksi_Credit_Card_Fraud)

## File info
### Main Folder:
The dataset used in this project, consist of 226,976 transactions with their details. This dataset was acquired from [Kaggle](https://www.kaggle.com/datasets/kelvinkelue/credit-card-fraud-prediction?resource=download)
- P1M2_Ridwan-Syahrul.ipynb: This script consist of processing the dataset, which are data loading, exploratory data analysis, data preprocessing, data modeling, model saving.
- P1M2_Ridwan-Syahrul_inf.ipynb: This script consist of code for testing the model saved using inference data.
- PPT_M2_Ridwan-Syahrul_.pptx: This is the powerpoint for this project.
- url.txt: This text consist of link for deployment.
  
### Deployment Folder:
- app.py: This script will launch the application by calling other script, which are eda.py and prediction.py.
- eda.py: This script will show the exploratory analysis of this project on the app.
- prediction.py: This script will load the model to be used in the credit card fraud prediction.
- best_model.pkl: This file is the best model that has been acquired from P1M2_Ridwan-Syahrul.ipynb script, which is Random Forest model.
- list_kat_col.txt: This text file consist list of categorical columns on the dataset.
- list_num_col.txt: This text file consist list of numerical columns on the dataset.
- requirements.txt: This is the library list for huggingface to use for the app to work.
