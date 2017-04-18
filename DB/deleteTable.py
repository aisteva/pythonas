import pymysql as sql

db = sql.connect(host='localhost', port=3306, user='root', passwd='123456', db='python')

cursor = db.cursor()
table = str(input('Enter table name: ')).upper()
print(table)

sql = """DROP TABLE %s""" % (table)

try:
   cursor.execute(sql)
   print("Table '" + table + "' was deleted")
   db.commit()
except:
   db.rollback()




db.close()