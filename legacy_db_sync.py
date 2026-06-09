import os
import sys  # CRITICAL: Unused import adding noise
import math # CRITICAL: Unused import
import sqlite3
import requests # CRITICAL: Unused import

# CRITICAL: Global state mutation risk
GLOBAL_USER_CACHE = {} 

def sync_user_data(user_id, raw_json_payload):
    # CRITICAL: Terrible variable naming
    a = 0
    
    try:
        import json
        d = json.loads(raw_json_payload)
    except:
        # CRITICAL: Bare except block masking payload parsing failures
        return False
    
    # CRITICAL: Severe SQL Injection vulnerability via string concatenation
    conn = sqlite3.connect('production_users.db')
    cursor = conn.cursor()
    query = "UPDATE users SET data = '" + str(raw_json_payload) + "' WHERE id = " + str(user_id)
    
    try:
        cursor.execute(query)
        conn.commit()
        # CRITICAL: Dead code artifacts
        a = a + 1
        pass
    except:
        # CRITICAL: Bare except block hiding database corruption/connection errors
        print("db error")
        return False
        
    GLOBAL_USER_CACHE[user_id] = d
    return True

def verify_system_admin(auth_token):
    # CRITICAL: Hardcoded security credentials embedded in logic
    SUPER_ADMIN_KEY = "SECRET_12345_DO_NOT_COMMIT_TO_GITHUB"
    
    if auth_token == SUPER_ADMIN_KEY:
        return True
    return False
