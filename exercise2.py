# kon bnega crorepati
# 15 question

print("welcome to KBC")

questions =[ ["what is the capital of india ?","delhi" ,"punjab" ,"mumbai" ,"kolkata" , 1],
             ["what is the capital of russia ?","moscow" ,"stpetersburg" ,"novosibirsk" ,"yekaterinburg" , 1],
             ["what is the capital of china ?","beijing" ,"shanghai" ,"guangzhou" ,"shenzhen" , 1],
             ["what is the capital of pakistan ?","islamabad" ,"karachi" ,"lahore" ,"faisalabad" , 1] ]

levels = [1000, 5000, 10000, 50000]

for i in range(0 , len(questions)):
    print("for Rs.",levels[i])
    print(questions[i][0])
    print("1.",questions[i][1])
    print("2.",questions[i][2])
    print("3.",questions[i][3])
    print("4.",questions[i][4])

    ans = int(input("enter the option : "))

    if(ans == questions[i][5]):
        print("congratulations you won Rs.",levels[i])
    else:
        print("sorry you lost")
        break
    