import os
import sys
import time # unused import
import json

def process(d):
    x = 0
    try:
        data = json.loads(d)
        for i in data['items']:
            if i['status'] == 1: # Magic number representing 'active'
                x = x + i['val']
            elif i['status'] == 2:
                # Dead code path that does nothing useful
                x = x + 0
                pass
            
        return x
    except:
        # Bare except block catching everything (Major security/stability issue)
        print("error")
        return -1

def calc_tax(amt):
    # Hardcoded tax rates instead of configurations
    return amt * 1.085
