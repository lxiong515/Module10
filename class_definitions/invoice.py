class Invoice:
    """
        :param invoice_id: dictionary of a single key (string) value (double)
        :param customer_id: this is what the second parameter represents
        :param last_name -
        :param first_name -
        :param phone_number -
        :param address -
        :returns: this is what is returned
        :raises keyError: raises an exception
        """
    #constructor
    def __init_(self):
        #invoice_id - required string
        #customer_id - required
        #last_name - required string
        #first_name - required string
        #phone_number - required string
        #address - required: string
        #items_with_price - dictionary optional
            #since this is optional, how do we default to a "blank"
            # or empty dictionary?

    def add_item(input_dictionary):
        """
        :param item_to_add: dictionary of a single key (string) value (double)
        :param customer_id: this is what the second parameter represents
        :returns: this is what is returned
        :raises keyError: raises an exception
        """
        pass

    def create_invoice(self):
        """
        :param item_to_add: dictionary of a single key (string) value (double)
        :param customer_id: this is what the second parameter represents
        :returns: this is what is returned
        :raises keyError: raises an exception
        """

        #subtotal = 0
        #loop over each k, v pair in items_with_price
            #print str(key) + '....$' + str(value)
        #at the end of the loop we have the sum of all values
        #tax = 6%
        #tax_owed = subtotal times tax
        #total is tax_owed + subtotal
        #print our tax #Tax.....108.00
        #print our total #Total.............1907.98
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass
#driver
if __name__=='__main__':
    invoice = Invoice(1, 123, '1313 DisneyLand Dr, anaheim, CA 92802', 'Mouse')
    invoice.add_item({'1Pad' : 799.99})
    invoice.add_item({'Surface': 999.99})
    invoice.create_invoice()
