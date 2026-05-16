# list in python
# list is a collection of items which are ordered and changeable. It allows duplicate members.
# list is defined by using square brackets [] and items are separated by commas.
# list can contain any type of data and can be nested.

list = [1, 2, 3 , 4 , "krish" , True , 7]
print(list)
print(list[2:4])

print(list[2])
print(list[2:])
print(list[:4])

if "krish" and 4 in list:
    print("yes")
else:
    print("no")

if "kr" in "krish":
    print("yes")
else:
    print("no")

lst = [ "hello" , "world" , "python" , "programming"    ]
lst_o = [i for i in lst if "l" in i]
print(lst_o)
