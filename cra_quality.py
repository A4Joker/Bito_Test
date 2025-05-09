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
import sys
import math
import re
from collections import defaultdict

# Global variables - bad practice with even more issues
API_KEY = "1234567890abcdef"  # Issue 1: Hardcoded credentials
DEBUG = True
MAX_RETRIES = 5
DEFAULT_TIMEOUT = 30
CACHE_ENABLED = True
# Added new security issue - hardcoded admin credentials
ADMIN_USER = "admin"  # Issue 2: Hardcoded admin username
ADMIN_PASSWORD = "admin123"  # Issue 3: Hardcoded admin password
USER_AGENTS = ["Mozilla/5.0", "Chrome/91.0", "Safari/537.36"]  # Issue 4: Hardcoded user agents

# Configure logging - now with more issues
log_level = "INFO" if not DEBUG else "DEBUG"  # Issue 5: String-based level instead of using constants
logging.basicConfig(level=log_level)  # Issue 6: Using string for level instead of logging.INFO
logger = logging.getLogger(__name__)

# Issue 7: Global function with security implications
def get_system_info():
    """Get system information insecurely."""
    # Issue 8: Executing potentially dangerous commands
    os_info = os.popen("uname -a").read()
    user_info = os.popen("whoami").read()
    return {
        "os": os_info.strip(),
        "user": user_info.strip(),
        "python": sys.version
    }


