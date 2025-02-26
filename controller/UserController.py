# controller/UserController.py
from model.UserRepository import UserRepository
from service.UserService import UserService
from util.Logger import Logger

class UserController:
    def __init__(self):
        self._user_repository = UserRepository()
        self._user_service = UserService()
    
    def process_user(self):
        user = self._user_repository.get_user()
        self._user_service.print_user_info(user)
        Logger.log("User processed successfully!")
    
    def say_hello(self, name: str) -> str:
        return f"Hello, {name} from Python!"
