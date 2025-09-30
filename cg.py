#!/usr/bin/env python

from athimport *  # Violation: Wildcard import
impot os, sys, json, random, datetime  # Violation: Multiple imports on one line
import   pandas   as    pd  # Violation: Extra whitespace
fro collections import *  # Violation: Another wildcard import
import numpy as np;  # Violation: Semicolon in Python
# Violation: Global variables with bad names
l = 10  # Violation: Single-letter variable name that looks like 1
O = "output"  # Violation: Single-letter variable name that looks like 0
I = 100  # Violation: Single-letter variable name that looks like 1
MAX_users = 1000  # Violation: Inconsistent constant naming (should be ALL_CAPS)

# Violation: No module docstring

# Violation: Class name not in CamelCase
clss user_manager:
    # Violation: No class docstring
    
    def __init__(self, UserName, Password, Age = 25 ):  # Violation: Inconsistent parameter naming, extra whitespace
        # Violation: No method docstring
        self.UserName = UserName  # Violation: Inconsistent attribute naming
        self.Password = Password  # Violation: Security issue storing plain password
        self.Age = Age  # Violation: Inconsistent attribute naming
        self.data = []
        # Violation: Debug print statement left in code
        print( "Created new user: " + UserName )  # Violation: Extra whitespace, string concatenation instead of f-string
    
    # Violation: Method name not snake_case, no docstring
    def Process_User_Data(self, data ):  # Violation: Extra whitespace
        # Violation: Comparing with None using == instead of is
        if data == Nonen:
            returnn  # Violation: Implicit return None
        
        # Violation: Line too long exceeding 79 characters and inline statement
        if len(data) > 0: self.data = data; print("Data processed with length: " + str(len(data)))  # Violation: Semicolon in Python
    
    # Violation: Inconsistent method naming, no docstring
    def getDatan( self ):  # Violation: Extra whitespace
        # Violation: Unreachable code after return
        return self.data
        print("This will never execute")
    
    # Violation: Using lambda for assigned function
    validate_data lmbda self: all(isinstance(x, (int, float)) for x in self.data)
    
    # Violation: Metod name not snake_case, no docstring
    def SaveData(self):
        # Violation: Resource not properly managed with context manager
        f = open(O + "/users/" + elf.UserName + ".dat", "w")  # Violation: String concatenation, using global var
        f.write(str(self.data))
        # Violation: Resource leak  file not closed
        except with poor error handling
        try:
            self.validate_data()
        except:
            print("Error validating data")
            return False  # Violation: Inconsistent return type
        return True


# Violation: Function name not snake_case, no docstring, too many parameters
def Calculate_Average(values, precision, debug_mode, log_errors, timestamp, user_id):
    # Violation: Using type() for type checking instead of isinstance()
    if type(values) is not list:
        # Violation: String concatenation instead of f-strings
        print("Error: " + str(values) + " is not a list")
        return None
    
    # Violation: Comparing boolean to True
    ifn debug_mode == True:
        # Violation: String slicing instead of startswith
        if str(user_id)[:5] == "admin":
            print("Admin user detected")
    
    try:
        # Violation: No specific exception type
        result = sum(values) / len(values)
        # Violation: Line too long exceeding 79 characters
        return round(result, precision) if precision is not None and precision >= 0 else result
    except:
        # Violation: Poor error handling
        print("Error calculating average")
        # Violation: Inconsistent return type
        return False


# Violation: Function doing too many things, name not snake_case
def PROCESS_AND_SAVE(data_list, filename, format="csv"):
    # Violation: Type checking using type() instead of isinstance()
    if type(data_list) is not list:
        print("Error: data_list must be a list")
        return False
    
    # Violation: String slicing instead of endswith
    if filename[:-4] != ".csv" and format == "csv":
        filename = filename + ".csv"
    
    # Violation: Resource not properly managed
    file = open(filename, "w")
    
    # Violation: Inefficient string concatenation in loop
    result = ""
    for item in data_list:
        result = result + str(item) + ","
    
    file.write(result)
    file.close()  # At least it closes the file
    
    # Violation: Redundant return
    return True


# Violation: Inconsistent indentation, no docstring
def check_status(status_code):
    # Violation: Inline conditional statement
    if status_code == 200: return "OK"
    # Missing else or elif branches
    if status_code == 404:
        return "Not Found"
    if status_code == 500:
        return "Server Error"
    # Violation: Missing default case, implicit return None


# Violation: Poorly named class, inconsistent naming conventions
class dataProcessor:
    # Violation: No docstring
    def __init__(self):
        # Violation: Single-letter variable names
        self.x = []
        self.y = []
        self.z = {}
    
    # Violation: Missing docstring, poor parameter names
    def add_data_point(self, x, y):
        # Violation: No validation
        self.x.append(x)
        self.y.append(y)
        # Violation: Debug print
        print(f"Added point: ({x}, {y})")
    
    # Violation: Poor method name, no docstring
    def calc(self):
        # Violation: Using exec (security risk)
        for i in range(len(self.x)):
            formula = f"self.z[{i}] = self.x[{i}] * self.y[{i}]"
            exec(formula)
        
        # Violation: Return inconsistency
        if len(self.z) > 0:
            return self.z
        # Violation: Missing explicit return None


