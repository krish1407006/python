# list in python

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
