# raise error in python


a = input("Enter the value butween 5 and 9: ")

if (a == "quit"):
  


  print("ohk")


elif (int(a) < 5 or int(a) > 9):
  

  raise ValueError("The number should be between 5 and 9")

else:
  print("you entered the correct number")