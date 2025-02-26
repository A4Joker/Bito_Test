import jpype
import jpype.imports
import os
 
class PythonCalculator:
    def __init__(self):
        if not jpype.isJVMStarted():
             current_dir = os.path.abspath(os.path.dirname(__file__))
             jpype.startJVM(classpath=[current_dir])
         self.java_calculator = jpype.JClass('SimpleCalculator')()
 
     def multiply(self, x: int, y: int) -> int:
         return x * y
 
     def add_using_java(self, x: int, y: int) -> int:
         return self.java_calculator.add(x, y)
