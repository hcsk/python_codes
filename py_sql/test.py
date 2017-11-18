

import MySQLdb

# conn=MySQLdb.connect(host='localhost',
# port=3306,
# user='root',
# passwd=''
# )

conn=MySQLdb.connect(
user='root',
#passwd=''
)

cur=conn.cursor()

cur.execute("show databases")
rows=cur.fetchall()
for row in rows:
    print row

cur.close()
conn.commit()
conn.close()