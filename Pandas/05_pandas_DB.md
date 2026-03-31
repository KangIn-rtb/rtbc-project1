#  파이썬 데이터 분석 (Pandas와 데이터베이스 연동)


Pandas는 내장된 SQL 처리 함수들을 통해 로컬 혹은 원격 데이터베이스(DB)와 매우 쉽게 연동된다. SQL 쿼리 결과를 데이터프레임으로 바로 불러오거나, 가공한 데이터프레임을 다시 DB 테이블에 저장할 수 있다.


## 1. 로컬 DB (SQLite3) 연동 및 DataFrame 변환
파이썬 내장 라이브러리인 `sqlite3`를 사용하여 메모리상(`:memory:`)에 임시 DB를 만들고, 데이터를 삽입한 후 다시 Pandas 데이터프레임으로 불러오는 기본 예제이다.

```python
import sqlite3
import pandas as pd

# 1. 메모리상에 임시 SQLite DB 생성 및 테이블 연결
conn = sqlite3.connect(':memory:')

# 테이블 생성
sql = "create table if not exists extab(product varchar(10), maker varchar(10), weight real, price integer)"
conn.execute(sql)
conn.commit()

# 2. 데이터 삽입 (단일 및 다중)
data = [('mouse', 'samsung', 12.5, 100000), ('keyboard', 'lg', 52.5, 35000)]
isql = "insert into extab values(?,?,?,?)"
conn.executemany(isql, data) # 다중 데이터 삽입

data1 = ('pen', 'abc', 5.0, 12000)
conn.execute(isql, data1)    # 단일 데이터 삽입
conn.commit()

# 3. 데이터 조회 및 DataFrame으로 변환
cursor = conn.execute("select * from extab")
rows = cursor.fetchall()

print('rows를 DataFrame에 저장')
# 조회된 튜플 리스트를 DataFrame으로 변환하며 컬럼명 지정
df1 = pd.DataFrame(rows, columns=['product', 'maker', 'weight', 'price'])

print(df1)
print(df1.describe()) # 수치형 데이터의 기초 통계량 요약 출력

cursor.close()
conn.close()
```


## 2. 원격 DB (MariaDB/MySQL) 연동 및 데이터 분석
`pymysql`을 이용해 원격 DB에 접속한 뒤, SQL 쿼리 결과를 파이썬으로 가져와 CSV로 내보내거나 `pd.read_sql()`을 이용해 곧바로 데이터프레임으로 변환할 수 있다.

```python
import pymysql
import pandas as pd

config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123',
    'database': 'test',
    'port': 3306,
    'charset': 'utf8'
}

try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    
    # 조인(JOIN) 쿼리 작성
    sql = """
        SELECT jikwonno, jikwonname, busername, jikwonjik, jikwongen, jikwonpay
        FROM jikwon INNER JOIN buser ON jikwon.busernum = buser.buserno
    """
    
    print("\n[Pandas의 SQL 처리 함수 이용]")
    # pd.read_sql()을 사용하면 cursor.execute()와 fetchall() 과정을 생략하고 바로 DF로 만든다.
    df = pd.read_sql(sql, conn)
    df.columns = ['번호', '이름', '부서', '직급', '성별', '연봉']
    print(df.head(3))
    
    # 교차표(빈도표) 작성
    ctab = pd.crosstab(df['성별'], df['직급'], margins=True)
    print("\n성별/직급 교차표:\n", ctab)
    
except Exception as e:
    print(e)
finally:
    cursor.close()
    conn.close()
```


## 3. 실전 예제 (필터링, 피벗 테이블, 시각화)

DB에서 가져온 데이터를 바탕으로 결측치 처리, 사분위수(Quantile)를 이용한 상위 % 추출, 피벗 테이블 작성 및 Matplotlib/Seaborn을 활용한 시각화를 수행하는 종합 예제이다.

