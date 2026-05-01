# Map , Filter , Reduce in Python

# Map

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


# Filter

def is_even(a):
    return a > 4
even_numbers = list(filter(is_even, numbers))
print(even_numbers) 

even_numbers = list(filter(lambda x: x > 4, numbers))
print(even_numbers)