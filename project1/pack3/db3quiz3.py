# 문3) 성별 직원 현황 출력 : 성별(남/여) 단위로 직원 수와 평균 급여 출력
# 성별 직원수 평균급여
# 남 3 8500
# 여 2 7800

import MySQLdb
import pickle

with open('mydb.dat', mode = 'rb') as obj:
    config = pickle.load(obj)
# config = {
#     'host' : '127.0.0.1',
#     'user' : 'root',
#     'password' : '123',
#     'database' : 'test',
#     'port' : 3306,
#     'charset' : 'utf8'
# }

def login():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = """select jikwongen, count(*), avg(jikwonpay)
                from jikwon
                group by jikwongen"""
        cursor.execute(sql)
        data = cursor.fetchall()
        print("성별 직원수 평균급여")
        for gen, some, avgpay in data:
            print(f" {gen}  {some}  {avgpay}")
        
    except Exception as e:
        print("err : ",e)
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    login()