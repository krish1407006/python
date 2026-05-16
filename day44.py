# class method as alternative constructor in python


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    @classmethod
    def from_string(cls, emp_str):
        name, age, salary = emp_str.split(',')
        return cls(name, int(age), float(salary))
    
emp_str = "Alice,30,50000"
emp1 = Employee.from_string(emp_str)
print(f"Name: {emp1.name}, Age: {emp1.age}, Salary: {emp1.salary}")  # Output: Name: Alice, Age: 30, Salary: 50000.0

