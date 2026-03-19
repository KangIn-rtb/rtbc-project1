# 5. Flask 상태 유지 기술 (쿠키와 세션)

## 1. 쿠키(Cookie)와 세션(Session)의 개념

웹 통신을 담당하는 HTTP는 기본적으로 **Stateless(무상태)** 프로토콜이다. 즉, 서버는 클라이언트의 이전 요청이나 현재 상태를 기억하지 못한다. 이를 해결하고 로그인 상태나 장바구니 데이터를 유지하기 위해 쿠키와 세션을 사용한다.

### 쿠키 (Cookie)
* **저장 위치**: 클라이언트(웹 브라우저) 쪽에 키-값(Key-Value) 형태로 작은 데이터를 저장한다.
* **특징**: 서버가 쿠키를 구워 브라우저에 보내면, 브라우저는 다음 요청부터 자동으로 쿠키를 서버에 함께 전송하여 흔적을 알린다.
* **단점**: 클라이언트가 임의로 쿠키를 차단하거나 조작/삭제할 수 있어 보안 신뢰도가 떨어진다.

### 세션 (Session)
* **저장 위치**: 중요한 클라이언트의 정보(상태)를 서버 메모리(또는 DB)에 저장한다.
* **특징**: 쿠키의 보안 취약점을 보완한 방식이다. 클라이언트에게는 암호화된 '세션 ID'만 쿠키로 발급하고, 실제 데이터는 서버가 쥐고 있는다.
* **Flask의 세션**: Flask는 서버 메모리를 아끼기 위해 클라이언트의 쿠키에 세션 데이터를 저장하되, 서버만 아는 **비밀키(Secret Key)**를 이용해 암호화(서명)하여 데이터 변질 여부를 검증하는 방식을 사용한다.

> **`redirect(url_for('함수명'))`**
> 클라이언트의 요청 없이 서버 내부에서 강제로 다른 라우팅 함수를 호출하여 페이지를 이동(리디렉션)시켜야 할 때 사용한다.


## 2. 쿠키 (Cookie) 실습

### 1) 쿠키 생성, 읽기, 삭제 (기본)
쿠키를 브라우저에 저장하려면 일반 `return` 대신 **응답 객체(`make_response`)**를 먼저 생성한 뒤 그 객체에 쿠키를 세팅해서 반환해야 한다.

```python
from flask import Flask, render_template_string, request, make_response, redirect, url_for

app = Flask(__name__)

HOME_HTML = """
<h2>Flask Cookie test</h2>
<form action="/set_cookie" method="post">
    쿠키 값 : <input type="text" name="name" placeholder="예:hong">
    <button type="submit">쿠키 저장</button>
</form>
<p>
    <a href="/read_cookie">쿠키 읽기</a>
    <a href="/delete_cookie">쿠키 삭제</a>
</p>
"""

@app.get("/")
def home():
    return render_template_string(HOME_HTML) # 문자열을 HTML로 바로 렌더링

@app.post("/set_cookie")
def set_cookie():
    name = request.form.get("name", "anonymous")
    
    # 1. 이동할 목적지 응답 객체 생성
    resp = make_response(redirect(url_for("read_cookie"))) 
    
    # 2. 브라우저에 쿠키 굽기(저장)
    resp.set_cookie( 
        key="name",             # 쿠키 이름
        value=name,             # 쿠키 값
        max_age=60 * 5,         # 유효 시간 (5분 뒤 만료)
        httponly=True,          # JS에서 document.cookie로 접근 불가하도록 보안 설정
        samesite="Lax"          # CSRF 공격 방지용
    )
    return resp 

@app.get("/read_cookie")
def read_cookie():
    # 클라이언트가 요청에 실어 보낸 쿠키 읽기
    name = request.cookies.get("name")
    return f"<h3>쿠키 읽기</h3><p>name 쿠키 값: {name}</p><a href='/'>홈페이지</a>"
    
@app.get("/delete_cookie")
def delete_cookie():
    resp = make_response(redirect(url_for("home")))
    # 쿠키 만료(삭제) 처리
    resp.delete_cookie("name")
    return resp

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### 2) 쿠키를 활용한 로그인 & 방문 횟수 카운트
```python
from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)
COOKIE_AGE = 60 * 60 * 24 * 7 # 7일 유지

@app.get("/login")
def login():
    name = request.cookies.get("name")
    visits = request.cookies.get("visits")
    
    if name:
        visits = int(visits or "0") + 1
        msg = f"안녕하세요. {name}님 {visits}번째 방문 입니다."
    else:
        visits = None
        msg = "이름을 입력하면 방문 횟수를 쿠키로 기억합니다."
        
    resp = make_response(render_template("login.html", msg=msg, visits=visits, name=name))
    
    # 로그인 상태면 visits 쿠키 1 증가시켜 갱신
    if name: 
        resp.set_cookie("visits", str(visits), max_age=COOKIE_AGE, samesite="Lax")
        
    return resp

@app.post("/login")
def login2():
    name = (request.form.get("name") or "").strip()
    resp = make_response(redirect(url_for("login")))
    resp.set_cookie("name", name, max_age=COOKIE_AGE, samesite="Lax")
    resp.set_cookie("visits", "0", max_age=COOKIE_AGE, samesite="Lax")
    return resp