```python
import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib # 한글 폰트 깨짐 방지용 라이브러리

# (DB 연결 코드는 위와 동일하므로 생략)
# ... conn = pymysql.connect(**config)

sql = """
    SELECT jikwonno AS 사번, jikwonname AS 이름, busername AS 부서명, 
           jikwonpay AS 연봉, jikwonjik AS 직급, jikwongen AS 성별
    FROM jikwon INNER JOIN buser ON jikwon.busernum = buser.buserno
"""
df = pd.read_sql(sql, conn)

# 1. 부서명별 연봉의 합, 최대/최소값 피벗 테이블
result = pd.pivot_table(df, index='부서명', values='연봉', aggfunc=['sum', 'max', 'min'])
result.columns = ['연봉합', '최대', '최소']
print(result)

# 2. 결측치(NaN) 처리 (담당 고객이 없는 경우)
# (고객 테이블과 LEFT OUTER JOIN 한 결과를 df3로 불러왔다고 가정)
# df3 = df3.fillna("담당 고객 X")

# 3. 연봉 상위 20% 직원 추출
threshold = df['연봉'].quantile(0.8) # 하위 80% 지점의 값 (즉, 상위 20% 컷오프)
print("연봉 상위 20%:\n", df[df['연봉'] >= threshold])

# 4. 연봉 상위 50% 직원들 중 직급별 평균 연봉 (조건 필터링 후 피벗)
pay_median = df['연봉'].median()
df_top50 = df[df['연봉'] >= pay_median]
df_pivot = df_top50.pivot_table(values='연봉', index='직급', aggfunc='mean')
print("\n상위 50% 직급별 평균 연봉:\n", df_pivot)

# 5. 데이터 시각화 (성별 연봉 박스플롯 및 히스토그램)
male = df[df['성별'] == '남']['연봉']
female = df[df['성별'] == '여']['연봉']

figure, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
figure.set_size_inches(12, 8)

# 박스플롯 (이상치 및 분포 확인)
sns.boxplot(y=male, ax=ax1).set(title='남성 연봉 분포')
sns.boxplot(y=female, ax=ax2).set(title='여성 연봉 분포')

# 히스토그램 (빈도 확인)
sns.histplot(data=male, bins=10, ax=ax3).set(title='남성 연봉 히스토그램')
sns.histplot(data=female, bins=10, ax=ax4).set(title='여성 연봉 히스토그램')

plt.tight_layout()
plt.show()
```


## 4. DataFrame을 원격 DB 테이블에 저장 (`to_sql`)
가공된 데이터프레임을 DB 테이블로 바로 밀어 넣을 때는 `sqlalchemy` 모듈의 `create_engine`을 사용한다.
* `if_exists='append'`: 기존 테이블이 존재하면 그 아래에 데이터를 추가한다.
* `if_exists='replace'`: 기존 테이블을 삭제하고 새로 만든다.
* `if_exists='fail'`: 테이블이 이미 존재하면 에러를 발생시킨다.

```python
import pandas as pd
from sqlalchemy import create_engine
import os

data = {
    'code': [6, 7, 8],
    'sang': ['사이다', '맥주', '와인'],
    'su': [20, 22, 25],
    'dan': [5000, 3000, 60000]
}
frame = pd.DataFrame(data)

try:
    # SQLAlchemy 엔진 생성 (MySQL 접속 규격: mysql+pymysql://계정:비번@주소:포트/DB명)
    engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/test?charset=utf8mb4")
    
    # DataFrame을 'sangdata'라는 이름의 테이블로 저장
    frame.to_sql(name='sangdata', con=engine, if_exists='append', index=False)
    
    # 저장 후 다시 읽어와서 확인
    df = pd.read_sql("select * from sangdata", engine)
    print(df)
    
except Exception as e:
    print(e)
```

> **보안 팁 (`.env` 활용)**
> 실제 실무 환경에서는 DB 접속 정보(아이디, 비밀번호)를 코드에 직접 적어두는 것(하드코딩)은 매우 위험하다. `dotenv` 라이브러리를 사용해 분리하는 것이 원칙이다.
> 
> ```python
> # .env 파일 내용: 
> # DB_USER=root
> # DB_PASS=123
> 
> from dotenv import load_dotenv
> import os
> load_dotenv() # .env 파일 로드
> 
> # 환경변수에서 값을 꺼내와 안전하게 엔진 생성
> engine = create_engine(
>     f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@127.0.0.1:3306/test?charset=utf8mb4"
> )
> ```