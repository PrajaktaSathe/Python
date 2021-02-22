# import random module -
import random 

# make a list of numbers on the die -
dice_numbers = [1, 2, 3, 4, 5, 6]

# initialize user_input to 1
user_input = 1

# continue to "roll" die until user wants to stop -
while(user_input == 1):
    print(random.choice(dice_numbers)) # print a random number from the list dice_numbers
    user_input = int(input("Enter 1 to continue, 0 to stop: ")) # take user input i.e. whether he wants to continue or stop
    