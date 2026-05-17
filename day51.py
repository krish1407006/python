# multiple inheritance in python

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)


class student:
    def __init__(self,rollno):
        self.rollno = rollno

    def display(self):
        print("Roll No:",self.rollno)



class student_person(person,student):
    def __init__(self,name,age,rollno):
        person.__init__(self,name,age)  # calling parent class constructor
        student.__init__(self,rollno)  # calling parent class constructor


s1 = student_person("John",20,101)
s1.display()  # this will call the display method of the student_person class