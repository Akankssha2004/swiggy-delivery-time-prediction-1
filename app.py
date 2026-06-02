import streamlit as st
import pandas as pd
import joblib

model = joblib.load("linear_regression_model.pkl")

st.title("Swiggy Delivery Time Prediction")

st.subheader("Delivery Partner Info")
age = st.number_input("Rider Age", min_value=18, max_value=60, value=28)
ratings = st.number_input("Rider Ratings", min_value=1.0, max_value=5.0, value=4.0, step=0.1)
multiple_deliveries = st.selectbox("Multiple Deliveries", options=[0, 1, 2, 3], index=0)
type_of_vehicle = st.selectbox(
    "Vehicle Type",
    options={"motorcycle": 0, "scooter": 1, "electric_scooter": 2, "bicycle": 3}.keys()
)
vehicle_map = {"motorcycle": 0, "scooter": 1, "electric_scooter": 2, "bicycle": 3}

st.subheader("Order Info")
type_of_order = st.selectbox(
    "Order Type",
    options={"Snack": 0, "Meal": 1, "Drinks": 2, "Buffet": 3}.keys()
)
order_map = {"Snack": 0, "Meal": 1, "Drinks": 2, "Buffet": 3}
order_time_of_day = st.selectbox(
    "Time of Day",
    options={"Morning": 0, "Afternoon": 1, "Evening": 2, "Night": 3, "Midnight": 4}.keys()
)
time_of_day_map = {"Morning": 0, "Afternoon": 1, "Evening": 2, "Night": 3, "Midnight": 4}
order_time_hour = st.slider("Order Hour (0-23)", min_value=0, max_value=23, value=12)
order_day_of_week = st.selectbox(
    "Day of Week",
    options={"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3,
             "Friday": 4, "Saturday": 5, "Sunday": 6}.keys()
)
day_map = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3,
           "Friday": 4, "Saturday": 5, "Sunday": 6}

st.subheader("Location & Conditions")
distance = st.number_input("Distance (km)", min_value=0.0, value=5.0, step=0.1)
pickup_time_minutes = st.number_input("Pickup Time (minutes)", min_value=0, value=10)
restaurant_latitude = st.number_input("Restaurant Latitude", value=12.97)
restaurant_longitude = st.number_input("Restaurant Longitude", value=77.59)
delivery_latitude = st.number_input("Delivery Latitude", value=12.98)
delivery_longitude = st.number_input("Delivery Longitude", value=77.60)
weather = st.selectbox(
    "Weather",
    options={"Sunny": 0, "Cloudy": 1, "Windy": 2, "Fog": 3, "Sandstorms": 4, "Stormy": 5}.keys()
)
weather_map = {"Sunny": 0, "Cloudy": 1, "Windy": 2, "Fog": 3, "Sandstorms": 4, "Stormy": 5}
traffic = st.selectbox(
    "Traffic Density",
    options={"Low": 0, "Medium": 1, "High": 2, "Jam": 3}.keys()
)
traffic_map = {"Low": 0, "Medium": 1, "High": 2, "Jam": 3}
festival = st.selectbox("Festival", options={"No": 0, "Yes": 1}.keys())
festival_map = {"No": 0, "Yes": 1}
city_type = st.selectbox(
    "City Type",
    options={"Urban": 0, "Metropolitian": 1, "Semi-Urban": 2}.keys()
)
city_type_map = {"Urban": 0, "Metropolitian": 1, "Semi-Urban": 2}
city_name = st.number_input(
    "City Name (encoded integer from training data)", min_value=0, max_value=50, value=0,
    help="Use the same integer encoding your LabelEncoder produced during training."
)

if st.button("Predict Delivery Time"):
    input_data = pd.DataFrame([{
        'age': age,
        'ratings': ratings,
        'restaurant_latitude': restaurant_latitude,
        'restaurant_longitude': restaurant_longitude,
        'delivery_latitude': delivery_latitude,
        'delivery_longitude': delivery_longitude,
        'multiple_deliveries': multiple_deliveries,
        'pickup_time_minutes': pickup_time_minutes,
        'order_time_hour': order_time_hour,
        'distance': distance,
        'weather': weather_map[weather],
        'traffic': traffic_map[traffic],
        'type_of_order': order_map[type_of_order],
        'type_of_vehicle': vehicle_map[type_of_vehicle],
        'festival': festival_map[festival],
        'city_type': city_type_map[city_type],
        'city_name': city_name,
        'order_day_of_week': day_map[order_day_of_week],
        'order_time_of_day': time_of_day_map[order_time_of_day],
    }])

    prediction = model.predict(input_data)
    st.success(f"Predicted Delivery Time: {prediction[0]:.2f} minutes")