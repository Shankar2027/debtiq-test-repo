import math

def apply_discount(price, customer_type):
    # Magic numbers and hardcoded strings
    if customer_type == "VIP":
        final_price = price - (price * 0.20)
    elif customer_type == "REGULAR":
        final_price = price - (price * 0.05)
    elif customer_type == "EMPLOYEE":
        final_price = price - (price * 0.50)
    else:
        final_price = price
        
    return math.ceil(final_price)

# Dictionary with duplicated structure that shouldn't be over-engineered
STORE_ITEMS = [
    {"name": "Laptop", "price": 1200, "in_stock": True},
    {"name": "Mouse", "price": 45, "in_stock": True},
    {"name": "Keyboard", "price": 30, "in_stock": False}
]
