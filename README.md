# Credit Card Fraud Prediction

## Introduction
A business quality is dependant on their customer feedbacks. Customer feedbacks are really important for company to see what they can improve on and change for the better. For example, an airline company. Customers has so many airline to choose from and the way they choose one that fit their needs (beside their destination) is to see the airline's review. Customer can see from other customer's past experience with the respective airline if they are worth to travel with. So, with that scenario in mind, the airline company can take adventage of the review they got to improve their airline quality. However, since there are countless of review, it won't be easy to read them one by one and check if it's a good review or a bad one. This sentiment analysis was made to help the airline to classify which review are Promoter (Good) review, Passive (Neutral) review, or Detractor (Bad) review, so that it will be easier to see what went wrong with the airline by only reading the Detractor review. This will help the company tremendously to improve their airline's quality and customer satisfaction.

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
