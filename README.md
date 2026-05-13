# 📊 Retail Sales Forecasting & Inventory Optimization System

## 🚀 Overview

This project is an end-to-end Retail Analytics solution that forecasts future product sales and optimizes inventory levels using Machine Learning and business-driven inventory logic.

The system simulates how modern retail companies like Amazon, Walmart, Flipkart, and Reliance Retail use forecasting and inventory optimization to improve supply chain efficiency and reduce operational costs.

---

## 🌐 Live Demo

🔗 https://retail-sales-forecasting-inventory-optimization-ra9jurgvlqogde.streamlit.app/

---

## ❗ Problem Statement

Retail businesses frequently face inventory management challenges such as:

- Overstocking 📦 → Increased holding/storage costs
- Stockouts ❌ → Lost sales and poor customer experience
- Poor demand forecasting 📉 → Inefficient inventory planning

Accurate forecasting and inventory optimization are critical for maintaining profitability and operational efficiency.

---

## ✅ Solution

This system helps retailers by:

- Predicting future product demand using Machine Learning
- Calculating Safety Stock levels
- Determining Reorder Points (ROP)
- Supporting data-driven inventory planning
- Reducing stockout and overstock risks

---

## 🧠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit

---

## ⚙️ Features

✅ Sales Forecasting using Random Forest Regressor  
✅ Feature Engineering (Lag Features & Rolling Mean)  
✅ Data Visualization & Trend Analysis  
✅ Inventory Optimization Logic  
✅ Safety Stock Calculation  
✅ Reorder Point (ROP) Prediction  
✅ Interactive Streamlit Dashboard  

---

## 📁 Project Structure

```bash
Retail-Sales-Forecasting-Inventory-Optimization/
│
├── data/                         # Dataset files
│   └── retail_data.csv
│
├── outputs/                      # Generated visualizations
│   ├── sales_trend.png
│   ├── feature_importance.png
│   └── actual_vs_predicted.png
│
├── preprocessing.py              # Data cleaning & preprocessing
├── features.py                   # Feature engineering logic
├── model.py                      # Machine Learning model training
├── inventory.py                  # Inventory optimization calculations
├── visualization.py              # Graph generation
├── main.py                       # Main project pipeline
├── app.py                        # Streamlit dashboard
├── requirements.txt              # Required dependencies
└── README.md                     # Project documentation
```

---

## ⚙️ Workflow

```text
Data Collection
      ↓
Data Cleaning & Preprocessing
      ↓
Exploratory Data Analysis (EDA)
      ↓
Feature Engineering
      ↓
Sales Forecasting Model
      ↓
Inventory Optimization
      ↓
Dashboard Visualization
```

---

## 📊 Machine Learning Approach

### 🔹 Forecasting Model
- Random Forest Regressor

### 🔹 Features Used
- Lag Features
- Rolling Mean
- Historical Sales Patterns

### 🔹 Inventory Logic
- Safety Stock Calculation
- Reorder Point (ROP)
- Inventory Recommendation

---

## ▶️ How to Run the Project

### 1️⃣ Clone Repository

```bash
git clone https://github.com/jatingujju/retail-sales-forecasting-inventory-optimization.git
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run Main Project

```bash
python main.py
```

---

### 4️⃣ Run Streamlit Dashboard

```bash
streamlit run app.py
```

---

## 📊 Results

- Accurate sales demand forecasting
- Reduced inventory planning errors
- Improved stock availability
- Better inventory optimization decisions

### 📈 Model Performance
- MAE: ~1.6
- High forecasting accuracy on simulated retail dataset

---

## 📸 Screenshots

### 📈 Sales Trend

<img src="outputs/sales_trend.png" width="850">

---

### 📊 Feature Importance

<img src="outputs/feature_importance.png" width="850">

---

### 📉 Actual vs Predicted

<img src="outputs/actual_vs_predicted.png" width="850">

---

## 🎥 Demo

🔗 Live Streamlit Dashboard:  
https://retail-sales-forecasting-inventory-optimization-ra9jurgvlqogde.streamlit.app/

---

## 💼 Business Impact

This project demonstrates how retailers can:

- Improve demand planning
- Reduce excess inventory costs
- Prevent stockouts
- Improve supply chain efficiency
- Enable data-driven decision making

---

## 🚀 Future Improvements

- Multi-store forecasting
- Product category forecasting
- XGBoost / LSTM forecasting models
- Real-time inventory tracking
- Weather & promotion impact analysis
- Automated replenishment recommendations
- Advanced dashboard analytics

---

## 📚 Learning Outcomes

Through this project, I learned:

- Time-series forecasting fundamentals
- Feature engineering techniques
- Inventory optimization concepts
- Machine Learning workflow
- Streamlit dashboard deployment
- GitHub project management

---

## 👨‍💻 Author

### Jatin Gujarathi

- Data Science Enthusiast
- Python Developer
- Aspiring Data Analyst / ML Engineer

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

---

## 🔗 GitHub Repository

https://github.com/jatingujju/retail-sales-forecasting-inventory-optimization
