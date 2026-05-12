# Decorator in python


def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        func(*args, **kwargs)
        print("After the function call")
    return wrapper



def add(a, b):
    print(a+ b)
decorator(add)(5, 3)




#

