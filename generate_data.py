import pandas as pd
import numpy as np

np.random.seed(42)

# Parameters
num_days = 365
num_stores = 3
num_items = 5

dates = pd.date_range(start="2023-01-01", periods=num_days)

data = []

for store in range(1, num_stores + 1):
    for item in range(1, num_items + 1):
        
        base_demand = np.random.randint(20, 50)
        
        for date in dates:
            
            # Seasonality (weekly pattern)
            day_of_week = date.dayofweek
            seasonal_factor = 1 + (0.2 if day_of_week in [5, 6] else 0)
            
            # Random noise
            noise = np.random.normal(0, 5)
            
            # Promotion effect
            on_promo = np.random.choice([0, 1], p=[0.8, 0.2])
            promo_effect = 1.5 if on_promo == 1 else 1
            
            qty_sold = max(0, int(base_demand * seasonal_factor * promo_effect + noise))
            
            data.append([
                store,
                item,
                date,
                qty_sold,
                on_promo
            ])

df = pd.DataFrame(data, columns=[
    "store_id", "item_id", "date", "qty_sold", "on_promo"
])

# Save dataset
df.to_csv("data/retail_data.csv", index=False)

print("✅ Dataset generated successfully!")
print(df.head())