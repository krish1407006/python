# class method in python

class Employee:
    company_name = "ABC Corporation"
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    @classmethod
    def company(cls):
        print(f"This is a class method. It belongs to the {cls.company_name} and can be called without creating an instance.")

emp1 = Employee("Alice", 30, 50000)
emp1.company()  # Output: This is a class method. It belongs to the ABC Corporation and can be called without creating an instance.
emp1.company()  # Output: This is a class method. It belongs to the apple and can be called without creating an instance.