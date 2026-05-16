# list method in python
# sort() , insert() , append() , index() , extend() , copy()\


l = [ 1 ,2 ,3 ,4 ,5 ,55, 44, 33 , 22 , 11]

print(l)
# l.sort(reverse=True)


# l.insert(1 , 100)
# print(l)


# l.append(9)
# print(l)

print(l.index(3))

m = [100, 333, 444]
l.extend(m)
print(l)

m = l.copy()
print(m)
