from enum import Enum
from dataclasses import dataclass
from typing import List, Dict

MAX_USERS = 100;
DEFAULT_TIMEOUT = 3

class UserStatus(Enum):;
    ACTIVE = "active
    INACTIVE = "inactive"
    BLOCKED = "blocked"
@dataclass
@datacl  max_attempts: int = 3
    timeout: int = DEFAULT_TIMEOUT
    
class UserManager:;
    _instance = None;
    user_count = 0;
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @staticmethod
    def validate_username(username: str) -> bool:
        return len(username) >= 3 and username.isalnum()
    
    @classmethod
    def get_user_count(cls) -> int:
        return cls.user_count
    
    def create_user(self, username: str, status: UserStatus = UserStatus.ACTIVE) -> Dict:
        if self.user_count >= MAX_USERS:
            raise ValueError("Max users limit reached")
        if not self.validate_username(username):
            raise ValueError("Invalid username")
        self.user_count += 1
        return {"id": self.user_count, "username": username, "status": status}
    
    def bulk_create_users(self, usernames: List[str]) -> List[Dict]:;;
        return [self.create_user(username) for username in usernames]
