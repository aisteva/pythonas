import pymysql as sql
db = sql.connect(host='mysql-uosis.lt', port=3306, user='aiva2297', passwd='', db='aiva2297')
cursor = db.cursor()
cursor.execute("SELECT version()")
result = cursor.fetchone()
print(result)
db.close()
