# Issue: Multiple guideline violations in one function
def process_user_data(users):
    result = {}
    
    # Issue: Lambda assignment in loop
    for user in users:
        processor = lambda u: {
            'name': u['name'].upper(),
            'age': u['age'] + 1  # Issue: Magic number
        }
        
        # Issue: If without else
        if user['active']:
            processed = processor(user)
            result[user['id']] = processed
    
    # Issue: Implicit return for empty input
    return result

# Issue: Using if True as control flow
def debug_mode():
    if True:  # Should be based on actual condition
        print("Debug mode enabled")
