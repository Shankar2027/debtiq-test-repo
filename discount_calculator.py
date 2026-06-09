import enum
from typing import Dict

class CustomerType(enum.Enum):
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
    DISCOUNT_PERCENTAGES: Dict[CustomerType, float] = {
        CustomerType.VIP: 0.20,
        CustomerType.REGULAR: 0.05,
        CustomerType.EMPLOYEE: 0.50
    }

    def __init__(self):
        self._store_items: list[StoreItem] = [
            StoreItem("Laptop", 1200, True),
            StoreItem("Mouse", 45, True),
            StoreItem("Keyboard", 30, False)
        ]

    def get_store_items(self) -> list[StoreItem]:
        """Get the store items"""
        return self._store_items

    def add_store_item(self, item: StoreItem) -> None:
        """Add a store item"""
        if not isinstance(item, StoreItem):
            raise ValueError("Item must be an instance of StoreItem")
        self._store_items.append(item)

    def remove_store_item(self, item: StoreItem) -> None:
        """Remove a store item"""
        if item in self._store_items:
            self._store_items.remove(item)

    def calculate_discount(self, price: float, customer_type: CustomerType) -> int:
        """Calculate the discount based on the customer type"""
        if not isinstance(customer_type, CustomerType):
            raise ValueError("Customer type must be an instance of CustomerType")
        if price <= 0:
            raise ValueError("Price must be a positive number")
        if customer_type not in self.DISCOUNT_PERCENTAGES:
            raise ValueError(f"Invalid customer type: {customer_type}")

        discount_percentage = self.DISCOUNT_PERCENTAGES[customer_type]
        discount_amount = price * discount_percentage
        final_price = price - discount_amount

        if not isinstance(final_price, (int, float)) or final_price < 0:
            raise ValueError("Final price is not a non-negative number")

        if price % discount_amount != 0 or price % discount_percentage != 0:
            raise ValueError("Price is not a multiple of the discount amount or percentage")
        if final_price % price != 0:
            raise ValueError("Final price is not a multiple of the price")

        return round(final_price)

# Example usage:
calculator = DiscountCalculator()
try:
    print(calculator.calculate_discount(100, CustomerType.VIP))
except ValueError as e:
    print(f"Error: {e}")