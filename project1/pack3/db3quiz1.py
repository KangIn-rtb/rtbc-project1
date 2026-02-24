# 문1) jikwon 테이블 자료 출력
# 키보드로부터 부서번호를 입력받아, 해당 부서에 직원 자료 출력
# 부서번호 입력 : _______
# 직원번호 직원명 근무지역 직급
# 1 홍길동 서울 이사
# ...
# 인원 수 :

import MySQLdb

config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '123',
    'database' : 'test',
    'port' : 3306,
    'charset' : 'utf8'
}

def jikwonja():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        bunum = input("부서번호 입력 : ")
        sql = """select jikwonno, jikwonname, buserloc, jikwonjik 
                from jikwon 
                inner join buser on busernum=buserno
                where busernum = %s
            """
        cursor.execute(sql,(bunum,))
        cnt = cursor.fetchall()
        if len(cnt) == 0:
            print(bunum + "번 부서는 없어요")
            return
        print("직원번호 직원명 근무지역 직급")
        for data in cursor:
            print(f"  {data[0]:<3}   {data[1]:<3}   {data[2]:>3}   {data[3]:>3}")
        print("인원 수 : ", len(cnt))
    except Exception as e:
        print("err : ",e)
    finally:
        cursor.close()
        conn.close()
if __name__ == "__main__":
    jikwonja()