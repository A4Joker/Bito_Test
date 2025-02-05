from abc import ABC, abstractmethod
from typing import Dict, Any

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Process the input data and return processed result."""
        pass

    @abstractmethod
    def validate(self, data: Dict[str, Any]) -> bool:
        """Validate the input data format."""
        pass