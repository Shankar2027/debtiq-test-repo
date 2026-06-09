import os
import sys
import json
import logging
from jsonschema import validate, ValidationError

# Define named constants for better readability
ACTIVE_STATUS = 1
INACTIVE_STATUS = 2

# Define a schema for the JSON data
json_schema = {
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "status": {"type": "integer"},
                    "val": {"type": "integer"}
                },
                "required": ["status", "val"]
            }
        }
    },
    "required": ["items"]
}

def process(data, tax_rates):
    """Process the given JSON data and return the total value of active items."""
    try:
        with open(data, 'r') as f:
            loaded_data = json.load(f)
        validate(instance=loaded_data, schema=json_schema)
        total_value = 0
        for item in loaded_data['items']:
            if item['status'] == ACTIVE_STATUS:
                total_value += item['val']
        return total_value
    except json.JSONDecodeError as e:
        # Handle JSON decoding errors specifically
        logging.error(f"Error decoding JSON: {e}")
        return -1
    except ValidationError as e:
        # Handle JSON validation errors specifically
        logging.error(f"Error validating JSON: {e}")
        return -1

def calc_tax(amt, tax_rates):
    """Calculate the tax for the given amount based on the provided tax rates."""
    try:
        return amt * tax_rates['default']
    except KeyError as e:
        # Handle missing tax rate specifically
        logging.error(f"Error calculating tax: Missing tax rate '{e}'")
        return 0

# Example usage:
tax_rates = {
    'default': 1.085
}

data = 'data.json'
total_value = process(data, tax_rates)
tax = calc_tax(total_value, tax_rates)
logging.info(f"Total value: {total_value}, Tax: {tax}")