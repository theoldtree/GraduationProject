import pymysql

conn = pymysql.connect(host='localhost',user='root',password='tlqkf12!@',db='pighouse',charset='utf8')
cursor = conn.cursor()
data = '333'
sql = 'insert into pighouse.decibel (decibel) values (%s)'
cursor.execute(sql,data)
conn.commit()
conn.close()