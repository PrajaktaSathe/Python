# calculator function - which when called will function as a calculator
def calculator(choice: int) -> str:
    """A basic calculator function.

     :return: The result of the calculation as a string.
     """

    # addition
    if choice == 1:
        num1 = float(input("1st number --> "))
        num2 = float(input("2nd number --> "))
        return f"{num1} + {num2} = {num1 + num2}"

    # subtraction
    elif choice == 2:
        num1 = float(input("1st number --> "))
        num2 = float(input("2nd number --> "))
        return f"{num1} - {num2} = {num1 - num2}"

    # multiplication
    elif choice == 3:
        num1 = float(input("1st number --> "))
        num2 = float(input("2nd number --> "))
        return f"{num1} x {num2} = {num1 * num2}"

    # division
    elif choice == 4:
        num1 = float(input("Dividend --> "))
        num2 = float(input("Divisor  --> "))
        # try-except which checks if divisor is zero (which isn't allowed)
        try:
            return f"{num1} ÷ {num2} = {num1 / num2}"
        except ZeroDivisionError:
            return f"{num1} ÷ {num2} = Error: Division by 0!"

    # power
    elif choice == 5:
        num = float(input("Number --> "))
        power = float(input("Power --> "))
        return f"{num} ^ {power} = {num ** power}"

    # root
    elif choice == 6:
        num = float(input("Number --> "))
        return f"√{num} = {num ** (1 / 2)}"

    else:
        return "Invalid input!!"


if __name__ == "__main__":
    print("<-- Basic Calculator -->")
    print("Does what it says on the tin!")
    print("-" * 30)  # decoration

    run = 'Y'
    while run == 'Y':
        print("Options:")

        print("\t[1] Add")
        print("\t[2] Subtract")
        print("\t[3] Multiply")
        print("\t[4] Divide")
        print("\t[5] Power)")
        print("\t[6] Square root")

        choice = int(input("--> "))  # take option input from user

        result = calculator(choice)

        print(result)

        print("-" * 30)

        print("Would you like calculate more?")
        print("\t[Y] Yes")
        print("\t[N] No")

        _input = input("--> ").upper()

        while _input not in ["y", "n"]:
            _input = input("--> ").lower()

        if _input == "n":
            run = False

        print("-" * 30)
