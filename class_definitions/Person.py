class Person(object):
    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, title, name, surname, allowed_titles=TITLES):
        if title not in allowed_titles:
            raise ValueError("%s is not a valid title."% title)

        self.title = title
        self.name = name
        self.surname = surname

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, value):
            if value.isdigit():
                raise ValueError
            self._name=value

    def __str__(self):
        return 'Person with last name ' + str(self.surname) + ', first name ' + str(self.name)
#driver
#valid person
person1 = Person('Dr', 'Duck', 'Donald')
print(str(person1))
