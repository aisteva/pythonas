import pymysql as sql
<<<<<<< HEAD
db = sql.connect(host='mysql-uosis.lt', port=3306, user='aiva2297', passwd='', db='aiva2297')
=======
db = sql.connect(host="mysql-uosis.mif", port=3306, user="aiva2297", passwd="Rytelis2", db="aiva2297")
>>>>>>> e96620bd71f657b694f416e5cdb56c64971afc33
cursor = db.cursor()
cursor.execute("SELECT version()")
result = cursor.fetchone()


# Create table as per requirement
#sql = """CREATE TABLE PEOPLE (
 #        FIRST_NAME  CHAR(20),
 #        LAST_NAME  CHAR(20),
 #        AGE INT  )"""
		 
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
