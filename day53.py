# hybrid and hierarchical inheritance in python

# hierarchical inheritance in python

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
    
class teacher(person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)  # calling parent class constructor

        self.subject = subject
    def display(self):
        super().display()  # calling parent class display method
        print("Subject:",self.subject)

t1 = teacher("Alice",30,"Math")
t1.display()

# hybrid inheritance in python
# Hybrid inheritance is a combination of multiple inheritance and multilevel inheritance.
#  It allows a class to inherit from multiple classes, which can be a combination of single, multiple, and multilevel inheritance.

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
class teacher(person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)  # calling parent class constructor
        self.subject = subject
    def display(self):

        super().display()  # calling parent class display method
        print("Subject:",self.subject)

class student_teacher(student,teacher):
    def __init__(self,name,age,rollno,subject):
        student.__init__(self,name,age,rollno)  # calling student class constructor
        teacher.__init__(self,name,age,subject)  # calling teacher class constructor

s2 = student_teacher("Bob",25,102,"Physics")
s2.display()
