class Person:
    def __init__(self, name, age, email):
        self._name = name
        self._age = age
        self.__email = email

    @property
    def age(self):
        """ The docstring for the age property """
        print('In age method')
        return self._age

    @age.setter
    def age(self, value):
        print('In set_age method')
        if isinstance(value, int) & value > 0 & value < 120:
            self._age = value

    @property
    def name(self):
        print('In name')
        return self._name

    @name.deleter
    def name(self):
        del self._name

    @property
    def email(self):
        print('In email')
        return self.__email

    @email.setter
    def email(self, value):
        print('In setter email')
        self.__email = value

    def __str__(self):
        return 'Person[' + str(self._name) + '] is ' + str(self._age) + ', email: ' + str(self.__email)


person = Person('John', 54, 'John122133@gmail.com')
print(person)
print(person.age)
print(person.name)
print(person.email)
person.age = 21
person.email = 'John211233@gmail.com'
# person._name = 'Arman'
# person.__email = 'ArmanKazemi1500@gmail.com'
# person._Person__email = 'ArmanKazemi1500@gmail.com'
print(person)
# print(person.__dict__)
