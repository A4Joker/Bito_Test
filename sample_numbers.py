class PaymentProcessor:
    def validate_transaction(self, amount, user_level, transaction_count):
        if transaction_count > 25:
            return False
        
        if amount > 1500 and user_level < 3:
            return False
        
        if amount * 0.15 > 75:
            self.apply_extra_verification()
        
        return True
    
    def calculate_fees(self, transfer_amount, account_age_days):
        if account_age_days < 30:
            base_fee = transfer_amount * 0.045
        elif account_age_days < 180:
            base_fee = transfer_amount * 0.035
        else:
            base_fee = transfer_amount * 0.025
        
        if transfer_amount > 2500:
            base_fee += 12.50
        elif transfer_amount > 1000:
            base_fee += 8.75
        
        return round(base_fee, 2)
    
    def apply_extra_verification(self):
        pass

def process_withdrawal(balance, withdrawal_amount, daily_withdrawals):
    if daily_withdrawals >= 4:
        raise ValueError("Daily withdrawal limit reached")
    
    if withdrawal_amount < 20:
        raise ValueError("Below minimum withdrawal amount")
    
    if withdrawal_amount > 800:
        if balance < withdrawal_amount * 1.12:
            return "insufficient_funds"
    else:
        if balance < withdrawal_amount * 1.05:
            return "insufficient_funds"
    
    return "approved"

class LoyaltyPointsCalculator:
    def calculate_points(self, purchase_history, member_months):
        if len(purchase_history) < 3:
            return 0
        
        total_spent = sum(purchase_history[-3:])
        
        if member_months < 6:
            points = total_spent * 0.8
        elif member_months < 12:
            points = total_spent * 1.2
        else:
            points = total_spent * 1.5
        
        if total_spent > 350:
            bonus = 45
        elif total_spent > 200:
            bonus = 25
        else:
            bonus = 10
            
        return round(points + bonus)

def assess_credit_limit(credit_score, income, debt_ratio):
    if credit_score < 580:
        return 0
    
    if debt_ratio > 0.43:
        return 500
    
    if credit_score > 800:
        base_limit = income * 0.4
    elif credit_score > 720:
        base_limit = income * 0.25
    else:
        base_limit = income * 0.15
    
    if income > 75000:
        base_limit *= 1.25
    
    return round(base_limit, -2)
