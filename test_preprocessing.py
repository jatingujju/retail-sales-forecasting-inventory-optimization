import sys
import os

# Get current folder path
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add src folder to path
sys.path.append(os.path.join(current_dir, "src"))

from preprocessing import load_data, clean_data

print("🚀 Running preprocessing test...")

df = load_data("data/retail_data.csv")
df = clean_data(df)

print("\n✅ Final Data:")
print(df.head())