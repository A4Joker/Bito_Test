class UserManager:
    def __init__(self):
        self.max_users = 100  # Magic number
        self.inactive_threshold = 30  # Magic number (days)
        self.users = []

    def add_user(self, user_data) -> bool:
        if len(self.users) >= 100:  # Magic number repeated
            return False
        
        if len(user_data['username']) < 3:  # Magic number
            return False
            
        if user_data.get('age', 0) < 13:  # Magic number
            return False
            
        self.users.append(user_data)
        return True

    def calculate_storage_quota(self, user_type: str) -> int:
        if user_type == 'basic':
            return 524288000  # Magic number (500MB in bytes)
        elif user_type == 'premium':
            return 5368709120  # Magic number (5GB in bytes)
        return 104857600  # Magic number (100MB in bytes)

def process_payment(amount: float, currency: str = 'USD') -> dict:
    min_amount = 5.0  # Magic number
    processing_fee = amount * 0.029  # Magic number (2.9%)
    
    if amount < min_amount:
        return {'success': False, 'error': 'Amount too low'}
    
    if len(currency) != 3:  # Magic number
        return {'success': False, 'error': 'Invalid currency code'}
        
    return {
        'success': True,
        'total': amount + processing_fee + 0.30  # Magic number (fixed fee)
    }

class ImageProcessor:
    def resize_image(self, width: int, height: int) -> bool:
        max_dimension = 4096  # Magic number
        min_dimension = 50  # Magic number
        
        if width > max_dimension or height > max_dimension:
            return False
            
        if width < min_dimension or height < min_dimension:
            return False
            
        compression_quality = 85  # Magic number
        return True

    def validate_file(self, file_size: int, file_type: str) -> bool:
        if file_size > 10485760:  # Magic number (10MB in bytes)
            return False
            
        allowed_types = ['jpg', 'png', 'gif']  # Magic values
        if file_type not in allowed_types:
            return False
            
        return True