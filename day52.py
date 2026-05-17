# Multilevel inheritence in python


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

class student_person(student):
    def __init__(self,name,age,rollno,grade):
        super().__init__(name,age,rollno)  # calling parent class constructor

        self.grade = grade

    def display(self):
        super().display()  # calling parent class display method
        print("Grade:",self.grade)


s1 = student_person("John",20,101,"A")
s1.display()


