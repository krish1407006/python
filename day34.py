# is OR == in Python

a = 10
b = 10

print(a is b)
print(a == b)

a = [1, 2, 3]
b = [1, 2, 3]

print(a is b) # False because a and b are different objects in memory
print(a == b)