from flask import Flask,render_template,request
import pymysql
import pandas as pd
import numpy as np
from markupsafe import escape

app = Flask(__name__)
db_config = {
    'host':'127.0.0.1','user':'root','password':'123',
    'database':'test','port':3306,'charset':'utf8mb4'
}
def get_connection():
    return pymysql.connect(**db_config)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dbshow")
def dbshow():
    dept = request.args.get("dept","").strip()
    sql = """
        select j.jikwonno as 직원번호, j.jikwonname as 직원명, b.busername as 부서명, b.busertel as 부서전화,
        j.jikwonpay as 연봉, j.jikwonjik as 직급
        from jikwon j
        inner join buser b on j.busernum=b.buserno
    """
    params = []
    if dept:
        sql += " where b.busername like %s"
        params.append(f"%{dept}%")    
    sql += " order by j.jikwonno asc"
    
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql,params)
            rows = cur.fetchall()
            cols = [c[0] for c in cur.description]
    
    df = pd.DataFrame(rows, columns=cols)
    # print(df.head(3))
    # 직원정보 html로 전송
    if not df.empty:
        jik_data = df[['직원번호','직원명','부서명','부서전화','연봉']]
    else:
        jik_data = "직원 정보가 없어요"
    if not df.empty:
        status_df = (
            df.groupby("직급")['연봉']
            .agg(
                평균 = "mean",
                표준편차 = lambda x:x.std(ddof=0),
                인원수 = "count"
            )
            .round(2)
            .reset_index()
            .sort_values(by='평균',ascending=False)
        )
        status_df['표준편차'] = status_df['표준편차'].fillna(0)

    return render_template("dbshow.html",jik_data=jik_data,status_df=status_df)


if __name__=='__main__':
    app.run(debug=True) 