# take user input of year -
year = int(input("Enter a year to check if leap year or not: "))

# initialize user_input to 1 -
user_input = 1

# continue until the user wants to stop - 
while (user_input == 1):
    # check condition of leap year -
    if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
        print("Entered year is a leap year!")
        user_input = int(input("Do you want to continue?(1 for yes, 0 to stop): "))
        if (user_input == 1):
            year = int(input("Enter a year to check if leap year or not: "))
    else:
        print("Entered year is not a leap year!")
        user_input = int(input("Do you want to continue?(1 for yes, 0 to stop): "))
        if (user_input == 1):
            year = int(input("Enter a year to check if leap year or not: "))