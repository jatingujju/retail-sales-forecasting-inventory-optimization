import sys
import os

# 🔥 Fix Python path (VERY IMPORTANT)
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# ✅ Imports
from preprocessing import load_data, clean_data
from features import create_features
from model import train_model
from inventory import calculate_inventory
from visualization import (
    plot_sales_trend,
    plot_actual_vs_predicted,
    plot_feature_importance
)


def main():
    print("🚀 Starting Retail Forecasting Project...\n")

    # Step 1: Load data
    df = load_data("data/retail_data.csv")

    # Step 2: Clean data
    df = clean_data(df)

    # Step 3: Feature engineering
    df = create_features(df)
    print("\n✅ Feature Engineering Done")

    # Step 4: Train model
    model = train_model(df)
    print("✅ Model Training Completed")

    # 🔥 Visualization 1: Sales Trend
    plot_sales_trend(df)

    # Step 5: Take latest data for prediction
    sample = df.iloc[-10:]

    features = [
        "store_id", "item_id",
        "lag_1", "lag_7",
        "rolling_mean_7",
        "day_of_week", "month",
        "on_promo"
    ]

    X_sample = sample[features]

    # Step 6: Forecast
    forecast = model.predict(X_sample)

    print("\n📊 Forecast Sample:")
    print(forecast)

    # 🔥 Visualization 2: Actual vs Predicted
    plot_actual_vs_predicted(sample["qty_sold"], forecast)

    # 🔥 Visualization 3: Feature Importance
    plot_feature_importance(model, features)

    # Step 7: Inventory calculation
    inventory = calculate_inventory(forecast, current_stock=100)

    print("\n📦 Inventory Recommendation:")
    print(inventory)

    print("\n🎉 Project Execution Completed Successfully!")


if __name__ == "__main__":
    main()