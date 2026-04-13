# if else statements example

a = int(input("enter your age:")) 
print("your age is:",a)
if (a>18):
 print("you can drive")
else:
 print("you cannot drive")

 #conditional operators
 #>, <, >=, <=, ==, !=

#  print (a>18)
#  print (a<18)
#  print (a>=18)  
#  print (a<=18)
#  print (a==18)
#  print (a!=18)

#elif statement example

num = int(input("enter the number:"))

if (num>0):
 print("number is positive")
elif (num==0):
 print("number is zero")
else:
    print("number is negative")


#nested if else statement example

num1 = int(input("enter the number"))
if(num1>0):
      print("number is positive")
elif(num1<0):
      print("number is negative")
      if(num1<=10):
        print("number is less than or equal to 10")
      elif(num1>10 and num1<20):
        print("number is greater than 10 and less than 20")
      else:       print("number is greater than or equal to 20")
else:      print("number is zero")