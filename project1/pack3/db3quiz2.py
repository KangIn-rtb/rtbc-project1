# 문2) 직원번호와 직원명을 입력(로그인)하여 성공하면 아래의 내용 출력
# 직원번호 입력 : _______
# 직원명 입력 : _______
# 직원번호 직원명 부서명 부서전화 직급 성별
# 1 홍길동 총무부 111-1111 이사 남

import MySQLdb
config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '123',
    'database' : 'test',
    'port' : 3306,
    'charset' : 'utf8'
}
def login():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        jikno = int(input("직원번호 입력 : "))
        jikname = input("직원명 입력 : ")
        # 문2
        # sql = """select jikwonno, jikwonname, busername, busertel, jikwonjik, jikwongen
        #         from jikwon
        #         inner join buser on busernum = buserno
        #         where jikwonno = %s and jikwonname = %s"""
        # 문2-1
        sql = """select jikwonno, jikwonname, busername, busertel, jikwonjik, jikwongen
                from jikwon
                inner join buser on busernum = buserno
                where busername = 
                (select busername from buser
                inner join jikwon on buserno = busernum 
                where jikwonno = %s and jikwonname = %s) order by jikwonjik, jikwonname"""
                
        sql2 = """select gogekno, gogekname, gogektel, 
                (YEAR(NOW()) - (1900+LEFT(gogekjumin,2)))
                from gogek
                inner join jikwon on jikwonno=gogekdamsano
                where jikwonno = %s and jikwonname = %s"""
                
        cursor.execute(sql, (jikno, jikname))
        data = cursor.fetchall()
        cursor.execute(sql2, (jikno, jikname))
        data2 = cursor.fetchall()
        
        if len(data) == 0:
            print("옳바른 번호, 이름을 입력하세요")
            return 
        
        print("직원번호 직원명 부서명  부서전화    직급 성별")
        for no, name, buname, butel, jik, gen in data:
            print(f"  {no}    {name}  {buname}   {butel} {jik}  {gen}")
        print("직원 수 : ",len(data))
        print()
        print("고객번호 고객명  고객전화   나이")
        for no, name, tel, age in data2:
            print(f"    {no}   {name} {tel} {int(age)}")
        print("관리 고객 수 : ",len(data2))
        
        
    except Exception as e:
        print("err : ",e)
    finally:
        cursor.close()
        conn.close()
        
if __name__ == "__main__":
    login()
    