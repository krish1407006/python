# kon bnega crorepati
# 15 question

print("welcome to KBC")

list = [ "who is the pm of india" , "what is the largest country in the world" , "what is full form of CPU"]
list2 = ["Modi" , "Russia" , "CPU"]

score = 0
for i in range(3):
    print(list[i])
    answer = input("enter your answer : ")
    if answer == list2[i]:
        print("your answer is correct")
        score = score + 1000
    else:
        print("your answer is wrong")
if score == 3000:
    print("congratulation aap jeet gaye 3000 dhanrashi")
elif score <= 1000:
    print("sorry aap haar gaye")
elif score == 2000:
    print("congratulation aap jeet gaye 2000 dhanrashi")
    
print("your final score is", score)