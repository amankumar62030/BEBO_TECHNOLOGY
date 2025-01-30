# WAP to display the current date in this format: MM/DD/YYYY

import datetime
today = datetime.date.today()
print(f"{today.month}/{today.day}/{today.year}")