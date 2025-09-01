def check_payment(total, amount, curr):  # Wrong parameter names
    # No input validation
    # No currency support
    # No error handling
    
    if amount == total:  # No tolerance, no currency conversion
        return "OK"
    else:
        return "Wrong amount"  # No detailed message
