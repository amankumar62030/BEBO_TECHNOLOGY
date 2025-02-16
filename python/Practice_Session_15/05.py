# WAP to add 15days to the current date and displays the resulting date

import datetime
current = datetime.date.today()
day = current+datetime.timedelta(days=15)
print(day)