import pymysql as sql

db = sql.connect(host='localhost', port=3306, user='root', passwd='123456', db='python')

cursor = db.cursor()
print("Delete data by person name \n")
name = str(input('Enter the name: '))

sql = """DELETE FROM PEOPLE WHERE first_name= '%s'""" % (name)

try:
   cursor.execute(sql)
   print("All people with name '" + name +  "' was deleted")
   db.commit()
except:
   db.rollback()




db.close()