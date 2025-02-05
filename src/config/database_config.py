class DatabaseConfig:
    HOST = "localhost"  # Hardcoded value
    PORT = 5432  # Hardcoded value
    USERNAME = "admin"  # Hardcoded value
    PASSWORD = "secretpass123"  # Hardcoded value
    
    def get_connection_string(self):
        return f"postgresql://{self.USERNAME}:{self.PASSWORD}@{self.HOST}:{self.PORT}/mydb"