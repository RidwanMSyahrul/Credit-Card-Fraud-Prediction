import pandas as pd
import streamlit as st
import pickle
import json

def run():
    # Load File
    with open('best_model.pkl', 'rb') as file_1:
        best_model = pickle.load(file_1)

    with open('list_kat_col.txt', 'r') as file_2:
        list_kat = json.load(file_2)

    with open('list_num_col.txt', 'r') as file_3:
        list_num = json.load(file_3)

    st.title('Prediksi Credit Card Fraud')
    # Input form
    with st.form ('Form Data Pengisi'):
        merchant= st.text_input('Merchant Name')

        category= st.text_input('Transaction Type')

        amt= st.number_input('Amount', min_value=0)

        options_gender= {'F':1, 'M':0}
        gender = st.radio('Gender', options_gender)

        state= st.text_input('State (Initial Only)')

        city_pop= st.number_input('City Population', min_value=0)

        job= st.text_input('Job')

        unix_time= st.number_input('Transaction Timestamp (in UNIX format)', min_value=0)

        sub= st.form_submit_button('Submit Data')
 

        # st.write(data_predict)
        if sub:
            data_inf = {
                'merchant': merchant,
                'category': category,
                'amt': amt,
                'gender': gender,
                'state': state,
                'city_pop': city_pop,
                'job': job,
                'unix_time':unix_time
                }
            dfpred= pd.DataFrame([data_inf])

            hasil_predict = best_model.predict(dfpred)
            if hasil_predict[0] == 0:
                result = 'Your credit card is legitimate'
            elif hasil_predict[0] == 1:
                result = 'Your credit card is fraud'

            st.write(result)
