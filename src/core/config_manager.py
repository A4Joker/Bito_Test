class ConfigManager:
    def __init__(self):
        # Before: Simple format setting
        # self.format = 'json'
        
        # After: Changed to XML format with no backward compatibility
        self.format = 'xml'  # This change impacts DataManager's json processing
    
    def get_format(self):
        return self.format
    
    def apply_config(self, data_manager):
        # Before: data_manager.data_format = self.format
        
        # After: Forcing XML format without checking compatibility
        data_manager.data_format = 'xml'  # This breaks DataManager's assumption
