# WAP to create a datetime object for 15th august 2025, 10:30:00 AM and display it in YYYY-MM-DD and HH:MM:SS format

import datetime
y = int(input("Enter year: "))
m = int(input("Enter month: "))
d = int(input("Enter day: "))
h = int(input("Enter hour: "))
min = int(input("Enter minute: "))
s = int(input("Enter second: "))
current_date = datetime.date(y,m,d)
current_time = datetime.time(h,min,s)
print(current_date)
print(current_time)
