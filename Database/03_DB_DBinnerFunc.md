# 함수

## 1. 내장 함수 (HeidiSQL 및 DB 내장)
내장 함수는 필요할 때마다 검색하여 사용하는 것이 효율적이다.

### 문자열 함수
* **추출 및 길이 확인**: `SUBSTR`, `LENGTH`, `INSTR` 등을 사용하여 문자열을 자르거나 길이를 확인한다.
```sql
SELECT SUBSTR('hello world', 3), SUBSTR('hello world', 3, 3), SUBSTR('hello world', -3, 3) FROM DUAL;
SELECT LENGTH('hello world'), INSTR('hello world', 'e') FROM DUAL;
```

### 날짜 함수
* **`DATE_ADD`**: 날짜(현재 시간 포함)에 특정 요소를 더할 때 사용한다.
* **`DATE_FORMAT`**: 날짜의 출력 서식을 변경한다.
```sql
SELECT jikwonname, jikwonibsail, DATE_FORMAT(jikwonibsail, '%W') FROM jikwon WHERE busernum = 10;
```

### 기타 함수 (순위 및 NULL 처리)
* **순위 함수**: `RANK() OVER (ORDER BY ~ DESC)`, `DENSE_RANK() OVER (ORDER BY ~ DESC)` 형태를 띤다.
* **`NVL` (또는 `IFNULL`)**: 값이 NULL일 경우 대체값을 지정한다.
* **`NVL2`**: 값이 NULL이 아닐 때와 NULL일 때의 반환값을 각각 지정한다.
* **`NULLIF`**: 두 값이 일치하면 NULL을, 아니면 첫 번째 값을 반환한다.
```sql
SELECT jikwonname, jikwonjik, NVL(jikwonjik, '임시직') FROM jikwon;
SELECT jikwonname, jikwonjik, NVL2(jikwonjik, '정규직', '임시직') FROM jikwon;
SELECT jikwonname, jikwonjik, NULLIF(jikwonjik, '대리') FROM jikwon;
```


## 2. 조건 표현식 (CASE, IF)

### CASE 표현식
조건에 따라 반환할 값을 다르게 설정한다. `ELSE`는 생략 가능하다.
```sql
-- 형식 1: 값을 직접 비교
SELECT CASE 10/5 WHEN 5 THEN '안녕' WHEN 2 THEN '반가워' ELSE '잘가' END AS 결과 FROM DUAL; 
SELECT jikwonname, jikwonpay, jikwonjik, 
       CASE jikwonjik WHEN '이사' THEN jikwonpay*0.05 
                      WHEN '부장' THEN jikwonpay*0.04 
                      ELSE jikwonpay*0.02 END AS donation 
FROM jikwon;

-- 형식 2: 조건식 사용
SELECT jikwonname, 
       CASE WHEN jikwongen = '남' THEN '남성' 
            WHEN jikwongen = '여' THEN '여성' END AS gender 
FROM jikwon;
```

### IF 함수
`IF(조건, 참일 때 값, 거짓일 때 값)` 형태로 간단한 분기 처리에 사용한다.
```sql
SELECT jikwonname, jikwonpay, IF(TRUNCATE(jikwonpay/1000, 0) >= 5, 'good', 'normal') AS result FROM jikwon;
```


## 3. 그룹 함수 (GROUP BY, HAVING)
`GROUP BY`는 집계 함수(SUM, AVG, COUNT 등)를 적용할 범위를 지정하는 역할을 한다. 
내부적으로 정렬 처리를 수반하며, `GROUP BY` 대상 컬럼에 대해서는 `ORDER BY`를 직접 사용할 수 없으나 출력된 최종 결과에 대해서는 `ORDER BY` 적용이 가능하다.

* **`WHERE` vs `HAVING`**: `WHERE`는 그룹화 이전에 원본 데이터를 필터링하고, `HAVING`은 그룹화 및 집계가 끝난 결과에 대해 조건을 검사한다.

```sql
SELECT jikwongen, AVG(jikwonpay), COUNT(*) FROM jikwon GROUP BY jikwongen;
SELECT busernum, SUM(jikwonpay) FROM jikwon GROUP BY busernum;

-- 그룹화 후 조건 검사 (HAVING)
SELECT busernum, SUM(jikwonpay) FROM jikwon GROUP BY busernum HAVING SUM(jikwonpay) >= 35000;

-- 별칭(Alias) 활용: HAVING과 ORDER BY 절에서는 SELECT에서 정의한 별칭 사용이 가능하다.
SELECT busernum, SUM(jikwonpay) AS paytotal FROM jikwon WHERE jikwongen = '여' GROUP BY busernum HAVING paytotal >= 15000;
```

### [연습 문제: 그룹 함수]
```sql
-- 1. 직급별 급여의 평균 (NULL인 직급 제외) 
SELECT jikwonjik AS 직급, AVG(jikwonpay) AS 급여평균 FROM jikwon WHERE jikwonjik IS NOT NULL GROUP BY jikwonjik;

-- 2. 직급별 성별 인원수, 급여합 출력 (NULL인 직급은 임시직으로 표현) 
SELECT NVL(jikwonjik, '임시직') AS 직급, jikwongen AS 성별, COUNT(*) AS 인원수, SUM(jikwonpay) AS 급여합 FROM jikwon GROUP BY jikwonjik, jikwongen;
```


