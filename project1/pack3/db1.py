# 개인용 database : sqlite3 - 파이썬의 기본 모듈로 제공
# https://www.sqlite.org/
# 모바일 기기, 임베디드 시스템 주로 사용.

import sqlite3 
print(sqlite3.sqlite_version)

# conn = sqlite3.connet('exam.db') # 테이블 컴퓨터에 저장 
conn = sqlite3.connect(':memory:') # 렘에만 db 저장 -> 휘발성 프로그램 끝나면 휘발

try:
    cur = conn.cursor(); # sql문 처리를 위한 cursor 객체 생성
    
    # 테이블 생성
    cur.execute("create table if not exists friends(name text, phone text, addr text)")
    # 자료 입력
    cur.execute("insert into friends values('홍길동', '222-2222', '서초 1동')")
    cur.execute("insert into friends values(?, ?, ?)", ('신기해', '333-3333', '역삼 2동'))
    inputdata = (('연구소', '444-4444', '신길 1동'))
    cur.execute("insert into friends values(?, ?, ?)", inputdata)
    conn.commit()
    # 자료 보기
    cur.execute("select * from friends")
    print(cur.fetchall()) # 레코드 읽기 -> 커서가 하나씩 데이터를 읽음 이건 다읽는 거니 포인터 끝까지 감 
    print()
    cur.execute("select name, addr, phone from friends") # 포인터 끝까지 가서 다시 읽어야됨
    for r in cur:
        # print(r)
        print(r[0] + ' ' + r[1] + ' ' + r[2])    
    
    
except Exception as e:
    print('err : ',e)
    conn.rollback()
finally:
    conn.close()
