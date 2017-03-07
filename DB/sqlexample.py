import pymysql as sql
db = sql.connect(host="mysql-uosis.mif", port=3306, user="aiva2297", passwd="Rytelis2", db="aiva2297")
cursor = db.cursor()
cursor.execute("SELECT version()")
result = cursor.fetchone()


# Create table as per requirement
sql = """CREATE TABLE PEOPLE (
         FIRST_NAME  CHAR(20),
         LAST_NAME  CHAR(20),
         AGE INT  )"""

cursor.execute(sql)
print(result)
db.close()
