# 1. Sukurti lentelę +
# 2 .Užpildyti lentelę duomenimis +
# 3 .Ištrinti pasirinktą elementą
# 4 .Ištrinti visus elementus
# 5 .Sunaikinti lentelę

import pymysql as sql

db = sql.connect(host='localhost', port=3306, user='root', passwd='', db='python')

cursor = db.cursor()
#cursor.execute("SELECT version()")
result = cursor.fetchone()

cursor.execute("""CREATE TABLE IF NOT EXISTS PEOPLE (
         FIRST_NAME  CHAR(20),
         LAST_NAME  CHAR(20),
         AGE INT  )""")
		 
# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO PEOPLE(FIRST_NAME,
         LAST_NAME, AGE)
         VALUES ('Jonas', 'Joninis', 25)"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()



print(result)
db.close()
