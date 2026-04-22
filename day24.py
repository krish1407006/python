# exceptional handling

a = input("enter the number :")

print("multiplication table of {a} is :")
try:
   for i in range(1, 20):
    print(f"{int(a)} X {i} = {int(a) * i}")
except:
  print("enter the valid integer")

