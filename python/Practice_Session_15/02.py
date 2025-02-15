# 2.	Write a program to extract and display the year, month, and day from the current date.

from datetime import datetime
now = datetime.now()
print("Year",now.year)
print("Month",now.month)
print("Day",now.day)
