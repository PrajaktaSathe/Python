def calculator():
    print("Options:\n\t[1] Add \n\t[2] Subtract \n\t[3] Multiply \n\t[4] Divide \n\t[5] Power \n\t[6] Square root")
    ch = int(input("\t--> "))
    
    if ch == 1: #addition
        num1 = float(input("1st number --> "))
        num2 = float(input("2nd number --> "))
        print(f"{num1} + {num2} = {num1 + num2}")
    elif ch == 2: #subtraction
        num1 = float(input("1st number --> "))
        num2 = float(input("2nd number --> "))
        print(f"{num1} - {num2} = {num1 - num2}")
    elif ch == 3: #multiplication
        num1 = float(input("1st number --> "))
        num2 = float(input("2nd number --> "))
        print(f"{num1} x {num2} = {num1 * num2}")
    elif ch == 4: #division
        num1 = float(input("Dividend --> "))
        num2 = float(input("Divisor  --> "))
        try:
          print(f"{num1} ÷ {num2} = {num1 / num2}")
        except ZeroDivisionError:
          print(f"{num1} ÷ {num2} = Error: Division by 0!")
    elif ch == 5: #power
        num = float(input("Number --> "))
        power = float(input("Power --> "))
        print(f"{num} ^ {power} = {num ** power}")
    elif ch == 6: #root
        num = float(input("Number --> "))
        print(f"√{num} = {num**(1/2)}")
    else:
        print("Invalid input!!")
#====================
# MAIN PROGRAM
print("<-- Basic Calculator -->")
print("Does what it says on the tin!")
print("-" * 30) #decoration

run = 'Y'
while run == 'Y':
  calculator()
  
  print("-" * 30)
  
  print("Would you like calculate more?\n\t[Y] Yes\n\t[N] No")
  run = input("\t--> ").upper()
  while run not in ['Y','YES','N','NO']:
    run = input("\t--> ").upper()
  
  print("-" * 30)
