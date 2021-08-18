import random

print("Welcome to the choice game!")
name = input("Enter your name: ").lower()
age = int(input("Enter your age: "))
win_lose = ["win", "lose"]

if age >= 16:
    print("You are allowed to play!")
    wants_to_play = input("Do you want to play? (yes/no) ").lower()
    if wants_to_play == "yes":
        print("Let's play!!")
        letter_choice = input("Choose a letter (a/b): ")
        if letter_choice == "a":
            win_or_lose = random.choice(win_lose)
            if win_or_lose == "win":
                left_or_right = input("Good! Choose left or right(left/right): ").lower()
                if left_or_right == "left":
                    win_or_lose_1 = random.choice(win_lose)
                    if win_or_lose_1 == "win":
                        print("Congratulations!! You win!!!")
                    else:
                        print("Sorry! You lose!")
            else:
                print("Sorry! You lose!")
        else:
            win_or_lose = random.choice(win_lose)
            if win_or_lose == "win":
                up_or_down = input("Good! Choose up/down(up/down): ").lower()
                if up_or_down == "up":
                    win_or_lose_1 = random.choice(win_lose)
                    if win_or_lose_1 == "win":
                        print("Congratulations!! You win!!!")
                    else:
                        print("Sorry! You lose!")
            else:
                print("Sorry! You lose!")
    else:
        print("Goodbye!")
else:
    print("Sorry, you aren't allowed to play!")

# if age >= 16:
#     print("You are allowed to play!")
#     wants_to_play = input("Do you want to play? (yes/no) ").lower()
#     if wants_to_play == "yes":
#         print("Let's play!!")
#         letter_choice = input("Choose a letter (a/b): ")
#         if letter_choice == "a":
#             up_or_down = input("Good choice! Do you want to go up or down?(up/down): ").lower()
#             if up_or_down == "up":
#                 print("Congratulations! You Win!")
#             else:
#                 print("Snap! You lost!")
#         else:
#             left_or_right = input("Well chosen! Do you want to go left/right?(left/right) ").lower()
#             if left_or_right == "right":
#                 print("Congratulations! You win!")
#             else:
#                 print("Snap! You lost!")
#     else:
#         print("Goodbye!")
# else:
#     print("Sorry, you aren't allowed to play!")
