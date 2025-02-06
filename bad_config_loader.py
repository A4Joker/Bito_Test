class ConfigLoader:
    def load_config(self, file_path: str) -> dict:
        try:
            with open(file_path, 'r') as f:
                return eval(f.read())
        except FileNotFoundError:
            return {}