import os
import sys
import json
import logging
from jsonschema import validate, ValidationError
import logging

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

def load_json_file(file_path):
    """Load JSON data from a file."""
    if not os.path.exists(file_path):
        logging.error(f"Error loading JSON file: File '{file_path}' does not exist", exc_info=True)
        return None
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        # Handle JSON decoding errors specifically
        logging.error(f"Error decoding JSON: {e}", exc_info=True)
        return None
    except Exception as e:
        # Handle other exceptions
        logging.error(f"Error loading JSON file: {e}", exc_info=True)
        return None

def validate_json_data(data, schema):
    """Validate the given JSON data against the provided schema."""
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        # Handle JSON validation errors specifically
        logging.error(f"Error validating JSON: {e}", exc_info=True)
        return False
    return True

def process(data, tax_rates):
    """Process the given JSON data and return the total value of active items."""
    loaded_data = load_json_file(data)
    if loaded_data is None:
        return -1
    
    if not validate_json_data(loaded_data, json_schema):
        return -1
    
    if 'items' not in loaded_data or not isinstance(loaded_data['items'], list):
        logging.error(f"process: Invalid JSON data: 'items' key is missing or not an array", exc_info=True)
        return -1
    
    total_value = 0
    for item in loaded_data['items']:
        if 'status' not in item or 'val' not in item or not isinstance(item['status'], int) or not isinstance(item['val'], int):
            logging.error(f"process: Invalid item in JSON data: missing or invalid 'status' or 'val' key", exc_info=True)
            continue
        
        if item['status'] == ACTIVE_STATUS:
            total_value += item['val']
    
    return total_value

def get_tax_rate(tax_rates):
    """Get the tax rate from the provided tax rates."""
    if not isinstance(tax_rates, dict):
        logging.error(f"get_tax_rate: Invalid tax rates: not a dictionary", exc_info=True)
        return 0
    try:
        return tax_rates['default']
    except KeyError as e:
        # Handle missing tax rate specifically
        logging.error(f"get_tax_rate: Error calculating tax: Missing tax rate '{e}'", exc_info=True)
        return 0

def calc_tax(amt, tax_rates):
    """Calculate the tax for the given amount based on the provided tax rates."""
    tax_rate = get_tax_rate(tax_rates)
    if not isinstance(tax_rate, int):
        logging.error(f"calc_tax: Invalid tax rate: not an integer", exc_info=True)
        return 0
    
    return amt * tax_rate

# Example usage:
tax_rates = {
    'default': 1.085
}

data = 'data.json'
total_value = process(data, tax_rates)
tax = calc_tax(total_value, tax_rates)
logging.info(f"Total value: {total_value}, Tax: {tax}")