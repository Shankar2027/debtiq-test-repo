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
        self.name = name
        self.price = price
        self.in_stock = in_stock

class DiscountCalculator:
    """Class for calculating discounts"""
    def __init__(self):
        self.STORE_ITEMS = [
            StoreItem("Laptop", 1200, True),
            StoreItem("Mouse", 45, True),
            StoreItem("Keyboard", 30, False)
        ]

    def calculate_discount(self, price: float, customer_type: CustomerType) -> int:
        """Calculate the discount based on the customer type"""
        if customer_type == CustomerType.VIP:
            discount_percentage = 0.20
        elif customer_type == CustomerType.REGULAR:
            discount_percentage = 0.05
        elif customer_type == CustomerType.EMPLOYEE:
            discount_percentage = 0.50
        else:
            raise ValueError("Invalid customer type")

        discount_amount = price * discount_percentage
        final_price = price - discount_amount

        # Check if the result of math.ceil is an integer
        if not isinstance(math.ceil(final_price), int):
            raise ValueError("Final price is not an integer")

        return math.ceil(final_price)

# Example usage:
calculator = DiscountCalculator()
try:
    print(calculator.calculate_discount(100, CustomerType.VIP))
except ValueError as e:
    print(f"Error: {e}")