@app.post("/logout")
def logout():
    resp = make_response(redirect(url_for("login")))
    resp.delete_cookie("name")
    resp.delete_cookie("visits")
    return resp
```


## 3. 세션 (Session) 실습
Flask에서 세션을 사용하려면 데이터를 암호화하기 위한 **`secret_key`** 설정이 반드시 필요하다. 데이터는 딕셔너리처럼 `session['키']` 형태로 다룬다.

### 1) 세션 기본 (운영체제 선택 예제)
```python
from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta

app = Flask(__name__)

# Flask 세션 암호화를 위한 비밀키 설정 (필수)
app.secret_key = "abcdef123456" 

# 세션 유지(만료) 시간 5초로 설정
app.permanent_session_lifetime = timedelta(seconds=5) 

@app.route("/setos")
def setos():
    favorite_os = request.args.get("favorite_os")
    
    if favorite_os:
        session.permanent = True # 설정한 만료 시간(5초) 적용 활성화
        session["f_os"] = favorite_os # 세션 딕셔너리에 데이터 저장
        return redirect(url_for("showos"))
    else:
        return render_template("setos.html")
    
@app.route("/showos")
def showos():
    context = {}
    if "f_os" in session: # 세션에 데이터가 살아있는지 확인
        context["f_os"] = session["f_os"]
        context["message"] = f"당신이 선택한 운영체제는 '{session['f_os']}'"
    else:
        context["f_os"] = None
        context["message"] = "운영체제를 선택하지 않았거나 5초가 지나 세션이 만료됨"
    
    return render_template("showos.html", context=context)
```

### 2) 세션을 활용한 장바구니 구현 (심화)

세션을 활용해 클라이언트가 고른 상품의 이름, 수량, 가격을 누적하여 기억하는 예제이다.

```python
from flask import Flask, render_template, redirect, url_for, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "abcdef12345"
app.permanent_session_lifetime = timedelta(minutes=5) # 5분 유지

# 상품 DB (JSON/Dict 형태 모의 데이터)
products = [ 
    {"id":1, "name":"노트북", "price":3500000},
    {"id":2, "name":"가방", "price":73000},
    {"id":3, "name":"RAM", "price":430000},
    {"id":4, "name":"키보드", "price":55000},
]

@app.route("/")
def product_list():
    return render_template("products.html", products=products)

@app.route("/cart")
def show_cart():
    cart = session.get("cart", {}) # 세션에서 cart 데이터 가져오기 (없으면 빈 딕셔너리)
    return render_template("cart.html", cart=cart)

@app.route("/add/<int:id>")
def add_cart(id):
    cart = session.get("cart", {})
    
    # next()를 활용해 id와 일치하는 상품 검색
    product = next((p for p in products if p["id"] == id), None)
    
    if product is None:
        return "상품을 찾을 수 없습니다.", 404
        
    item_name = product["name"]
    if item_name in cart:
        cart[item_name]["qty"] += 1 # 이미 카트에 있으면 수량만 1 증가
    else:
        cart[item_name] = {"price": product["price"], "qty": 1} # 없으면 신규 추가
        
    session["cart"] = cart  # 변경된 장바구니 딕셔너리를 다시 세션에 덮어쓰기
    session.permanent = True 
    
    return redirect(url_for("show_cart"))

@app.route("/remove/<item_name>")
def remove_to_cart(item_name):
    # 장바구니 부분 삭제 로직
    cart = session.get("cart", {})
    if item_name in cart:
        del cart[item_name]
        session["cart"] = cart # 변경 후 반드시 갱신해야 함
    return redirect(url_for("show_cart")) 
    
@app.route("/clear")
def clear_cart():
    # 장바구니 전체 비우기 로직 (pop 사용)
    session.pop("cart", None)
    return redirect(url_for("show_cart"))
```

### 3) 장바구니 템플릿 (`cart.html`)
Jinja2 템플릿의 `{% set %}` 변수를 활용하면 상품별 총합계 금액을 템플릿 내에서 직접 계산하여 출력할 수 있다.
```html
{% extends "base.html" %}
{% block content %}
    <h3>* 장바구니 *</h3>
    {% if cart %}
    <table border="1">
        <tr>
            <th>상품명</th><th>가격</th><th>수량</th><th>총합</th><th>비고</th>
        </tr>
        {% for name, info in cart.items() %}
            {% set subtotal = info.price * info.qty %} 
            <tr>
                <td>{{ name }}</td>
                <td>{{ info.price }}</td>
                <td>{{ info.qty }}</td>
                <td>{{ subtotal }}</td>
                <td><a href="/remove/{{ name }}">삭제</a></td>
            </tr>
        {% endfor %}
    </table>
    <br>
    <a href="/clear">장바구니 비우기</a>
    <a href="/">상품 더 담기</a>
    {% else %}
    <p>장바구니가 비었습니다.</p>
    <a href="/">상품 담으러 가기</a>
    {% endif %}
{% endblock %}
```