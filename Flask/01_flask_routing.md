# 1. Flask 라우팅, WSGI 서버 및 요청/응답 처리

## 1. Flask와 실무용 WSGI 서버 (Waitress)

Flask에 내장된 기본 서버는 가볍고 빠르지만(Light-weight server), 보안과 안정성 측면에서 개발 및 학습용으로만 적합하다. 실제 서비스(Production) 환경에서는 Python 애플리케이션 서버 코드를 실행해서 다수의 요청을 안정적으로 처리해 줄 실무용 **WSGI 서버**(gunicorn, waitress 등)와 웹 서버(nginx 등)를 연동해서 사용해야 한다.

* 윈도우 환경 등에서 간편하게 사용할 수 있는 실무용 서버로 `waitress`가 있으며, `pip install waitress` 명령어로 설치하여 사용한다.

### 라우팅 및 Waitress 구동 실습 코드
`@app.route("경로")` 데코레이터를 사용하여 URL 경로(URL 매핑)와 클라이언트 요청을 처리할 함수를 연결한다. 동적 URL 리소스(`<name>`)를 받아 함수 매개변수로 활용할 수도 있다.

```python
from flask import Flask
from waitress import serve # 실무용 WSGI 서버

app = Flask(__name__) # flask 객체 생성

@app.route("/") 
def abc(): 
    # 클라이언트 요청이 '/'일 때 수행되는 함수
    return "<h1>안녕하세요</h1>"

@app.route("/about")
def about():
    return "플라스크를 소개하자면..."

# 동적 라우팅: URL 경로의 일부를 변수로 받음
@app.route("/user/<name>")
def user(name):
    return f"내 친구 {name}"

if __name__ == "__main__":
    # 개발용 내장 서버 구동 방식
    # app.run(debug=True, host='0.0.0.0', port=5000)
    
    # Waitress 실무용 서버 구동 방식
    print("웹 서버 서비스 시작...")
    serve(app=app, host='0.0.0.0', port=8000)
```


## 2. 요청(Request)과 응답(Response) 처리 (GET / POST)

클라이언트가 폼(Form) 등을 통해 서버로 데이터를 보낼 때, Flask는 `request` 객체를 통해 해당 정보를 받아내고 `make_response`를 통해 응답을 생성한다.

* **`request`**: 현재 들어온 HTTP 요청 정보(파라미터, 폼 데이터, 헤더, 쿠키 등)를 담고 있는 객체이다.
* **`make_response`**: 응답 객체를 직접 생성하여 반환할 때 사용하는 함수이며, HTTP 상태 코드(예: 200, 405 등)를 명시적으로 지정할 수 있다.

### GET/POST 분기 처리 및 폼 데이터 수신 코드
라우트 설정 시 `methods=['GET', 'POST']` 리스트를 통해 허용할 HTTP 메서드들을 지정한다. 이후 함수 내부에서는 `request.method`의 값(단수형 문자열)을 비교하여 분기 처리한다.

```python
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>홈 페이지</h2><p><a href='/login'>/login으로 이동해 보세요</a></p>"

# GET과 POST 요청을 모두 허용하도록 methods 지정
@app.route("/login", methods=['GET', 'POST']) 
def login():
    if request.method == 'GET': 
        # GET 요청 시: 로그인 입력 폼을 담은 HTML 문자열 반환
        return """
            <h2>로그인 페이지</h2>
            <form method="post"> 
                <input type="text" name="username" placeholder="사용자 이름 입력">
                <button type="submit">로그인</button>
            </form>
            <p>POST 요청 시 username 값을 서버가 받아 처리함</p>
        """             
    elif request.method == 'POST':
        # POST 요청 시: body에 담겨온 폼 데이터를 추출 (없으면 빈 문자열 반환 후 공백 제거)
        user = request.form.get("username", '').strip()
        
        if not user:
            return "사용자 이름을 올바르게 입력하세요!<br><a href='/login'>돌아가기</a>"
        
        # 정상 입력 시 응답 메시지 생성
        message = f"""
            <h2>로그인 성공!</h2>
            <p>안녕하세요 {user} 회원님. 서비스를 마음껏 활용하세요.</p>
            <a href="/">홈으로 돌아가기</a>
        """
        # make_response를 통해 내용과 HTTP 상태 코드(200: 정상)를 함께 반환
        return make_response(message, 200)
        
    else:
        # GET, POST 외의 잘못된 방식의 요청이 들어왔을 때 (405: Method Not Allowed)
        return make_response('잘못된 요청', 405)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
```