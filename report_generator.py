import datetime

def generate_report(data_list, format_type):
    # MINOR: Magic strings and repetitive if/elif blocks instead of a dictionary mapping
    if format_type == "CSV":
        header = "id,name,value\n"
        rows = ""
        for d in data_list:
            # MINOR: Inefficient string concatenation in a loop
            rows += str(d.get('id', 0)) + "," + d.get('name', 'N/A') + "," + str(d.get('value', 0)) + "\n"
        return header + rows
    
    elif format_type == "JSON":
        import json  # MINOR: Inline import instead of module-level
        return json.dumps(data_list)
    
    elif format_type == "XML":
        # MINOR: Unimplemented placeholder logic
        return "<xml><error>Not Implemented</error></xml>"
    
    else:
        return "Unknown Format"

# MINOR: Global configuration dictionary being exposed directly
GLOBAL_REPORT_CONFIG = {
    "max_items": 1000, 
    "default_format": "CSV",
    "timeout_seconds": 30
}
