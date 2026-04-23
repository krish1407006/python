# finally clause in pyhton

def funct():
    try:
        l = [1,2,3,]
        i = int(input("enter the index of list : "  ))

        print(l[i])
    except:
        print("some error occured")

    finally:
        print("this will always execute")

x = funct()
print(x)