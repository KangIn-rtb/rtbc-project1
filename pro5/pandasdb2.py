# 원격 DB 연동 
import pymysql
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import csv

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8'
}

try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    sql = """
        select jikwonno, jikwonname,busername,jikwonjik,jikwongen,jikwonpay
        from jikwon inner join buser on jikwon.busernum=buser.buserno
    """
    cursor.execute(sql)
    # for (jikwonno,jikwonname,busername,jikwonjik,jikwongen,jikwonpay) in cursor:
    #     print(jikwonno,jikwonname,busername,jikwonjik,jikwongen,jikwonpay)
    df1 = pd.DataFrame(cursor.fetchall(),columns=['jikwonno','jikwonname','busername','jikwonjik','jikwongen','jikwonpay'])
    print(df1.head(3))
    print('연봉 총합 : ',df1['jikwonpay'].sum())
    
    print()
    cursor.execute(sql)
    with open('pandasdb2.csv', mode='w',encoding='utf-8') as fobj:
        writer = csv.writer(fobj)
        for row in cursor.fetchall():
            writer.writerow(row)
    df2 = pd.read_csv('pandasdb2.csv',header=None,names=['번호','이름','부서','직급','성별','연봉'])
    print(df2.head(3))
    
    print("\n\n pandas의 sql 처리 함수 이용")
    df = pd.read_sql(sql,conn)
    df.columns = ['번호','이름','부서','직급','성별','연봉']
    print(df.head(3))
    ctab = pd.crosstab(df['성별'],df['직급'],margins=True)
    print(ctab)
    # 시각화
    jik_ypay = df.groupby(['직급']) # 직급별 연봉 평균
    
except Exception as e:
    print(e)
finally:
    cursor.close()
    conn.close()