class User:
    def __init__(self, name=None):
        self.name = name
        self.address = None
        self.orders = None

def process_user_data(user):
    # Scenario 1: Accessing attribute of None
    print(user.name.upper())  # Will fail if user is None

def process_address(user):
    # Scenario 2: Nested attribute access of None
    if user is not None and user.address is not None:
        return user.address.city
    else:
        return None
 
def calculate_total_orders(user):
    # Scenario 3: Method call on None
    return user.orders.calculate_total()  # Will fail if orders is None

def process_list_items(items):
    # Scenario 4: None in list operations
    return items.append("new_item")  # Will fail if items is None

def string_operations(text):
    # Scenario 5: String operations on None
    return text.strip().lower()  # Will fail if text is None

def main():
    # Creating scenarios that will cause TypeError
    user = User()
    
    # Scenario 1: Will fail
    process_user_data(None)
    
    # Scenario 2: Will fail
    process_address(user)
    
    # Scenario 3: Will fail
    calculate_total_orders(user)
    
    # Scenario 4: Will fail
    items = None
    process_list_items(items)
    
    # Scenario 5: Will fail
    text = None
    string_operations(text)

if __name__ == "__main__":
    main()