## 4. 테이블 조인 (JOIN)

하나 이상의 테이블에서 원하는 자료를 추출하기 위해 연결하는 기능이다. 조인을 수행하려면 반드시 공통 컬럼이 있어야 하며, 컬럼명은 달라도 되지만 데이터 형식은 같아야 한다. 가독성을 위해 테이블에 별칭(Alias)을 부여하고 `별칭.컬럼명` 형태로 사용하는 것이 권장된다.

* **CROSS JOIN**: 양 테이블의 모든 행을 교차 조합한다.
* **EQUI JOIN (내부 조인)**: 조인 조건에 `=` 연산자를 사용한다. (대부분의 PK-FK 조인)
* **NON-EQUI JOIN**: `=` 이외의 연산자(BETWEEN, > 등)를 사용한다.

### INNER JOIN (내부 조인)
두 테이블 모두에 조건이 일치하는 데이터가 있는 경우에만 추출한다. (ANSI 표준 권장)
```sql
SELECT jikwonno, jikwonname, busername 
FROM jikwon INNER JOIN buser ON busernum = buserno 
WHERE jikwongen = '남';
```

### OUTER JOIN (외부 조인)
한쪽 테이블에만 데이터가 있어도 추출을 허용한다.
```sql
-- LEFT OUTER JOIN: 왼쪽 테이블의 자료는 모두 출력하고, 오른쪽 테이블에 없는 값은 NULL로 표시한다.
SELECT jikwonno, jikwonname, busername FROM jikwon LEFT OUTER JOIN buser ON busernum = buserno;

-- FULL OUTER JOIN (MariaDB 미지원 대체법): LEFT JOIN과 RIGHT JOIN을 UNION으로 합친다.
SELECT jikwonno, jikwonname, busername FROM jikwon LEFT OUTER JOIN buser ON busernum = buserno
UNION 
SELECT jikwonno, jikwonname, busername FROM jikwon RIGHT OUTER JOIN buser ON busernum = buserno;
```


## 5. UNION (집합 연산자)
두 쿼리의 결과를 합친다. 위아래로 합쳐지므로 조회하는 컬럼의 개수와 구조가 동일해야 한다.
```sql
SELECT bun AS 번호, pummok AS 품명 FROM pum1 
UNION 
SELECT mum, sangpum FROM pum2;
```


## 6. 서브쿼리 (Subquery)

쿼리 내부에 포함된 또 다른 쿼리를 뜻한다. 주로 안쪽 질의의 결과를 바깥쪽 질의의 조건이나 데이터로 활용할 때 사용한다.
단일 결과가 아닌 여러 데이터(행)가 반환될 때는 `=` 대신 `IN` 연산자를 사용해야 오류가 발생하지 않는다.

```sql
-- 단일 행 반환 서브쿼리
SELECT * FROM jikwon WHERE jikwonjik = (SELECT jikwonjik FROM jikwon WHERE jikwonname = '이미라');

-- 다중 행 반환 서브쿼리 (IN 사용)
SELECT * FROM jikwon WHERE busernum IN (SELECT buserno FROM buser WHERE buserloc != '인천');
```

### 상관 서브쿼리 (Correlated Subquery)
바깥쪽 쿼리(Outer query)의 각 행을 안쪽 쿼리(Inner query)에서 참조하여 수행하는 방식이다.
```sql
-- 각 부서의 최대 연봉자 구하기
SELECT * FROM jikwon a 
WHERE a.jikwonpay = (SELECT MAX(b.jikwonpay) FROM jikwon b WHERE a.busernum = b.busernum);
```

### ANY, ALL, EXISTS 연산자 (NULL 제외 처리)
* `> ANY`: 서브쿼리 반환값 중 최솟값보다 큰 데이터 (하나라도 크면 참)
* `< ANY`: 서브쿼리 반환값 중 최댓값보다 작은 데이터
* `> ALL`: 서브쿼리 반환값 중 최댓값보다 큰 데이터 (모두보다 커야 참)
* `EXISTS`: 서브쿼리의 반환 결과가 하나라도 존재하면 참(True)을 반환한다.

```sql
-- 30번 부서의 최고 연봉자보다 연봉을 많이 받는 직원
SELECT jikwonno, jikwonname, jikwonpay FROM jikwon 
WHERE jikwonpay > ALL (SELECT jikwonpay FROM jikwon WHERE busernum = 30);

-- 직원이 없는 부서 출력
SELECT busername, buserloc FROM buser bu
WHERE NOT EXISTS (SELECT 1 FROM jikwon WHERE jikwon.busernum = bu.buserno);
```


## 7. 서브쿼리를 이용한 테이블 생성 및 복사
기존 테이블의 구조와 데이터를 이용해 새로운 테이블을 쉽게 생성할 수 있다. 단, Primary Key 등의 제약 조건은 복사되지 않는다.

```sql
-- 데이터와 구조 모두 복사
CREATE TABLE jiktab1 AS SELECT * FROM jikwon;

-- 구조만 복사 (1=0과 같이 거짓 조건을 주어 빈 테이블 생성)
CREATE TABLE jiktab2 AS SELECT * FROM jikwon WHERE 1=0;

-- 이후 원하는 조건의 자료만 서브쿼리를 통해 삽입 가능
INSERT INTO jiktab2 SELECT * FROM jikwon WHERE jikwonjik='과장';
```