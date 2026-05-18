# Walrus operator in python


# The walrus operator (:=) is a new assignment expression introduced in Python 3.8. It allows you to assign a value to a variable as part of an expression. This can be useful for reducing the number of lines of code and improving readability.

# Example 1: Using the walrus operator in a while loop

# Without walrus operator

count = 0
while count < 5:
    print(count)
    count += 1

# With walrus operator

count = 0
while (count := count + 1) < 5:
    print(count)
    
