# 6. Flask DB 연동 (CRUD 게시판 구현)

## 1. Flask DB 연동 및 주요 개념

웹 페이지에서 데이터베이스(MariaDB/MySQL)에 접근하여 데이터를 조회하고 조작하는 전체 흐름(CRUD)이다.

* **`pymysql`**: 파이썬에서 MySQL/MariaDB에 접속하기 위해 사용하는 라이브러리이다.
* **`DictCursor`**: 기본적으로 DB에서 데이터를 조회하면 튜플 형태 `(1, '마우스', ...)`로 가져오지만, `DictCursor`를 사용하면 딕셔너리 형태 `{'code': 1, 'sang': '마우스'}`로 가져와서 `row['sang']`처럼 키 이름으로 접근할 수 있어 훨씬 직관적이다.
* **`flash()`**: 사용자에게 임시 알림 메시지(예: "저장 성공", "에러 발생" 등)를 띄울 때 사용한다. 내부적으로 세션을 사용하므로 반드시 `app.secret_key` 설정이 필요하며, 템플릿에서 `get_flashed_messages()`로 꺼내서 출력한다.


## 2. 메인 서버 코드 (`app.py`)
데이터베이스 연결 정보 설정과 CRUD(조회, 추가, 수정, 삭제) 라우팅을 모두 포함한 메인 서버 파일이다.

```python
from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages
import pymysql
import os

app = Flask(__name__)
# flash 및 session 데이터 서명용 비밀키 설정
app.secret_key = "abcdef12345" 

# MariaDB 연결 정보 (환경변수 활용, 없으면 기본값 사용)
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "123")
DB_NAME = os.getenv("DB_NAME", "test")

# DB 연결 객체를 반환하는 함수
def get_conn():
    return pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        passwd=DB_PASSWORD,
        database=DB_NAME,
        charset="utf8mb4", # 전 세계 문자 및 이모지 처리
        cursorclass=pymysql.cursors.DictCursor, # SELECT 결과를 딕셔너리로 반환
        autocommit=False   # 수동 트랜잭션 (직접 commit/rollback 제어)
    )

@app.route("/")
def root():
    return redirect(url_for("show_list"))

# ==========================================
# 1. 자료 목록 조회 (Read)
# ==========================================
@app.route("/show/")
def show_list():
    conn = get_conn()
    try:
        with conn.cursor() as cur: # with문을 쓰면 cursor가 자동으로 닫힌다.
            cur.execute("SELECT code, sang, su, dan FROM sangdata ORDER BY code")
            rows = cur.fetchall()
        
        messages = list(get_flashed_messages())
        return render_template("list.html", rows=rows, messages=messages)
    except Exception as e:
        flash(f"DB 자료 읽기 오류 : {e}")
        return render_template("list.html", rows=[], messages=messages)
    finally:
        conn.close()

# ==========================================
# 2. 자료 추가 (Create)
# ==========================================
@app.route("/add/")
def add_form():
    # 추가 폼 화면 출력
    messages = list(get_flashed_messages())
    return render_template("form_add.html", messages=messages) 

@app.post("/save/")
def add_save():
    # 클라이언트로부터 폼 데이터 수신
    sang = (request.form.get("sang") or "").strip()
    su_raw = (request.form.get("su") or "").strip()
    dan_raw = (request.form.get("dan") or "").strip()
    
    # 서버 측 유효성 검사
    if not sang or not su_raw.isdigit() or not dan_raw.isdigit():
        flash("상품명은 필수이며, 수량과 단가는 숫자만 허용됩니다.")
        return redirect(url_for("add_form"))
        
    su = int(su_raw) 
    dan = int(dan_raw)
    
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            # 가장 큰 코드 번호를 찾아 +1 처리 (Auto Increment 대용)
            cur.execute("SELECT MAX(code) AS max_code FROM sangdata")
            row = cur.fetchone()
            max_code = row["max_code"] if row else None
            next_code = (max_code + 1) if max_code is not None else 1
            
            # DB에 INSERT
            cur.execute("INSERT INTO sangdata(code, sang, su, dan) VALUES (%s, %s, %s, %s)", 
                        (next_code, sang, su, dan))
        conn.commit()
        return redirect(url_for('show_list'))
    except Exception as e:
        conn.rollback() 
        flash(f"저장 실패 : {e}")
        return redirect(url_for("add_form"))
    finally:
        conn.close()

# ==========================================
# 3. 자료 수정 (Update)
# ==========================================
@app.route("/edit/<int:code>")
def edit_form(code: int):
    # 동적 라우팅으로 받은 code에 해당하는 상품 정보를 조회하여 폼에 뿌려줌
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM sangdata WHERE code=%s", (code,))
            row = cur.fetchone()
            
        if not row:
            flash("해당 자료가 없습니다.")
            return redirect(url_for("show_list"))
            
        messages = list(get_flashed_messages())
        return render_template("form_edit.html", row=row, messages=messages)
    finally:
        conn.close()

@app.post("/edit/<int:code>/")
def edit_save(code: int):
    sang = (request.form.get("sang") or "").strip()
    su_raw = (request.form.get("su") or "").strip()
    dan_raw = (request.form.get("dan") or "").strip()
    
    if not sang or not su_raw.isdigit() or not dan_raw.isdigit():
        flash("상품명은 필수이며, 수량과 단가는 숫자만 허용됩니다.")
        return redirect(url_for("edit_form", code=code))
        
    su = int(su_raw) 
    dan = int(dan_raw)
    
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("UPDATE sangdata SET sang=%s, su=%s, dan=%s WHERE code=%s", 
                        (sang, su, dan, code))
        conn.commit()
        return redirect(url_for('show_list'))
    except Exception as e:
        conn.rollback() 
        flash(f"수정 실패 : {e}")
        return redirect(url_for("edit_form", code=code))
    finally:
        conn.close()

# ==========================================
# 4. 자료 삭제 (Delete)
# ==========================================
@app.post("/delete/<int:code>/")
def delete_row(code: int):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM sangdata WHERE code=%s", (code,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        flash(f"삭제 중 오류 발생 : {e}")
    finally:
        conn.close()
    return redirect(url_for("show_list"))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
```


