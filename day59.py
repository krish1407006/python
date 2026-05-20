# function catching in python

from functools import lru_cache
import time

@lru_cache(maxsize=None)  # Cache results of the function
def a(n):
    time.sleep(6)
    return n*5

# Test the function
print(a(10))  # Output: 55
print(a(20))  # Output: 6765    
