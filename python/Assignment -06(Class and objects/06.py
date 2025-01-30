# 6.	Write a program to add 30 days to the current date and print the result.

import datetime

now = datetime.datetime.now()
add = now+datetime.timedelta(days=30)
print("Current date: ",now.date())
print("After adding 30days: ",add.date())