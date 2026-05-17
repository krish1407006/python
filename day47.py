# magic and dunder methods in python

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    

p1 = person("Alice",30)
print(p1)  # this will call the __str__ method of the person class

print(repr(p1))  # this will call the __repr__ method of the person class

def __repr__(self):
    return f"person(name='{self.name}', age={self.age})"

p1 = person("Alice",30)
print(repr(p1))  # this will call the __repr__ method of the person class