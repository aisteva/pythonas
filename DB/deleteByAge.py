import pymysql as sql

db = sql.connect(host='localhost', port=3306, user='root', passwd='', db='python')

cursor = db.cursor()
print("Delete data by person name \n")
name = str(input('Enter the name: '))


sql = """DELETE FROM PEOPLE WHERE age= '%s'""" % (name)

try:



   # Execute the SQL command
   cursor.execute(sql)
#   cursor.execute(sql1)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()




db.close()