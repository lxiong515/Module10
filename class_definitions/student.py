class Student(object):
    """Student class"""
    def __init__(self, lname, fname):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        num_characters = set("1234567890.")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        #if gpa and not num_characters.student(gpa):
            #raise ValueError
        self.last_name = lname
        self.first_name = fname
        #self.major = major
        #self.gpa = gpa

    def display(self):
        return(self.first_name + ' ' + self.last_name)

class GPA:
    def __init__(self, gpa=0.0):
        num_characters = set("1234567890.")
        if not (num_characters.issuperset(gpa)):
            raise ValueError
        self.gpa=gpa

    def display(self):
        return self.gpa

class Major:
    def __init__(self, major):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(major)):
            raise ValueError
        self.major=major

    def display(self):
        return self.major

class Address:
    def __init__(self, house_num, street, type, city, state, zip):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        num_characters = set("1234567890.")
        if not (name_characters.issuperset(house_num) and name_characters.issuperset(street) and name_characters.issuperset(type) and name_characters.issuperset(city) and name_characters.issuperset(state)):
            raise ValueError
        if not num_characters.issuperset(zip):
            raise ValueError
        self.house_num = house_num
        self.street_name = street
        self.type = type
        self.city = city
        self.state = state
        self.zip = zip

    def display(self):
        return(self.house_num + ' ' + self.street_name +' ' + self.type + '\n' + self.city +', ' +self.state + self.zip)

    def change_major(self):
        #changes major
        change = Major()
        return change

    def update_gpa(self):
        #updates gpa
        update = GPA()
        return update

    def display(self):
        return self.student.display() + '\n' + self.address.display() +'\n'+ self.gpa.display() +'\n'+self.major.display()
        #return Student, Major, GPA, Address
    def __str__(self):
        #return self.last_name + ", " + self.first_name + " has major: " + self.major + " with gpa: " + str(self.gpa)
        return self.student.display() + '\n' + self.address.display() +'\n'+ self.gpa.display() +'\n'+self.major.display()

# Driver
if __name__=='__main__':
    #student1 = Student('Duck', 'Donald', 'Science')
    #print(str(student1))
    #print(str())
    #Creates a student object
    addy1 = Address('123', 'Main', 'Street', 'Small Town', 'Iowa', 11111)
    person1= Student('last', 'first', addy1)
    gpa1 = GPA(4.0)
    major1 = Major('Being Awesome!')
    print(person1.display(person1, addy1, gpa1, major1))
    #displays the student
    addy2 = Address('456', 'First', 'Street', 'Small Town', 'Iowa', 22222)
    person2= Student('Holmes', 'Murphy', addy2)
    gpa2 = GPA(3.0)
    major2 = Major('Being kind of Awesome!')
    print(person2.display(person2, addy2, gpa2, major2))
    #perform garbage collection
    del(addy1, addy2)
    del(person1, person2)


