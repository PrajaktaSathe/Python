def add_number(phone_numbers: dict, name: str, num) -> dict:
    """Function to add/update number to the list (dictionary)."""

    name.capitalize()

    # if statement checks if the number entered is numeric and 10 digits long -
    if num.isnumeric() and num.__len__() == 10:
        phone_numbers.update({name: num})
        print("Entry added to contact list!")
    else:
        print("You have entered the number incorrectly!")

    return phone_numbers


def search(phone_numbers: dict, name: str):
    """Function to search for a number using a specific name."""

    if name in phone_numbers:
        print(phone_numbers[name])
    else:
        print("Name and number not found!")


def display_list(phone_numbers: dict):
    """Function to display the dictionary."""

    print(phone_numbers)


if __name__ == "__main__":
    # create an empty dictionary -
    phone_numbers_dict = {}

    run = True
    while run:
        user_input_choice = int(input("Enter 1 to add/update number, 2 to search for a number, 3 to display list: "))

        if user_input_choice == 1:
            user_input_name = input("Enter name: ").capitalize()
            user_input_num = input("Enter number: ")
            phone_numbers_dict = add_number(phone_numbers_dict, user_input_name, user_input_num)
        elif user_input_choice == 2:
            user_input_name = input("Enter name to search: ").capitalize()
            search(phone_numbers_dict, user_input_name)
        elif user_input_choice == 3:
            display_list(phone_numbers_dict)
        else:
            print("Invalid input!")

        choice = input("Do you want to continue? (1: continue/0: stop): ")

        if choice == "0":
            run = False
