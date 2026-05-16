# static method in python

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    @staticmethod
    def company():
        print("This is a static method. It belongs to the class and can be called without creating an instance.")

emp1 = Employee("Alice", 30, 50000)
emp1.company()  # Output: This is a static method. It belongs to the class and can be called without creating an instance.
  


class math:
    def __init__(self, num):
        self.num = num

    def add(self, n):
        self.num = self.num + n

    @staticmethod
    def add_static(a, b):
        return a + b
    
a = math (5)
print(a.num)  # Output: 5
a.add(3)
print(a.num)  # Output: 8
print(math.add_static(3, 4))  # Output: 7
