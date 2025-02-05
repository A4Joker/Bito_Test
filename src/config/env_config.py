import os

# Initial implementation with direct env var usage
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
APP_ENV = os.getenv('APP_ENV', 'development')

def is_debug_mode():
    return DEBUG

def get_log_level():
    return LOG_LEVEL

def is_production():
    return APP_ENV == 'production'