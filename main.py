# main.py

# Global variables (similar to Java's static variables)
global_var = 42
global_var1 = 42
global_var2 = "Hello, World!"
global_var3 = True

class ClassB:
    def __init__(self):
        # Using global variables in constructor
        self.value = global_var
        
    def use_global_vars(self):
        # Using multiple global variables
        print(global_var1)  # changed line (similar to Java example)
        print(global_var2)
        if global_var3:
            print("Global var3 is True")

# Main execution (similar to Java's main method)
if __name__ == "__main__":
    class_b_instance = ClassB()
    class_b_instance.use_global_vars()
