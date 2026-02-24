# 원격 데이터 베이스
# mariaDB : driver file 설치 후 사용
# pip install mysqlclient 

# conn = MySQLdb.connect(
#     host = '127.0.0.1',
#     user = 'root',
#     password = '123',
#     database = 'test',
#     port = 3306
# )
# print(conn)
# conn.close()

# sangdata 자료 CRUD

import MySQLdb

config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '123',
    'database' : 'test',
    'port' : 3306,
    'charset' : 'utf8'
}

def myFunc():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        # 자료 추가
        # isql = "insert into sangdata(code, sang, su, dan) values(5, '신상1', 5, 7800)"
        # cursor.execute(isql)
        # conn.commit() # 파이썬은 수동 트랜잭션 이므로 commit을 해줘야함 그리고 한번 하고 또하면 err남
        # isql = "insert into sangdata values(%s, %s, %s, %s)"
        # sql_data = 6,'신상2',10,4000
        # cursor.execute(isql,sql_data)
        # conn.commit()
        
        # 자료 수정
        # usql = "update sangdata set sang=%s, su=%s, dan=%s where code = %s"
        # sql_data = ('물티슈', 66 ,1000, 5)
        # cursor.execute(usql, sql_data)
        # conn.commit()
        
        usql = "update sangdata set sang=%s, su=%s, dan=%s where code = %s"
        sql_data = ('콜라', 77 ,850, 5)
        cou = cursor.execute(usql, sql_data)
        print('수정건수 : ', cou)
        
        
        # 자료 삭제
        code = '6'
        dsql = "delete from sangdata where code = %s"
        cou = cursor.execute(dsql, (code,))
        if cou != 0:
            print("삭제 성공")
        else:
            print("삭제 실패")
        conn.commit()
        

        # 자료읽기
        sql = "select * from sangdata"
        cursor.execute(sql)
        for data in cursor:
            # print(data)
            # print('%s %s %s %s'%data)
            print(f"{data[0]} {data[1]} {data[2]} {data[3]}")
        # print()
        # for code, sang, su, dan in cursor:
        #     print(code, sang, su, dan)
            
    except Exception as e:
        print('err : ',e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
    

if __name__ == "__main__":
    myFunc()
    