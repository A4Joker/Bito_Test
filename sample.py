import os
import subprocess
import pickle
import sqlite3
import random

# CRITICAL: Hardcoded credentials
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "admin123"

class CriticalIssues:
    
    # CRITICAL: SQL Injection vulnerability
    def find_user(self, username):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        # Direct string formatting in SQL - SQL injection risk
        query = f"SELECT * FROM users WHERE username = '{username}'"
        cursor.execute(query)
        result = cursor.fetchone()
        # CRITICAL: Resource leak - connection not closed
        return result
    
    # CRITICAL: Command injection vulnerability
    def execute_command(self, user_input):
        # Direct execution of user input - command injection risk
        result = subprocess.run(f"ls -la {user_input}", shell=True, capture_output=True)
        return result.stdout
    
    # CRITICAL: Unsafe deserialization
    def deserialize_data(self, data):
        # Deserializing untrusted data with pickle
        return pickle.loads(data)
    
    # CRITICAL: Path traversal vulnerability
    def read_file(self, filename):
        # No validation of filename - path traversal risk
        file_path = f"/app/data/{filename}"
        with open(file_path, 'r') as file:
            return file.read()
    
    # CRITICAL: Null/None pointer dereference
    def process_user(self, user):
        # No None check before accessing user properties
        print(f"Processing user: {user['name']}")
        print(f"Email: {user['email'].lower()}")
        
        # CRITICAL: Potential index error
        parts = user['email'].split('@')
        print(f"Domain: {parts[1]}")  # No check if len(parts) > 1
    
    # CRITICAL: Infinite loop potential
    def process_data(self, data):
        i = 0
        while i < len(data):
            item = data[i]
            if 'skip' in item:
                # Missing i increment - infinite loop
                continue
            print(item)
            i += 1
    
    # CRITICAL: Exception swallowing
    def risky_operation(self):
        try:
            # Some risky operation
            raise Exception("Something went wrong")
        except Exception:
            # Swallowing exception without logging
            pass
    
    # CRITICAL: Weak random number generation
    def generate_token(self):
        return str(random.randint(100000, 999999))
    
    # CRITICAL: Eval with user input
    def calculate_expression(self, expression):
        # Direct eval of user input - code injection risk
        return eval(expression)
    
    # CRITICAL: File operations without proper error handling
    def write_log(self, message):
        # File operations without try/catch
        file = open('/var/log/app.log', 'a')
        file.write(message)
        # File not closed properly
    
    # CRITICAL: Hardcoded file paths
    def backup_data(self):
        # Hardcoded sensitive paths
        os.system("cp /etc/passwd /tmp/backup.txt")
        os.system("chmod 777 /tmp/backup.txt")
    
    # CRITICAL: Using assert for validation
    def validate_input(self, value):
        # Using assert for production validation
        assert value is not None, "Value cannot be None"
        assert len(value) > 0, "Value cannot be empty"
        return True
    
    # CRITICAL: Catching broad exceptions
    def broad_exception_handling(self):
        try:
            # Some operation
            pass
        except Exception as e:
            # Too broad exception catching
            print("Something went wrong")
    
    # CRITICAL: Mutable default arguments
    def add_item(self, item, items=[]):
        items.append(item)
        return items
    
    # CRITICAL: Using input() without validation
    def get_user_input(self):
        # Using input() which can be dangerous
        user_data = input("Enter data: ")
        return eval(user_data)  # Double danger with eval
