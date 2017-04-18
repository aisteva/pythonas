import pymysql as sql

db = sql.connect(host='localhost', port=3306, user='root', passwd='123456')

cursor = db.cursor()


sql = """CREATE DATABASE python"""

try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()




db.close()