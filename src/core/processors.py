from src.core.data_processor import DataProcessor
from typing import Dict, Any
import json

class JsonProcessor(DataProcessor):
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        return json.loads(json.dumps(data))
    
    def validate(self, data: Dict[str, Any]) -> bool:
        try:
            json.dumps(data)
            return True
        except (TypeError, ValueError):
            return False

class XmlProcessor(DataProcessor):
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        # Simple XML-like processing
        processed = {}
        for key, value in data.items():
            processed[f"<{key}>{value}</{key}>"] = value
        return processed
    
    def validate(self, data: Dict[str, Any]) -> bool:
        return all(isinstance(k, str) and isinstance(v, (str, int, float, bool))
                  for k, v in data.items())