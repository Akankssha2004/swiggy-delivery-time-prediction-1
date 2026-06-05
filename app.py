import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Swiggy Delivery Predictor",
    page_icon="🚚",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

.main-title{
    text-align:center;
    color:#FC8019;
    font-size:50px;
    font-weight:bold;
}

.sub-title{
    text-align:center;
    color:gray;
    font-size:18px;
    margin-bottom:20px;
}

.stButton > button{
    width:100%;
    background-color:#FC8019;
    color:white;
    font-size:20px;
    font-weight:bold;
    border-radius:12px;
    height:60px;
}

.prediction-box{
    background-color:#FFF3E0;
    padding:25px;
    border-radius:15px;
    text-align:center;
    font-size:32px;
    font-weight:bold;
    color:#E65100;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD MODEL
# -----------------------------
model = joblib.load("linear_regression_model.pkl")

# -----------------------------
# HEADER
# -----------------------------
st.markdown(
    "<div class='main-title'>🚚 Swiggy Delivery Time Prediction</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Predict food delivery time using Machine Learning</div>",
    unsafe_allow_html=True
)

# ==========================================================
# RIDER DETAILS
# ==========================================================

with st.expander("🚴 Rider Details", expanded=True):

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input(
            "Age",
            min_value=18,
            max_value=60,
            value=25
        )

        ratings = st.number_input(
            "Ratings",
            min_value=1.0,
            max_value=5.0,
            value=4.5
        )

    with col2:

        vehicle_condition = st.selectbox(
            "Vehicle Condition",
            [0, 1, 2]
        )

        type_of_vehicle = st.selectbox(
            "Vehicle Type",
            [
                "motorcycle",
                "scooter",
                "electric_scooter"
            ]
        )

# ==========================================================
# ORDER DETAILS
# ==========================================================

with st.expander("🍔 Order Details", expanded=True):

    col1, col2 = st.columns(2)

    with col1:

        type_of_order = st.selectbox(
            "Type of Order",
            [
                "Snack",
                "Meal",
                "Drinks",
                "Buffet"
            ]
        )

        multiple_deliveries = st.number_input(
            "Multiple Deliveries",
            min_value=0,
            max_value=5,
            value=0
        )

        pickup_time_minutes = st.number_input(
            "Pickup Time Minutes",
            min_value=0,
            value=15
        )

    with col2:

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

        order_day_of_week = st.selectbox(
            "Day Of Week",
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

        order_time_hour = st.number_input(
            "Order Time Hour",
            min_value=0,
            max_value=23,
            value=14
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

# ==========================================================
# ENVIRONMENT DETAILS
# ==========================================================

with st.expander("🌦️ Environment Details", expanded=True):

    col1, col2 = st.columns(2)

    with col1:

        weather = st.selectbox(
            "Weather",
            [
                "Sunny",
                "Cloudy",
                "Fog",
                "Stormy",
                "Sandstorms"
            ]
        )

        traffic = st.selectbox(
            "Traffic",
            [
                "Low",
                "Medium",
                "High",
                "Jam"
            ]
        )

        festival = st.selectbox(
            "Festival",
            [
                "Yes",
                "No"
            ]
        )

    with col2:

        city_type = st.selectbox(
            "City Type",
            [
                "Urban",
                "Metropolitan"
            ]
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

        distance = st.number_input(
            "Distance (km)",
            min_value=0.0,
            value=5.0
        )

        is_weekend = st.selectbox(
            "Is Weekend",
            [0, 1]
        )

# ==========================================================
# LOCATION DETAILS
# ==========================================================

with st.expander("📍 Location Details", expanded=False):

    col1, col2 = st.columns(2)

    with col1:

        restaurant_latitude = st.number_input(
            "Restaurant Latitude",
            value=17.3850
        )

        restaurant_longitude = st.number_input(
            "Restaurant Longitude",
            value=78.4867
        )

    with col2:

        delivery_latitude = st.number_input(
            "Delivery Latitude",
            value=17.4500
        )

        delivery_longitude = st.number_input(
            "Delivery Longitude",
            value=78.3900
        )

# ==========================================================
# PREDICTION BUTTON
# ==========================================================

if st.button("🚀 Predict Delivery Time"):

    input_data = pd.DataFrame({

        "age":[age],
        "ratings":[ratings],

        "restaurant_latitude":[restaurant_latitude],
        "restaurant_longitude":[restaurant_longitude],

        "delivery_latitude":[delivery_latitude],
        "delivery_longitude":[delivery_longitude],

        "weather":[weather],
        "traffic":[traffic],

        "vehicle_condition":[vehicle_condition],

        "type_of_order":[type_of_order],
        "type_of_vehicle":[type_of_vehicle],

        "multiple_deliveries":[multiple_deliveries],

        "festival":[festival],

        "city_type":[city_type],
        "city_name":[city_name],

        "order_day":[order_day],
        "order_month":[order_month],

        "order_day_of_week":[order_day_of_week],

        "is_weekend":[is_weekend],

        "pickup_time_minutes":[pickup_time_minutes],

        "order_time_hour":[order_time_hour],

        "order_time_of_day":[order_time_of_day],

        "distance":[distance]
    })

    prediction = model.predict(input_data)

    st.markdown(
        f"""
        <div class="prediction-box">
            ⏱️ Estimated Delivery Time<br><br>
            {prediction[0]:.2f} Minutes
        </div>
        """,
        unsafe_allow_html=True
    )
