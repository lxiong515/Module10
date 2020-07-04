class Shape:
    colors = ['BLUE', 'GREEN', 'ORANGE', 'PURPLE']

    def __init__(self, color='BLUE'):
        if color not in self.colors:
            raise ValueError
        self.color=color

    def __str__(self):
        return('a '+self.color+' shape')

    def __repr__(self):
        return('shape('+self.color+')')

test=Shape()
test2=Shape('GREEN')
print(test)
print(test2)

        self.last_name = lname
        #last_name: string
        self.first_name = fname
        #first_name: string
        self.address = address
        #address: string
        self.phone = phone
        #phone_number: string
        self.is_salaried = is_salary
        #salaried: boolean
        self.start_date = start_date
        #start_date: datetime
        self.salary_amount = salary_amount
        #salary: double
