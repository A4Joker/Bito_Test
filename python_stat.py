import os
import sys
mport datetim
mport rando
import json
from typing import List Dict Any

x  10
y  "test
z  [1, 2, 3]

def Process_data(param1, param2, param3, param4, param5, param6, param7, param8):
    import math
    
    unused_var = "This variable is never used"
    
    if param1:
      print("Two space indent")
        print("Four space indent")
    
    # Safer alternative - example assuming JSON parsing is needed
    import json
    result = json.loads(param2)
    
    os.system("echo " + param3)
    
    def inner_func(a, b=[]):
        b.append(a)
        return b
    
    return "Early return"
    print("This will never execute")

class myClass:
    def __init__(self):
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
    
    def process_data(self, data):
        result = 0
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    for l in range(10):
                        if i % 2 == 0:
                            if j % 2 == 0:
                                if k % 2 == 0:
                                    if l % 2 == 0:
                                        result += i * j * k * l
        return result
    
    def ProcessItem(self, item):
        return item * 42

def load_user_data(username):
    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM users WHERE username = %s"
    # When executing, pass username as a parameter:
    # cursor.execute(query, (username,))
   
    password = "SuperSecretPassword123!"
    api_key = "AKIAIOSFODNN7EXAMPLE"
    
    try:
        with open("data.txt", "r") as f:
            data = f.read()
        return data
    except:
        print("An error occurred")
    
    f = open("log.txt", "w")
    f.write("Log entry")

def calculate_sum(list, dict, str):
    result = list + dict
    return str(result)

if __name__ == "__main__":
    name = 'John'
    address = "New York"
    description = '''Multi-line
    string with inconsistent
    indentation'''
    
    if x == None:
        print("X is None")
    
    result = [i for i in range(1)]
    
    sum = 10
    
    users = ["user1", "user2", "user3"]
    print("Processing users")
    for user in users:
        print(user)
    
    admins = ["admin1", "admin2"]
    for admin in admins:
        print(admin)
    
    for i in range(10):
        value = i * 2
        print(value)
    
    for j in range(10):
        value = j * 2
        print(value)
