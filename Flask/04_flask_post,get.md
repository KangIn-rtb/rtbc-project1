# 4. Flask 폼 데이터 전송 (GET vs POST 방식)

## 1. GET 방식과 POST 방식의 이해

클라이언트(웹 브라우저)에서 서버(Flask)로 데이터를 보낼 때 사용하는 대표적인 두 가지 HTTP 통신 방식이다.

* **GET 방식**: URL의 끝에 데이터(Query String)를 매달아 전송한다. (`요청명?변수=값&변수=값`) 
  * 데이터가 화면에 노출되며, 전송 길이에 제한이 있다.
  * Flask에서는 `request.args.get("변수명")`으로 데이터를 추출한다.
* **POST 방식**: HTTP 요청의 Body 영역에 데이터를 숨겨서 전송한다.
  * URL에 데이터가 노출되지 않아 GET 방식보다 보안상 유리하며 대용량 데이터 전송이 가능하다.
  * Flask에서는 `request.form.get("변수명")`으로 데이터를 추출한다.
  * 서버에서 받을 때 라우팅 데코레이터에 반드시 `methods=['POST']`를 명시해야 한다.

> **주의**: 클라이언트에서 서버로 넘어오는 모든 데이터는 기본적으로 **문자열(String) 타입**이다. 숫자로 계산이 필요하다면 서버 단에서 형변환(`int()`, `float()`)을 거쳐야 한다.


## 2. Flask 서버 라우팅 코드 (`app.py`)
`request` 객체를 활용하여 클라이언트가 보낸 폼 데이터를 수신하고 가공한 뒤, 다시 결과 템플릿으로 넘겨주는 전체 흐름이다.

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index")
def index0():
    return render_template("index.html")

# ==========================================
# GET 방식 라우팅
# ==========================================
@app.route("/get")
def get():
    return render_template("get.html")

@app.route("/get_result")
def get_result():
    # GET 방식 요청 데이터는 request.args.get()으로 받는다.
    name = request.args.get("username")
    age = request.args.get("age") # 넘어온 데이터는 모두 문자열 취급이다.
    
    age = age + "살" # 문자열 결합 연산 수행
    
    return render_template("get_result.html", name=name, age=age)

# ==========================================
# POST 방식 라우팅
# ==========================================
@app.route("/post")
def post():
    return render_template("post.html")

# POST 방식은 라우트에 반드시 methods=['POST']를 명시해야 한다.
@app.route("/post_result", methods=['POST'])
def post_result():
    # POST 방식 요청 데이터는 request.form.get()으로 받는다.
    name = request.form.get("username")
    email = request.form.get("email")
    
    return render_template("post_result.html", name=name, email=email)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
```


## 3. GET 방식 템플릿 작성

### 1) 입력 화면 (`get.html`)
링크(`<a>` 태그)를 통해서 직접 URL에 쿼리 스트링을 달아 전송할 수도 있고, 폼 태그의 `method="get"`을 이용할 수도 있다.
```html
{% extends "base.html" %}
{% block title %}GET 입력{% endblock %}

{% block content %}
    <h2>GET 방식 요청 (요청명?변수=값&변수=값)</h2>
    
    방법1 : 하이퍼링크로 직접 전달<br>
    <a href="/get_result?username=관우&age=26">GET으로 자료 전달하기</a>
    <br><br>
    
    방법2 : Form 태그 이용 전달<br>
    <form action="get_result" method="get">
        이름 : <input type="text" name="username"><br>
        나이 : <input type="number" name="age"><br>
        <input type="submit" value="전송">
    </form>
{% endblock %}
```

### 2) 결과 화면 (`get_result.html`)
```html
{% extends "base.html" %}
{% block title %}GET 결과{% endblock %}

{% block content %}
    <h2>GET 방식 결과</h2>
    이름 : {{ name }}<br>
    나이 : {{ age }}<br>
    <br>
    <a href="/index">홈으로 돌아가기</a>
{% endblock %}
```


## 4. POST 방식 템플릿 작성 (자바스크립트 유효성 검사 포함)

### 1) 입력 화면 (`post.html`)
순수 자바스크립트(Vanilla JS)를 이용해 폼 전송 전에 데이터가 올바른지 검사하는 로직이 포함되어 있다.
```html
{% extends "base.html" %}
{% block title %}POST 입력{% endblock %}

{% block content %}
    <h2>POST 방식 요청 (자료가 Body 영역에 담겨 서버로 전달)</h2>
    <ul>
        <li>대량의 데이터 및 보안이 필요한 데이터 전송 가능</li>
    </ul>
    
    <form action="post_result" method="post" name="postForm">
        이름 : <input type="text" name="username" id="username"><br>
        이메일 : <input type="text" name="email" id="email"><br>
        <input type="button" value="전송" id="btnSend">
    </form>

    <script>
    // DOMContentLoaded: HTML 문서가 완전히 로드된 후 스크립트 실행
    document.addEventListener("DOMContentLoaded", () => {
        const form = document.querySelector("form[name='postForm']");
        const btn = document.querySelector("#btnSend");

        // 버튼 클릭 시 폼 전송 이벤트를 발생시킨다.
        btn.addEventListener("click", () => {
            form.requestSubmit(); // 폼의 submit 이벤트를 정상적으로 트리거함
        });

        // 폼이 제출(submit)될 때 실행되는 유효성 검사 로직
        form.addEventListener("submit", (event) => {
            const name = document.querySelector("#username").value.trim();
            const email = document.querySelector("#email").value.trim();
            
            if(!name) {
                alert("이름을 입력하세요.");
                event.preventDefault(); // 전송 중단
                return;
            }

            // 이메일 칸이 비었거나 '@' 기호가 포함되지 않은 경우
            if(!email || !email.includes("@")) {
                alert("올바른 이메일 형식을 입력하세요.");
                event.preventDefault(); // 전송 중단
                return;
            }
        });
    });
    </script>
{% endblock %}
```

### 2) 결과 화면 (`post_result.html`)
```html
{% extends "base.html" %}
{% block title %}POST 결과{% endblock %}

{% block content %}
    <h3>POST 전송 결과</h3>
    이름: {{ name }}<br>
    이메일: {{ email }}<br>
    <br>
    <a href="/index">홈으로 돌아가기</a>
{% endblock %}
```