def generate_username(choice):
    username = ""
    # vowels = ['a', 'e', 'i', 'o', 'u']

    if choice == 1:
        name = input("Enter name/nickname: ").lower()
        lastname = input("Enter last name: ").lower()
        birthday = input("Enter birth-date (only day): ")

        for letter in name:
            # if letter in vowels:
            #     letter = letter.upper()
            username += letter

        username = username + "_"

        for letter in lastname:
            # if letter in vowels:
            #     letter = letter.capitalize()
            username += letter

        username = username + "_" + birthday

    elif choice == 2:
        fav_adj = input("Enter adjective: ").lower()
        fav_animal = input("Enter your favourite animal/cartoon/character: ").lower()
        fav_num = input("Enter your favourite number: ")

        username = fav_adj + "_" + fav_animal + "_" + fav_num

    else:
        raise ValueError("Invalid input!")

    return username


if __name__ == "__main__":
    choice = int(input("Do you want to generate a username with your name (1) or username without your name (2): "))
    username = generate_username(choice)
    print(username)
