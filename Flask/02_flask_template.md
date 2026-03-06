# 2. Flask 템플릿 엔진 (Jinja2)과 렌더링

## 1. 템플릿 엔진과 Jinja2의 개념

파이썬 코드 안에서 `print()`나 `return`으로 길고 복잡한 HTML을 직접 작성하는 것은 매우 비효율적이다. 이를 해결하기 위해 Flask는 **Jinja2**라는 강력한 템플릿 엔진을 내장하고 있다.

* **Jinja2**: HTML 파일 안에 파이썬 변수를 넣거나, 조건문(`if`), 반복문(`for`) 등을 사용할 수 있게 해주는 도구이다. 서버에서 HTML 문서를 동적으로 완성한 후 클라이언트(브라우저)로 전송할 수 있게 해준다.
* **`render_template()`**: Flask에서 제공하는 함수로, 지정한 HTML 템플릿 파일을 읽어와 필요한 변수 값을 채워 넣고 완성된 HTML 문서로 변환해주는 역할을 한다.

> ** [중요] Flask의 기본 폴더 구조 규칙**
> `render_template()` 함수가 HTML 파일을 정상적으로 찾고, 이미지를 화면에 띄우기 위해서는 반드시 아래와 같은 폴더 구조를 지켜야 한다.
> * **`templates/`** 폴더: `.html` 파일들을 모아둔다.
> * **`static/`** 폴더: 이미지(`.png`, `.jpg`), CSS, JS 파일 등 정적 파일들을 모아둔다.


## 2. Flask 라우팅 및 서버 실행 코드 (app.py)
Flask 앱의 진입점(Entry point)으로, 라우팅과 서버 실행을 담당한다. 기본적으로 로컬호스트 환경에서 실행되지만, `waitress` 등의 WSGI 서버를 결합하면 외부(원격) 서비스도 가능하다.

```python
from flask import Flask, render_template

app = Flask(__name__)

# 1. 홈 페이지 라우팅
@app.route("/")
def home():
    # templates 폴더 안에 있는 home.html을 렌더링하여 반환한다.
    return render_template("home.html")

# 2. Jinja2 템플릿 변수 전달 라우팅
@app.route("/hello")
def hello():
    name = "길동아"
    addr = "강남구 테헤란로"
    # HTML 템플릿으로 데이터를 전달할 때는 '변수명=파이썬데이터' 형태로 적어준다.
    return render_template("hello.html", name=name, juso=addr)

# 3. 정적 파일(이미지) 출력 라우팅
@app.route("/world")
def world_image():
    return render_template("my.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
```


## 3. HTML 템플릿 파일 작성 (`templates/` 폴더 내부)

### 1) `home.html` (메인 페이지)
다른 경로들로 이동할 수 있는 단순한 a 태그 링크들로 구성된 페이지이다.
```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>홈 페이지</title>
</head>
<body>
    <h2>홈 페이지</h2>
    <a href="/hello">인사하기</a><br>
    <a href="/world">그림보기</a><br>
</body>
</html>
```

### 2) `hello.html` (Jinja2 변수 바인딩)
`{{ }}` (이중 중괄호) 기호를 사용하면 파이썬 코드(`app.py`)에서 `render_template`을 통해 넘겨준 변수의 값을 HTML 문서 안에 출력할 수 있다.
```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello</title>
</head>
<body>
    안녕, {{name}}! {{juso}} 지역 날씨는 어때? {{name}}
    <br><br>
    <a href="/">홈으로</a>
</body>
</html>
```

### 3) `my.html` (정적 이미지 파일 연결)
파이썬 서버를 통해 HTML을 렌더링할 때, 서버 폴더 구조에 맞추어 `static` 폴더에 위치한 이미지를 불러오는 페이지이다.
```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>이미지 보기</title>
</head>
<body>
    도시 이미지<br>
    <img src="../static/images/satporo.png" style="width: 300px;" alt="삿포로 이미지">
    <br><br>
    <a href="/">홈으로</a>
</body>
</html>
```