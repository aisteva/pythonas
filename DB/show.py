import pymysql as sql

db = sql.connect(host='localhost', port=3306, user='root', passwd='123456', db='python')

cursor = db.cursor()

sql = """SELECT * FROM PEOPLE"""

	
try:
    cursor.execute(sql)
    result = cursor.fetchall()


    print(result)
except:
	print("Printing error")

db.close()