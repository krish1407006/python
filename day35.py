# OOPS in Python

# Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure code.
#  It allows for better organization, reusability, and maintainability of code. In Python, OOP is implemented using classes and objects.

# Class: A class is a blueprint for creating objects. It defines the properties (attributes) and behaviors (methods) that the objects created from the class will have.

# Object: An object is an instance of a class. It is created from a class and can have its own unique values for the attributes defined in the class.

# Example of a simple class and object in Python


class person:
    name = "krish"
    age = 20
    occupation = "student"

    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old and I am a {self.occupation}.")

a = person()  # Creating an object of the person class

a.name = "krishan"
a.age = 21
a.occupation = "software developer"

a.introduce()  # Calling the introduce method of the person class

b = person()  # Creating another object of the person class
b.name = "john"
b.age = 25
b.occupation = "engineer"

b.introduce()  # Calling the introduce method of the person class
