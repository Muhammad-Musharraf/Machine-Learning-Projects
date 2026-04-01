import streamlit as st
import pickle

import pandas as pd

# Load the trained model and the data
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df (1).pkl', 'rb'))



st.title("Car Price Prediction")

# Brand
brand = st.selectbox('Car Model', df['name'].unique())
# company
company=st.selectbox('Company', df['company'].unique())

# Year
year=st.selectbox('Year', df['year'].unique())

# Kms Driven
kms_driven=st.number_input('Kms Driven')

# Fuel Type
fuel_type=st.selectbox('Fuel Type', df['fuel_type'].unique())


if st.button('Predict Price'):
    query = pd.DataFrame([{
    'name': brand,
    'company': company,
    'year': year,
    'kms_driven': kms_driven,
    'fuel_type': fuel_type}])
    prediction = pipe.predict(query)[0]
    st.title("The predicted price of the car is " + str(int(prediction)))
    
    


