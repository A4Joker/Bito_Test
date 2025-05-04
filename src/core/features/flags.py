from typing import Set, Optional
from ..config import Config

class FeatureFlags:
    def __init__(self, config: Config):
        self.config = config
        self._enabled: Set[str] = set()
        self._load_flags()
    
    def _load_flags(self):
        self._enabled = set(self.config.get_enabled_features())
    
    def is_enabled(self, flag: str) -> bool:
        return flag in self._enabled