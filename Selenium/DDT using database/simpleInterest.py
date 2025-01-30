import pymysql

try:
    con = pymysql.connect(
        host = "localhost",
        port = 3306,
        user="root",
        password="root1234",
        database="youtube"
    )
    cursor = con.cursor()
    cursor.execute("select * from simpleinterestdata")

    for row in cursor:
        # print(row[0],row[1],row[2],row[3],row[4])
        principle = row[0]
        print(principle)
    con.close()

except:
    print("DB not connected")
