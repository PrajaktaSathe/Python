def leap_check(year) -> str:
    """Check if a year is a leap year.

    :return: A string telling us weather or not it is a leap year.
    """

    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return f"{year} is a leap year!"
    else:
        return f"{year} is not a leap year!"


if __name__ == "__main__":
    print("<-- Leap Year Checker -->")
    print("This program will check if a year you input is a leap year.")

    run = True

    while run:  # Runs once before user intervention.
        print("Enter a year.")
        _input = input("--> ")

        try:
            input_year = int(_input)
        except ValueError:
            raise ValueError("Year must be an integer.")

        print(leap_check(input_year))

        print("-" * 30)  # decoration

        print("Would you like to check another year? [Y/N]")
        _input = input("--> ").lower()

        while _input not in ["y", "n"]:
            _input = input("--> ").lower()

        if _input == "n":
            run = False

        print("-" * 30)
