# 1.	Calculate the difference in days between two dates: 15th August 2025 and 1st January 2025.

import datetime

date_1 = datetime.date(2025,8,15)
date_2 = datetime.date(2025,1,1)
diff = date_2-date_1
print(f"The difference between {date_1} and {date_2} is: {abs(diff.days)} days")
