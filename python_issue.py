import os
import random
import json
import pickle
import subprocess
from typing import List, Dict, Any

# Global variables with poor naming
x = 10
y = "test"
z = [1, 2, 3]

# Function with too many issues to count
def do_stuff(param1, param2 = None, Param3 = [], PARAM4 = {}):
    """this is a poorly documented function that does stuff
    """
    # Unused import
    import sys
    
    # Unused variable
    unused_var = "This variable is never used"
    
    # Inconsistent return types
    if param1 == "return_int":
        return 42
    elif param1 == "return_str":
        return "string"
    elif param1 == "return_none":
        pass  # No return statement
    
    # Dangerous eval usage
    if isinstance(param2, str):
        result = eval(param2)  # Security issue: eval on user input
    
    # Mutable default argument usage
    Param3.append(param1)
    
    # Command injection vulnerability
    if isinstance(param1, str):
        os.system("echo " + param1)  # Security issue: command injection
        subprocess.call("ls " + param1, shell=True)  # Another command injection
    
    # Potential resource leak
    f = open("some_file.txt", "w")
    f.write("This file is never closed")
    
    # Mixed indentation
    if param1:
      print("Two space indent")
        print("Four space indent")
    
    # Hardcoded credentials
    password = "SuperSecretPassword123!"
    api_key = "AKIAIOSFODNN7EXAMPLE"
    
    # Catching too broad exceptions
    try:
        risky_operation = 1 / 0
    except:  # Too broad exception clause
        print("Something went wrong")
    
    # Complex nested structures
    if param1:
        if param2:
            if Param3:
                if PARAM4:
                    print("Too many nested levels")
                    
    # Inconsistent variable naming
    camelCase = "This is not Python convention"
    snake_case = "This is Python convention"
    PascalCase = "This should be for classes"
    
    # Unreachable code
    return "Early return"
    print("This will never execute")


# Class with issues
class my_class:  # Should use PascalCase for class names
    
    def __init__(self):
        # Too many instance attributes
        self.attr1 = 1
        self.attr2 = 2
        self.attr3 = 3
        self.attr4 = 4
        self.attr5 = 5
        self.attr6 = 6
        self.attr7 = 7
        self.attr8 = 8
        self.attr9 = 9
        self.attr10 = 10
    
    # Method with too many arguments
    def process_data(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8):
        # Function too complex
        result = 0
        for i in range(arg1):
            for j in range(arg2):
                for k in range(arg3):
                    for l in range(arg4):
                        result += i * j * k * l
        return result
    
    # Method too long
    def long_method(self, input_data):
        # This method has too many lines
        result = []
        for i in range(100):
            temp = i * 2
            if temp % 2 == 0:
                temp += 1
            elif temp % 3 == 0:
                temp += 2
            elif temp % 5 == 0:
                temp += 3
            elif temp % 7 == 0:
                temp += 4
            else:
                temp += 5
            
            # Duplicate code
            value = 0
            for j in range(10):
                value += j * j
            
            # More duplicate code
            value2 = 0
            for j in range(10):
                value2 += j * j
                
            result.append(temp + value + value2)
        
        return result


# Dangerous pickle usage
def load_data(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)  # Security issue: unsafe deserialization

# Poorly typed function
def process_items(items):  # No type hints
    results = []
    for item in items:
        # Potential attribute error if item doesn't have 'value'
        if item.value > 10:
            results.append(item.value * 2)
    return results

# Dead code
def unused_function():
    """This function is never called."""
    return "I'm never used"

# Inconsistent string quotes
single_quote = 'This uses single quotes'
double_quote = "This uses double quotes"
triple_single = '''This uses triple single quotes'''
triple_double = """This uses triple double quotes"""

# Main execution with issues
if __name__ == "__main__":
    # Magic numbers
    for i in range(17):
        if i % 3 == 0:
            print(i * 42)
    
    # Shadowing built-in names
    list = [1, 2, 3]
    dict = {"key": "value"}
    
    # Unnecessary comprehension
    result = [x for x in range(10)]
    
    # Potential race condition with temporary file
    temp_file = "/tmp/temp_" + str(random.randint(1, 1000))
    with open(temp_file, "w") as f:
        f.write("Sensitive data")
    
    # Accessing private members
    instance = my_class()
    instance._private_var = "Shouldn't access private variables"
    
    # Too many arguments in function call
    instance.process_data(1, 2, 3, 4, 5, 6, 7, 8)
