"""
Program: multi-inheritance.py
Author:  Luke Xiong
Date: 7/8/2020

Write a class Manager that inherits from Person and Employee

"""

from _datetime import datetime


class Employee:

    def __init__(self, lname, fname, address, phone_number, start_date, salary):
        self.last_name = lname
        self.first_name = fname
        self.address = address
        self.phone_number = phone_number
        self._start_date = datetime.strptime(start_date, '%b %d %Y')
        self.salary = salary

    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname

    def set_address(self, address):
        self.address = address

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_start_date(self, start_date):
        self._start_date = datetime.strptime(start_date, '%b %d %Y')

    def set_salary(self, salary):
        self.salary = salary

    def display(self):
        return str(self.last_name) + ", " + str(self.first_name) + '\n' + str(self.address) + '\n' + str(self.phone_number) + '\n' + 'Start Date: ' + str(self._start_date) + '\n' + 'Starting Salary: $' + str(self.salary)

    def __str__(self):
        return 'Person with last name ' + str(self.last_name) + ', first name ' + str(self.first_name) + '\n' + str(self.address) + '\n' + str(self.phone_number) + '\n' + str(self._start_date) + '\n' + str(self.salary)



class Manager:
    #def __init__(self, lname, fname, address, phone_number, start_date, hourly, department, direct_report): #default values
    def __init__(self, department, direct_report): #default values
        #super().__init__(lname, fname, address, phone_number) #call bass constructor
        #self._start_date = datetime.strptime(start_date, '%b %d %Y')
        #self._hourly = hourly
        self._department = department
        self.direct_report = direct_report

    #def give_raise(self, salary):
        #self._salary = salary

    def list_of_reports(self, direct_report):
        return self.direct_report

    def display(self):
        return 'Department: ' + self._department + '\n' + 'Direct Reports: ' + str(self.direct_report)

    def str(self):
        return 'Department: ' + self._department + '\n' + 'Direct Reports: ' + str(self.direct_report)

    def __repr__(self):
        pass

class DerivedClassName(Employee, Manager):
    #can't get my derived class to cooperate

    def __init__(self, last_name, first_name, address, phone_number, start_date, salary, department, direct_report): #default values
        #super().__init__(self, last_name, first_name, address, phone_number, start_date, salary, department, direct_report) #call bass constructor
        #super(Manager).__init__(department, direct_report)
        pass

    def display(self):
        return self.last_name + ' '+ self.first_name + '\n' + self.address + '\n' + self.phone_number + '\n' + str(self._start_date) + '\n' + '$' + str(self.salary + '\n' + 'Department: ' + self._department + '\n' + self.direct_report)

    def str(self):
        return self.last_name + ' '+ self.first_name + '\n' + self.address + '\n' + self.phone_number + '\n' + str(self._start_date) + '\n' + '$' + str(self.salary + '\n' + 'Department: ' + self._department + '\n' + self.direct_report)

#Creates a Manager  object (select a meaningful name) with your name, start date today, starting salary $40,000
manager1 = Employee('McDonald', 'Ronald', '1 Main St, York, PA', '787-000-1234', 'Jul 8 2020', 40000.00)
dict={1:'John', 2:'Joe'}
manager2 = Manager('Accounting', dict)
manager3 = DerivedClassName('McDonald', 'Ronald', '1 Main St, York, PA', '787-000-1234', 'Jul 8 2020', 40000.00, 'Accounting', dict)
#Displays the Manager object  # include a comment on which display() was used
print(Employee.display(manager1))
#Displays the Manager object's direct_reports
print(Manager.display(manager2))
#Change salary to $42,000
manager1.set_salary(42000.00)
print(Employee.display(manager1))
#Displays the Manager object  # include a comment on which display() was used
print(DerivedClassName.display(manager3))
#tried using the display() from derivedclassname class to print
#Performs garbage
#del manager1

#Displays the Manager object  # include a comment on which display() was used
