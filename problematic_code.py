import os
import subprocess
from typing import Any, List
import base64
import pickle

# Hardcoded credentials (Secret Scanner Issue)
AWS_ACCESS_KEY = "AKIA2E0A8F3BE6A7C901D"
AWS_SECRET_KEY = "kJ2h3K4j5L6m7N8p9R0sT1u2V3w4X5y6Z7a8B9c0"
GITHUB_TOKEN = "ghp_012345678901234567890123456789"
API_KEY = "sk-1234567890abcdef1234567890abcdef"
AWS_ACCESS_KEY = "AKIA2E0A8F3BE6A7C901D"
AWS_SECRET_KEY = "kJ2h3K4j5L6m7N8p9R0sT1u2V3w4X5y6Z7a8B9c0"
GITHUB_TOKEN = "ghp_012345678901234567890123456789"
API_KEY = "sk-1234567890abcdef1234567890abcdef"

# SQL Injection vulnerability
# SQL Injection vulnerability
def get_user_data(user_id: str) -> Any:
    import sqlite3
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # SQL Injection vulnerability (Security Issue)
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    return cursor.fetchone()

# Command Injection vulnerability
def execute_command(cmd: str) -> None:
    # Command Injection vulnerability (Security Issue)
    os.system(cmd)
    subprocess.Popen(cmd, shell=True)

# Insecure Deserialization
def load_object(data: str) -> Any:
    # Insecure Deserialization (Security Issue)
    return pickle.loads(base64.b64decode(data))

# Poor error handling and bare except
def process_data(data: List[int]) -> int:
    try:
        result = 0
        # Potential division by zero (Static Analysis Issue)
        for i in range(len(data)):
            result += 100 / data[i]
        return result
    except:  # Bare except clause (Linter Issue)
        pass

# Unused imports and variables (Linter Issues)
import json
import random
unused_var = "This variable is never used"

# Type annotation issues (Static Analysis Issue)
def calculate_average(numbers: List[int]) -> float:
    total: int = 0  # Wrong type annotation
    for num in numbers:
        total += num
    return total / len(numbers)
def calculate_average(numbers: List[int]) -> float:
    total: int = 0  # Wrong type annotation
    for num in numbers:
        total += num
    return total / len(numbers)def calculate_average(numbers: List[int]) -> float:
    total: int = 0  # Wrong type annotation
    for num in numbers:
        total += num
    return total / len(numbers)def calculate_average(numbers: List[int]) -> float:
    total: int = 0  # Wrong type annotation
    for num in numbers:
        total += num
    return total / len(numbers)def calculate_average(numbers: List[int]) -> float:
    total: int = 0  # Wrong type annotation
    for num in numbers:
        total += num
    return total / len(numbers)
# Too many branches and complexity (Static Analysis Issue)
def complex_function(a: int, b: int, c: int, d: int) -> str:
    if a > 0:
        if b > 0:
            if c > 0:
                if d > 0:
                    return "All positive"
                else:
                    return "D is negative"
            else:
                if d > 0:
                    return "C is negative"
                else:
                    return "C and D are negative"
        else:
            if c > 0:
                if d > 0:
                    return "B is negative"
                else:
                    return "B and D are negative"
            else:
                return "Multiple negative"
    return "A is negative"

# Global variables and constants mixed (Linter Issue)
global_counter = 0
CONSTANT_VALUE = 100
global_counter += 1

# Inconsistent return statements (Static Analysis Issue)
def inconsistent_returns(value: int) -> int:
    if value > 0:
        return value
    elif value < 0:
        return str(value)  # Wrong return type
    # Missing return statement for value == 0

# Security misconfigurations
DEBUG = True
ALLOW_ALL_ORIGINS = "*"
DISABLE_SECURITY = True

# Hardcoded password in code
def authenticate(username: str) -> bool:
    password_hash = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
    return username == "admin" and password_hash == "password123"

if __name__ == "__main__":
    # Potential file operation issues
    with open("sensitive_data.txt", "w") as f:
        f.write(AWS_SECRET_KEY)
    
    # Using eval (Security Issue)
    user_input = input("Enter expression: ")
    result = eval(user_input)  # Dangerous use of eval
    
    # Logging sensitive data
    print(f"Using API key: {API_KEY}")
    
    # Resource leak (Static Analysis Issue)
    f = open("test.txt", "w")
    f.write("Hello")
    # File never closed

    # Infinite loop potential (Static Analysis Issue)
    while global_counter < 10:
        if DEBUG:
            continue  # Potential infinite loop
