# Rock Paper Scissors Game


import random

print("Welcome to Rock Paper Scissors Game!")
choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter your choice (rock, paper, scissors) or 'exit' to quit: ").lower()
    if user_choice == 'exit':
        print("Thanks for playing!")
        break

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    if user_choice in choices:
        print(f"You chose {user_choice}")
    computer_choice = random.choice(choices)



    print(f"Computer chose {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):

        print("You win!")
    else:
        print("Computer wins!") 
