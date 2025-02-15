# 7.	Write a program to calculate the difference in hours, minutes, and seconds between two given times: 10:30:00 and 14:45:30.

from datetime import datetime
time1 = datetime.strptime("10:30:00", "%H:%M:%S")
time2 = datetime.strptime("14:45:30", "%H:%M:%S")

time_diff = time1-time2
print(abs(time_diff))