from flask import Flask, render_template, request
import pymysql
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import base64
from datetime import datetime

# 한글 깨짐 방지
import koreanize_matplotlib

app = Flask(__name__)

db_config = {
    'host':'127.0.0.1', 'user':'root', 'password':'123',
    'database':'test', 'port':3306, 'charset':'utf8mb4'
}

def get_connection():
    return pymysql.connect(**db_config)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dbshow")
def dbshow():
    # 1) 데이터 읽기 및 DataFrame 작성 (Join 포함)
    sql = """
        SELECT j.jikwonno, j.jikwonname, b.busername, j.jikwonjik, j.jikwonpay, j.jikwonibsail, j.jikwongen, b.buserno
        FROM jikwon j
        INNER JOIN buser b ON j.busernum = b.buserno
    """
    
    with get_connection() as conn:
        df = pd.read_sql(sql, conn)

    # 근무년수 
    df['jikwonibsail'] = pd.to_datetime(df['jikwonibsail'])
    now = pd.to_datetime(datetime.now())
    df['근무년수'] = (now - df['jikwonibsail']).dt.days // 365
    
    # 부서번호, 직원명 순 오름차순 정렬
    df = df.sort_values(by=['buserno', 'jikwonname'], ascending=True)
    df = df.rename(columns={'jikwonno':'직원번호', 'jikwonname':'이름', 'busername':'부서명', 'jikwonjik':'직급', 'jikwonpay':'연봉','jikwongen':'성별'})
    # 출력용 데이터프레임
    jik_data_df = df[['직원번호', '이름', '부서명', '직급', '연봉', '근무년수']]

    # 부서명, 직급별 연봉합 및 연봉평균
    dept_jik_stats = df.groupby(['부서명', '직급'])['연봉'].agg(['sum', 'mean']).reset_index()

    # 부서명별 연봉합, 평균 세로막대 그래프 생성
    dept_stats = df.groupby('부서명')['연봉'].agg(['sum', 'mean'])
    
    plt.figure(figsize=(10, 5))
    
    # 연봉 합 그래프
    plt.subplot(1, 2, 1)
    dept_stats['sum'].plot(kind='bar', color='skyblue')
    plt.title('부서별 연봉 합')
    
    # 연봉 평균 그래프
    plt.subplot(1, 2, 2)
    dept_stats['mean'].plot(kind='bar', color='salmon')
    plt.title('부서별 연봉 평균')
    
    plt.tight_layout()
    
    # 그래프를 이미지 문자열로 변환
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    # 성별, 직급별 빈도표 
    ctab = pd.crosstab(df['성별'], df['직급'])
    
    # 부서별 최고 연봉
    top_indices = df.groupby('부서명')['연봉'].idxmax()
    top_earners = df.loc[top_indices, ['부서명', '이름', '연봉']]
    
    # 부서별 직원 비율
    total = len(df)
    dept_counts = df['부서명'].value_counts()
    dept_ratio = (dept_counts / total * 100).round(2)
    ratio_df = dept_ratio.reset_index()
    ratio_df.columns = ['부서명','비율(%)']


    return render_template("dbshow.html", 
                        jik_table=jik_data_df.to_html(classes='table table-bordered', index=False),
                        stats_table=dept_jik_stats.to_html(classes='table table-bordered'),
                        graph_url=graph_url,
                        ctab_table=ctab.to_html(classes='table table-bordered'),
                        top_earners = top_earners.to_html(classes='table table-bordered'),
                        ratio_df = ratio_df.to_html(classes='table table-bordered')
                        )

if __name__ == "__main__":
    app.run(debug=True)