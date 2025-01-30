# 3. Modify a file named log.txt by appending the current date and time at the end of the file.

import datetime
now = str(datetime.datetime.now())
f = open(r"D:\BEBO TECHNOLOGY\python\Practice-Session-20(File Handling)\log.txt", "a")
f.write(now)
f.close()