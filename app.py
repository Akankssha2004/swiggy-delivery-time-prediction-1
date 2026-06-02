import streamlit as st
import pandas as pd
import joblib

model = joblib.load("linear_regression_model.pkl")

st.title("Swiggy Delivery Time Prediction")

age = st.number_input("Age")
ratings = st.number_input("Ratings")
distance = st.number_input("Distance")
pickup_time = st.number_input("Pickup Time")

if st.button("Predict"):

    data = pd.DataFrame({
        'age':[age],
        'ratings':[ratings],
        'distance':[distance],
        'pickup_time_minutes':[pickup_time]
    })

    prediction = model.predict(data)

    st.success(
        f"Predicted Delivery Time: {prediction[0]:.2f} minutes"
    )