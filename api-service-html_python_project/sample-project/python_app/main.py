import os

# Issue: File operation without with statement
def read_config():
    file = open("config.txt", "r")
    data = file.read()
    file.close()
    return data

# Issue: Lambda assignment and lambda function
process_data = lambda x: x * 2

# Issue: Dictionary usage
config_dict = {"host": "localhost", "port": 8080}

# Issue: No else for if condition
def check_status(status):
    if status == "active":
        return "Running"
    # Missing else
    
# Issue: If True statement
def always_true():
    if True:
        return "This always executes"

# Issue: Implicit return
def calculate(x, y):
    if x > y:
        return x - y
    # Missing return for other cases

print(process_data(5))