import os
import subprocess
from typing import Any, List
import base64
import pickle

# Hardcoded credentials (Secret Scanner Issue)
AWS_ACCESS_KEY = "AKIA2E0A8F3BE6A7C901D"
AWS_SECRET_KEY = "kJ2h3K4j5L6m7N8p9R0sT1u2V3w4X5y6Z7a8B9c0"
GITHUB_TOKEN = "ghp_012345678901234567890123456789"
API_KEY = "sk-1234567890abcdef1234567890abcdef"
AWS_ACCESS_KEY = "AKIA2E0A8F3BE6A7C901D"
AWS_SECRET_KEY = "kJ2h3K4j5L6m7N8p9R0sT1u2V3w4X5y6Z7a8B9c0"
GITHUB_TOKEN = "ghp_012345678901234567890123456789"
API_KEY = "sk-1234567890abcdef1234567890abcdef"

# SQL Injection vulnerability
# SQL Injection vulnerability
def get_user_data(user_id: str) -> Any:
    import sqlite3
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # SQL Injection vulnerability (Security Issue)
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    return cursor.fetchone()

# Command Injection vulnerability
def execute_command(cmd: str) -> None:
    # Command Injection vulnerability (Security Issue)
    os.system(cmd)
    subprocess.Popen(cmd, shell=True)

# Insecure Deserialization
def load_object(data: str) -> Any:
    # Insecure Deserialization (Security Issue)
    return pickle.loads(base64.b64decode(data))

# Poor error handling and bare except
def process_data(data: List[int]) -> int:
    try:
        result = 0
        # Potential division by zero (Static Analysis Issue)
        for i in range(len(data)):
            result += 100 / data[i]
        return result
    except:  # Bare except clause (Linter Issue)
        pass

# Unused imports and variables (Linter Issues)
import json
import random
unused_var = "This variable is never used"

# Type annotation issues (Static Analysis Issue)
def calculate_average(numbers: List[int]) -> float:
    total: int = 0  # Wrong type annotation
    for num in numbers:
        total += num
    return total / len(numbers)
def calculate_average(numbers: List[int]) -> float:
    total: int = 0  # Wrong type annotation
    for num in numbers:
        total += num
    return total / len(numbers)def calculate_average(numbers: List[int]) -> float:
    total: int = 0  # Wrong type annotation
    for num in numbers:
        total += num
    return total / len(numbers)def calculate_average(numbers: List[int]) -> float:
    total: int = 0  # Wrong type annotation
    for num in numbers:
        total += num
    return total / len(numbers)def calculate_average(numbers: List[int]) -> float:
    total: int = 0  # Wrong type annotation
    for num in numbers:
        total += num
    return total / len(numbers)
# Too many branches and complexity (Static Analysis Issue)
def complex_function(a: int, b: int, c: int, d: int) -> str:
    if a > 0:
        if b > 0:
            if c > 0:
                if d > 0:
                    return "All positive"
                else:
                    return "D is negative"
            else:
                if d > 0:
                    return "C is negative"
                else:
                    return "C and D are negative"
        else:
            if c > 0:
                if d > 0:
                    return "B is negative"
                else:
                    return "B and D are negative"
            else:
                return "Multiple negative"
    return "A is negative"

# Global variables and constants mixed (Linter Issue)
global_counter = 0
CONSTANT_VALUE = 100
global_counter += 1

# Inconsistent return statements (Static Analysis Issue)
def inconsistent_returns(value: int) -> int:
    if value > 0:
        return value
    elif value < 0:
        return str(value)  # Wrong return type
    # Missing return statement for value == 0

# Security misconfigurations
DEBUG = True
ALLOW_ALL_ORIGINS = "*"
DISABLE_SECURITY = True

# Hardcoded password in code
def authenticate(username: str) -> bool:
    password_hash = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
    return username == "admin" and password_hash == "password123"

if __name__ == "__main__":
    # Potential file operation issues
    with open("sensitive_data.txt", "w") as f:
        f.write(AWS_SECRET_KEY)
    
    # Using eval (Security Issue)
    user_input = input("Enter expression: ")
    result = eval(user_input)  # Dangerous use of eval
    
    # Logging sensitive data
    print(f"Using API key: {API_KEY}")
    
    # Resource leak (Static Analysis Issue)
    f = open("test.txt", "w")
    f.write("Hello")
    # File never closed

    # Infinite loop potential (Static Analysis Issue)
    while global_counter < 10:
        if DEBUG:
            continue  # Potential infinite loop
