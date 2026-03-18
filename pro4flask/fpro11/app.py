from flask import Flask, render_template, request, make_response, redirect, url_for, session, flash
import pymysql
import os
from flask import get_flashed_messages 
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = "abcdef12345" 

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT"))
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

load_dotenv() # .env 파일에 저장된 환경변수 읽기 함수

def get_conn():
    return pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        passwd=DB_PASSWORD,
        database=DB_NAME,
        charset="utf8mb4", 
        cursorclass=pymysql.cursors.DictCursor, 
        autocommit=False
    )
@app.route("/")
def root():
    return redirect(url_for("login_form"))

@app.route("/login")
def login_form():
    return render_template("login.html")

@app.post("/login")
def login_post():
    jikwonno_raw = (request.form.get("jikwonno") or "").strip()
    jikwonname = (request.form.get("jikwonname") or "").strip()
    
    if not jikwonno_raw.isdigit() or not jikwonname:
        flash("직원 번호는 숫자, 직원이름은 필수 입니다.")
        return redirect(url_for("login_form"))
    jikwonno = int(jikwonno_raw)
    
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            #로그인 체크
            cur.execute("""
                select jikwonno, jikwonname from jikwon
                where jikwonno=%s and jikwonname=%s        
            """,(jikwonno, jikwonname))
            me = cur.fetchone()
            if not me:
                flash("로그인 실패 직원 정보가 일치하지 않습니다.")
                return  redirect(url_for("login_form"))
            cur.execute("""
                        select jikwonno,jikwonname,busername,jikwonjik,jikwonpay,
                        year(jikwonibsail) as jikwonibsail_year
                        from jikwon inner join buser
                        on busernum=buserno order by jikwonno
                        """)
            rows = cur.fetchall()
            
        session["jikwonno"] = me["jikwonno"]
        session["jikwonname"] = me["jikwonname"]
        
        return render_template("jikwonlist.html",rows=rows, login_user=me)
            
    finally:
        conn.close()
        
        
@app.route("/gogek/<int:jikwonno>")
def gogek_list(jikwonno:int):
    if "jikwonno" not in session:
        flash("로그인 해주세요")
        return redirect(url_for("login_form"))
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                        select gogekno,gogekname,gogektel from gogek
                        where gogekdamsano=%s order by gogekno
                        """,(jikwonno,))
            customers = cur.fetchall()
            cur.execute("""
                        select jikwonname from jikwon 
                        where jikwonno = %s
                        """,(jikwonno,))
            emp = cur.fetchone()
        
        return render_template("gogeklist.html",customers=customers, empno=jikwonno,empname=(emp["jikwonname"] if emp else ""))
    
    finally:
        conn.close()

@app.route("/jikwons")
def jikwon_list():
    if "jikwonno" not in session:
        flash("로그인 해주세요")
        return redirect(url_for("login_form"))
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                            select jikwonno,jikwonname,busername,jikwonjik,jikwonpay,
                            year(jikwonibsail) as jikwonibsail_year
                            from jikwon inner join buser
                            on busernum=buserno order by jikwonno
                            """)
            rows = cur.fetchall()
        login_user = {"jikwonno":session["jikwonno"],"jikwonname":session["jikwonname"]}
        return render_template("jikwonlist.html",rows=rows, login_user=login_user)
    finally:
        conn.close()

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login_form"))
        

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)