## 3. HTML 템플릿 파일 (`templates/` 폴더)

### 1) 목록 조회 화면 (`list.html`)
DB에서 가져온 상품 목록을 보여주고, 각 항목마다 `[수정]` 링크와 `[삭제]` 폼을 배치한다.
```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>상품 목록</title>
</head>
<body>
    <h3>** 상품 정보 **</h3>
    
    {% if messages %}
        <ul>
            {% for m in messages %}
            <li style="color:red;">{{ m }}</li>
            {% endfor %}
        </ul>
    {% endif %}
    
    <p><a href="{{ url_for('add_form') }}">[새 상품 추가]</a></p>
    
    <table border="1">
        <tr>
            <th>코드</th><th>품명</th><th>수량</th><th>단가</th><th>관리</th>
        </tr>
        {% for r in rows %}
        <tr>
            <td>{{ r.code }}</td>
            <td>{{ r.sang }}</td>
            <td>{{ r.su }}</td>
            <td>{{ r.dan }}</td>
            <td>
                <a href="{{ url_for('edit_form', code=r.code) }}">[수정]</a>
                <form action="{{ url_for('delete_row', code=r.code) }}" method="post" style="display: inline;" onsubmit="return confirm('정말 삭제할까요?')">
                    <button type="submit">삭제</button>
                </form>
            </td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```

### 2) 추가 입력 화면 (`form_add.html`)
```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>상품 추가</title>
</head>
<body>
    <h3>상품 추가</h3>
    
    {% if messages %}
        <ul>
            {% for m in messages %}
            <li style="color:red;">{{ m }}</li>
            {% endfor %}
        </ul>
    {% endif %}
    
    <form id="addform" action="{{ url_for('add_save') }}" method="post">
        <p>품명 : <input type="text" name="sang" id="sang"></p>
        <p>수량 : <input type="text" name="su" id="su"></p>
        <p>단가 : <input type="text" name="dan" id="dan"></p>
        <button type="submit">저장</button>
        <a href="{{ url_for('show_list') }}">취소</a>
    </form>
    
    <script src="{{ url_for('static', filename='validate_add.js') }}"></script>
</body>
</html>
```

### 3) 수정 화면 (`form_edit.html`)
```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>상품 수정</title>
</head>
<body>
    <h2>상품 수정</h2>
    
    {% if messages %}
        <ul>
            {% for m in messages %}
            <li style="color:red;">{{ m }}</li>
            {% endfor %}
        </ul>
    {% endif %}

    <form action="{{ url_for('edit_save', code=row.code) }}" method="post">
        <p>코드: <b>{{ row.code }}</b> (기본키는 수정 불가)</p>
        <p>품명: <input type="text" name="sang" value="{{ row.sang }}"></p>
        <p>수량: <input type="text" name="su" value="{{ row.su }}"></p>
        <p>단가: <input type="text" name="dan" value="{{ row.dan }}"></p>
        <button type="submit">수정</button>
        <a href="{{ url_for('show_list') }}">취소</a>
    </form>
</body>
</html>
```


## 4. 프론트엔드 유효성 검사 스크립트 (`static/validate_add.js`)
반드시 `static` 폴더를 생성하고 그 안에 자바스크립트 파일을 위치시켜야 한다. 정규표현식을 사용하여 숫자인지 클라이언트 단에서 먼저 검증한다.

```javascript
// 자료 추가 시 입력 자료를 간단하게 검증하는 스크립트
document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("addform");
    if(!form) return;

    form.addEventListener("submit", (e) => {
        const sang = document.getElementById("sang").value.trim();
        const su = document.getElementById("su").value.trim();
        const dan = document.getElementById("dan").value.trim();

        if(sang === ""){
            alert("상품명을 입력하시오.");
            e.preventDefault();
            return;
        }

        // 정규표현식: 처음부터 끝까지 숫자(\d)로만 이루어져 있는지 검사
        if(!/^\d+$/.test(su)){
            alert("수량은 숫자만 허용됩니다.");
            e.preventDefault();
            return;
        }

        if(!/^\d+$/.test(dan)){
            alert("단가는 숫자만 허용됩니다.");
            e.preventDefault();
            return;
        }
    });
});
```