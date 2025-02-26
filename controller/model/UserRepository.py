# model/UserRepository.py
from typing import Dict

class UserRepository:
    def get_user(self) -> Dict:
        return {"name": "Alice", "age": 30}
