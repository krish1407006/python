# constructor in python

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}") 

emp1 = Employee("Alice", 30, 50000)
emp1.display()  # Output: Name: Alice, Age: 30, Salary: 50000   

