import sys
sys.stdout.reconfigure(encoding='utf-8')

import MySQLdb
import pickle

with open("cgi-bin/mydb.dat", mode="rb") as obj:
    config = pickle.load(obj)
    

print('Content-Type: text/html; charset=utf-8')
print()
print("<htlm><body><b>** 상품 정보 **</b></br>")
print("<table border='1'>")
print("<tr><td>코드</td><td>상품명</td><td>수량</td><td>단가(원)</td></tr>")
try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    cursor.execute("select * from sangdata order by code desc")
    datas = cursor.fetchall()
    for code,sang,su,dan in datas:
        print(f"<tr><td>{code}</td><td>{sang}</td><td>{su}</td><td>{dan}</td></tr>")
except Exception as e:
    print("err : ",e)
finally:
    cursor.close()
    conn.close()
print("</table>")
print("</body></html>")