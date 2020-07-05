"""
Program: invoice.py
Author:  Luke Xiong
Date: 7/4/2020

This program is a Customer class with the following data members, which are identified as required or optional in the constructor.
The class is simply the blueprint for creating objects and had methods that may or may not be used for that object.

"""
import collections


class Invoice:
    """
        :param invoice_id: dictionary of a single key (string) value (double)
        :param customer_id: this is the customer #
        :param last_name - customers last name
        :param first_name - customers first name
        :param phone_number - customers phone number
        :param address - customer address
        :returns: this is what is returned
        :raises keyError: raises an exception
        """
    #constructor
    def __init__(self, invoice, cid, last_name, first_name, phone_number, address, items, price):
        #invoice_id - required string
        #customer_id - required
        #last_name - required string
        #first_name - required string
        #phone_number - required string
        #address - required: string
        #items_with_price - dictionary optional
            #since this is optional, how do we default to a "blank"
            # or empty dictionary?
        self.invoice_id = invoice
        self.customer_id = cid
        self.last_name = last_name #last_name - required string
        self.first_name = first_name #first_name - required string
        self.phone_number = phone_number #phone_number - required string
        self.address = address #address - required: string
        self.items_with_price = items
        self.price = price

    def get_invoice_id(self):
        return self._invoice_id

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

    def get_items_with_price(self, items):
        return self._items

    def get_price(self):
        return self._price
    #setters
    def set_invoice_id(self, invoice):
        if invoice.isinstance():
            raise ValueError
        self.invoice_id = invoice

    def set_customer_id(self, cid):
        if cid.isinstance():
            raise ValueError
        self.customer_id = cid

    def set_last_name(self, lname):
        if lname.isdigit():
            raise ValueError
        self.last_name = lname

    def set_first_name(self, fname):
        if fname.isdigit():
            raise ValueError
        self.first_name = fname

    def set_address(self, address):
        self.address = address

    def set_phone(self, phone):
        self.phone = phone

    def set_price(self, price):
        if price.isinstance():
            raise ValueError
        self._price = price

    def set_items_with_price(self, items):
        if items.isdigit():
            raise ValueError
        self.items_with_price = items

    @staticmethod
    def add_item(items, price):
        """
        :param item: dictionary of a single key (string) value (double)
        :param price: this is what the second parameter represents
        :returns: dictionary of items with price
        :raises keyError: raises an exception
        """
        #storedict={items}
        full_list=[]
        #price = 0.00
        #storedict[items] = price
        for n in items:
            storedict=collections.defaultdict(dict)
            storedict[items][price] = str(n)
            full_list.append(storedict)
        return storedict

        #add_item() that adds an item to
        #items_with_price dictionary (Recall: what is the dictionary function to add?)

    def create_invoice(add_item):
        """
        :param item_to_add: dictionary of a single key (string) value (double)
        :param customer_id: this is what the second parameter represents
        :returns: this is what is returned
        :raises keyError: raises an exception
        """
        #create_invoice() that prints each item and price, then a total with tax calculated
        storedict={}
        #subtotal = 0
        #loop over each k, v pair in items_with_price
            #print str(key) + '....$' + str(value)
        #at the end of the loop we have the sum of all values
        subtotal = sum(storedict.values())
        tax = 0.06
        tax_owed = subtotal*tax
        total = tax_owed + subtotal
        print('Tax: ' + tax_owed)
        print('Total: '+ total)

    def display(self):
        return self.invoice_id, self.customer_id, self.first_name, self.last_name, self.phone_number, self.address, self.items_with_price, self.price

    def __str__(self):
        return str(self.invoice_id, self.customer_id, self.first_name, self.last_name, self.phone_number, self.address, self.items_with_price, self.price)

    def __repr__(self):
        return str(self.invoice_id, self.customer_id, self.first_name, self.last_name, self.phone_number, self.address, self.items_with_price, self.price)
#driver
if __name__=='__main__':
    invoice = Invoice(1, 123, 'William', 'Ryan', '515-444-3333', '1313 DisneyLand Dr, anaheim, CA 92802', 'Mouse', 9.99)
    #print(invoice)
    #invoice.add_item({'1Pad' : 799.99})
    #invoice.add_item({'Surface': 999.99})
    #invoice.create_invoice()
    #print(invoice.display()) this one works
    add = {'1Pad' : 799.99}
    sub = '1Pad', 799
    print(invoice.add_item(add))


