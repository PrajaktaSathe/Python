# This program calculates the number of days an individual has been alive for

import datetime
a = int(input("What year were you born ? "))
b = int(input("What month were you born(Number format where January is 1 and December is 12) ? "))
c = int(input("What day of the month were you born in ? "))
birthday = datetime.date(a, b, c)
today = datetime.date.today()
days_alive = today - birthday
print(" You have been alive for " + str(days_alive))
