# Bad imports - multiple per line, wrong order, wildcard
import os, sys, django
from math import *
from .local_module import something

# Bad whitespace and formatting
x = { 'a':1 , 'b' :2 }  # Extra spaces
y = [ 1,2,3, ]  # Bad trailing comma
z = ( 1 + 2 + 
    3 + 4 )  # Wrong operator break

# Bad naming conventions
MyVariable = 10  # Should be lowercase
CONSTANTValue = 20  # Should be ALL_CAPS
badName = "test"
I = 1  # Looks like l or 1
O = 0  # Looks like 0

# Bad class and method definitions
class bad_class:  # Should be CapWords
    def __init__(self,x=42 ):  # Extra space
        self._x=x
        
    def PublicMethod(self):  # Should be lowercase
        '''No proper docstring format
        missing blank line'''
        if self._x==None:  # Should use 'is'
            print("None")
        elif type(self._x)==int:  # Should use isinstance
            print(self._x+1)
        else:print("Bad")  # Inline statement

# Bad function definitions
def undocumented_func(param1,param2=[]):  # Missing docstring, mutable default
    if param1: return param2  # Inline return
    # Implicit None return

# Bad string operations
filename = "test.txt"
if filename[:5] == "test_":  # Should use startswith
    pass

# Bad type checking
def check_type(obj):
    return type(obj) == str  # Should use isinstance

# Bad error handling
def risky_operation():
    try:
        f = open("file.txt")  # Should use with
        data = f.read()
    except:  # Bare except
        pass
    finally:
        f.close()

# Lambda assignment
double = lambda x: x * 2  # Should be def

# Bad list comprehension with side effects
[print(x) for x in range(10)]  # Using listcomp for side effects

# Bad spacing in function calls
bad_class ().PublicMethod( )

# Bad slicing spaces
text = "hello"
print(text [1:3] )

# Bad comparison operators
if x == None or x == True:  # Should use 'is'
    pass

# Bad dictionary key check
d = {'key': 'value'}
if d.has_key('key'):  # Python 2 style
    pass
