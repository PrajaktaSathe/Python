def leap_check(year) -> str:
  """ Check if a year is a leap year """
  if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)):
    return f"{year} is a leap year!"
  else:
    return f"{year} is not a leap year!"
#====================
# MAIN PROGRAM
print("<-- Leap Year Checker -->")
print("This program will check if a year you input is a leap year")
print("\n")

run = 'Y'
while run == 'Y': #runs once before user intervention
  try:
    input_year = int(input("Enter a year\n\t--> "))
  except ValueError:
    input_year = int(input("Must be an integer!\n\t--> "))
  print(leap_check(input_year))
  
  print("-" * 30) #decoration
  
  print("Would you like to check another year?\n\t[Y] Yes\n\t[N] No")
  run = input("\t--> ").upper()
  while run not in ['Y','Yes','N','No']: #input validation
    run = input("\t--> ").upper()
  
  print("-" * 30)l
