from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

def train_model(df):
    """
    Train Random Forest model
    """

    features = [
        "store_id", "item_id",
        "lag_1", "lag_7",
        "rolling_mean_7",
        "day_of_week", "month",
        "on_promo"
    ]

    X = df[features]
    y = df["qty_sold"]

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X, y)

    # Predictions
    predictions = model.predict(X)

    # Evaluate
    mae = mean_absolute_error(y, predictions)
    print(f"📊 Model MAE: {round(mae, 2)}")

    # Save model
    joblib.dump(model, "model.pkl")

    return model