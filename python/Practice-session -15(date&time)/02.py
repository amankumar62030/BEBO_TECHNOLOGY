# WAP to extract and display the year month and day from the current date

import datetime
now = datetime.datetime.now()
print("Year: ",now.year)
print("Month: ",now.month)
print("Day: ",now.day)


# for time
now = datetime.datetime.now().time()
print(now)

