"""
Program: employee.py
Author:  Luke Xiong
Date: 7/4/2020

This program is
.
"""
#class Employee(object):
 #   TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    #def __init__(self, title, name, surname, allowed_titles=TITLES):
        #if title not in allowed_titles:
            #raise ValueError("%s is not a valid title."% title)

        #self.title = title
        #self.name = name
       # self.surname = surname

class Employee:

    def __init__(self, lname, fname):
        self.last_name = lname
        self.first_name = fname

    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname

    def display(self):
        return str(self.last_name) + ", " + str(self.first_name)

    def __str__(self):
        return 'Person with last name ' + str(self.last_name) + ', first name ' + str(self.first_name)
#driver
emp = Employee('Ruiz', 'Matthew') #call the constructor
print(emp.display())
emp.set_first_name('Matt')
print(emp.display()) #display returns a str
del emp #clean up

