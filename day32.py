# lambda function

def add(x, y):
    return x + y

add  = lambda x, y: x + y

avg = lambda x, y: x + y /2

print(add(2, 3))          # Output: 5
print(add(2, 3))   # Output: 5

print(avg(2, 3))   # Output: 2.5




def func(fx , value):
    return 6 + fx(value)
print(func(lambda x: x * x, 3))   # Output: 15