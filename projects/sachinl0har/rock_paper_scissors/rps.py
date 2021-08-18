from os import system
import random


def play():
    while True:
        player = int(input("\n1. ROCK \n2. PAPER \n3. SCISSORS \n4. End Game \nEnter Your Choice: \n"))
        if player == 1 or player == 2 or player == 3 or player == 4:
            alpha = random.randint(1, 3)
            if alpha == 1 and player == 1:
                print("\nALPHA: Rock\nYou: Rock\nTIE\n")
            elif alpha == 2 and player == 2:
                print("\nALPHA: Paper\nYou: Paper\nTIE\n")
            elif alpha == 3 and player == 3:
                print("\nALPHA: Scissors\nYou: Scissors\nTIE\n")
            elif alpha == 2 and player == 1:
                print("\nALPHA: Paper\nYou: Rock\nALPHA WON!!\n")
            elif alpha == 3 and player == 2:
                print("\nALPHA: Scissors\nYou: Paper\nALPHA WON!!\n")
            elif alpha == 1 and player == 3:
                print("\nALPHA: Rock\nYou: Scissors\nALPHA WON!!\n")
            elif alpha == 2 and player == 3:
                print("\nALPHA: Paper\nYou: Scissors\nYOU WON!!\n")
            elif alpha == 3 and player == 1:
                print("\nALPHA: Scissors\nYou: Rock\nYOU WON!!\n")
            elif alpha == 1 and player == 2:
                print("\nALPHA: Rock\nYou: Paper\nYOU WON!!\n")
            elif player == 4:
                self_exit()
        else:
            print("\nInvalid Input!!\n")


def how():
    print(
        "\n\nHow to Play\n\nWhen its time to play, you and ALPHA will each form one of the three objects either rock, "
        "paper or scissors. You will then name a winner based on which object you both played.\nFor instance, "
        "rock crushes scissors but is covered by paper, paper covers rock but is cut by scissors, and scissors is "
        "crushed by rock but cuts paper. The player who picks the stronger of the two objects is the winner.\n")
    input("\nPress any key to go Back: \n")


def about():
    print(
        "\n\nAbout\n\nRock, Paper, Scissors (aka \"Ro-Sham-Bo\"; janken; \"Bato, Bato, Pick\"; and \"Scissors, Paper, "
        "Stone\") is a simple hand game with many names and variations. It is played around the world and is commonly "
        "used as a way of coming to decisions. In some cases is even played for sport.\nThis is a Basic Rock, "
        "Paper and Scissors Game Program in Python.\nGame Developed by sachinl0har.\n\n@copyrights All Rights "
        "Reserved\n")
    input("\nPress any key to go Back: \n")


def self_exit():
    """Closes the program."""

    print("\n\nThanks For Playing\n\n")
    exit()


def main():
    system('cls')
    choice = int(input("1. Play Game \n2. How to play? \n3. About \n4. Exit \nEnter your choice: \n"))

    # An interesting implementation of case switch in python!
    switcher = {
        1: play,
        2: how,
        3: about,
        4: self_exit
    }
    func = switcher.get(choice)

    system('cls')
    return func()


if __name__ == "__main__":
    while True:
        main()
