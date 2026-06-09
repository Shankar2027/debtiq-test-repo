import os
import sys
import json

# Define named constants for better readability
ACTIVE_STATUS = 1
INACTIVE_STATUS = 2

def process(d):
    """Process the given JSON data and return the total value of active items."""
    try:
        data = json.loads(d)
        total_value = 0
        for item in data['items']:
            if item['status'] == ACTIVE_STATUS:
                total_value += item['val']
        return total_value
    except json.JSONDecodeError as e:
        # Handle JSON decoding errors specifically
        print(f"Error decoding JSON: {e}")
        return -1

def calc_tax(amt, tax_rates):
    """Calculate the tax for the given amount based on the provided tax rates."""
    return amt * tax_rates['default']

# Example usage:
tax_rates = {
    'default': 1.085
}

data = '{"items": [{"status": 1, "val": 100}, {"status": 2, "val": 200}]}'
total_value = process(data)
tax = calc_tax(total_value, tax_rates)
print(f"Total value: {total_value}, Tax: {tax}")