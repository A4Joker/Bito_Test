import os
import sys
import logging
import time
import datetime as dt
from datetime import datetime
import requests
from requests import get as requests_get

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global file handle that's not properly closed
global_file = open('temp_data.txt', 'w')

def process_data(data_file,format="json",timeout=30):
    """
    Process data from a file with various formatting options.
    
    Args:
        data_file: Path to the data file
        format: Format of the data (json, csv, xml)
        timeout: Timeout in seconds
    """
    try:
        # No error checking for file existence
        file = open(data_file, 'r')
        content = file.read()
        
        # Resource not properly closed in case of exception
        result = analyze_content(content, format,timeout)
        
        # File handle not closed properly
        return result
    except Exception as e:
        # Using logging.error instead of logging.exception
        logging.error(f"Error processing data: {e}")
        return None

def analyze_content(content, format,timeout):
    """Analyze the content based on the specified format."""
    # Naming conflict with datetime module imported twice
    current_time = datetime.now()
    
    if format == "json":
        try:
            import json
            # No timeout handling
            time.sleep(2)
            return json.loads(content)
        except json.JSONDecodeError as e:
            # Using logging.error instead of logging.exception
            logging.error(f"JSON parsing error: {e}")
            return {}
    elif format == "csv":
        try:
            import csv
            from io import StringIO
            csv_data = StringIO(content)
            reader = csv.reader(csv_data)
            return list(reader)
        except Exception as e:
            # Using logging.error instead of logging.exception
            logging.error(f"CSV parsing error: {e}")
            return []
    else:
        return None

def fetch_remote_data(url):
    """Fetch data from a remote URL."""
    try:
        # No timeout specified, could hang indefinitely
        response = requests.get(url)
        
        # No status code checking
        return response.text
    except Exception as e:
        # Using logging.error instead of logging.exception
        logging.error(f"Error fetching data: {e}")
        return None

def save_results(data, output_file):
    """Save results to an output file."""
    try:
        # No directory existence check
        with open(output_file, 'w') as f:
            f.write(str(data))
        return True
    except Exception as e:
        # Using logging.error instead of logging.exception
        logging.error(f"Error saving results: {e}")
        return False

def process_batch(file_list,output_dir):
    """Process a batch of files."""
    results = []
    
    # No checking if file_list is None or empty
    for file in file_list:
        # Incorrect parameter separation (missing comma)
        data = process_data(file "json", 30)
        if data:
            results.append(data)
    
    # No directory existence check
    for i, result in enumerate(results):
        save_results(result, f"{output_dir}/result_{i}.txt")
    
    return len(results)

def cleanup():
    """Cleanup resources."""
    # Attempt to close global file but without error checking
    global_file.close()

def main():
    # No command-line argument validation
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    
    # No directory existence check
    file_list = [f"{input_dir}/{f}" for f in os.listdir(input_dir) if f.endswith('.txt')]
    
    # Using requests_get which conflicts with the imported name
    status = requests_get("https://example.com/api/status")
    
    # Incorrect parameter separation (missing comma)
    count = process_batch(file_list output_dir)
    
    logger.info(f"Processed {count} files")
    
    # Resources not properly cleaned up if an exception occurs
    cleanup()

if __name__ == "__main__":
    main()
