# HeidiSQL Basic

## 1. DB 접속 및 기본 개념
* **호스트명**: IP를 변경하여 다른 컴퓨터(데이터베이스가 설치된 서버)에 접속 가능
* **포트(Port)**: `0 ~ 65535` 사이의 포트 번호 사용 (연습용에선 포트를`3306` 그대로 사용 하지만 실제 환경에선 포트를 따로 선택해야함)
* **작업 환경**: DB 접속 후 UI 환경(좌측 DB 목록) 또는 CLI에서 SQL 코딩 진행

> **Tip (Python과 연동 시)**: 파이썬 내부에서 SQL은 문자열로 취급되므로, 쿼리문 전체는 큰따옴표(`" "`)로 묶고 내부의 SQL 문자열 데이터는 작은따옴표(`' '`)로 묶는 것이 좋음


## 2. 테이블 생성 및 자료 조작 (DDL, DML)

### 테이블 생성 (CREATE)
```sql
CREATE TABLE dept(
    NO INT PRIMARY KEY, 
    NAME VARCHAR(10), 
    tel VARCHAR(15), 
    inwon INT, 
    addr TEXT
) CHARSET = utf8mb4; 

```

### 자료 추가 (INSERT)
```sql
INSERT INTO dept(NO, NAME, tel, inwon, addr) VALUES(1, '인사과', '111-1111', 3, '삼성동12');
INSERT INTO dept VALUES(2, '영업과', '111-2222', 5, '서초동12'); -- 컬럼명을 생략하면 순서대로 들어감
INSERT INTO dept(NO, NAME) VALUES(3, '영업과'); 
INSERT INTO dept(NO, addr, tel, NAME) VALUES(4, '역삼2동33', '111-5555', '자재2과');

-- 특정 컬럼을 지정하지 않고 INSERT 하면 나머지 값은 기본적으로 NULL이 들어감
INSERT INTO dept(NAME, tel) VALUES('영업2과','111-6666'); -- 에러 발생: PRIMARY KEY인 NO는 필수(NOT NULL)
```

### 자료 수정 (UPDATE)
`WHERE` 조건을 사용해 특정 데이터만 변경할 수 있다 (Primary Key 컬럼은 보통 수정 대상에서 제외)
```sql
UPDATE dept SET tel = '123-4567' WHERE NO = 2;
UPDATE dept SET addr = '압구정동33', inwon = 7, tel = '777-8888' WHERE NO = 3;
```

### 자료 삭제 (DELETE, TRUNCATE, DROP)
```sql
DELETE FROM dept WHERE NAME='자재2과'; -- 조건에 맞는 행만 삭제
DELETE FROM dept; -- 테이블 내 모든 데이터 삭제 (조건 안 쓰면 다 지워짐 주의)

TRUNCATE TABLE dept; -- 테이블 비우기 (DELETE보다 속도가 빠름. 데이터가 많을 때 체감됨)
DROP TABLE dept; -- 테이블 구조 자체를 완전히 삭제
```


## 3. 무결성 제약 조건 (Constraints)
테이블 생성 시 잘못된 자료 입력을 막기 위해 다양한 제한을 둘 수 있다.

* **PRIMARY KEY (기본키)**: 중복 레코드 입력 방지, 자동으로 `NOT NULL` 적용
* **CHECK**: 입력 자료의 특정 칼럼 값 조건 검사 (DB에 넣기 전 최종 검사 장치)
* **UNIQUE**: 특정 칼럼값의 중복을 허용하지 않음
* **NOT NULL**: NULL 값 입력을 방지
* **DEFAULT**: 데이터가 안 들어올 경우 부여할 초기치 설정
* **AUTO_INCREMENT**: 숫자 자동 증가 생성

```sql
-- 제약 조건 적용 예시
CREATE TABLE aa(
    bun INT AUTO_INCREMENT PRIMARY KEY, 
    nai INT CHECK(nai >= 20), 
    irum CHAR(10) NOT NULL UNIQUE,
    juso CHAR(20) DEFAULT '강남구 역삼동'
); 
```

### FOREIGN KEY (외래키, 참조키)
특정 컬럼이 다른 테이블의 `PRIMARY KEY`를 참조하도록 하는 제약이다. 외래키로 연결된 자료를 함부로 지우려 하면 에러가 발생한다.

```sql
-- 부모 테이블 (직원)
CREATE TABLE jikwon(
    bun INT PRIMARY KEY, 
    irum CHAR(10) NOT NULL, 
    buser CHAR(10) NOT NULL
); 

-- 자식 테이블 (가족)
CREATE TABLE gajok(
    code INT PRIMARY KEY,
    NAME VARCHAR(10) NOT NULL,
    birth DATE, 
    jikwonbun INT, 
    FOREIGN KEY(jikwonbun) REFERENCES jikwon(bun) ON DELETE CASCADE
);
```
> **`ON DELETE CASCADE`**: 부모 테이블(참조되는 테이블)의 PK 자료가 삭제될 때, 이를 참조하는 자식 테이블(FK)의 자료도 함께 연쇄 삭제되는 옵션이다.


