from typing import List, Dict, Optional, Any
import datetime
from dataclasses import dataclass
from base_processor import UserProfile, DataProcessor

class ExtendedDataProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        # Overriding parent class constants with different types
        self.MAX_USERS = "1000"  # Changed from int to str
        self.TIMEOUT_MINUTES = 30.0  # Changed from int to float
        self.cache: Dict[str, Any] = {}

    def add_user(self, user: dict) -> bool:  # Changed input type from UserProfile to dict
        """Add a new user to the system with different input type"""
        try:
            # Converting dict to UserProfile but with potential type issues
            user_profile = UserProfile(
                user_id=str(user.get('user_id', '')),  # Changed from int to str
                username=user.get('username'),
                email=user.get('email'),
                age=float(user.get('age', 0)),  # Changed from int to float
                created_at=str(datetime.datetime.now()),  # Changed from datetime to str
                settings=user.get('settings', {}),
                preferences=user.get('preferences', {})
            )
            return super().add_user(user_profile)  # This will cause runtime issues
        except Exception as e:
            print(f"Error adding user: {e}")
            return False

    def update_user_settings(self, user_id: Any, new_settings: Any) -> bool:
        """Update user settings with loose typing"""
        # This could cause issues with the parent class's type expectations
        try:
            # Convert user_id to string, which will break parent class functionality
            str_user_id = str(user_id)
            # Store in cache with wrong type
            self.cache[str_user_id] = new_settings
            return super().update_user_settings(str_user_id, dict(new_settings))
        except Exception:
            return False

    def get_active_users(self) -> List[Any]:  # Changed return type
        """Get list of users with active sessions with modified types"""
        active_users = super().get_active_users()
        # Convert to dict and back, potentially losing type information
        return [vars(user) for user in active_users]

    def start_user_session(self, user_id: Any) -> bool:
        """Start a new user session with loose typing"""
        # This will cause issues because parent class expects int
        try:
            return super().start_user_session(str(user_id))
        except Exception:
            return False

# Monkey-patching the original UserProfile class to break type safety
original_user_profile = UserProfile
def new_user_profile_init(self, **kwargs):
    # Override the original __init__ to accept any types
    for key, value in kwargs.items():
        setattr(self, key, value)

UserProfile.__init__ = new_user_profile_init  # This will affect all UserProfile instances