import numpy as np
from scipy.stats import norm

def calculate_inventory(forecast, current_stock, lead_time=7, service_level=0.95):
    """
    Calculate inventory metrics:
    - Safety Stock
    - Reorder Point
    - Order Quantity
    """

    # Z-score for service level
    z = norm.ppf(service_level)

    # Demand during lead time
    demand_mean = np.mean(forecast[:lead_time])
    demand_std = np.std(forecast[:lead_time])

    # Safety stock
    safety_stock = z * demand_std

    # Reorder point
    reorder_point = demand_mean + safety_stock

    # Order quantity
    order_quantity = max(0, reorder_point - current_stock)

    print("✅ Inventory calculated")

    return {
        "safety_stock": round(safety_stock, 2),
        "reorder_point": round(reorder_point, 2),
        "order_quantity": round(order_quantity, 2)
    }