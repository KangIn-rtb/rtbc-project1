# 2. 파이썬 웹 프로그래밍 기초 (Web Programming Basic)

## 1. 웹의 기본 개념
* **URL 구조**: `http(프로토콜)://도메인_또는_IP주소:포트/요청명`
* **기본 요청명**: 요청명을 명시하지 않으면 서버는 기본적으로 `index.html`을 찾아 보여준다.
* **웹 브라우저의 역할**: 브라우저는 파이썬 같은 서버용 코드를 해석하지 못하며, 오직 **HTML 해석기** 역할만 수행한다.

### HTTP 상태(오류) 코드
* `3xx` (리디렉션): 서버가 클라이언트(브라우저)에게 "최종 수정일 이후 변경된 내용이 없으니 캐시된 데이터를 사용하라"고 알리는 등의 정상적인 응답이다.
* `4xx` (클라이언트 오류): 경로를 찾을 수 없거나 파일이 없는 경우 발생한다. (예: 404 Not Found)
* `5xx` (서버 오류): 서버 내부의 권한 문제나 코드 에러 등으로 인해 발생한다. (예: 500 Internal Server Error)


## 2. 파이썬 HTTP 웹 서버 구동 (CGI)

파이썬의 내장 라이브러리인 `http.server`를 이용하면 간단한 웹 서버를 구축할 수 있다. `CGIHTTPRequestHandler`를 사용하면 파이썬 스크립트(`.py`)를 웹 상에서 실행할 수 있다.

### 서버 실행 코드 (httpserver.py)
```python
from http.server import HTTPServer, CGIHTTPRequestHandler

PORT = 8888

class Handler(CGIHTTPRequestHandler):
    # cgi-bin 폴더 안에 있는 파이썬 스크립트의 실행 권한을 부여한다.
    cgi_directories = ['/cgi-bin']    

def run():
    serv = HTTPServer(('127.0.0.1', PORT), Handler)
    
    print("웹 서비스 진행중...")
    try:
        serv.serve_forever() # 서버 무한 대기 (실행)
    except Exception as e:
        print('err : ', e)
        print("서버 종료")
    finally:
        serv.server_close()

if __name__ == "__main__":
    run()
```

### 파이썬 모듈로 HTML 출력하기 (hello.py)
브라우저는 HTML만 해석할 수 있으므로, 파이썬 코드의 실행 결과를 브라우저에 띄우려면 `print()` 함수를 이용해 HTML 태그 형태로 문자열을 전달해야 한다.
```python
# cgi-bin/hello.py
import sys
sys.stdout.reconfigure(encoding='utf-8') # 한글 깨짐 방지

ss = "파이썬 자료 출력"
ss2 = 123

# 클라이언트 브라우저로 HTML 형식 출력
print('Content-Type: text/html; charset=utf-8')
print() # 헤더와 바디를 구분하는 빈 줄 (필수)
print("<html><head><meta charset='UTF-8'></head><body>")
print("<b>안녕 파이썬 모듈로 작성한 문서야</b><br/>")
print("파이썬 변수 값 : %s, %d" % (ss, ss2))
print("</body></html>")
```
> **템플릿(Template) 파일**: 위처럼 `print()`로 일일이 HTML을 작성하는 것은 비효율적이므로, 실제 개발에서는 HTML 코드 안에 파이썬 변수를 끼워 넣을 수 있는 템플릿 엔진을 주로 사용한다.


## 3. GET 방식 vs POST 방식

클라이언트가 서버로 데이터를 보낼 때 사용하는 대표적인 두 가지 방식이다.

### GET 방식
* **형태**: `요청명?변수명=값&변수명=값` (URL 뒤에 데이터가 붙어서 전송됨)
* **특징**: 데이터의 길이가 제한적(보통 256바이트)이므로 대량의 데이터 전송이 불가하다. 
* **단점**: 패스워드 등의 중요 정보가 URL에 그대로 노출되어 보안에 매우 취약하다.

### POST 방식
* **특징**: GET의 단점을 보완하여 데이터를 HTTP Body에 숨겨서 전송하므로 URL에 데이터가 보이지 않는다.
* **용도**: 게시판, 방명록, 사진 업로드 등 크기가 큰 데이터나 보안이 필요한 데이터를 전송할 때 사용한다. HTML Form 태그에 반드시 `method="post"`를 명시해야 한다.

