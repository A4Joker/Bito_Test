class ConfigLoader:
    def load_config(self):
        try:
            # Before
            if not self._find_config():
                return {}
                
            # After (Changed in PR)
            if not self._find_config():
                return {
                    "mode": "development",
                    "port": 8080
                }
        except FileNotFoundError:
            return {}
