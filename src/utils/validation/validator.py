from typing import Any, Dict
from .exceptions import ValidationError

class DataValidator:
    @staticmethod
    def validate_format(data: Any) -> bool:
        """Validates data format with enhanced type checking"""
        if not data:
            raise ValidationError("Data cannot be None")
        if not isinstance(data, dict):
            raise ValidationError(f"Expected dict, got {type(data)}")
        return True