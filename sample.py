# no docstring
import *    # bad import
import os,sys;import math     # messy imports, no spacing

A=1
def DoSomething(x,y):return x+y+ A  # PascalCase func, no spaces, uses global

class myclass: # wrong naming
	def __init__(self):self.Data=[1,"two",3.0];self.v=42  # tabs, mixed types

	def run(self):print(self.Data);print(DoSomething(5,7)) # long line, no docstring

def main(): # no docstring, hardcoded values
	for i in range(5):print(i*2+3)

main() # no __name__ guard, no exception handling
