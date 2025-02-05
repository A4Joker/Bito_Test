from decouple import config

class DatabaseConfig:
    HOST = config('DB_HOST', default='localhost')
    PORT = config('DB_PORT', default=5432, cast=int)
    USERNAME = config('DB_USERNAME')
    PASSWORD = config('DB_PASSWORD')
    
    def get_connection_string(self):
        return f"postgresql://{self.USERNAME}:{self.PASSWORD}@{self.HOST}:{self.PORT}/mydb"

# Usage examples showing context
def get_connection():
    config = DatabaseConfig()
    return config.get_connection_string()

def create_pool():
    config = DatabaseConfig()
    return {
        'host': config.HOST,
        'port': config.PORT,
        'user': config.USERNAME,
        'password': config.PASSWORD
    }