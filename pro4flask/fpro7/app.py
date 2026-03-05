from flask import Flask, render_template, request, make_response, redirect, url_for
app = Flask(__name__)
COOKIE_AGE = 60*60*24*7

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/login")
def login():
    name = request.cookies.get("name")
    visits = request.cookies.get("visits")
    
    if name:
        visits = int(visits or "0") + 1
        msg = f"안녕하세요. {name}님 {visits}번째 방문 입니다"
    else:
        visits = None
        msg = "이름을 입력하면 방문 횟수를 쿠키로 기억합니다"
    resp = make_response(render_template("login.html", msg=msg,visits=visits,name=name))
    
    if name: # 로그인 상태면 visits 쿠키 갱신
        resp.set_cookie("visits",str(visits), max_age=COOKIE_AGE,samesite="Lax")
        
    return resp

@app.post("/login")
def login2():
    name = (request.form.get("name") or "").strip()
    resp = make_response(redirect(url_for("login")))
    resp.set_cookie("name", name, max_age=COOKIE_AGE,samesite="Lax")
    resp.set_cookie("visits", "0", max_age=COOKIE_AGE,samesite="Lax")
    return resp

@app.post("/logout")
def logout():
    resp = make_response(redirect(url_for("login")))
    resp.delete_cookie("name")
    resp.delete_cookie("visits")
    return resp
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
    