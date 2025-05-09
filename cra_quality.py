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
            
        # Added insecure initialization
        self.session_id = hashlib.md5(str(time.time()).encode()).hexdigest()  # Issue 6: Using MD5 for session ID
    
    def fetch_data(self) -> Dict[str, Any]:
        """Fetch data from the source."""
        logger.info(f"Fetching data from {self.data_source}")
        
        # Issue 7: No error handling for connection issues
        response = requests.get(
            f"https://api.example.com/data?source={self.data_source}",
            headers={"Authorization": f"Bearer {API_KEY}"}
        )
        
        # Issue 8: Not checking response status code
        data = response.json()
        
        # Issue 9: Storing sensitive data without encryption
        self.data = data
        
        # Issue 10: Writing to file without proper path handling
        cache_file = self.cache_dir + "/" + self.data_source + ".json"
        with open(cache_file, "w") as f:
            f.write(json.dumps(data))
            
        return data
    
    def process_items(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Process a list of items with various transformations."""
        # Issue 11: No input validation
        result = []
        
        for item in items:
            # Issue 12: Using exec with potentially unsafe input
            if "custom_processing" in item and DEBUG:
                exec(item["custom_processing"])
            
            # Issue 13: Inefficient string concatenation in loop
            output = ""
            for key, value in item.items():
                output = output + str(key) + ": " + str(value) + ", "
            
            # Issue 14: Not handling potential KeyError
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
    
    # Added a new method with security issues
    def export_to_file(self, filename: str, format: str = "json") -> bool:
        """Export processed data to a file."""
        # Issue 15: No path validation for filename
        if not self.processed:
            logger.warning("Data not processed yet")
            return False
            
        try:
            # Issue 16: Path traversal vulnerability
            with open(filename, "w") as f:
                if format == "json":
                    f.write(json.dumps(self.data))
                elif format == "csv":
                    # Issue 17: Naive CSV implementation without escaping
                    header = ",".join(self.data.get("items", [{}])[0].keys()) if self.data.get("items") else ""
                    f.write(header + "\n")
                    for item in self.data.get("items", []):
                        f.write(",".join(str(v) for v in item.values()) + "\n")
                else:
                    # Issue 18: Using string format with user input
                    f.write(f"Format {format} not supported")
                    return False
            return True
        except Exception as e:
            # Issue 19: Broad exception handling
            logger.error(f"Export failed: {e}")
            return False

    def analyze_data(self) -> Dict[str, Any]:
        """Analyze the processed data and return statistics."""
        # Issue 20: Not checking if data has been processed
        if not self.data:
            # Issue 21: Using print instead of logger
            print("No data available for analysis")
            return {}
        
        # Issue 22: Inefficient data processing
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
        
        # Issue 23: Division by zero risk
        average_value = total_value / items_count if items_count > 0 else 0
        
        return {
            "total_items": items_count,
            "total_value": total_value,
            "average_value": average_value,
            "max_value": max_value
        }
    
    def generate_report(self, output_format: str = "json") -> str:
        """Generate a report of the analyzed data."""
        # Issue 24: Not checking if analysis has been performed
        analysis = self.analyze_data()
        
        # Issue 25: Unsafe string formatting
        if output_format == "json":
            return json.dumps(analysis)
        elif output_format == "text":
            return "Report:\n" + \
                   "Total Items: %d\n" % analysis["total_items"] + \
                   "Total Value: %d\n" % analysis["total_value"] + \
                   "Average Value: %.2f\n" % analysis["average_value"] + \
                   "Max Value: %d" % analysis["max_value"]
        elif output_format == "html":
            # Issue 26: Unsafe HTML generation (XSS risk)
            return "<html><body>" + \
                   "<h1>Report</h1>" + \
                   "<p>Total Items: " + str(analysis["total_items"]) + "</p>" + \
                   "<p>Total Value: " + str(analysis["total_value"]) + "</p>" + \
                   "<p>Average Value: " + str(analysis["average_value"]) + "</p>" + \
                   "<p>Max Value: " + str(analysis["max_value"]) + "</p>" + \
                   "</body></html>"
        else:
            # Issue 27: Not using proper exception
            raise Exception(f"Unsupported format: {output_format}")
    
    # Added a new method with authentication issues
    def authenticate_admin(self, password: str) -> bool:
        """Authenticate as admin to perform privileged operations."""
        # Issue 28: Hardcoded password comparison
        if password == ADMIN_PASSWORD:
            logger.info("Admin authenticated successfully")
            return True
        else:
            # Issue 29: Information disclosure in error message
            logger.warning(f"Admin authentication failed with password: {password}")
            return False


class CacheManager:
    """Manage cached data files."""
    
    def __init__(self, cache_dir: str):
        self.cache_dir = cache_dir
        # Issue 30: No validation or directory creation check
    
    def list_cache_files(self) -> List[str]:
        """List all cache files."""
        # Issue 31: No error handling for OS operations
        return os.listdir(self.cache_dir)
    
    def clear_cache(self) -> bool:
        """Clear all cache files."""
        try:
            # Issue 32: Unsafe file deletion without confirmation
            for filename in self.list_cache_files():
                file_path = os.path.join(self.cache_dir, filename)
                os.remove(file_path)
            return True
        except Exception as e:
            # Issue 33: Catching generic Exception
            logger.error(f"Error clearing cache: {str(e)}")
            return False
    
    # Added a new method with security issues
    def import_from_url(self, url: str, filename: str) -> bool:
        """Import a file from URL into the cache directory."""
        try:
            # Issue 34: No URL validation
            response = requests.get(url, stream=True)
            
            # Issue 35: No content type or size validation
            # Issue 36: Path traversal in filename
            file_path = os.path.join(self.cache_dir, filename)
            
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            return True
        except Exception as e:
            # Issue 37: Broad exception catching
            logger.error(f"Import failed: {e}")
            return False
    
    def get_cache_size(self) -> int:
        """Get the total size of cached files in bytes."""
        # Issue 38: Inefficient file size calculation
        total_size = 0
        for filename in self.list_cache_files():
            file_path = os.path.join(self.cache_dir, filename)
            # Issue 39: Not checking if path is a file
            total_size += os.path.getsize(file_path)
        return total_size
    
    # Added a new method with security issues
    def execute_on_cache(self, command: str) -> str:
        """Execute a command on each cache file and return results."""
        # Issue 40: Command injection vulnerability
        results = []
        for filename in self.list_cache_files():
            file_path = os.path.join(self.cache_dir, filename)
            if os.path.isfile(file_path):
                # Issue 41: Using shell=True with user input
                result = os.popen(f"{command} {file_path}").read()
                results.append(f"{filename}: {result}")
        
        return "\n".join(results)


class DatabaseManager:
    """Manager for database operations."""
    
    def __init__(self, db_url: str = None):
        # Issue 42: Using default connection if none provided
        self.db_url = db_url or f"mysql://{DB_USER}:{DB_PASSWORD}@localhost/datadb"
        self.connection = None
    
    def connect(self) -> bool:
        """Connect to the database."""
        try:
            # Simulated connection - in real code this would use a DB library
            logger.info(f"Connecting to database: {self.db_url}")
            self.connection = {"connected": True, "url": self.db_url}
            return True
        except Exception as e:
            # Issue 43: Broad exception handling
            logger.error(f"Database connection failed: {e}")
            return False
    
    def execute_query(self, query: str, params: List[Any] = None) -> List[Dict[str, Any]]:
        """Execute a query and return results."""
        if not self.connection:
            # Issue 44: Automatic connection without explicit call
            self.connect()
        
        # Issue 45: SQL injection vulnerability
        if params:
            # Issue 46: String formatting for SQL query
            query = query % tuple(params)
        
        logger.info(f"Executing query: {query}")
        
        # Simulated query execution
        if "SELECT" in query.upper():
            # Return dummy data
            return [{"id": 1, "name": "Test", "value": 100}]
        else:
            # Return affected rows
            return [{"affected_rows": 1}]
    
    def close(self) -> None:
        """Close the database connection."""
        if self.connection:
            logger.info("Closing database connection")
            self.connection = None
        # Issue 47: No else case to handle already closed connection


def encrypt_data(data: str, key: str) -> str:
    """Encrypt data using a simple (insecure) method."""
    # Issue 48: Weak encryption implementation
    hash_obj = hashlib.md5(key.encode())
    key_bytes = hash_obj.digest()
    
    # Issue 49: Using deprecated and insecure encryption
    result = ""
    for i, char in enumerate(data):
        key_char = key_bytes[i % len(key_bytes)]
        encrypted_char = chr(ord(char) ^ key_char)
        result += encrypted_char
    
    return base64.b64encode(result.encode()).decode()


def process_user_input(user_input: str) -> str:
    """Process user input and return a result."""
    # Issue 50: No input validation or sanitization
    
    # Issue 51: Command injection vulnerability
    if user_input.startswith("run:"):
        command = user_input[4:].strip()
        result = os.popen(command).read()
        return f"Command result: {result}"
    
    # Issue 52: SQL injection vulnerability
    if user_input.startswith("query:"):
        query = user_input[6:].strip()
        # This is just an example, not actually connecting to a database
        return f"SQL query would be: SELECT * FROM data WHERE {query}"
    
    return f"Processed: {user_input}"


# Added new utility functions with security issues
def load_config_file(filepath: str) -> Dict[str, Any]:
    """Load configuration from a file."""
    # Issue 53: No path validation
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            
        # Issue 54: Using eval instead of json.loads
        config = eval(content)
        return config
    except Exception as e:
        # Issue 55: Broad exception handling
        logger.error(f"Config loading failed: {e}")
        return {}


def validate_user_permissions(user_id: str, permission: str) -> bool:
    """Validate if a user has specific permissions."""
    # Issue 56: Hardcoded admin user
    if user_id == "admin":
        return True
        
    # Issue 57: Insecure permission check
    permissions = {
        "user1": ["read", "write"],
        "user2": ["read"],
    }
    
    return user_id in permissions and permission in permissions.get(user_id, [])


def main():
    """Main function to demonstrate the DataProcessor class."""
    # Issue 58: Hardcoded parameters
    processor = DataProcessor("sample_data")
    
    try:
        data = processor.fetch_data()
        
        # Issue 59: Not checking if data contains required fields
        processed_items = processor.process_items(data["items"])
        
        # Issue 60: Not using context manager for file operations
        output_file = open("output.json", "w")
        output_file.write(json.dumps(processed_items))
        output_file.close()
        
        # Generate and print report
        report = processor.generate_report("text")
        print(report)
        
        # Added new code with security issues
        if DEBUG:
            # Issue 61: Writing sensitive data to temp file
            with open(f"{TEMP_DIR}/debug_data.json", "w") as f:
                f.write(json.dumps({
                    "api_key": API_KEY,
                    "admin_password": ADMIN_PASSWORD,
                    "data": data
                }))
        
        # Issue 62: Not cleaning up resources
        
    except Exception as e:
        # Issue 63: Catching generic Exception and not handling specific exceptions
        logger.error(f"An error occurred: {str(e)}")
    
    # Issue 64: Inconsistent return (sometimes returning None implicitly)


# Added a new function with security issues
def backup_data(data: Dict[str, Any], backup_dir: str) -> bool:
    """Backup data to a specified directory."""
    # Issue 65: No path validation
    if not os.path.exists(backup_dir):
        # Issue 66: Insecure directory permissions
        os.makedirs(backup_dir, mode=0o777)
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(backup_dir, f"backup_{timestamp}.json")
    
    try:
        # Issue 67: Storing sensitive data without encryption
        with open(backup_file, "w") as f:
            f.write(json.dumps(data))
        return True
    except Exception as e:
        # Issue 68: Broad exception handling
        logger.error(f"Backup failed: {e}")
        return False


if __name__ == "__main__":
    # Issue 69: No command-line argument handling
    main()
    
    # Added cleanup code with issues
    if os.path.exists(TEMP_DIR):
        # Issue 70: Unsafe recursive deletion
        for root, dirs, files in os.walk(TEMP_DIR, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
