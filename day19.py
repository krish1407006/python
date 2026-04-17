# recursion


def factorial(num):
    if (num == 0 or num == 1):
        return 1
    else:
        return num * factorial(num-1)
    
print(factorial(4))

# fibonacci series

def fibonacci (n):
    f0 = 0
    f1 = 1
    if n == 0:
        return f0
    elif n == 1:
        return f1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

print(fibonacci(4))
