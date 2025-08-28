# user_validation.py
import re

def validate_registration(username, email, password):
    """
    Validate user registration data.
    
    Args:
        username (str): Proposed username
        email (str): User email address
        password (str): Proposed password
        
    Returns:
        tuple: (bool success, str message)
    """
    
    # Validate username
    if not re.match(r'^[a-zA-Z0-9]{3,20}$', username):
        return False, "Username must be 3-20 alphanumeric characters"
    
    # Validate email
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        return False, "Invalid email format"
    
    # Validate password
    if len(password) < 8:
        return False, "Password must be at least 8 characters"
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter"
    if not re.search(r'[0-9]', password):
        return False, "Password must contain at least one number"
    
    return True, "Registration data is valid"


# Example usage
if __name__ == "__main__":
    # Test cases
    print(validate_registration("john123", "john@email.com", "Pass1234"))  # Valid
    print(validate_registration("jo", "john@email.com", "Pass1234"))       # Invalid username
    print(validate_registration("john123", "invalid-email", "Pass1234"))   # Invalid email
    print(validate_registration("john123", "john@email.com", "weak"))      # Invalid password
