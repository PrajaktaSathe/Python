import random

## The actions possible in the game
actions = ["rock", "paper", "scissors"]
## User makes a selection
while (1):
    print("Welcome to the game")
    user_choice = input(
        "Make your choice (rock ,paper, scissors) or type 'Q' to exit the game : \n"
    )
    computer_choice = random.choice(actions)
    if user_choice == computer_choice:
        print("It is a tie!!!")
    elif user_choice == 'rock':
        if computer_choice == 'paper':
            print(
                f"Computer chose : {computer_choice}. You lose !!! Better luck next time"
            )
        else:
            print(f"Computer chose : {computer_choice}. You Win !!!")
    elif user_choice == 'scissor':
        if computer_choice == "rock":
            print(
                f"Computer chose : {computer_choice}. You lose !!! Better luck next time"
            )
        else:
            print(f"Computer chose : {computer_choice}. You Win !!!")
    elif user_choice == 'paper':
        if computer_choice == 'scissors':
            print(
                f"Computer chose : {computer_choice}. You lose !!! Better luck next time"
            )
        else:
            print(f"Computer chose : {computer_choice}. You win !!!")
    elif user_choice == 'Q':
        break
    else:
        print("Please make a correct choice: (rock, paper, scissors) or 'Q' ")
