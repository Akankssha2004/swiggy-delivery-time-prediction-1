import streamlit as st
import joblib

model = joblib.load("linear_regression_model.pkl")

st.title("Swiggy Delivery Time Prediction")

st.subheader("Model Features")

try:
    st.write(model.feature_names_in_)
except:
    st.write("Feature names not available")

st.stop()