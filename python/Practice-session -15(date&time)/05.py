# WAP to add 15days to the current date and displays the resulting date

import datetime
today = datetime.date.today()
future_date = today+datetime.timedelta(days=15)
print(future_date)