import streamlit as st
import pandas as pd

from preprocessing import load_data, clean_data
from features import create_features
from model import train_model
from inventory import calculate_inventory

st.set_page_config(page_title="Retail Forecasting Dashboard", layout="wide")

st.title("📊 Retail Sales Forecasting & Inventory Optimization")

# Load data
df = load_data("data/retail_data.csv")
df = clean_data(df)
df = create_features(df)

# Train model
model = train_model(df)

# Sidebar inputs
st.sidebar.header("🔧 Controls")

store = st.sidebar.selectbox("Select Store", df["store_id"].unique())
item = st.sidebar.selectbox("Select Item", df["item_id"].unique())
stock = st.sidebar.slider("Current Stock", 0, 500, 100)

# Filter data
filtered_df = df[(df["store_id"] == store) & (df["item_id"] == item)]

st.subheader("📈 Sales Trend")
st.line_chart(filtered_df.set_index("date")["qty_sold"])

# Prepare latest data
sample = filtered_df.iloc[-10:]

features = [
    "store_id", "item_id",
    "lag_1", "lag_7",
    "rolling_mean_7",
    "day_of_week", "month",
    "on_promo"
]

X_sample = sample[features]

# Prediction
forecast = model.predict(X_sample)

st.subheader("📊 Forecast")
st.write(forecast)

# Inventory calculation
inventory = calculate_inventory(forecast, current_stock=stock)

st.subheader("📦 Inventory Recommendation")

st.metric("Safety Stock", inventory["safety_stock"])
st.metric("Reorder Point", inventory["reorder_point"])
st.metric("Order Quantity", inventory["order_quantity"])

st.success("✅ System running successfully!")