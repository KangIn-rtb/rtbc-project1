# 6. Python과 데이터베이스 (Database) 연동

## 1. 로컬 환경 (SQLite3)

SQLite3는 파이썬에서 기본 모듈로 제공하는 가벼운 관계형 데이터베이스이다. 별도의 서버 프로세스가 필요 없으며 파일이나 메모리에 직접 데이터를 저장하므로, 모바일 기기나 임베디드 시스템에서 주로 사용한다.

```python
import sqlite3 
print(sqlite3.sqlite_version)

# conn = sqlite3.connect('exam.db') # 하드디스크에 DB 파일로 저장
conn = sqlite3.connect(':memory:')  # RAM에만 DB 저장 (휘발성, 프로그램 종료 시 삭제됨)

try:
    cur = conn.cursor() # SQL문 실행을 위한 커서(Cursor) 객체 생성
    
    # 테이블 생성
    cur.execute("CREATE TABLE IF NOT EXISTS friends(name text, phone text, addr text)")
    
    # 자료 입력 (INSERT)
    cur.execute("INSERT INTO friends VALUES('홍길동', '222-2222', '서초 1동')")
    
    # 파라미터 바인딩 (? 사용)
    cur.execute("INSERT INTO friends VALUES(?, ?, ?)", ('신기해', '333-3333', '역삼 2동'))
    inputdata = ('연구소', '444-4444', '신길 1동')
    cur.execute("INSERT INTO friends VALUES(?, ?, ?)", inputdata)
    
    conn.commit() # 메모리 또는 파일에 최종 반영
    
    # 자료 읽기 (SELECT)
    cur.execute("SELECT * FROM friends")
    print(cur.fetchall()) # fetchall(): 쿼리 결과를 모두 리스트로 반환 (커서가 끝까지 이동함)
    print()
    
    cur.execute("SELECT name, addr, phone FROM friends") 
    # fetchall() 이후에는 커서가 끝에 있으므로, 다시 읽으려면 쿼리를 재실행해야 한다.
    for r in cur:
        print(r[0] + ' ' + r[1] + ' ' + r[2])    
    
except Exception as e:
    print('err : ', e)
    conn.rollback() # 오류 발생 시 롤백 처리
finally:
    conn.close() # DB 연결 종료 (필수)
```


## 2. 원격 DB 연동 (MariaDB / MySQL)

원격 데이터베이스를 사용하려면 해당 DB에 맞는 드라이버 파일을 설치해야 한다. (예: `pip install mysqlclient`)

파이썬에서 DB 자료형은 DB의 설정을 그대로 따라간다. 예를 들어 DB 연산에서 `AVG` 계산 결과가 `Double`로 나오면, 파이썬에서는 자동으로 `float` 자료형으로 받아들인다.

### DB 연결 및 자료 읽기 (SELECT)
```python
import MySQLdb

# DB 접속 정보 설정 (Dictionary 형태)
config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '123',
    'database' : 'test',
    'port' : 3306,
    'charset' : 'utf8' # 최근에는 utf8mb4 사용을 권장함
}

def myFunc():
    try:
        # **config를 통해 딕셔너리 언패킹으로 연결 정보 전달
        conn = MySQLdb.connect(**config) 
        cursor = conn.cursor()
        
        # 자료 읽기
        sql = "SELECT * FROM sangdata"
        cursor.execute(sql)
        
        # 커서를 순회하며 데이터 출력
        for data in cursor:
            print(f"{data[0]} {data[1]} {data[2]} {data[3]}")
            
        # 변수 언패킹 활용
        # for code, sang, su, dan in cursor:
        #     print(code, sang, su, dan)
            
    except Exception as e:
        print('err : ', e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    myFunc()
```

### DB 자료 추가, 수정, 삭제 (CRUD & 수동 Commit)
**중요 사항**: 파이썬의 DB 연동은 기본적으로 **수동 트랜잭션** 상태이다. 따라서 `INSERT`, `UPDATE`, `DELETE` 수행 후에는 반드시 `conn.commit()`을 호출해야 DB 서버에 반영된다. 

원격 DB 쿼리에서는 파라미터 바인딩을 위해 `?` 대신 **`%s`**를 사용하며, 보안(SQL Injection 방지)을 위해 시큐어 코딩 가이드에 따라 튜플(Tuple) 형태로 값을 전달하는 것이 좋다.

