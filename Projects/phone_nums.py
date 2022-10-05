# create an empty dictionary -
phone_nums_dict = {}


# function to add/update number to the list(dictionary) -
def add_num(name, num):
    name.capitalize()
    # if statement checks if the number entered is numeric and 10 digits long -
    if (num.isnumeric() and num.__len__() == 10):
        phone_nums_dict.update({name: num})
        print("Entry added to contact list!")
    else:
        print("You have entered the number incorrectly!")


# function to search for a number using a specific name -
def search(name):
    if (name in phone_nums_dict):
        print(phone_nums_dict[name])
    else:
        print("Name and number not found!")


# function to display the dictionary -
def display_list():
    print(phone_nums_dict)


choice = 1
while (choice == 1):
    user_input_choice = int(
        input(
            "Enter 1 to add/update number, 2 to search for a number, 3 to display list: "
        ))
    if (user_input_choice == 1):
        user_input_name = input("Enter name: ").capitalize()
        user_input_num = input("Enter number: ")
        add_num(user_input_name, user_input_num)
    elif (user_input_choice == 2):
        user_input_name = input("Enter name to search: ").capitalize()
        search(user_input_name)
    elif (user_input_choice == 3):
        display_list()
    else:
        print("Invalid input!")
    choice = int(input("Do you want to continue? (1: continue/0: stop): "))
