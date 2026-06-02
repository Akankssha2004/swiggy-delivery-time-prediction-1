import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("linear_regression_model.pkl")

st.title("🚚 Swiggy Delivery Time Prediction")

st.write("Enter order details below")

# Numerical Inputs
age = st.number_input("Age", min_value=18, max_value=60, value=25)
ratings = st.number_input("Ratings", min_value=1.0, max_value=5.0, value=4.5)
restaurant_latitude = st.number_input("Restaurant Latitude", value=17.3850)
restaurant_longitude = st.number_input("Restaurant Longitude", value=78.4867)

delivery_latitude = st.number_input("Delivery Latitude", value=17.4500)
delivery_longitude = st.number_input("Delivery Longitude", value=78.3900)

vehicle_condition = st.selectbox(
    "Vehicle Condition",
    [0, 1, 2]
)

multiple_deliveries = st.number_input(
    "Multiple Deliveries",
    min_value=0,
    max_value=5,
    value=0
)

order_day = st.number_input(
    "Order Day",
    min_value=1,
    max_value=31,
    value=15
)

order_month = st.number_input(
    "Order Month",
    min_value=1,
    max_value=12,
    value=6
)

is_weekend = st.selectbox(
    "Is Weekend",
    [0, 1]
)

pickup_time_minutes = st.number_input(
    "Pickup Time Minutes",
    min_value=0,
    value=15
)

order_time_hour = st.number_input(
    "Order Time Hour",
    min_value=0,
    max_value=23,
    value=14
)

distance = st.number_input(
    "Distance (km)",
    min_value=0.0,
    value=5.0
)

# Categorical Inputs

weather = st.selectbox(
    "Weather",
    ["Sunny", "Cloudy", "Fog", "Stormy", "Sandstorms"]
)

traffic = st.selectbox(
    "Traffic",
    ["Low", "Medium", "High", "Jam"]
)

type_of_order = st.selectbox(
    "Type of Order",
    ["Snack", "Meal", "Drinks", "Buffet"]
)

type_of_vehicle = st.selectbox(
    "Type of Vehicle",
    ["motorcycle", "scooter", "electric_scooter"]
)

festival = st.selectbox(
    "Festival",
    ["Yes", "No"]
)

city_type = st.selectbox(
    "City Type",
    ["Urban", "Metropolitan"]
)

city_name = st.selectbox(
    "City",
    [
        "BANG",
        "HYD",
        "CHEN",
        "MUM",
        "KOL",
        "PUNE",
        "DEL"
    ]
)

order_day_of_week = st.selectbox(
    "Day of Week",
    [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
)

order_time_of_day = st.selectbox(
    "Time Of Day",
    [
        "Morning",
        "Afternoon",
        "Evening",
        "Night"
    ]
)

if st.button("Predict Delivery Time"):

    input_data = pd.DataFrame({
        "age": [age],
        "ratings": [ratings],
        "restaurant_latitude": [restaurant_latitude],
        "restaurant_longitude": [restaurant_longitude],
        "delivery_latitude": [delivery_latitude],
        "delivery_longitude": [delivery_longitude],
        "weather": [weather],
        "traffic": [traffic],
        "vehicle_condition": [vehicle_condition],
        "type_of_order": [type_of_order],
        "type_of_vehicle": [type_of_vehicle],
        "multiple_deliveries": [multiple_deliveries],
        "festival": [festival],
        "city_type": [city_type],
        "city_name": [city_name],
        "order_day": [order_day],
        "order_month": [order_month],
        "order_day_of_week": [order_day_of_week],
        "is_weekend": [is_weekend],
        "pickup_time_minutes": [pickup_time_minutes],
        "order_time_hour": [order_time_hour],
        "order_time_of_day": [order_time_of_day],
        "distance": [distance]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Estimated Delivery Time: {prediction[0]:.2f} minutes"
    )