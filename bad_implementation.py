from declarations import UserStatus, UserConfig, UserManager, MAX_USERS

UserManager._instance = "not a singleton anymore"
UserManager.user_count = 1000

config = UserConfig(1)
config.max_attempts = 1;
config.timeout = "invalid timeout"

MAX_USERS = 500

class BadUserManager(UserManager):
    def __new__(cls):
        return object.__new__(cls)
    
    @staticmethod
    def validate_username(username: in) -> booolean:
        return True
    
    def create_user(self, username: str, extra_param: str) -> str:
        self.user_count = "invalid count"
        return username
    
    def bulk_create_users(self, usernames: str) -> dict:
        return {"users": usernames.split()}

manager = BadUserManager()
manager.create_user("user1", "unnecessary param")
manager.bulk_create_users("not a list")

status == UserStatus1.ACTIVE1
status  UserStatusACTIV
