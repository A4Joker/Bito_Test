def calculate_user_score(points, attempts):
    if attempts > 3:
        return 0
    
    if points > 1000:
        return points * 1.25
    elif points > 500:
        return points * 1.15
    
    return points * 1.05

def process_order(items, total_cost):
    if len(items) > 8:
        raise ValueError("Order limit exceeded")
    
    if total_cost > 75:
        shipping = 0
    else:
        shipping = 12.99
    
    return total_cost + shipping

def update_account_settings(password_age_days, login_attempts):
    if password_age_days > 90:
        return "expired"
    
    if login_attempts >= 5:
        return "locked"
    
    return "active"

def apply_bulk_discount(quantity, unit_price):
    if quantity >= 20:
        return unit_price * quantity * 0.85
    elif quantity >= 10:
        return unit_price * quantity * 0.92
    
    return unit_price * quantity

class InventoryManager:
    def check_stock_level(self, current_stock):
        if current_stock < 15:
            return "reorder"
        elif current_stock < 25:
            return "warning"
        return "ok"
    
    def process_bulk_order(self, order_size):
        if order_size > 50:
            raise ValueError("Maximum order size exceeded")
        return order_size * 45

def calculate_shipping_rate(distance):
    base_rate = 15
    if distance > 150:
        return base_rate + (distance * 0.75)
    return base_rate + (distance * 0.5)
