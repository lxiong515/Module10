"""
Program: hourly_employee.py
Author:  Luke Xiong
Date: 7/8/2020

Create two derived classes, SalariedEmployee and HourlyEmployee

"""

import class_definitions
from class_definitions import employee
from class_definitions.employee import Employee
from _datetime import datetime


class Hourly_Employee(Employee):
    def __init__(self, lname, fname, address, phone_number, start_date, hourly): #default values
        super().__init__(lname, fname, address, phone_number) #call bass constructor
        self._start_date = datetime.strptime(start_date, '%b %d %Y')
        self._hourly = hourly

    def give_raise(self, hourly):
        self._hourly = hourly

    def display(self):
        return self.last_name + ' '+ self.first_name + '\n' + self.address + '\n' + self.phone_number + '\n' + str(self._start_date) + '\n' + '$' + str(self._hourly)

    def str(self):
        return self.last_name + ' '+ self.first_name + '\n' + self.address + '\n' + self.phone_number + '\n' + str(self._start_date) + '\n' + '$' + str(self._hourly)

    def __repr__(self):
        pass

if __name__=='__main__':
    #salaried_employee = $40k
    pass
#Creates a SalariedEmployee object (select a meaningful name) with your name, start date today, starting salary $40,000.
emp = Hourly_Employee('Ruiz', 'Matthew', '123 Main St, New York, NY', '555-111-3333', 'Jul 8 2020', 10.00 ) #call the constructor
#Displays the Employee object
print(emp.display())
#Changes hourly_pay to $12.00 an hour
emp.give_raise(12.00)
#Displays the Employee object
print(emp.display())
#Performs garbage
del emp
