# SQL 심화: 트랜잭션 & 뷰 (Transaction & View)

## 1. 트랜잭션 (Transaction)

데이터베이스의 상태를 변경시키는 논리적인 작업의 단위이다. 계좌 이체와 같이 한꺼번에 모두 수행되거나 모두 취소되어야 할 연산들을 하나로 묶어놓은 것이다. 

* `INSERT`, `UPDATE`, `DELETE` 등의 DML 명령으로 트랜잭션이 시작된다.
* **`COMMIT`**: 작업장(메모리)에서 변경된 내역을 실제 DB 서버에 영구적으로 반영하며 트랜잭션을 종료한다.
* **`ROLLBACK`**: 작업 중인 내역을 모두 취소하고 트랜잭션 시작 이전 상태로 되돌리며 트랜잭션을 종료한다.
* (참고) 서버 종료나 타임아웃 발생 시에도 트랜잭션은 종료된다.

### 오토커밋 (Autocommit)
기본적으로 DB는 명령어를 입력할 때마다 즉시 커밋되는 오토커밋 상태로 설정되어 있다. 트랜잭션을 수동으로 제어하려면 이를 비활성화해야 한다.
```sql
SHOW VARIABLES LIKE 'autocommit%'; -- 오토커밋 상태 확인
SET autocommit = FALSE; -- 오토커밋 비활성화 (트랜잭션 수동 제어 시작)
SET autocommit = TRUE;  -- 오토커밋 활성화
```

### 트랜잭션 제어 실습 및 SAVEPOINT
`SAVEPOINT`를 사용하면 트랜잭션 전체를 취소(`ROLLBACK`)하지 않고, 특정 지점까지만 부분적으로 되돌릴 수 있다.
```sql
-- 실습용 테이블 복사
CREATE TABLE jiktab3 AS SELECT * FROM jikwon;
SET autocommit = FALSE; -- 트랜잭션 시작

UPDATE jiktab3 SET jikwonpay=7777 WHERE jikwonno=4;

SAVEPOINT a; -- 현재 상태를 'a'라는 이름으로 저장

UPDATE jiktab3 SET jikwonpay=8888 WHERE jikwonno=5;
SELECT * FROM jiktab3 WHERE jikwonno = 5; -- 8888로 변경된 것 확인 가능

ROLLBACK TO SAVEPOINT a; -- 세이브포인트 'a' 시점으로 되돌아감 (5번 직원의 급여 변경만 취소됨)
SELECT * FROM jiktab3 WHERE jikwonno <= 6;

COMMIT; -- 최종적으로 4번 직원의 급여 변경 내역만 DB에 반영함
```

### 교착상태 (Deadlock)
두 개 이상의 트랜잭션이 서로 상대방이 점유한 자원(Lock)을 기다리며 영원히 진행하지 못하는 무한 대기 상태를 말한다.
하나의 세션에서 트랜잭션을 진행(수정)하는 도중 아직 `COMMIT`이나 `ROLLBACK`을 하지 않았는데, 다른 세션에서 동일한 데이터를 수정하려고 하면 락이 걸려 대기 상태가 된다. 트랜잭션을 수행 완료하거나 취소해야 락이 풀리며 작업이 다시 진행된다.


## 2. 뷰 (View)

실제 데이터를 저장하지 않고 기존 테이블을 참조하여 보여주기만 하는 가상의 테이블이다. 
물리적인 테이블은 아니지만 SQL 문법상에서는 테이블처럼 동일하게 취급되어 `SELECT` 조회가 가능하다. 보안 목적이나 복잡한 쿼리를 단순화하기 위해 자주 사용한다.

* **생성/수정**: `CREATE OR REPLACE VIEW`를 사용하면 뷰가 이미 존재할 경우 덮어쓰기(업데이트)가 되므로 오류가 발생하지 않는다.
```sql
CREATE OR REPLACE VIEW v_a AS 
SELECT jikwonno, jikwonname, jikwonpay FROM jikwon WHERE jikwonibsail < '2010-12-31';

SHOW TABLES; -- 뷰 테이블도 목록에 함께 표시된다.
```

### 뷰의 수정(UPDATE) 제약 조건
뷰에서 계산된 열이나 조인된 열은 참조(조회)만 가능하며, 제약 조건에 따라 수정/삽입/삭제가 제한된다.
* **`GROUP BY`를 사용한 뷰**: 계산에 의한 결과이므로 `INSERT`, `UPDATE`, `DELETE`가 불가능하다.
* **`JOIN`을 사용한 뷰**: 자료 수정은 가능하나 한 번에 하나의 기본 테이블 컬럼만 수정할 수 있다. MariaDB 등에서는 `JOIN`된 뷰의 `DELETE`가 기본적으로 불가능하다. (Oracle 등 일부 DB에서는 설정에 따라 가능)

