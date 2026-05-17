# method overriding in python

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

class student(person):
    def __init__(self,name,age,rollno):
        super().__init__(name,age)  # calling parent class constructor

        self.rollno = rollno
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Roll No:",self.rollno)   

s1 = student("John",20,101)
s1.display()
