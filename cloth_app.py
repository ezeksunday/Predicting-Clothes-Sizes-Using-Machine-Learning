import streamlit as st
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

import gzip

#Load model
model = pickle.load(gzip.open('compressed_model.pkl.gz', 'rb'))

def predict_size(input_data):
    size_labels = ['L', 'M', 'S', 'XL', 'XXL', 'XXS', 'XXXL']
    label_encoder = LabelEncoder()
    label_encoder.fit(size_labels)
    prediction = model.predict(input_data)
    predicted_size = label_encoder.inverse_transform(prediction)
    return predicted_size

#Main App
htmlfile=""""
<div style = "background-color:Tomato; padding:10px;margin:10px;">
<h1 style = "color:white; text-align:center;"> CLOTHES SIZE PREDICTION APP </h1>
</div>
"""
st.markdown(htmlfile, unsafe_allow_html=True)
st.markdown('<p style = "font-weight:bold;"> Weight (in kg) </p>', unsafe_allow_html = True)
weight = st.number_input('', min_value=20.0, max_value=500.0, step=1.0)
st.markdown('<p style = "font-weight:bold;"> Age </p>', unsafe_allow_html = True)
age = st.number_input('', min_value=10, max_value=120, step=1)
st.markdown('<p style = "font-weight:bold;"> Height (in cm) </p>', unsafe_allow_html = True)
height = st.number_input('', min_value=100.0, max_value=500.0, step=1.0)

if st.button('Predict Clothing Size'):
    if weight > 0 and age > 0 and height > 0:
        bmi=height/weight
        input_data = [[age, height,weight,bmi]]
        predicted_size = predict_size(input_data)
        st.success(f"The predicted clothing size is: {predicted_size[0]}")
    else:
        st.warning("Please fill in all the required fields.")