## 4. 인덱스 (Index)
검색 속도 향상을 위해 특정 컬럼에 색인을 부여한다. PK 컬럼은 자동으로 오름차순 인덱싱이 적용된다. 인덱스는 검색은 빠르게 하지만, 입력/수정/삭제 작업이 빈번한 경우에는 오히려 성능을 떨어뜨릴 수 있으므로 주의해야 한다.

```sql
ALTER TABLE aa ADD INDEX ind_juso(juso); -- 인덱스 추가
ALTER TABLE aa DROP INDEX ind_juso; -- 인덱스 삭제

SHOW INDEX FROM aa; -- 인덱스 확인
EXPLAIN SELECT * FROM aa; -- 쿼리 실행 계획 확인 (인덱스를 탔는지 확인 가능)
```
* **Index 속성**:
  * `Non_unique`: `0`이면 중복 불허(PK, Unique), `1`이면 중복 허용
  * `Index_type`: 기본적으로 `BTREE`(2진 탐색 변형) 방식 등을 사용함
  * `Collation`: `A`는 오름차순 `D`는 내림차순
  * `index`가 생기면 열쇠 모양이 생김

## 5. 테이블 구조 변경 (ALTER)
```sql
ALTER TABLE aa RENAME kbs; -- 테이블 이름 변경
ALTER TABLE kbs ADD (job_id INT DEFAULT 10); -- 컬럼 추가
ALTER TABLE kbs CHANGE job_id job_num INT; -- 컬럼명 및 성격 변경
ALTER TABLE kbs MODIFY job_num VARCHAR(10); -- 컬럼 데이터 타입 변경
ALTER TABLE kbs DROP COLUMN job_num; -- 컬럼 삭제
```


## 6. 데이터 조회 (SELECT)
DB 서버로부터 자료를 읽어오는(로컬로 불러오는) 핵심 명령어

```sql
SELECT * FROM jikwon;
SELECT jikwonno AS '직원번호', jikwonname AS '직원명' FROM jikwon; -- 별명(Alias) 지정
SELECT jikwonno, jikwonpay, jikwonpay * 0.05 AS tax FROM jikwon; -- 수식 적용
SELECT CONCAT(jikwonname, '님') AS jikwonetc FROM jikwon; -- 데이터 가공(문자열 합치기)
```

### 정렬 (ORDER BY)
* `ASC`: 오름차순 (기본값)
* `DESC`: 내림차순
```sql
SELECT * FROM jikwon ORDER BY jikwonjik ASC, busernum DESC; -- 여러 기준 적용 가능
```

### 중복 제거 (DISTINCT)
```sql
SELECT DISTINCT jikwonjik FROM jikwon; -- 중복 배제 (작성 말고 선택하기 기능을 구현할 때, DB에서 중복을 배제하고 불러와 선택지로 제공하면 유용함)
```

### 연산자 및 조건식 (WHERE)
```sql
SELECT * FROM jikwon WHERE jikwonjik = '사원' AND jikwongen = '여';
SELECT * FROM jikwon WHERE jikwonjik = '사원' AND (jikwongen = '여' OR jikwonibsail >= '2017-01-01');

SELECT * FROM jikwon WHERE jikwonibsail BETWEEN '2017-01-01' AND '2019-12-31';
SELECT * FROM jikwon WHERE jikwonjik IN('대리', '과장', '부장');

SELECT * FROM jikwon WHERE jikwonjik IS NULL; -- NULL 값 찾기 ( = NULL 이 아님에 주의)
```
> **Tip**: 긍정적 조건(`=`, `IN`)을 사용하는 것이 부정적 조건(`!=`, `NOT IN`)보다 검색 속도 향상에 도움이 된다.

### 패턴 매칭 (LIKE)
* `%`: 0개 이상의 모든 문자열
* `_`: 정확히 1개의 문자
```sql
SELECT * FROM jikwon WHERE jikwonname LIKE '이%'; -- '이'로 시작하는 모든 데이터 (예: 이씨 성)
SELECT * FROM jikwon WHERE jikwonname LIKE '%라'; -- '라'로 끝나는 모든 데이터
```

### 결과 제한 (LIMIT)
```sql
SELECT * FROM jikwon LIMIT 3; -- 상위 3개만 출력
SELECT * FROM jikwon ORDER BY jikwonno DESC LIMIT 3; -- 내림차순 정렬 후 상위 3개
SELECT * FROM jikwon LIMIT 5, 3; -- 인덱스 5번(6번째)부터 3개의 데이터 출력
```