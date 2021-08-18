# import random module -
import random

# initialize user_input to 1 -
roll = True

# continue to "roll" die until user wants to stop -
while roll:
    print("Dice numbers: ", random.randint(1, 6))  # print a random number from the list dice_numbers
    user_input = input("Enter 1 to continue, 0 to stop: ")  # take user input i.e. whether he wants to continue
    # or stop
    if user_input == "0":
        roll = False
