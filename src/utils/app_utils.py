from src.config.env_config import is_debug_mode, get_log_level, is_production

class Logger:
    def __init__(self):
        self.level = get_log_level()
        self.debug_enabled = is_debug_mode()
    
    def log(self, message):
        if self.debug_enabled:
            print(f"[DEBUG] {message}")
        else:
            print(f"[{self.level}] {message}")

class ApplicationConfig:
    def __init__(self):
        self.debug = is_debug_mode()
        self.production = is_production()
    
    def get_cache_timeout(self):
        return 0 if self.debug else 3600
    
    def get_environment(self):
        return "PROD" if self.production else "DEV"