# 문4)직원별 관리 고객 수 출력 (관리 고객이 없으면 출력에서 제외)
# 직원번호 직원명 관리 고객 수
# 1 홍길동 3
# 2 한송이 1

import MySQLdb
import pickle

with open('mydb.dat', mode = 'rb') as obj:
    config = pickle.load(obj)

def login():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        sql = """select jikwonno, jikwonname, count(*)
                from jikwon
                inner join gogek on jikwonno=gogekdamsano
                group by jikwonno, jikwonname"""
        cursor.execute(sql)
        data = cursor.fetchall()
        print("성별 직원수 평균급여")
        for gen, num, pay in data:
            print(f" {gen}  {num}  {pay}")
    except Exception as e:
        print("err : ",e)
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    login()