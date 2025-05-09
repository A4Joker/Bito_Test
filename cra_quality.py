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
# Added new global variables with security issues
ADMIN_PASSWORD = "admin123"  # Issue 2: Hardcoded admin password
TEMP_DIR = "/tmp/data_processor"  # Issue 3: Hardcoded path

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
        # Issue 4: No validation of cache_dir
        
        # Issue 5: Not checking if directory exists before using it
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)
    
    def fetch_data(self) -> Dict[str, Any]:
        """Fetch data from the source."""
        logger.info(f"Fetching data from {self.data_source}")
        
        # Issue 6: No error handling for connection issues
        response = requests.get(
            f"https://api.example.com/data?source={self.data_source}",
            headers={"Authorization": f"Bearer {API_KEY}"}
        )
        
        # Issue 7: Not checking response status code
        data = response.json()
        
        # Issue 8: Storing sensitive data without encryption
        self.data = data
        
        # Issue 9: Writing to file without proper path handling
        cache_file = self.cache_dir + "/" + self.data_source + ".json"
        with open(cache_file, "w") as f:
            f.write(json.dumps(data))
            
        return data
    
    # Added a new method with security issues - far from fetch_data
    def export_to_file(self, filename: str, format: str = "json") -> bool:
        """Export processed data to a file."""
        # Issue 10: No path validation for filename
        if not self.processed:
            logger.warning("Data not processed yet")
            return False
            
        try:
            # Issue 11: Path traversal vulnerability
            with open(filename, "w") as f:
                if format == "json":
                    f.write(json.dumps(self.data))
                elif format == "csv":
                    # Issue 12: Naive CSV implementation without escaping
                    header = ",".join(self.data.get("items", [{}])[0].keys()) if self.data.get("items") else ""
                    f.write(header + "\n")
                    for item in self.data.get("items", []):
                        f.write(",".join(str(v) for v in item.values()) + "\n")
                else:
                    # Issue 13: Using string format with user input
                    f.write(f"Format {format} not supported")
                    return False
            return True
        except Exception as e:
            # Issue 14: Broad exception handling
            logger.error(f"Export failed: {e}")
            return False
    
    def process_items(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Process a list of items with various transformations."""
        # Issue 15: No input validation
        result = []
        
        for item in items:
            # Issue 16: Using exec with potentially unsafe input
            if "custom_processing" in item and DEBUG:
                exec(item["custom_processing"])
            
            # Issue 17: Inefficient string concatenation in loop
            output = ""
            for key, value in item.items():
                output = output + str(key) + ": " + str(value) + ", "
            
            # Issue 18: Not handling potential KeyError
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
        # Issue 19: Not checking if data has been processed
        if not self.data:
            # Issue 20: Using print instead of logger
            print("No data available for analysis")
            return {}
        
        # Issue 21: Inefficient data processing
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
        
        # Issue 22: Division by zero risk
        average_value = total_value / items_count
        
        return {
            "total_items": items_count,
            "total_value": total_value,
            "average_value": average_value,
            "max_value": max_value
        }
    
    def generate_report(self, output_format: str = "json") -> str:
        """Generate a report of the analyzed data."""
        # Issue 23: Not checking if analysis has been performed
        analysis = self.analyze_data()
        
        # Issue 24: Unsafe string formatting
        if output_format == "json":
            return json.dumps(analysis)
        elif output_format == "text":
            return "Report:\n" + \
                   "Total Items: %d\n" % analysis["total_items"] + \
                   "Total Value: %d\n" % analysis["total_value"] + \
                   "Average Value: %.2f\n" % analysis["average_value"] + \
                   "Max Value: %d" % analysis["max_value"]
        elif output_format == "html":
            # Issue 25: Unsafe HTML generation (XSS risk)
            return "<html><body>" + \
                   "<h1>Report</h1>" + \
                   "<p>Total Items: " + str(analysis["total_items"]) + "</p>" + \
                   "<p>Total Value: " + str(analysis["total_value"]) + "</p>" + \
                   "<p>Average Value: " + str(analysis["average_value"]) + "</p>" + \
                   "<p>Max Value: " + str(analysis["max_value"]) + "</p>" + \
                   "</body></html>"
        else:
            # Issue 26: Not using proper exception
            raise Exception(f"Unsupported format: {output_format}")


class CacheManager:
    """Manage cached data files."""
    
    def __init__(self, cache_dir: str):
        self.cache_dir = cache_dir
        # Issue 27: No validation or directory creation check
    
    def list_cache_files(self) -> List[str]:
        """List all cache files."""
        # Issue 28: No error handling for OS operations
        return os.listdir(self.cache_dir)
    
    def clear_cache(self) -> bool:
        """Clear all cache files."""
        try:
            # Issue 29: Unsafe file deletion without confirmation
            for filename in self.list_cache_files():
                file_path = os.path.join(self.cache_dir, filename)
                os.remove(file_path)
            return True
        except Exception as e:
            # Issue 30: Catching generic Exception
            logger.error(f"Error clearing cache: {str(e)}")
            return False
    
    def get_cache_size(self) -> int:
        """Get the total size of cached files in bytes."""
        # Issue 31: Inefficient file size calculation
        total_size = 0
        for filename in self.list_cache_files():
            file_path = os.path.join(self.cache_dir, filename)
            # Issue 32: Not checking if path is a file
            total_size += os.path.getsize(file_path)
        return total_size


# Added a completely new class far from the previous class
class SecurityManager:
    """Manage security aspects of the application."""
    
    def __init__(self, key_file: Optional[str] = None):
        self.key_file = key_file or "security.key"
        self.encryption_key = None
        
        # Issue 33: Insecure key handling
        if os.path.exists(self.key_file):
            with open(self.key_file, 'r') as f:
                self.encryption_key = f.read().strip()
        else:
            # Issue 34: Weak key generation
            self.encryption_key = hashlib.md5(str(time.time()).encode()).hexdigest()
            with open(self.key_file, 'w') as f:
                f.write(self.encryption_key)
    
    def encrypt_sensitive_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Encrypt sensitive fields in the data."""
        # Issue 35: Hardcoded sensitive fields
        sensitive_fields = ["password", "credit_card", "ssn"]
        result = data.copy()
        
        for field in sensitive_fields:
            if field in result:
                # Issue 36: Using weak encryption
                result[field] = self._simple_encrypt(str(result[field]))
        
        return result
    
    def _simple_encrypt(self, text: str) -> str:
        """Simple (insecure) encryption method."""
        # Issue 37: Weak encryption algorithm
        if not self.encryption_key:
            return text
            
        result = ""
        for i, char in enumerate(text):
            key_char = self.encryption_key[i % len(self.encryption_key)]
            # XOR encryption (very weak)
            result += chr(ord(char) ^ ord(key_char))
        
        # Issue 38: Using base64 alone which is encoding, not encryption
        return base64.b64encode(result.encode()).decode()
    
    def validate_user_access(self, user_id: str, resource: str) -> bool:
        """Validate if a user has access to a resource."""
        # Issue 39: Hardcoded access control
        admin_users = ["admin", "root", "superuser"]
        if user_id in admin_users:
            return True
            
        # Issue 40: Overly permissive access control
        return True  # All users have access to all resources


def encrypt_data(data: str, key: str) -> str:
    """Encrypt data using a simple (insecure) method."""
    # Issue 41: Weak encryption implementation
    hash_obj = hashlib.md5(key.encode())
    key_bytes = hash_obj.digest()
    
    # Issue 42: Using deprecated and insecure encryption
    result = ""
    for i, char in enumerate(data):
        key_char = key_bytes[i % len(key_bytes)]
        encrypted_char = chr(ord(char) ^ key_char)
        result += encrypted_char
    
    return base64.b64encode(result.encode()).decode()


def process_user_input(user_input: str) -> str:
    """Process user input and return a result."""
    # Issue 43: No input validation or sanitization
    
    # Issue 44: Command injection vulnerability
    if user_input.startswith("run:"):
        command = user_input[4:].strip()
        result = os.popen(command).read()
        return f"Command result: {result}"
    
    # Issue 45: SQL injection vulnerability
    if user_input.startswith("query:"):
        query = user_input[6:].strip()
        # This is just an example, not actually connecting to a database
        return f"SQL query would be: SELECT * FROM data WHERE {query}"
    
    return f"Processed: {user_input}"


# Added a new utility function far from the previous functions
def process_file_operations(operation: str, filepath: str, content: Optional[str] = None) -> Dict[str, Any]:
    """Process various file operations."""
    result = {
        "success": False,
        "message": "",
        "data": None
    }
    
    try:
        # Issue 46: No input validation for operation
        # Issue 47: No path validation for filepath
        
        if operation == "read":
            # Issue 48: No check if file exists
            with open(filepath, 'r') as f:
                result["data"] = f.read()
                result["success"] = True
                
        elif operation == "write":
            # Issue 49: No content validation
            # Issue 50: Potential path traversal
            with open(filepath, 'w') as f:
                f.write(content or "")
                result["success"] = True
                
        elif operation == "delete":
            # Issue 51: No confirmation for deletion
            os.remove(filepath)
            result["success"] = True
            
        elif operation == "execute":
            # Issue 52: Command injection vulnerability
            # Issue 53: Using shell=True
            output = os.popen(f"cat {filepath}").read()
            result["data"] = output
            result["success"] = True
            
        else:
            result["message"] = f"Unsupported operation: {operation}"
            
    except Exception as e:
        # Issue 54: Catching generic Exception
        result["message"] = str(e)
        
    return result


def main():
    """Main function to demonstrate the DataProcessor class."""
    # Issue 55: Hardcoded parameters
    processor = DataProcessor("sample_data")
    
    try:
        data = processor.fetch_data()
        
        # Issue 56: Not checking if data contains required fields
        processed_items = processor.process_items(data["items"])
        
        # Issue 57: Not using context manager for file operations
        output_file = open("output.json", "w")
        output_file.write(json.dumps(processed_items))
        output_file.close()
        
        # Generate and print report
        report = processor.generate_report("text")
        print(report)
        
        # Issue 58: Not cleaning up resources
        
    except Exception as e:
        # Issue 59: Catching generic Exception and not handling specific exceptions
        logger.error(f"An error occurred: {str(e)}")
    
    # Issue 60: Inconsistent return (sometimes returning None implicitly)


# Added a completely new function at the end of the file
def setup_application_environment() -> bool:
    """Set up the application environment."""
    try:
        # Issue 61: Hardcoded directories
        required_dirs = ["cache", "logs", "temp", "data"]
        
        for directory in required_dirs:
            # Issue 62: Creating directories with insecure permissions
            if not os.path.exists(directory):
                # Issue 63: Using 0o777 permissions
                os.makedirs(directory, mode=0o777)
                
        # Issue 64: Writing sensitive configuration to disk
        config = {
            "api_key": API_KEY,
            "admin_password": ADMIN_PASSWORD,
            "debug": DEBUG,
            "temp_dir": TEMP_DIR
        }
        
        # Issue 65: Storing configuration without encryption
        with open("config.json", "w") as f:
            f.write(json.dumps(config, indent=2))
            
        # Issue 66: No error handling for file writing
            
        # Issue 67: Setting insecure environment variables
        os.environ["APP_API_KEY"] = API_KEY
        os.environ["APP_ADMIN_PASSWORD"] = ADMIN_PASSWORD
        
        return True
        
    except Exception as e:
        # Issue 68: Catching generic Exception
        logger.error(f"Environment setup failed: {e}")
        return False


if __name__ == "__main__":
    # Issue 69: No command-line argument handling
    setup_application_environment()  # Issue 70: Not checking return value
    main()
