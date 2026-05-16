# finally clause in python

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


#finally clause is used to execute some code no matter what happens in the try block.
#  It is used to clean up resources or to perform some actions that must be executed regardless of whether an exception occurred or not.