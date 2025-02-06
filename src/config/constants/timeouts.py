from typing import Final
from ..settings import Config

config = Config()

DEFAULT_TIMEOUT: Final = config.get_int('DEFAULT_TIMEOUT', 30)
MAX_RETRIES: Final = config.get_int('MAX_RETRIES', 3)