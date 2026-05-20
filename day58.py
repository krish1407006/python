# Generator in python

# A generator is a special type of iterator that allows you to iterate over a sequence of values without storing them all in memory at once.
# Generators are defined using a function and the yield statement.


def count_up_to(n):
    count = 1
    while count <= n:
        yield count  # Yield the current count value
        count += 1  # Increment the count

# Create a generator object

counter = count_up_to(5)
print(next(counter))  # Output: 1
# Iterate through the generator

