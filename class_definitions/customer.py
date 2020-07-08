"""
Program: customer.py
Author:  Luke Xiong
Date: 7/4/2020

This program is a Customer class with the following data members, which are identified as required or optional in the constructor.
The class is simply the blueprint for creating objects and had methods that may or may not be used for that object.

"""
class Customer:
    #constructor
    def __init__(self, cid, last_name, first_name, phone_number, address):
        self.customer_id = cid
        self.last_name = last_name #last_name - required string
        self.first_name = first_name #first_name - required string
        self.phone_number = phone_number #phone_number - required string
        self.address = address #address - required: string
    #getters
    def get_customer_id(self):
        return self._customer_id

    def get_last_name(self):
        return self._last_name

    def get_first_name(self, fname):
        return self._first_name

    def get_address(self, address):
        return self._address

    def get_phone(self, phone):
        return self._phone
    #setters
    def set_customer_id(self, cid):
        self.customer_id = cid

    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname

    def set_address(self, address):
        self.address = address

    def set_phone(self, phone):
        self.phone = phone
    #method
    def add_item(self):
        #display that returns a string of the customer object
        #return self.customer_id
        pass
    #display for printing
    def display(self):
        #return self.customer_id + '\n' + self.first_name + '\n' + self.last_name + '\n' + self.phone + '\n' + self.address
        return 'Customer ID: ' + str(self.customer_id) + '\n' + self.first_name + ' ' + self.last_name + '\n' + self.phone_number + '\n' + self.address

    def __str__(self):
        return (self.customer_id, self.first_name, self.last_name, self.phone_number, self.address)
        #return cust

    def __repr__(self):
        return (self.customer_id, self.first_name, self.last_name, self.phone_number, self.address)

#driver
if __name__=='__main__':
    customer1 = Customer(123, 'Johnson', 'Mike', '515-123-4444', '123 Main Street')
    print(customer1.display())
    try:
        customer2 = Customer('this should fail')
        print(customer2.display())
    except AttributeError:
        print('Successfully errored out!')

#Which method raised the exception? The constructor or the display()? Include in your comments which one!
#the constructor caused the exception because it is missing the required arguments.