```python
        # 1. 자료 추가 (INSERT)
        isql = "INSERT INTO sangdata VALUES(%s, %s, %s, %s)"
        sql_data = (6, '신상2', 10, 4000)
        cursor.execute(isql, sql_data)
        conn.commit() # 수동 커밋 필수
        
        # 2. 자료 수정 (UPDATE)
        usql = "UPDATE sangdata SET sang=%s, su=%s, dan=%s WHERE code = %s"
        sql_data = ('물티슈', 66, 1000, 5)
        
        # DML 연산(execute)의 리턴값은 처리된 행(Row)의 개수이다.
        cou = cursor.execute(usql, sql_data)
        print('수정건수 : ', cou) # 0이면 실패 또는 대상 없음, 1 이상이면 성공
        conn.commit()
        
        # 3. 자료 삭제 (DELETE)
        code = '6'
        dsql = "DELETE FROM sangdata WHERE code = %s"
        # 데이터가 하나일지라도 튜플 형태 (값,) 로 전달해야 에러가 나지 않는다.
        cursor.execute(dsql, (code,)) 
        conn.commit()
```
* **DML 실행 반환값**: 
  * `INSERT`, `DELETE`: 처리에 성공한 행의 개수 (단건 연산 시 성공하면 1, 실패하면 0)
  * `UPDATE`: 조건에 맞아 성공적으로 수정된 행의 개수 (여러 개가 수정되면 그만큼 숫자가 커짐)

## 1. 보안을 위한 환경 설정 분리
데이터베이스 접속 정보(호스트, 아이디, 비밀번호 등)를 소스 코드에 직접 하드코딩하면 보안상 매우 취약하다. 이를 방지하기 위해 파이썬의 객체 직렬화 모듈인 `pickle`을 사용하여 설정(Config) 딕셔너리를 외부 파일(`mydb.dat`)로 빼서 숨기는 방식을 활용할 수 있다.

> **참고**: 실무에서는 `.env` 파일(환경변수)이나 별도의 `.yaml`, `.json` 설정 파일을 주로 사용하지만, 파이썬 객체를 그대로 저장하고 불러올 때는 `pickle`이 유용하다.

### [선행 작업] 설정 파일(mydb.dat) 생성하기
먼저 아래 코드를 한 번 실행하여 설정 정보를 담은 이진(Binary) 파일을 생성해 두어야 한다.
```python
import pickle

config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '123',
    'database' : 'test',
    'port' : 3306,
    'charset' : 'utf8'
}

# 딕셔너리 객체를 mydb.dat 파일로 직렬화하여 저장 (Write Binary)
with open('mydb.dat', mode='wb') as obj:
    pickle.dump(config, obj)
```

## 2. 성별 직원 현황 출력 실습
미리 저장해 둔 `mydb.dat` 파일을 읽어와 데이터베이스에 접속하고, `GROUP BY` 구문을 활용해 성별 직원 수와 평균 급여를 출력하는 코드이다.

```python
import MySQLdb
import pickle

# 1. 분리해둔 DB 접속 정보 불러오기 (Read Binary)
with open('mydb.dat', mode='rb') as obj:
    config = pickle.load(obj)

def login():
    try:
        # **config를 이용해 언패킹 방식으로 연결 정보 전달
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        
        # 2. SQL 쿼리 작성 (성별로 그룹화하여 인원수와 평균 급여 계산)
        sql = """
            SELECT jikwongen, COUNT(*), AVG(jikwonpay)
            FROM jikwon
            GROUP BY jikwongen
        """
        cursor.execute(sql)
        
        # 3. 데이터 패치 및 출력
        data = cursor.fetchall() # 모든 결과를 리스트(튜플) 형태로 가져옴
        
        print("성별 직원수 평균급여")
        print("-" * 20)
        
        for gen, some, avgpay in data:
            # 가져온 데이터를 포맷팅하여 출력
            print(f" {gen}    {some}    {int(avgpay)}") 
            # (avgpay는 소수점이 나올 수 있으므로 int()로 정수 변환을 해주면 더 깔끔하다)
        
    except Exception as e:
        print("err : ", e)
    finally:
        # 4. 자원 반납
        cursor.close()
        conn.close()

if __name__ == "__main__":
    login()
```

```text
성별 직원수 평균급여
--------------------
 남    3    8500
 여    2    7800
``` 