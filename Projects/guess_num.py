# Guessing game -

# importing random module -
import random

print("Welcome to the guess-the-number game!!")
print("You have 10 chances to begin with!")


# function which implements the game -
def guess_num():
    # random number from 1 to 100 is stored -
    random_num = random.randint(1, 100)
    # choices variable is set to 10 -
    chances = 10
    # guess variable is set to 0 -
    guess = 0
    while guess != random_num or chances == 0:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess > random_num:
            print("Nope! Guessed number is too high!")
            chances -= 1
            print("You have " + str(chances) + " chance(s) left!")
        elif guess < random_num:
            print("Nope! Guessed number is too low!")
            chances -= 1
            print("You have " + str(chances) + " chance(s) left!")
        else:
            print("Yay!! You guessed the number correctly!!")


guess_num()
