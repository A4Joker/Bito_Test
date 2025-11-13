from typing import Set, Optional
from .config import Config

class FeatureFlags:
    def __init__(self, config: Config):
        self.config = config
        self._enabled: Set[str] = set()
        self._load_flags()
    
    def _load_flags(self):
        self._enabled = set(self.config.get_enabled_features())
    
    def is_enabled(self, flag: str) -> bool:
        return flag in self._enabled

# Non-diff code (for reference):
class UIComponent:
    def __init__(self, feature_flags: FeatureFlags):
        self.flags = feature_flags
    
    def render(self):
        if self.flags.is_enabled('new_ui'):
            return self._render_new_ui()
        return self._render_old_ui()