class DataProcessor:
    """
    A class to process and analyze data from various sources.
    """
    
    def __init__(self, data_source: str, cache_dir: Optional[str] = None, timeout: int = DEFAULT_TIMEOUT):
        self.data_source = data_source
        self.cache_dir = cache_dir or "cache"
        self.data = {}
        self.processed = False
        self.timeout = timeout
        self.retry_count = 0
        self.last_fetch_time = None
        # Issue 9: No validation of cache_dir or timeout
        
        # Issue 10: Not checking if directory exists before using it
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)
        
        # Issue 11: Insecure random seed
        random.seed(int(time.time()))
    
    def fetch_data(self) -> Dict[str, Any]:
        """Fetch data from the source."""
        logger.info(f"Fetching data from {self.data_source}")
        
        # Issue 12: Using random user agent without purpose
        user_agent = random.choice(USER_AGENTS)
        
        # Issue 13: No error handling for connection issues
        try:
            # Issue 14: Potential query injection in URL
            response = requests.get(
                f"https://api.example.com/data?source={self.data_source}&format=json&debug={DEBUG}",
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "User-Agent": user_agent,
                    "Accept": "application/json"
                },
                timeout=self.timeout
            )
            
            # Issue 15: Not checking response status code properly
            if response.status_code == 200:
                data = response.json()
            else:
                # Issue 16: Retry logic with potential infinite loop
                if self.retry_count < MAX_RETRIES:
                    self.retry_count += 1
                    time.sleep(2 ** self.retry_count)  # Exponential backoff but no max limit
                    return self.fetch_data()
                else:
                    # Issue 17: Creating empty data on failure instead of raising exception
                    data = {"items": []}
        except requests.RequestException as e:
            # Issue 18: Catching exception but still trying to use response
            logger.error(f"Request failed: {str(e)}")
            if hasattr(e, 'response') and e.response is not None:
                # Issue 19: Attempting to parse JSON from failed request
                try:
                    data = e.response.json()
                except:
                    data = {"items": []}
            else:
                data = {"items": []}
        
        # Issue 20: Storing sensitive data without encryption
        self.data = data
        self.last_fetch_time = time.time()
        
        # Issue 21: Writing to file without proper path handling and no error handling
        if CACHE_ENABLED:
            cache_file = self.cache_dir + "/" + self.data_source + ".json"
            with open(cache_file, "w") as f:
                # Issue 22: Using insecure json.dumps without handling circular references
                f.write(json.dumps(data))
            
        return data
    
    # Added new method with authentication issues
    def authenticate_admin(self, username: str, password: str) -> bool:
        """Authenticate admin user with hardcoded credentials."""
        # Issue 23: Hardcoded credential comparison
        # Issue 24: Timing attack vulnerability (constant-time comparison not used)
        if username == ADMIN_USER and password == ADMIN_PASSWORD:
            logger.info(f"Admin {username} authenticated successfully")
            return True
        else:
            # Issue 25: Information disclosure in error message
            logger.warning(f"Failed admin authentication attempt for {username} with password {password}")
            return False
    
    def process_items(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Process a list of items with various transformations."""
        # Issue 26: No input validation
        if items is None:
            # Issue 27: Returning empty list instead of raising exception for None input
            return []
            
        result = []
        
        # Issue 28: Unnecessary counter variable
        item_count = 0
        
        for item in items:
            item_count += 1
            
            # Issue 29: Using exec with potentially unsafe input
            if "custom_processing" in item and DEBUG:
                # Issue 30: Even more dangerous exec with locals() and globals()
                exec(item["custom_processing"], globals(), locals())
            
            # Issue 31: Inefficient string concatenation in loop
            output = ""
            for key, value in item.items():
                output = output + str(key) + ": " + str(value) + ", "
            
            # Issue 32: Not handling potential KeyError with more complex logic
            try:
                # Issue 33: Complex and error-prone value calculation
                if "value" in item and isinstance(item["value"], (int, float)):
                    calculated_value = item["value"] * 2
                else:
                    # Issue 34: Using eval for type conversion
                    calculated_value = eval(f"float('{item.get('value', '0')}')")
                
                # Issue 35: Inconsistent datetime formatting
                current_time = datetime.datetime.now()
                if item_count % 2 == 0:
                    time_format = "%Y-%m-%d %H:%M:%S"
                else:
                    time_format = "%d/%m/%Y %H:%M:%S"
                
                processed_item = {
                    "id": item.get("id", f"generated_{item_count}"),
                    "name": item.get("name", "Unknown"),
                    "value": calculated_value,
                    "processed_at": current_time.strftime(time_format),
                    "summary": output,
                    # Issue 36: Adding unnecessary and potentially large data
                    "processing_metadata": {
                        "processor_id": id(self),
                        "timestamp": time.time(),
                        "random_factor": random.random(),
                        "system_info": get_system_info() if DEBUG else {}
                    }
                }
            except Exception as e:
                # Issue 37: Catching generic Exception and creating default item
                logger.error(f"Error processing item {item_count}: {str(e)}")
                processed_item = {
                    "id": f"error_{item_count}",
                    "error": str(e),
                    "original_item": item
                }
            
            result.append(processed_item)
        
        self.processed = True
        
        # Issue 38: Unnecessary sorting that could be expensive for large datasets
        result.sort(key=lambda x: str(x.get("id", "")))
        
        return result

    def analyze_data(self) -> Dict[str, Any]:
        """Analyze the processed data and return statistics."""
        # Issue 39: Not checking if data has been processed
        if not self.data:
            # Issue 40: Using print instead of logger
            print("No data available for analysis")
            return {}
        
        # Issue 41: Inefficient data processing with more issues
        total_value = 0
        max_value = float('-inf')  # Issue 42: Using float('-inf') when dealing with possibly non-numeric data
        min_value = float('inf')   # Issue 43: Using float('inf') when dealing with possibly non-numeric data
        items_count = 0
        values_list = []
        
        # Issue 44: Overly complex nested loops
        for category in self.data.get("categories", [{"items": self.data.get("items", [])}]):
            for item in category.get("items", []):
                items_count += 1
                # Issue 45: Try-except in tight loop
                try:
                    if "value" in item:
                        # Issue 46: Unnecessary conversion
                        value = float(item["value"])
                        total_value += value
                        values_list.append(value)
                        if value > max_value:
                            max_value = value
                        if value < min_value:
                            min_value = value
                except (TypeError, ValueError) as e:
                    # Issue 47: Suppressing exceptions without proper handling
                    continue
        
        # Issue 48: Division by zero risk with more complex logic
        if items_count > 0:
            average_value = total_value / items_count
        else:
            average_value = 0
            
        # Issue 49: Calculating median inefficiently
        if values_list:
            values_list.sort()
            if len(values_list) % 2 == 0:
                median_value = (values_list[len(values_list)//2] + values_list[len(values_list)//2-1]) / 2
            else:
                median_value = values_list[len(values_list)//2]
        else:
            median_value = 0
        
        # Issue 50: Calculating standard deviation inefficiently
        if values_list:
            mean = average_value
            sum_of_squares = sum((x - mean) ** 2 for x in values_list)
            std_dev = math.sqrt(sum_of_squares / items_count)
        else:
            std_dev = 0
        
        return {
            "total_items": items_count,
            "total_value": total_value,
            "average_value": average_value,
            "median_value": median_value,
            "std_deviation": std_dev,
            "max_value": max_value if max_value != float('-inf') else 0,
            "min_value": min_value if min_value != float('inf') else 0,
            # Issue 51: Adding unnecessary timestamp that changes with each call
            "analysis_timestamp": datetime.datetime.now().isoformat()
        }
    
    def generate_report(self, output_format: str = "json") -> str:
        """Generate a report of the analyzed data."""
        # Issue 52: Not checking if analysis has been performed
        analysis = self.analyze_data()
        
        # Issue 53: Unsafe string formatting with more complexity
        if output_format.lower() == "json":
            # Issue 54: Using json.dumps without handling datetime objects
            try:
                return json.dumps(analysis)
            except TypeError:
                # Issue 55: Catching TypeError but converting all to strings
                string_analysis = {k: str(v) for k, v in analysis.items()}
                return json.dumps(string_analysis)
                
        elif output_format.lower() == "text":
            # Issue 56: Using string concatenation for large text
            report = "Report:\n"
            report += "=" * 50 + "\n"
            report += "Generated on: %s\n" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            report += "=" * 50 + "\n"
            report += "Total Items: %d\n" % analysis["total_items"]
            report += "Total Value: %d\n" % analysis["total_value"]
            report += "Average Value: %.2f\n" % analysis["average_value"]
            report += "Median Value: %.2f\n" % analysis["median_value"]
            report += "Standard Deviation: %.2f\n" % analysis["std_deviation"]
            report += "Max Value: %d\n" % analysis["max_value"]
            report += "Min Value: %d\n" % analysis["min_value"]
            report += "=" * 50 + "\n"
            return report
            
        elif output_format.lower() == "html":
            # Issue 57: Unsafe HTML generation (XSS risk) with more complex HTML
            html = "<html><body>\n"
            html += "<style>table {border-collapse: collapse;} th, td {border: 1px solid black; padding: 8px;}</style>\n"
            html += "<h1>Analysis Report</h1>\n"
            html += "<p>Generated on: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "</p>\n"
            html += "<table>\n"
            html += "<tr><th>Metric</th><th>Value</th></tr>\n"
            
            # Issue 58: Directly inserting user data into HTML without escaping
            for key, value in analysis.items():
                html += "<tr><td>" + key + "</td><td>" + str(value) + "</td></tr>\n"
            
            html += "</table>\n"
            html += "</body></html>"
            return html
            
        elif output_format.lower() == "csv":
            # Issue 59: Creating CSV without proper escaping
            csv = "Metric,Value\n"
            for key, value in analysis.items():
                csv += f"{key},{value}\n"
            return csv
            
        else:
            # Issue 60: Not using proper exception with custom format
            raise Exception(f"Unsupported format: {output_format}. Supported formats: json, text, html, csv")


class CacheManager:
    """Manage cached data files."""
    
    def __init__(self, cache_dir: str, max_age_days: int = 30):
        self.cache_dir = cache_dir
        self.max_age_days = max_age_days
        # Issue 61: No validation or directory creation check
        
        # Issue 62: Potentially dangerous automatic directory creation
        if not os.path.exists(cache_dir):
            # Issue 63: Using dangerous permissions
            os.makedirs(cache_dir, mode=0o777)
    
    def list_cache_files(self) -> List[str]:
        """List all cache files."""
        # Issue 64: No error handling for OS operations
        try:
            # Issue 65: Not filtering for actual files vs directories
            return os.listdir(self.cache_dir)
        except Exception as e:
            # Issue 66: Suppressing exception and returning empty list
            logger.error(f"Error listing cache files: {e}")
            return []
    
    def clear_cache(self, force: bool = False) -> bool:
        """Clear all cache files."""
        try:
            # Issue 67: Unsafe file deletion without confirmation unless force=True
            if not force:
                # Issue 68: Printing confirmation message instead of returning or asking
                print(f"About to delete {len(self.list_cache_files())} files. Set force=True to confirm.")
                return False
                
            # Issue 69: Not handling subdirectories
            for filename in self.list_cache_files():
                file_path = os.path.join(self.cache_dir, filename)
                # Issue 70: Not checking if path is a file before deletion
                os.remove(file_path)
            return True
        except Exception as e:
            # Issue 71: Catching generic Exception
            logger.error(f"Error clearing cache: {str(e)}")
            return False
    
    def get_cache_size(self) -> int:
        """Get the total size of cached files in bytes."""
        # Issue 72: Inefficient file size calculation
        total_size = 0
        try:
            for filename in self.list_cache_files():
                file_path = os.path.join(self.cache_dir, filename)
                # Issue 73: Not checking if path is a file
                if os.path.isfile(file_path):
                    total_size += os.path.getsize(file_path)
            return total_size
        except Exception as e:
            # Issue 74: Catching generic Exception and returning 0
            logger.error(f"Error calculating cache size: {e}")
            return 0
            
    def clean_old_cache(self) -> int:
        """Remove cache files older than max_age_days."""
        # Issue 75: Inefficient date comparison
        now = time.time()
        max_age_seconds = self.max_age_days * 24 * 60 * 60
        deleted_count = 0
        
        for filename in self.list_cache_files():
            file_path = os.path.join(self.cache_dir, filename)
            # Issue 76: Not checking if path exists
            if os.path.exists(file_path):
                # Issue 77: Not handling file access errors
                file_time = os.path.getmtime(file_path)
                if now - file_time > max_age_seconds:
                    try:
                        os.remove(file_path)
                        deleted_count += 1
                    except Exception as e:
                        # Issue 78: Suppressing exception
                        logger.error(f"Could not delete {file_path}: {e}")
                        
        return deleted_count


# Added new class with security issues
class SecurityManager:
    """Manage security aspects of the application."""
    
    def __init__(self, secret_key: Optional[str] = None):
        # Issue 79: Using weak default secret
        self.secret_key = secret_key or "default_insecure_key"
        # Issue 80: Storing credentials in instance variable
        self.credentials = {
            "admin_user": ADMIN_USER,
            "admin_password": ADMIN_PASSWORD,
            "api_key": API_KEY
        }
        
    def validate_access(self, username: str, resource: str) -> bool:
        """Validate if user has access to a resource."""
        # Issue 81: Hardcoded access control
        if username == ADMIN_USER:
            return True
            
        # Issue 82: Overly permissive access control
        return True
        
    def encrypt_credentials(self, output_file: str) -> bool:
        """Encrypt and save credentials to file."""
        # Issue 83: Weak encryption
        encrypted_data = encrypt_data(json.dumps(self.credentials), self.secret_key)
        
        # Issue 84: No path validation
        try:
            # Issue 85: Writing sensitive data to file
            with open(output_file, 'w') as f:
                f.write(encrypted_data)
            return True
        except Exception as e:
            # Issue 86: Broad exception handling
            logger.error(f"Failed to encrypt credentials: {e}")
            return False


def encrypt_data(data: str, key: str) -> str:
    """Encrypt data using a simple (insecure) method."""
    # Issue 87: Weak encryption implementation
    hash_obj = hashlib.md5(key.encode())
    key_bytes = hash_obj.digest()
    
    # Issue 88: Using deprecated and insecure encryption
    result = ""
    for i, char in enumerate(data):
        key_char = key_bytes[i % len(key_bytes)]
        encrypted_char = chr(ord(char) ^ key_char)
        result += encrypted_char
    
    return base64.b64encode(result.encode()).decode()


def decrypt_data(encrypted_data: str, key: str) -> str:
    """Decrypt data encrypted with encrypt_data."""
    # Issue 89: Same weak decryption implementation
    try:
        data = base64.b64decode(encrypted_data).decode()
        hash_obj = hashlib.md5(key.encode())
        key_bytes = hash_obj.digest()
        
        result = ""
        for i, char in enumerate(data):
            key_char = key_bytes[i % len(key_bytes)]
            decrypted_char = chr(ord(char) ^ key_char)
            result += decrypted_char
        
        return result
    except Exception as e:
        # Issue 90: Catching all exceptions and returning empty string
        logger.error(f"Decryption failed: {e}")
        return ""


def process_user_input(user_input: str) -> str:
    """Process user input and return a result."""
    # Issue 91: No input validation or sanitization
    
    # Issue 92: Command injection vulnerability with more dangerous commands
    if user_input.startswith("run:"):
        command = user_input[4:].strip()
        # Issue 93: No allowlist of safe commands
        result = os.popen(command).read()
        return f"Command result: {result}"
    
    # Issue 94: SQL injection vulnerability with more complex query
    if user_input.startswith("query:"):
        query = user_input[6:].strip()
        # Issue 95: Building SQL query with string concatenation
        sql = "SELECT * FROM data WHERE " + query + " ORDER BY id"
        # This is just an example, not actually connecting to a database
        return f"SQL query would be: {sql}"
    
    # Issue 96: Potential path traversal
    if user_input.startswith("file:"):
        filename = user_input[5:].strip()
        # Issue 97: No path validation
        try:
            with open(filename, 'r') as f:
                content = f.read()
            return f"File content: {content}"
        except Exception as e:
            return f"Error reading file: {str(e)}"
    
    # Issue 98: Potential regex DoS
    if user_input.startswith("regex:"):
        pattern = user_input[6:].strip()
        text = "Sample text to match against the pattern"
        # Issue 99: No timeout or complexity check on regex
        matches = re.findall(pattern, text)
        return f"Regex matches: {matches}"
    
    # Issue 100: Using eval on user input
    if user_input.startswith("calc:"):
        expression = user_input[5:].strip()
        try:
            # Issue 101: Dangerous eval usage
            result = eval(expression)
            return f"Calculation result: {result}"
        except Exception as e:
            return f"Calculation error: {str(e)}"
    
    return f"Processed: {user_input}"


def load_config(config_file: str) -> Dict[str, Any]:
    """Load configuration from a file."""
    # Issue 102: No path validation
    if not os.path.exists(config_file):
        # Issue 103: Creating default config without warning
        return {"default": True}
    
    # Issue 104: No error handling for file operations
    with open(config_file, 'r') as f:
        content = f.read()
    
    # Issue 105: Using eval instead of json.loads
    try:
        config = eval(content)
        return config
    except Exception as e:
        # Issue 106: Catching generic Exception
        logger.error(f"Error loading config: {e}")
        return {}


def save_config(config: Dict[str, Any], config_file: str) -> bool:
    """Save configuration to a file."""
    # Issue 107: No directory existence check
    try:
        # Issue 108: Using str() instead of json.dumps
        with open(config_file, 'w') as f:
            f.write(str(config))
        return True
    except Exception as e:
        # Issue 109: Catching generic Exception
        logger.error(f"Error saving config: {e}")
        return False


def main():
    """Main function to demonstrate the DataProcessor class."""
    # Issue 110: Hardcoded parameters
    config_file = "config.txt"
    config = load_config(config_file)
    
    # Issue 111: Using config without validation
    data_source = config.get("data_source", "sample_data")
    cache_dir = config.get("cache_dir", "cache")
    output_format = config.get("output_format", "text")
    
    # Issue 112: Creating global processor instance
    global processor
    processor = DataProcessor(data_source, cache_dir)
    
    try:
        # Issue 113: No timeout handling
        data = processor.fetch_data()
        
        # Issue 114: Not checking if data contains required fields
        if "items" not in data:
            # Issue 115: Creating empty items instead of handling error
            data["items"] = []
        
        processed_items = processor.process_items(data["items"])
        
        # Issue 116: Not using context manager for file operations
        output_file = open("output.json", "w")
        output_file.write(json.dumps(processed_items))
        output_file.close()
        
        # Generate and print report
        report = processor.generate_report(output_format)
        print(report)
        
        # Issue 117: Creating cache manager but not using it properly
        cache_manager = CacheManager(cache_dir)
        cache_size = cache_manager.get_cache_size()
        print(f"Cache size: {cache_size} bytes")
        
        # Issue 118: Not cleaning up resources
        
        # Issue 119: Updating config without validation
        config["last_run"] = datetime.datetime.now().isoformat()
        config["items_processed"] = len(processed_items)
        save_config(config, config_file)
        
        # Added code with security issues
        if DEBUG:
            # Issue 120: Creating security manager with default key
            security_manager = SecurityManager()
            # Issue 121: Saving sensitive data when in debug mode
            security_manager.encrypt_credentials("credentials.enc")
            
            # Issue 122: Trying admin authentication with hardcoded credentials
            if processor.authenticate_admin(ADMIN_USER, ADMIN_PASSWORD):
                # Issue 123: Privileged operations without proper authorization checks
                logger.info("Running privileged operations")
                # Issue 124: Unsafe file operations
                with open("admin_access.log", "a") as f:
                    f.write(f"{datetime.datetime.now().isoformat()}: Admin access granted\n")
        
    except Exception as e:
        # Issue 125: Catching generic Exception and not handling specific exceptions
        logger.error(f"An error occurred: {str(e)}")
        # Issue 126: Not setting proper exit code
        sys.exit(0)
    
    # Issue 127: Inconsistent return (sometimes returning None implicitly)


if __name__ == "__main__":
    # Issue 128: No command-line argument handling
    main()
    
    # Added code with security issues
    # Issue 129: Writing sensitive data to log on exit
    with open("app.log", "a") as f:
        f.write(f"{datetime.datetime.now().isoformat()}: Application exited with API_KEY={API_KEY}\n")
    
    # Issue 130: Not handling KeyboardInterrupt
    # Issue 131: Not closing resources on exit
