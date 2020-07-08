"""
Program: class_composition.py
Author:  Luke Xiong
Date: 7/7/2020

create a class with a data member of the type of a class you defined

"""
import class_definitions
from class_definitions import student
from class_definitions.student import Student, Address, GPA, Major


class Person(Student):
    def __init__(self, lname, fname, addy=''): #default values
        super().__init__() #call bass constructor
        self._last_name = lname
        self._first_name = fname
        self._address = addy

    def display(self):
        return str(self._last_name + ' ' + self._first_name +":" + self._address)

#Add attribute major, default value 'Computer Science'
#Add attribute gpa, default value '0.0'
#Add attribute student_id, not optional

#driver
my_student = Student('Song', 'River')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
print(my_student.display())
del my_student

#method override display
addy2 = Address('456', 'First', 'Street', 'Small Town', 'Iowa', 22222)
student1 = Student('Holmes', 'Murphy', addy2)
gpa2 = GPA(3.0)
major2 = Major('Being kind of Awesome!')
print(student1.display(student1, addy2, gpa2, major2))
