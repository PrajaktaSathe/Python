print("<-- Basic Calculator -->")
print("Options:\n\t[1] Add \n\t[2] Subtract \n\t[3] Multiply \n\t[4] Divide \n\t[5] Square root")
ch = int(input("\t--> "))
if ch == 1:
    num1 = float(input("1st number --> "))
    num2 = float(input("2nd number --> "))
    print(f"{num1} + {num2} = {num1 + num2}")
elif ch == 2:
    num1 = float(input("1st number --> "))
    num2 = float(input("2nd number --> "))
    print(f"{num1} - {num2} = {num1 - num2}")
elif ch == 3:
    num1 = float(input("1st number --> "))
    num2 = float(input("2nd number --> "))
    print(f"{num1} * {num2} = {num1 * num2}")
elif ch == 4:
    num1 = float(input("Dividend --> "))
    num2 = float(input("Divisor --> "))
    print(f"{num1} ÷ {num2} = {num1 / num2}")
elif ch == 5:
    num1 = float(input("1st number --> "))
    print(f"√{num1} = {num1**(1/2)}") 
else:
    print("Invalid input!!")
