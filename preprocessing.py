import pandas as pd

def load_data(path):
    """
    Load dataset from CSV file
    """
    try:
        df = pd.read_csv(path, parse_dates=["date"])
        print("✅ Data loaded successfully")
        print(df.head())
        return df
    except Exception as e:
        print("❌ Error loading data:", e)


def clean_data(df):
    """
    Clean dataset:
    - Remove duplicates
    - Handle missing values
    - Remove negative values
    """
    print("\n🔹 Before Cleaning:", df.shape)

    # Remove duplicates
    df = df.drop_duplicates()

    # Fill missing values
    df["qty_sold"] = df["qty_sold"].fillna(0)
    df["on_promo"] = df["on_promo"].fillna(0)

    # Remove negative sales
    df = df[df["qty_sold"] >= 0]

    print("🔹 After Cleaning:", df.shape)

    return df