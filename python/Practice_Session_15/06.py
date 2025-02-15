# WAP to display the current date in this format: MM/DD/YYYY

import datetime
current = datetime.date.today()

frmt = current.strftime("%m-%d-%Y")
print(frmt)