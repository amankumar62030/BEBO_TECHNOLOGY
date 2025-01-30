# 3.	Write a program to print the current date and time in the format YYYY-MM-DD HH:MM:SS. Create a datetime object for 1st January 2025, 12:00 PM and print it in the format Day Month, Year at HH:MM.

import datetime
now = datetime.datetime.now()
print(now)

date = datetime.datetime(2025,1,1,12,0)
# print(f"{date.day}-{date.month}-{date.year} at {time.hour}:{time.minute}")
print(date.strftime("%d %B %Y at %H:%M"))