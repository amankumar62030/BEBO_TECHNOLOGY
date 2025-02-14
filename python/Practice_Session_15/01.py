# 1.	Write a program to display the current date and time in the format YYYY-MM-DD HH:MM:SS.

from datetime import datetime

current = datetime.now()
format_dt = current.strftime("%Y-%m-%d %H:%M:%S")
print(format_dt)