#Python Code Random Option Chooser

#imported random module
import random

print("Hello...! This is random option chooser program. ")

#define a empty list to store options
options = []

#variable for run the infinite while loop
inf = 0

#start the while loop
while inf == 0:
    print("\nChoose a number to continue.")
    print(
        " \t01) Add the options. \n \t02) Choose a random option. \n \t03) How to use. \n \t04) About the program. \n \t05) Exit"
    )
    a = input("Your option : ")

    #if cond. to store options in the list
    if a == "1":
        del options[:]
        c = int(input("\nEnter the number of options : "))

        if c == 0:
            print(
                "\nNumber of options cannot be zero. Please enter more than one option."
            )
            continue
        elif c == 1:
            print(
                "\nYou have enter number of options as one. Please enter more than one option for better performance."
            )
            continue
        else:
            for d in range(c):
                options.append(
                    input("\nEnter the " + str(d + 1) + " option : "))

    #if cond. to choose a random option from the list. Items in the list should be more than two.
    if a == "2":
        e = options[random.randint(0, c - 1)]
        print("\nRandomly chose option for you is : " + e)
        continue

    #How to use print line
    if a == "3":
        print(
            "\nFirst enter number one in the terminal and add your options to the program.\nThen to get a random option, enter number two in the terminal.\nIf you want to edit the options, you can enter number two again and add the options.\nEnter number four to know about the program.\nTo exit from the program enter number five."
        )
        continue

    #About the program print line
    if a == "4":
        print(
            "\nYou can a choose a random option with this program.\nFor a example if you want to choose a random name from a list of name, you can enter those names first and then get a random name without an infleunce from anyone and anything."
        )
        continue

    #exit from the infinite while loop
    if a == "5":
        print("\nThank you for using this program. Good Bye !")
        inf = 1

quit()
