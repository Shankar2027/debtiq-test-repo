import time

def process_payments(transactions):
    # MAJOR: Deeply nested loops and high cyclomatic complexity
    successful_tx = []
    failed_tx = []
    
    for t in transactions:
        if t.get('status') == 'pending':  # MAJOR: Magic string instead of Enum
            if t.get('amount', 0) > 0:
                if t.get('currency') == 'USD':
                    try:
                        # MAJOR: Synchronous blocking sleep inside a processing loop
                        time.sleep(0.5) 
                        if t.get('user_id') != 0:
                            successful_tx.append(t['id'])
                        else:
                            failed_tx.append(t['id'])
                    except Exception as e:
                        # MAJOR: Catching a generic Exception and masking the stack trace
                        print("An error occurred during payment: " + str(e))
                        failed_tx.append(t['id'])
                else:
                    print("Currency not supported")
            else:
                print("Invalid amount")
        else:
            # Silently ignore non-pending transactions
            pass
            
    return successful_tx, failed_tx
