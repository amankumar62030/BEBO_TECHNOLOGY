# WAP to calculate the number of days between 2024-01-01 and the current date

import datetime
given_date = datetime.date(2024,1,1)
current_date = datetime.date.today()
diff = current_date - given_date
print(diff.days)
