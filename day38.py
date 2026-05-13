# getters and setters in python

class Person:
    def __init__(self, name, age):
        self._name = name  # Using a single underscore to indicate that this is a "protected" attribute
        self._age = age
    @property
    def name(self):

        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and value:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >= 0:
            self._age = value
        else:
            raise ValueError("Age must be a non-negative integer")
person = Person("John", 25)
print(person.name)  # Output: John