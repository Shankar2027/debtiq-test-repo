import math
from enum import Enum
from typing import Dict

class CustomerType(Enum):
    """Enum for customer types"""
    VIP = "VIP"
    REGULAR = "REGULAR"
    EMPLOYEE = "EMPLOYEE"

class StoreItem:
    """Class representing a store item"""
    def __init__(self, name: str, price: float, in_stock: bool):
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number")
        if not isinstance(in_stock, bool):
            raise ValueError("In stock must be a boolean value")
        self.name = name
        self.price = price
        self.in_stock = in_stock

class DiscountCalculator:
    """Class for calculating discounts"""
    DISCOUNT_PERCENTAGES = {
        CustomerType.VIP: 0.20,
        CustomerType.REGULAR: 0.05,
        CustomerType.EMPLOYEE: 0.50
    }

    def __init__(self):
        self.STORE_ITEMS = [
            StoreItem("Laptop", 1200, True),
            StoreItem("Mouse", 45, True),
            StoreItem("Keyboard", 30, False)
        ]

    def calculate_discount(self, price: float, customer_type: CustomerType) -> int:
        """Calculate the discount based on the customer type"""
        if customer_type not in self.DISCOUNT_PERCENTAGES:
            raise ValueError(f"Invalid customer type: {customer_type}")

        if price <= 0:
            raise ValueError("Price must be a positive number")

        discount_percentage = self.DISCOUNT_PERCENTAGES[customer_type]
        discount_amount = price * discount_percentage
        final_price = price - discount_amount

        if not isinstance(final_price, (int, float)) or final_price < 0:
            raise ValueError("Final price is not a non-negative number")

        return math.ceil(final_price)

# Example usage:
calculator = DiscountCalculator()
try:
    print(calculator.calculate_discount(100, CustomerType.VIP))
except ValueError as e:
    print(f"Error: {e}")