import sys

# Issue: Multiple nested ifs without else
def validate_user(age, name):
    if age > 18:
        if len(name) > 0:
            if name != "admin":
                return True
    return False

# Issue: Lambda in higher order function
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

# Issue: Complex dictionary comprehension with lambda
operations = {
    'double': lambda x: x * 2,
    'square': lambda x: x ** 2,
    'triple': lambda x: x * 3
}

# Issue: File write without with
def write_log(message):
    log_file = open("app.log", "a")
    log_file.write(message + "\n")
    log_file.close()
