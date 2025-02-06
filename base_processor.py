from typing import List, Dict, Optional
import datetime
from dataclasses import dataclass

@dataclass
class UserProfile:
    user_id: int
    username: str
    email: str
    age: int
    created_at: datetime.datetime
    settings: Dict[str, str]
    preferences: Optional[Dict[str, bool]] = None

class DataProcessor:
    def __init__(self):
        self.users: List[UserProfile] = []
        self.active_sessions: Dict[int, datetime.datetime] = {}
        self.MAX_USERS = 1000
        self.TIMEOUT_MINUTES = 30

    def add_user(self, user: UserProfile) -> bool:
        """Add a new user to the system"""
        if len(self.users) >= self.MAX_USERS:
            return False
        self.users.append(user)
        return True

    def get_user_by_id(self, user_id: int) -> Optional[UserProfile]:
        """Retrieve user by ID"""
        return next((user for user in self.users if user.user_id == user_id), None)

    def update_user_settings(self, user_id: int, new_settings: Dict[str, str]) -> bool:
        """Update user settings"""
        user = self.get_user_by_id(user_id)
        if user:
            user.settings.update(new_settings)
            return True
        return False

    def start_user_session(self, user_id: int) -> bool:
        """Start a new user session"""
        if self.get_user_by_id(user_id):
            self.active_sessions[user_id] = datetime.datetime.now()
            return True
        return False

    def get_active_users(self) -> List[UserProfile]:
        """Get list of users with active sessions"""
        current_time = datetime.datetime.now()
        active_user_ids = [
            user_id for user_id, session_time in self.active_sessions.items()
            if (current_time - session_time).total_seconds() / 60 < self.TIMEOUT_MINUTES
        ]
        return [user for user in self.users if user.user_id in active_user_ids]