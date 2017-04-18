# 1. Sukurti lentelę +
# 2 .Užpildyti lentelę duomenimis +
# 3 .Ištrinti pasirinktą elementą
# 4 .Ištrinti visus elementus
# 5 .Sunaikinti lentelę

import pymysql as sql

db = sql.connect(host='localhost', port=3306, user='root', passwd='123456', db='python')

cursor = db.cursor()

name = str(input('Enter name: '))
lastname = str(input('Enter last name: '))
age = int(input('Enter age: '))


sql = """CREATE TABLE IF NOT EXISTS PEOPLE (
    FIRST_NAME CHAR(20),
    LAST_NAME CHAR(20),
    AGE INT)"""
sql1 = """INSERT INTO PEOPLE (FIRST_NAME, LAST_NAME, AGE) VALUES ('%s', '%s', %d)""" % (name, lastname, age)

	
try:
# Execute the SQL commands
    cursor.execute(sql)
    print("Table created")
    cursor.execute(sql1)
    print("Data inserted")
# Commit your changes in the database
    db.commit()

except:
   # Rollback in case there is any error
    db.rollback()

db.close()
