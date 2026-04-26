#local variable and global variable
x = 10 #global variable
def hello():

    global x #accessing global variable inside the function

    
    print("hello world")
    x = 4 
    print(x)  
 
hello()

print(x) #accessing global variable outside the function