```sql
-- 수정 불가능한 뷰 (GROUP BY)
CREATE VIEW v_group AS 
SELECT jikwonjik, SUM(jikwonpay) AS hap, AVG(jikwonpay) AS ave 
FROM jikwon GROUP BY jikwonjik;
-- SELECT * FROM v_group; (조회만 가능)

-- 제한적으로 수정 가능한 뷰 (JOIN)
CREATE OR REPLACE VIEW v_join AS 
SELECT jikwonno, jikwonname, busername, jikwonjik FROM jikwon
INNER JOIN buser ON jikwon.busernum=buser.buserno
WHERE jikwon.busernum IN (10, 20);

UPDATE v_join SET jikwonname = '손오공' WHERE jikwonname = '박명화'; -- 단일 테이블 컬럼 수정은 가능
-- UPDATE v_join SET jikwonname = '사오정', busername = '영업부' WHERE jikwonname = '손오공'; -- 에러 발생 (양쪽 테이블 동시 수정 불가)
```


## 3. 뷰(View) 활용 예제

```sql
-- 예제 1: 다중 조인 및 가공을 통한 뷰 생성
CREATE OR REPLACE VIEW v_exam1 AS
SELECT DISTINCT jikwonno AS 사번, jikwonname AS 이름, busername AS 부서, NVL(jikwonjik, '임시직') AS 직급, 
       DATE_FORMAT(NOW(), '%Y') - DATE_FORMAT(jikwonibsail, '%Y') AS 근무년수, 
       CASE NVL(gogekname, 'a') WHEN 'a' THEN 'X' ELSE 'O' END AS 고객확보
FROM jikwon 
LEFT OUTER JOIN buser ON busernum = buserno
LEFT OUTER JOIN gogek ON jikwonno = gogekdamsano
WHERE busername <> '전산부' OR busername IS NULL;

-- 예제 2: 인원수가 가장 많은 부서 뷰 (FROM 절 서브쿼리 활용)
CREATE OR REPLACE VIEW v_exam2 AS
SELECT busername AS 부서명, COUNT(*) AS 인원수
FROM jikwon
INNER JOIN buser ON busernum = buserno
GROUP BY busername
HAVING 인원수 = (
    SELECT MAX(cnt) FROM (SELECT COUNT(*) AS cnt FROM jikwon GROUP BY busernum) AS b
);
/* 참고: 단일 최댓값만 구할 때는 아래처럼 ORDER BY와 LIMIT을 쓸 수도 있다. (단, 공동 1위가 있을 때는 위 서브쿼리 방식이 안전함)
HAVING COUNT(*) = (SELECT COUNT(*) FROM jikwon GROUP BY busernum ORDER BY COUNT(*) DESC LIMIT 1) 
*/

-- 예제 3: 가장 많이 입사한 요일의 직원 목록 뷰 생성
CREATE OR REPLACE VIEW v_exam3 AS
SELECT jikwonname AS 직원명,
       CASE DATE_FORMAT(jikwonibsail, '%w')
            WHEN 0 THEN '일요일' WHEN 1 THEN '월요일' WHEN 2 THEN '화요일'
            WHEN 3 THEN '수요일' WHEN 4 THEN '목요일' WHEN 5 THEN '금요일'
            WHEN 6 THEN '토요일' END AS 요일, 
       busername AS 부서명, busertel AS 부서전화
FROM jikwon 
LEFT OUTER JOIN buser ON busernum = buserno
WHERE DATE_FORMAT(jikwonibsail, '%w') IN (
    -- 요일별로 그룹화하여 카운트한 데이터 중 최댓값과 일치하는 요일만 추출
    SELECT DATE_FORMAT(jikwonibsail, '%w') FROM jikwon
    GROUP BY DATE_FORMAT(jikwonibsail, '%w') 
    HAVING COUNT(*) = (
        SELECT MAX(cnt) 
        FROM (SELECT COUNT(*) AS cnt FROM jikwon GROUP BY DATE_FORMAT(jikwonibsail, '%w')) AS b
    )
);
```

> **핵심 규칙**: `FROM` 절 안에 서브쿼리를 하나의 가상 테이블로 사용할 때는 문법 오류를 방지하기 위해 반드시 외부에서 식별할 수 있는 **별명(Alias, 예: `AS b`)**을 붙여야 한다.