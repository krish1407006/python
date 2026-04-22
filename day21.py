# sets in python

s = {1, 2, 3, 4, 5}
print(s)

#method of sets

s.add(6)
print(s)    

s.remove(3)
print(s)

s.discard(10) # does not throw error if element is not present
print(s)

s.clear() # removes all elements from the set

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.union(s2)) # returns a new set with all unique elements from both sets
print(s1.intersection(s2)) # returns a new set with elements that are common to