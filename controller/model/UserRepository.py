# model/UserRepository.py
from typing import Dict

class UserRepository:
    def __init__(self):
        self._user = {"name": "Alice", "age": 30}
        
    def get_user(self) -> Dict:
        return self._user
