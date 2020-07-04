"""
Program: simple_example.py
Author:  Luke Xiong
Date: 7/4/2020

This program is an example of using class
.
"""

class SimpleExample:
    """A simple example class"""
    max = 256

    def message(self):
        return 'Hello, Classes!'

#driver
simpleObj = SimpleExample() #make a class object
print(simpleObj.max) # access class definition
print(simpleObj.message()) #call class method
del simpleObj
