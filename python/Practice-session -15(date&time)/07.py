# WAP to calculate the difference in hours, minutes and seconds between two given times: 10:30:00  and  14:45:30


import datetime
# a = datetime.time(10,30,00)
# b = datetime.time(14,45,30)
# print(f"{abs(a.hour-b.hour)}:{abs(a.minute-b.minute)}:{abs(a.second-b.second)}")

from datetime import datetime
time1 = datetime.strptime("10:30:00", "%H:%M:%S")
time2 = datetime.strptime("14:45:30", "%H:%M:%S")

time_diff = time1-time2
print(abs(time_diff))