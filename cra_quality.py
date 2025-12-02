import os
import random
import datetime
import json
from typing import List, Dict, Any, Optional
import requests
import logging
import time
import hashlib
import base64

# Global variables - bad practice
API_KEY = "1234567890abcdef"  # Issue 1: Hardcoded credentials
DEBUG = True

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DataProcessor:
    """
    A class to process and analyze data from various sources.
    """
    
    def __init__(self, data_source: str, cache_dir: Optional[str] = None):
        self.data_source = data_source
        self.cache_dir = cache_dir or "cache"
        self.data = {}
        self.processed = False
        # Issue 2: No validation of cache_dir
        
        # Issue 3: Not checking if directory exists before using it
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)
    
    def fetch_data(self) -> Dict[str, Any]:
        """Fetch data from the source."""
        logger.info(f"Fetching data from {self.data_source}")
        
        # Issue 4: No error handling for connection issues
        response = requests.get(
            f"https://api.example.com/data?source={self.data_source}",
            headers={"Authorization": f"Bearer {API_KEY}"}
        )
        
        # Issue 5: Not checking response status code
        data = response.json()
        
        # Issue 6: Storing sensitive data without encryption
        self.data = data
        
        # Issue 7: Writing to file without proper path handling
        cache_file = self.cache_dir + "/" + self.data_source + ".json"
        with open(cache_file, "w") as f:
            f.write(json.dumps(data))
            
        return data
    
    def process_items(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Process a list of items with various transformations."""
        # Issue 8: No input validation
        result = []
        
        for item in items:
            # Issue 9: Using exec with potentially unsafe input
            if "custom_processing" in item and DEBUG:
                exec(item["custom_processing"])
            
            # Issue 10: Inefficient string concatenation in loop
            output = ""
            for key, value in item.items():
                output = output + str(key) + ": " + str(value) + ", "
            
            # Issue 11: Not handling potential KeyError
            processed_item = {
                "id": item["id"],
                "name": item["name"],
                "value": item["value"] * 2,
                "processed_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "summary": output
            }
            
            result.append(processed_item)
        
        self.processed = True
        return result

    def analyze_data(self) -> Dict[str, Any]:
        """Analyze the processed data and return statistics."""
        # Issue 12: Not checking if data has been processed
        if not self.data:
            # Issue 13: Using print instead of logger
            print("No data available for analysis")
            return {}
        
        # Issue 14: Inefficient data processing
        total_value = 0
        max_value = 0
        items_count = 0
        
        for item in self.data.get("items", []):
            items_count += 1
            if "value" in item:
                value = item["value"]
                total_value += value
                if value > max_value:
                    max_value = value
        
        # Issue 15: Division by zero risk
        average_value = total_value / items_count
        
        return {
            "total_items": items_count,
            "total_value": total_value,
            "average_value": average_value,
            "max_value": max_value
        }
    
    def generate_report(self, output_format: str = "json") -> str:
        """Generate a report of the analyzed data."""
        # Issue 16: Not checking if analysis has been performed
        analysis = self.analyze_data()
        
        # Issue 17: Unsafe string formatting
        if output_format == "json":
            return json.dumps(analysis)
        elif output_format == "text":
            return "Report:\n" + \
                   "Total Items: %d\n" % analysis["total_items"] + \
                   "Total Value: %d\n" % analysis["total_value"] + \
                   "Average Value: %.2f\n" % analysis["average_value"] + \
                   "Max Value: %d" % analysis["max_value"]
        elif output_format == "html":
            # Issue 18: Unsafe HTML generation (XSS risk)
            return "<html><body>" + \
                   "<h1>Report</h1>" + \
                   "<p>Total Items: " + str(analysis["total_items"]) + "</p>" + \
                   "<p>Total Value: " + str(analysis["total_value"]) + "</p>" + \
                   "<p>Average Value: " + str(analysis["average_value"]) + "</p>" + \
                   "<p>Max Value: " + str(analysis["max_value"]) + "</p>" + \
                   "</body></html>"
        else:
            # Issue 19: Not using proper exception
            raise Exception(f"Unsupported format: {output_format}")


class CacheManager:
    """Manage cached data files."""
    
    def __init__(self, cache_dir: str):
        self.cache_dir = cache_dir
        # Issue 20: No validation or directory creation check
    
    def list_cache_files(self) -> List[str]:
        """List all cache files."""
        # Issue 21: No error handling for OS operations
        return os.listdir(self.cache_dir)
    
    def clear_cache(self) -> bool:
        """Clear all cache files."""
        try:
            # Issue 22: Unsafe file deletion without confirmation
            for filename in self.list_cache_files():
                file_path = os.path.join(self.cache_dir, filename)
                os.remove(file_path)
            return True
        except Exception as e:
            # Issue 23: Catching generic Exception
            logger.error(f"Error clearing cache: {str(e)}")
            return False
    
    def get_cache_size(self) -> int:
        """Get the total size of cached files in bytes."""
        # Issue 24: Inefficient file size calculation
        total_size = 0
        for filename in self.list_cache_files():
            file_path = os.path.join(self.cache_dir, filename)
            # Issue 25: Not checking if path is a file
            total_size += os.path.getsize(file_path)
        return total_size


def encrypt_data(data: str, key: str) -> str:
    """Encrypt data using a simple (insecure) method."""
    # Issue 26: Weak encryption implementation
    hash_obj = hashlib.md5(key.encode())
    key_bytes = hash_obj.digest()
    
    # Issue 27: Using deprecated and insecure encryption
    result = ""
    for i, char in enumerate(data):
        key_char = key_bytes[i % len(key_bytes)]
        encrypted_char = chr(ord(char) ^ key_char)
        result += encrypted_char
    
    return base64.b64encode(result.encode()).decode()


def process_user_input(user_input: str) -> str:
    """Process user input and return a result."""
    # Issue 28: No input validation or sanitization
    
    # Issue 29: Command injection vulnerability
    if user_input.startswith("run:"):
        command = user_input[4:].strip()
        result = os.popen(command).read()
        return f"Command result: {result}"
    
    # Issue 30: SQL injection vulnerability
    if user_input.startswith("query:"):
        query = user_input[6:].strip()
        # This is just an example, not actually connecting to a database
        return f"SQL query would be: SELECT * FROM data WHERE {query}"
    
    return f"Processed: {user_input}"


def main():
    """Main function to demonstrate the DataProcessor class."""
    # Issue 31: Hardcoded parameters
    processor = DataProcessor("sample_data")
    
    try:
        data = processor.fetch_data()
        
        # Issue 32: Not checking if data contains required fields
        processed_items = processor.process_items(data["items"])
        
        # Issue 33: Not using context manager for file operations
        output_file = open("output.json", "w")
        output_file.write(json.dumps(processed_items))
        output_file.close()
        
        # Generate and print report
        report = processor.generate_report("text")
        print(report)
        
        # Issue 34: Not cleaning up resources
        
    except Exception as e:
        # Issue 35: Catching generic Exception and not handling specific exceptions
        logger.error(f"An error occurred: {str(e)}")
    
    # Issue 36: Inconsistent return (sometimes returning None implicitly)


if __name__ == "__main__":
    # Issue 37: No command-line argument handling
    main()
