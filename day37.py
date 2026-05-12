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




import logging

logging.basicConfig(level=logging.INFO)

def log_decorator(func):

    def wrapper(*args, **kwargs):
        logging.info(f"Function {func.__name__} is called with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper

@log_decorator
def multiply(a, b):
    return a * b
result = multiply(4, 5)


