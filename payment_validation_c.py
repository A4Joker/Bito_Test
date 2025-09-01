def validate_payment_amount(order_total: float, payment_amount: float, currency: str) -> Tuple[bool, str]:
    """
    Validate payment amount against order total with currency support
    """
    valid_currencies = ['USD', 'EUR', 'GBP']
    conversion_rates = {'USD': 1.0, 'EUR': 0.85, 'GBP': 0.75}
    
    if currency not in valid_currencies:
        raise ValueError(f"Unsupported currency: {currency}")
    
    if order_total <= 0 or payment_amount <= 0:
        raise ValueError("Amounts must be positive")
    
    # Convert to USD for comparison
    order_usd = order_total * conversion_rates[currency]
    payment_usd = payment_amount * conversion_rates[currency]
    
    # Allow 2% tolerance
    tolerance = order_usd * 0.02
    min_amount = order_usd - tolerance
    max_amount = order_usd + tolerance
    
    if min_amount <= payment_usd <= max_amount:
        return True, "Payment amount validated successfully"
    else:
        return False, f"Payment amount out of tolerance. Expected: {order_total} {currency} ±2%"
