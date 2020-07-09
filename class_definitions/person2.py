"""
Program: person2.py
Author:  Luke Xiong
Date: 7/8/2020

Derived Classes. Created a child and parent class. Child class inherits the attributes
from the parent.
"""

class Person:
    """Person class"""
    def __init__(self, lname, fname, addy=''):
        self._last_name = lname
        self._first_name = fname
        self._address = addy

    def display(self):
        return self._last_name + ", " + self._first_name + ":" + self._address

class Student(Person):
    """Student class"""
    #put the attributes from the parent class in with the child attributes
    def __init__(self, studNo, lname, fname, major='', gpa=0.0):
        super().__init__(lname, fname)
        self._studNo = studNo
        self._major = major
        self._gpa = gpa

    #display both parent and child attributes
    def display(self):
         return self._studNo, self._last_name, self._first_name, self._major, self._gpa


#Driver
my_student = Student(900111111, 'Song', 'River')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
print(my_student.display())
del my_student

