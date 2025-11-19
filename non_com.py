# user_validation.py (with issues)
def check_user_data(user, mail, passwd):  # Wrong parameter names
    # Missing email validation
    # Missing username length check
    
    if len(passwd) < 6:  # Wrong minimum length (should be 8)
        return "Password too short"
    
    if not any(char.isdigit() for char in passwd):
        return "Add numbers"
    
    # Missing uppercase validation
    # Returns string instead of tuple
    # No specific error messages
    
    return "OK"  # Should return tuple (bool, str)
