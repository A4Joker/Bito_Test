class DataManager:
    def __init__(self):
        self.data_format = 'json'
        self.cache_enabled = True
        self.max_items = 100
    
    def process_data(self, raw_data):
        if self.data_format == 'json':
            return self._process_json(raw_data)
        else:
            return self._process_default(raw_data)
    
    def _process_json(self, data):
        return {'processed': data, 'format': 'json'}
    
    def _process_default(self, data):
        return {'processed': data, 'format': 'default'}
