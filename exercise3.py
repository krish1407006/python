   
n = input("do you want to coding or decoding? ")

if n == "coding":
    n1 = input("enter the message you want to code:")
    n2 = n1.split()
    for i in n2:
        if len(i) <= 3:
            print(i[::-1] , end = "  ")
        else:
            print("kkk" + i[1:] + i[0] + "kkk" , end = "  ")
elif n == "decoding":
    n1 = input("enter the message you want to decode:")
    n2 = n1.split()
    for i in n2:
        if len(i) <= 3:
            print(i[::-1] , end = "  ")
        else:
            print("klk" + i[:-4] + i[3:4] + "klk" , end = "  ")