#dictionary in python


dic = { 566 : "krish" , 567 : "krish2" , 568 : "krish3" }
print(dic.get(567))

print(dic.items())

for key , value in dic.items():
    print(key, value)


#method of dictionary
# update method in dictionary

ep = { 699 : 87 , 700 : 88, 210 : 99 }

ep2 = {299 : 99 , 777 : 88}

ep.update(ep2)
print(ep)

# clear method in dictionary

ep.clear()
print(ep)

#pop method in dictionary

ep3 = { 699 : 87 , 700 : 88, 210 : 99 }
ep3.pop(699)
print(ep3)

#popitem method in dictionary

ep3.popitem() # removes the last item from the dictionary
print(ep3)

#copy method in dictionary

ep4 = ep3.copy()
print(ep4)

#fromkeys method in dictionary

keys = [1, 2, 3]
values = "krish"
dic_fromkeys = dict.fromkeys(keys, values)
print(dic_fromkeys)

