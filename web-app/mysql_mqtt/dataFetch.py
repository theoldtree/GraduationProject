import pymysql
con = pymysql.connect(host='localhost',user='root',passwd='tlqkf12!@',db='pighouse')
cur = con.cursor()
query = "SELECT * FROM strange_action"
cur.execute(query)
con.commit()
datas = cur.fetchall()
for data in datas:
    print(data)
con.close()