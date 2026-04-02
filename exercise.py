import time 
name = input("What is your name? ")
recenttime=time.strftime("%H:%M:%S", time.localtime())
print("Hello",name,"the current time is",recenttime)
if(recenttime>="04:00:00" and recenttime<"12:00:00"):
    print("goodmorning sir")
elif(recenttime>="12:00:00" and recenttime<"17:00:00"):
    print("goodafternoon sir")
elif(recenttime>="17:00:00" and recenttime<"21:00:00"):
    print("goodevening sir")
else:    print("goodnight sir")