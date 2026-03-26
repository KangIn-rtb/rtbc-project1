# local db 연동 후 DataFrame에 자료 저장
import sqlite3

sql = "create table if not exists extab(product varchar(10), maker varchar(10), weight real, price integer)"
conn = sqlite3.connect(':memory:')
conn.execute(sql)
conn.commit()

data = [('mouse','samsung',12.5,100000),('keyboard','lg',52.5,35000)]
isql = "insert into extab values(?,?,?,?)"
conn.executemany(isql,data)
data1 = ('pen','abc',5.0,12000)
conn.execute(isql,data1)
conn.commit()

cursor = conn.execute("select * from extab")
rows = cursor.fetchall()
for a in rows:
    print(a)

print('rosw를 DataFrame에 저장 ')
import pandas as pd
df1 = pd.DataFrame(rows, columns=['product','marker','weight','price'])
print(df1)
print(df1.describe())
cursor.close()
conn.close()
