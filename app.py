import streamlit as st
import pandas as pd
import joblib

model = joblib.load("linear_regression_model.pkl")

st.title("Swiggy Delivery Time Prediction")

age = st.number_input("Age",18,60,25)

ratings = st.number_input("Ratings",
                          1.0,
                          5.0,
                          4.5)

vehicle_condition = st.selectbox(
    "Vehicle Condition",
    [0,1,2]
)

multiple_deliveries = st.number_input(
    "Multiple Deliveries",
    0,
    5,
    1
)

pickup_time_minutes = st.number_input(
    "Pickup Time Minutes",
    1,
    60,
    15
)

distance = st.number_input(
    "Distance(KM)",
    0.1,
    50.0,
    5.0
)

order_time_hour = st.number_input(
    "Order Time Hour",
    0,
    23,
    12
)

weather = st.selectbox(
    "Weather",
    ['Sunny','Cloudy','Fog','Stormy','Sandstorms']
)

traffic = st.selectbox(
    "Traffic",
    ['Low','Medium','High','Jam']
)

type_of_order = st.selectbox(
    "Order Type",
    ['Snack','Meal','Drinks','Buffet']
)

type_of_vehicle = st.selectbox(
    "Vehicle Type",
    ['motorcycle','scooter']
)

city_type = st.selectbox(
    "City Type",
    ['Urban','Metropolitan']
)

city_name = st.selectbox(
    "City",
    ['BANG','HYD','CHEN']
)

festival = st.selectbox(
    "Festival",
    ['No','Yes']
)

order_day_of_week = st.selectbox(
    "Day",
    ['Monday','Tuesday','Wednesday',
     'Thursday','Friday',
     'Saturday','Sunday']
)

order_time_of_day = st.selectbox(
    "Time Of Day",
    ['Morning','Afternoon',
     'Evening','Night']
)

if st.button("Predict"):

    data = pd.DataFrame({

        'age':[age],
        'ratings':[ratings],
        'vehicle_condition':[vehicle_condition],
        'multiple_deliveries':[multiple_deliveries],
        'pickup_time_minutes':[pickup_time_minutes],
        'distance':[distance],
        'order_time_hour':[order_time_hour],

        'weather':[weather],
        'traffic':[traffic],
        'type_of_order':[type_of_order],
        'type_of_vehicle':[type_of_vehicle],
        'festival':[festival],
        'city_type':[city_type],
        'city_name':[city_name],
        'order_day':[15],
        'order_month':[6],
        'order_day_of_week':[order_day_of_week],
        'is_weekend':[0],
        'order_time_of_day':[order_time_of_day],

        'restaurant_latitude':[17.3850],
        'restaurant_longitude':[78.4867],
        'delivery_latitude':[17.4500],
        'delivery_longitude':[78.5000]

    })

    prediction = model.predict(data)

    st.success(
        f"Estimated Delivery Time: {prediction[0]:.2f} Minutes"
    )