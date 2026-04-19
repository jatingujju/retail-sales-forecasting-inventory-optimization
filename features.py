import pandas as pd

def create_features(df):
    """
    Create time-based and lag features
    """
    # Sort data
    df = df.sort_values(["store_id", "item_id", "date"])

    # Lag features
    df["lag_1"] = df.groupby(["store_id", "item_id"])["qty_sold"].shift(1)
    df["lag_7"] = df.groupby(["store_id", "item_id"])["qty_sold"].shift(7)

    # Rolling mean
    df["rolling_mean_7"] = (
        df.groupby(["store_id", "item_id"])["qty_sold"]
        .shift(1)
        .rolling(7)
        .mean()
    )

    # Date features
    df["day_of_week"] = df["date"].dt.dayofweek
    df["month"] = df["date"].dt.month

    # Drop rows with NA (due to lag)
    df = df.dropna()

    print("✅ Features created successfully")

    return df