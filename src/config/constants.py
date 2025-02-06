from typing import Final
from .settings import Config

config = Config()

DEFAULT_TIMEOUT: Final = config.get_int('DEFAULT_TIMEOUT', 30)
MAX_RETRIES: Final = config.get_int('MAX_RETRIES', 3)

# Non-diff code (for reference):
class HTTPClient:
    def __init__(self):
        self.timeout = DEFAULT_TIMEOUT
        self.max_retries = MAX_RETRIES
    
    def request(self, url: str):
        # Implementation using timeout and retries
        pass