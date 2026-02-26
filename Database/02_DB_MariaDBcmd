# MariaDB SQL 기본 정리

> **환경 참고**
> - MariaDB 프롬프트: 일회용 / 검증용 -> 실제 상황에선 파이썬 작성 후 검증에 사용
> - 수업에선 편의를 위해 **HeidiSQL** 사용

---

## 기본 규칙

- SQL 문 끝에 `;` 는 **MariaDB 프롬프트에서만** 필요
- 실제 SQL 문 자체에는 `;` 포함하지 않음
- SQL 키워드는 **대소문자 구분 없음** (`SELECT` = `select`)

---

## Database 관련

```sql
-- 데이터베이스 목록 조회
SHOW DATABASES;

-- 데이터베이스 생성
CREATE DATABASE exdb;

-- 데이터베이스 선택 (사용)
USE test;

-- 데이터베이스 삭제
DROP DATABASE exdb;
```

---

## Table 관련

```sql
-- 테이블 목록 조회
SHOW TABLES;

-- 테이블 구조 확인
DESC mytab;

-- 테이블 생성
CREATE TABLE mytab (
    no   INT,
    name VARCHAR(10)
);

-- 테이블 삭제
DROP TABLE mytab;
```

---

## CRUD

### Read — 데이터 조회

```sql
SELECT * FROM mytab;
```

### Create — 데이터 삽입

```sql
-- 단일 행
INSERT INTO mytab (no, name) VALUES (1, '홍길동');

-- 다중 행
INSERT INTO mytab (no, name) VALUES (2, '김철수'), (3, '이영희');
```

### Update — 데이터 수정

```sql
UPDATE mytab SET name = '홍' WHERE no = 1;
```

### Delete — 데이터 삭제

```sql
DELETE FROM mytab WHERE no = 2;
```

---

## 빠른 참조 요약

| 작업 | 명령어 |
|------|--------|
| DB 목록 | `SHOW DATABASES;` |
| DB 생성 | `CREATE DATABASE 이름;` |
| DB 선택 | `USE 이름;` |
| DB 삭제 | `DROP DATABASE 이름;` |
| 테이블 목록 | `SHOW TABLES;` |
| 테이블 구조 | `DESC 테이블명;` |
| 테이블 생성 | `CREATE TABLE 테이블명 (컬럼 타입, ...);` |
| 테이블 삭제 | `DROP TABLE 테이블명;` |
| 조회 | `SELECT * FROM 테이블명;` |
| 삽입 | `INSERT INTO 테이블명 (컬럼) VALUES (값);` |
| 수정 | `UPDATE 테이블명 SET 컬럼=값 WHERE 조건;` |
| 삭제 | `DELETE FROM 테이블명 WHERE 조건;` |