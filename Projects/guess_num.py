# Guessing game - 
import random

def guess_num():
    random_num = random.randint(1, 100)
    guess = 0
    while guess != random_num:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess > random_num:
            print("Nope! Guessed number is too high!")
        elif guess < random_num:
            print("Nope! Guessed number is too low!")
    print("Yay!!! You guessed the number correctly!!")

guess_num()