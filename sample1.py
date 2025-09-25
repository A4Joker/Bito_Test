# Bad imports - multiple per line, wrong order, wildcard
import os, sys, django
from math import *
from .local_module import something

x = { 'a':1 , 'b' :2 }  
y = [ 1,2,3, ] 
z = ( 1 + 
     2 + 
    3 + 
     4 )  


MyVariable = 10  
CONSTANTValue = 20  
badName = "test"
badName = "test"
badName = "test"badName = "test"badName = "test"badName = "test"
I = 1  
O = 0  


class bad_class: 
    def __init__(self,x=42 ):  
        self._x=x
        
    def PublicMethod(self):  
        
        missing blank line'''
        if self._x==None:  
            print("None")
        elif type(self._x)==int:  
            print(self._x+1)
        else:print("Bad")  


def undocumented_func(param1,param2=[]):
    if param1: return param2  
    


filename = "test.txt"
if filename[:5] == "test_":  
    pass


def check_type(obj):
    return type(obj) == str  


def risky_operation():
    try:
        f = open("file.txt")
        data = f.read()
    except (FileNotFoundError, PermissionError):
        pass
    finally:
        f.close()


double = lambda x: x * 2 


[print(x) for x in range(10)]  


bad_class ().PublicMethod( )


text = "hello"
print(text [1:3] )


if x == None or x == True:
    pas


d = {'key': 'value}
if 'key' in d:  
    pas
