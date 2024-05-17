import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run():
    st.title('Prediksi Credit Card Fraud')

    st.write('Dataframe yang diambil untuk membuat model')

    st.write(pd.read_csv('fraud test.csv'))


    st.write('#####################################################################')
    '''
    Hasil EDA
    '''
    df = pd.read_csv('fraud test.csv')
    st.write('Visualisasi data fraud')
    fig, ax = plt.subplots(figsize=(7,5))
    sns.countplot(x = 'is_fraud', data = df)
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.legend(bbox_to_anchor=(1,1))
    st.pyplot(fig)

    st.write('Visualisasi data fraud berdasarkan gender')
    fig, ax = plt.subplots(figsize=(7,5))
    sns.countplot(x = 'gender', data = df, hue = 'is_fraud')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.legend(bbox_to_anchor=(1,1))
    st.pyplot(fig)
    

    st.write('Visualisasi data fraud berdasarkan category')
    fig, ax = plt.subplots(figsize=(20,5))
    sns.countplot(x = 'category', data = df, hue = 'is_fraud')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.legend(bbox_to_anchor=(1,1))
    st.pyplot(fig)
    

    st.write('Visualisasi Amount')
    fig, ax = plt.subplots(figsize=(7,5))
    sns.histplot(df['amt'], log_scale=True)
    plt.xlabel('Amount')
    plt.ylabel('Count')
    plt.legend(bbox_to_anchor=(1,1))
    st.pyplot(fig)
    