### 데이터 전송 HTML 폼 (friend.html)
```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>친구 정보 입력</title>
</head>
<body>
    <b>**친구 정보**</b><br/>
    <form action="cgi-bin/friend.py" method="post">
        이름 : <input type="text" name="name"> <br/>
        전화 : <input type="text" name="phone"> <br/>
        성별 : 
        <input type="radio" name="gen" value="남" checked>남자
        <input type="radio" name="gen" value="여">여자
        <br/>
        <input type="submit" value="서버로 자료 전송">
    </form>
</body>
</html>
```

### GET / POST 모두 처리하는 파이썬 코드 (friend.py)
환경 변수(`os.environ`)를 확인하여 요청 방식(Method)에 따라 데이터를 추출하는 방식이 다르다.
```python
# cgi-bin/friend.py
import os
import urllib.parse
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. GET / POST 요청 방식 판별
method = os.environ.get("REQUEST_METHOD", "GET")

if method == "POST":
    # POST 방식: Body에서 길이를 읽어와 데이터를 추출한다.
    length = int(os.environ.get("CONTENT_LENGTH", 0))
    body = sys.stdin.read(length)
else:
    # GET 방식: URL의 Query String에서 데이터를 추출한다.
    body = os.environ.get("QUERY_STRING", "")

# 2. 추출한 문자열 데이터를 파이썬 딕셔너리 형태로 파싱
params = urllib.parse.parse_qs(body)

# 3. 데이터 추출 (값이 없을 경우를 대비해 기본값 [""] 설정)
irum = params.get("name", [""])[0]
phone = params.get("phone", [""])[0]
gen = params.get("gen", [""])[0]

# 4. 브라우저로 결과 출력
print('Content-Type: text/html; charset=utf-8')
print()
print(f"""
<html lang="ko">
<head><meta charset="UTF-8"><title>결과 페이지</title></head>
<body>
    <h2>전달받은 데이터 확인</h2>
    <ul>
        <li><b>이름:</b> {irum}</li>
        <li><b>전화번호:</b> {phone}</li>
        <li><b>성별:</b> {gen}</li>
    </ul>
    <a href="../index.html">메인으로 돌아가기</a>
</body>
</html>
""")
```


## 4. 데이터베이스 연동 및 웹 출력 (Web + DB)
파이썬을 이용해 데이터베이스에서 조회한 자료를 HTML 테이블 요소로 가공하여 브라우저에 띄운다.

### DB 데이터 출력 코드 (sangpum.py)
```python
# cgi-bin/sangpum.py
import sys
sys.stdout.reconfigure(encoding='utf-8')

import MySQLdb
import pickle

# 숨겨둔 DB 접속 정보 로드
with open("cgi-bin/mydb.dat", mode="rb") as obj:
    config = pickle.load(obj)

print('Content-Type: text/html; charset=utf-8')
print()
print("<html><body><b>** 상품 정보 **</b></br>")
print("<table border='1'>")
print("<tr><td>코드</td><td>상품명</td><td>수량</td><td>단가(원)</td></tr>")

try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sangdata ORDER BY code DESC")
    datas = cursor.fetchall()
    
    # DB에서 읽어온 데이터를 HTML 테이블의 행(tr)과 열(td)로 반복 출력한다.
    for code, sang, su, dan in datas:
        print(f"<tr><td>{code}</td><td>{sang}</td><td>{su}</td><td>{dan}</td></tr>")
        
except Exception as e:
    print("err : ", e)
finally:
    cursor.close()
    conn.close()
    
print("</table>")
print("</body></html>")
```

## 5. 업데이트된 메인 페이지 (index.html)
위에서 작성한 모든 기능들을 연결하는 최종 메인 페이지 구조이다.
```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>메인</title>
</head>
<body>
    <h1>메인 페이지</h1>
    <a href="cgi-bin/hello.py">hello (기본 출력)</a><br/>
    <a href="cgi-bin/world.py">world</a><br/>
    
    <a href="cgi-bin/my.py?name=tom&age=23">my (GET방식 전송)</a><br/>
    
    <a href="friend.html">friend (GET/POST 폼 입력)</a><br/>
    <a href="cgi-bin/sangpum.py">sangpum (DB 연동 출력)</a>
</body>
</html>
```