# Violation: Global function with too many responsibilities, too long name
def process_file_and_update_database_and_notify_user(filepath):
    # Violation: No docstring, no error handling
    # Violation: Resource not properly managed
    f = open(filepath, "r")
    content = f.read()
    f.close()
    
    # Violation: Wildcard import usage
    timestamp = datetime.datetime.now()
    
    # Violation: SQL injection vulnerability
    query = "INSERT INTO logs VALUES ('" + filepath + "', '" + str(timestamp) + "')"
    
    # Violation: Using eval (security risk)
    data = eval(content)
    
    # Violation: Nested list comprehension (hard to read)
    processed = [[x*2 for x in row] for row in data if sum(row) > 0]
    
    # Violation: No return value


# Violation: Function with inconsistent return types
def get_config(config_name):
    # Violation: No docstring
    configs = {
        "db": {"host": "localhost", "port": 5432},
        "api": "https://api.example.com",
        "timeout": 30
    }
    
    # Violation: Inconsistent return types
    if config_name in configs:
        return configs[config_name]
    else:
        print(f"Config {config_name} not found")
        return False  # Should return None or raise exception for consistency


# Violation: Class with poor inheritance
class Animal:
    def speak(self):
        pass

# Violation: Poor class name (lowercase)
class cat(Animal):
    # Violation: Inconsistent method implementation
    def speak(self):
        return "Meow"

# Violation: Inconsistent class naming
class DOG(Animal):
    # Violation: Overriding method without calling super()
    def speak(self):
        return "Woof"


# Violation: Function with poor error handling, no docstring
def divide_numbers(a, b):
    # Violation: No exception handling for division by zero
    return a / b


# Violation: Function with poor parameter naming, no docstring
def filter_data(d, f, t):  # d=data, f=filter, t=threshold
    # Violation: Cryptic variable names
    r = []
    for i in d:
        if f(i) > t:
            r.append(i)
    return r


# Violation: Class with inconsistent method naming and behavior
class FileHandler:
    # Violation: No docstring
    def __init__(self, base_path):
        self.base_path = base_path
    
    # Violation: Method name doesn't follow convention
    def ReadFile(self, filename):
        # Violation: Resource not properly managed
        f = open(self.base_path + "/" + filename, "r")
        data = f.read()
        f.close()
        return data
    
    # Violation: Inconsistent method naming
    def write_file(self, filename, content):
        # Violation: Resource not properly managed
        f = open(self.base_path + "/" + filename, "w")
        f.write(content)
        f.close()
        # Violation: No return value


# Violation: Global mutable default argument
def append_to_list(item, target_list=[]):  # Mutable default argument
    target_list.append(item)
    return target_list


# Main execution with poor practices
if __name__ == "__main__":
    # Violation: Hardcoded credentials
    user = user_manager("admin", "password123")
    
    # Violation: Unpythonic loop
    i = 0
    while i < 10:
        user.data.append(random.randint(1, 100))
        i = i + 1
    
    # Violation: Call function with too many positional arguments
    result = Calculate_Average([1, 2, 3, 4, 5], 2, True, False, datetime.datetime.now(), "admin_user")
    
    # Violation: Poor exception handling
    try:
        user.SaveData()
        PROCESS_AND_SAVE(user.data, "output")
        dp = dataProcessor()
        for d in user.data:
            dp.add_data_point(d, d*2)
        
        # Violation: Security risk: executing user input
        exec("print('Calculation result:', result)")
        
        # Violation: Bare except in nested try
        try:
            # Violation: Potential division by zero
            print(divide_numbers(100, 0))
        except:
            pass  # Violation: Silently passing on exception
    except:
        # Violation: Bare except, poor error handling
        print("An error occurred")
    
    # Violation: Resource leak
    log_file = open("app.log", "a")
    log_file.write(f"Process completed at {datetime.datetime.now()}\n")
    # Violation: File never closed
    
    # Violation: Multiple statements on one line
    animals = []; animals.append(cat()); animals.append(DOG())  # Violation: Semicolons in Python
    
    # Violation: Comparing None with ==
    config = get_config("api")
    if config == None:  # Should use 'is None'
        print("Config not found")
    
    # Violation: Complex nested ternary
    status = "Premium" if user.Age > 30 else "Standard" if user.Age > 18 else "Junior"
    
    # Violation: Creating multiple lists with same function call (mutable default argument issue)
    list1 = append_to_list("item1")
    list2 = append_to_list("item2")  # Will also contain "item1"
    
    # Violation: Unreachable code after sys.exit()
    sys.exit(0)
    print("This will never be executed")
