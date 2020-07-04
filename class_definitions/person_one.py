import datetime

class Employee(object):

    def __init__(self, fname, lname, address, is_salary, start_date, salary_amount):
        """
        Use reST style
        :param last_name: this is employees last name
        :param first_name: employees first name
        :param address: street address of employee
        :param phone: contact number for employee
        :param salary: confirms if they receive salary
        :param start_date: uses datetime to format start date
        :param salary_amount: total salary of employee
        returns: a string iwth the above parameters
        :raises keyError:
        """

    def __init__(self, fname, lname, address, phone, is_salary, start_date, salary_amount):
        self.last_name = lname
        self.first_name = fname

    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname

    def set_address(self, address):
        self.address = address

    def set_phone(self, phone):
        self.phone = phone

    def set_is_salaried(self, is_salary):
        self.is_salaried = is_salary

    def set_start_date(self, start_date):
        self.start_date = start_date

    def set_salary_amount(self, salary_amount):
        self.salary_amount = salary_amount

        @property
        def first_name(self):
            return self._first_name

        @first_name.setter
        def first_name(self, value):
            if value.isdigit():
                raise ValueError
            self._first_name=value

    def display(self):
        """
        Use reST style
        :param last_name: this is employees last name
        :param first_name: employees first name
        :param address: street address of employee
        :param phone: contact number for employee
        :param is_salary: confirms if they receive salary
        :param start_date: uses datetime to format start date
        :param salary_amount: total salary of employee
        returns: a string that when printed will follow the below format
        :raises keyError:
        """

        #Sasha Patel
        #123 Main Street
        #Urban, Iowa
        #Salaried employee: $40,000/year       # OR Hourly employee: $7.25/hour
        #Start date: 6-28-2019

        #what is a line break or carriage return?
        #line_break # ""whatever that character is
        #space = ' ' #maybe
        #assum address passed in as '123 Main street, Urban, Iowa'
        #or you could assume address has line break passed in
            #'123 Main Street/nUrban, Iowa"
        #output_string = fname + space + lname + line_break + address
        #(or address before first comma + line_break + address after first comma
        #fname + space + lname = line_break
        return(self.first_name, self.last_name, self.address, self.is_salary, self.start_date, self.salary_amount)

    def __str__(self):
        return str(self.first_name, self.last_name, self.address, self.is_salary, self.start_date, self.salary_amount)


    def __repr__(self):
        pass
#driver
#valid person
if __name__ == '__main__':
    employee1 = Employee('Sasha', 'Patel', '123 Main St\n Urban, IA', True, 6-28-2019, 40,000.00)
    #print(employee1)
    #print(str(employee1))
    print(employee1.display())
#, first_name, last_name, address, is_salary, start_date, salary_amount

