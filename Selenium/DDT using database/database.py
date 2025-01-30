# insert,update,delete
insert_query = "insert into students values(104,'Kim',89)"
update_query = "update students set sname = 'Mary' where sid=104"
delete_query = "delete from student where sid=104"


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
    cursor.execute("select * from student")

    for row in cursor:
        print(row[0],row[1],row[2])

    con.close()

except:
    print("DB not connected")



























