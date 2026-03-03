# SQL 심화: 계정 및 권한 관리 (User & Privilege Management)

데이터베이스의 보안과 안전한 운영을 위해 사용자(User) 계정을 생성하고, 각 계정마다 적절한 권한(Privilege)을 부여하거나 회수하는 작업이 필요하다. 
기본 관리자 계정인 `root` 계정은 `INSERT`, `UPDATE`, `DELETE` 등 모든 작업을 자유롭게 수행할 수 있는 최고 권한을 가진다.

## 1. 계정 생성 및 확인
계정을 생성할 때는 접속을 허용할 호스트(Host)를 지정해야 한다.
* `@'%'`: 외부(원격)에서의 접속을 허용한다.
* `@'localhost'`: 데이터베이스가 설치된 로컬 PC에서만의 접속을 허용한다.

```sql
-- 원격 접속이 가능한 사용자 생성
CREATE USER 'testuser'@'%' IDENTIFIED BY '1234'; 

-- 로컬에서만 접속 가능한 사용자 생성
CREATE USER 'testuser'@'localhost' IDENTIFIED BY '1234'; 

-- 생성된 전체 유저 목록 및 호스트 확인
SELECT User, Host FROM mysql.user; 
```


## 2. 권한 부여 (GRANT) 및 회수 (REVOKE)

생성된 계정은 초기에는 아무런 권한이 없으므로 `GRANT` 명령어를 통해 데이터베이스나 테이블에 대한 접근 및 조작 권한을 할당해야 한다. 반대로 부여된 권한을 빼앗을 때는 `REVOKE` 명령어를 사용한다.

### 전체 권한 할당 및 회수
특정 데이터베이스(`mydb.*`) 또는 전체 데이터베이스(`*.*`)에 대한 모든 권한을 제어할 수 있다.
```sql
-- testuser에게 mydb 데이터베이스의 모든 테이블에 대한 모든 권한 부여
GRANT ALL PRIVILEGES ON mydb.* TO 'testuser'@'%'; 
-- (로컬 계정일 경우 'testuser'@'localhost'로 지정)

-- testuser에게 존재하는 모든 데이터베이스(*.*)에 대한 모든 권한 부여 (비밀번호 설정 포함)
GRANT ALL PRIVILEGES ON *.* TO 'testuser'@'%' IDENTIFIED BY '1234'; 

-- testuser가 mydb 데이터베이스에 대해 가지고 있는 모든 권한 회수
REVOKE ALL PRIVILEGES ON mydb.* FROM 'testuser'@'%';
```

### 일부 권한 할당 및 회수
모든 권한이 아닌 `SELECT`, `UPDATE` 등 특정 기능만 제한적으로 할당하거나 회수할 수 있다.
```sql
-- mydb 데이터베이스의 abctab 테이블에 대해 '조회(SELECT)' 권한만 부여
GRANT SELECT ON mydb.abctab TO 'testuser'@'%';

-- abctab 테이블에 대해 '조회(SELECT)'와 '수정(UPDATE)' 권한 부여
GRANT SELECT, UPDATE ON mydb.abctab TO 'testuser'@'%';  

-- abctab 테이블에 부여된 권한 중 '수정(UPDATE)' 권한만 명시적으로 회수
REVOKE UPDATE ON mydb.abctab FROM 'testuser'@'%';
```

### 권한 확인
특정 계정에 현재 어떤 권한들이 부여되어 있는지 확인할 수 있다.
```sql
-- 로컬 testuser 계정의 권한 확인
SHOW GRANTS FOR 'testuser'@'localhost';

-- 외부 접속용 testuser 계정의 권한 확인
SHOW GRANTS FOR 'testuser'@'%';
```

## 3. 계정 삭제 (DROP USER)
더 이상 사용하지 않는 계정은 `DROP USER` 명령어를 통해 데이터베이스에서 완전히 삭제한다.
```sql
-- 외부 접속용 testuser 계정 삭제
DROP USER 'testuser'@'%';
```