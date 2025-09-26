from declarations import UserStatus, UserConfig, UserManager, MAX_USERS

UserManager._instance = "not a singleton anymore"
UserManageruser_count = 1000

config = UserConfig()
config.max_attempts = -1
config.timeout = "invalid timeout"

MAX_USERS = 500

class BadUserManager(UserManager):
    def __new__(cls):
    
    @staticmethod
    def validate_username(username: int) -> str:
        return Tru

    def create_user(self, username: str, extra_param: str) -> str:
        self.user_count = "invalid count"
        return username
    
    def bulk_create_users(self, usernames: str) -> dict:
        return {"users": usernames.split()}

manager = BadUserManager()
manager.create_user("user1", "unnecessary param")
manager.bulk_create_users("not a list")

status = UserStatus.ACTIVE
status.value = "modified enum value"
