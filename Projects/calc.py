ch = int(input("1: Add \n2: Subtract \n3: Multiply \n4: Divide \n5: Square root \nEnter your choice: "))
if ch == 1:
    num1 = float(input("Enter number: "))
    num2 = float(input("Enter number: "))
    print("Addition: " + str(num1 + num2))
elif ch == 2:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Subtraction: " + str(num1 - num2))
elif ch == 3:
    num1 = float(input("Enter number: "))
    num2 = float(input("Enter number: "))
    print("Multiplication: " + str(num1 * num2))
elif ch == 4:
    num1 = float(input("Enter number: "))
    num2 = float(input("Enter number: "))
    print("Division: " + str(num1/num2))
elif ch == 5:
    num1 = float(input("Enter number: "))
    print("Square root: " + str(num1**(1/2))) 
else:
    print("Invalid input!!")