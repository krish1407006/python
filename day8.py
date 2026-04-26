# Match case statements


x = int(input("Enter the value of X:"))


match x:
    case 1:
        print("x is 1")
    case 6:
        print("x is 6")
    case _ if x >= 50 :
        print(x, "is greater or = to  50")
    case _ if x != 90 :
        print(x, "is less than 50 and greater than 20")
              