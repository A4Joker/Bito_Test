from typing import List, Dict, Any

class DataProcessor:
    def __init__(self):
        self.data: List[Dict[str, Any]] = []
        self.processed_count: int = 0
        self.error_count: int = 0
        
    def add_data(self, item: Dict[str, Any]) -> bool:
        """Add a new data item to the processor.
        
        Args:
            item: Dictionary containing data to process
            
        Returns:
            bool: True if data was added successfully
        """
        try:
            self.data.append(item)
            self.processed_count += 1
            return True
        except Exception:
            self.error_count += 1
            return False
            
    def get_statistics(self) -> Dict[str, int]:
        """Get processing statistics.
        
        Returns:
            Dict containing processed and error counts
        """
        return {
            "processed": self.processed_count,
            "errors": self.error_count,
            "total_items": len(self.data)
        }
        
    def process_batch(self, items: List[Dict[str, Any]]) -> Dict[str, int]:
        """Process a batch of items.
        
        Args:
            items: List of dictionaries to process
            
        Returns:
            Dict containing processing statistics
        """
        for item in items:
            self.add_data(item)
        return self.get_statistics()