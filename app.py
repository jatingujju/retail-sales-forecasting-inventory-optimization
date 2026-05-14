import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="Retail Forecast Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------------
# TITLE
# -----------------------------------
st.title("📊 Retail Sales Forecasting Dashboard")

st.markdown("### Interactive Inventory Optimization System")

# -----------------------------------
# LOAD DATA
# -----------------------------------
df = pd.read_csv("data/retail_data.csv")

# Fill missing values
df['qty_sold'] = df['qty_sold'].fillna(0)

# -----------------------------------
# SIDEBAR CONTROLS
# -----------------------------------
st.sidebar.header("📌 Dashboard Filters")

# Number of rows selector
num_rows = st.sidebar.slider(
    "Select Number of Rows",
    min_value=10,
    max_value=len(df),
    value=20
)

# Graph type selector
graph_type = st.sidebar.selectbox(
    "Select Graph Type",
    ["Line Chart", "Bar Chart"]
)

# Show dataset checkbox
show_data = st.sidebar.checkbox("Show Dataset", True)

# -----------------------------------
# FILTERED DATA
# -----------------------------------
filtered_df = df.head(num_rows)

# -----------------------------------
# KPI METRICS
# -----------------------------------
total_sales = int(filtered_df['qty_sold'].sum())
avg_sales = round(filtered_df['qty_sold'].mean(), 2)

std_sales = np.std(filtered_df['qty_sold'])

safety_stock = round(1.65 * std_sales, 2)
reorder_point = round(avg_sales + safety_stock, 2)

# -----------------------------------
# KPI CARDS
# -----------------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("📦 Total Sales", total_sales)
col2.metric("📈 Avg Sales", avg_sales)
col3.metric("🛡 Safety Stock", safety_stock)
col4.metric("🔄 Reorder Point", reorder_point)

# -----------------------------------
# SHOW DATASET
# -----------------------------------
if show_data:
    st.subheader("📁 Dataset Preview")
    st.dataframe(filtered_df)

# -----------------------------------
# INTERACTIVE GRAPH
# -----------------------------------
st.subheader("📊 Interactive Sales Visualization")

if graph_type == "Line Chart":
    st.line_chart(filtered_df['qty_sold'])

elif graph_type == "Bar Chart":
    st.bar_chart(filtered_df['qty_sold'])

# -----------------------------------
# MATPLOTLIB VISUALIZATION
# -----------------------------------
st.subheader("📉 Detailed Sales Analysis")

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(filtered_df['qty_sold'], marker='o')

ax.set_xlabel("Index")
ax.set_ylabel("Quantity Sold")
ax.set_title("Retail Sales Trend")

st.pyplot(fig)

# -----------------------------------
# INVENTORY INSIGHTS
# -----------------------------------
st.subheader("📦 Inventory Optimization Insights")

inventory_df = pd.DataFrame({
    "Metric": [
        "Average Sales",
        "Safety Stock",
        "Reorder Point"
    ],
    "Value": [
        avg_sales,
        safety_stock,
        reorder_point
    ]
})

st.table(inventory_df)

# -----------------------------------
# DOWNLOAD BUTTON
# -----------------------------------
csv = filtered_df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="⬇ Download Filtered Data",
    data=csv,
    file_name='filtered_retail_data.csv',
    mime='text/csv'
)

# -----------------------------------
# FOOTER
# -----------------------------------
st.markdown("---")

st.markdown(
    "👨‍💻 Developed by **Jatin Gujarathi** | Interactive Retail Dashboard"
)