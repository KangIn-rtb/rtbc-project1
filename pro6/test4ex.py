# 1)
import pandas as pd
import scipy.stats as stats
data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/cleanDescriptive.csv")
data_clean = data.dropna(subset=['level', 'pass'])

table = pd.crosstab(data_clean['level'], data_clean['pass'])
print("--- 교차표 ---")
print(table)

chi2, p, dof, expected = stats.chi2_contingency(table)

print(f'\n카이제곱 통계량: {chi2}')
print(f'p-value: {p}')

if p < 0.05:
    print("결론: p < 0.05 이므로 부모 학력과 자녀 진학은 관련이 있음")
else:
    print("결론: p >= 0.05 이므로 부모 학력과 자녀 진학은 관련이 없음")
    
    
# 2)
import pymysql
import pandas as pd
from scipy import stats

config = {
    'host':'127.0.0.1', 'user':'root', 'password':'123',
    'database':'test', 'port':3306, 'charset':'utf8mb4'
}
try:
    conn = pymysql.connect(**config)
    sql = "SELECT jikwonjik, jikwonpay FROM jikwon"
    df_jikwon = pd.read_sql(sql, conn)
    df_jikwon = df_jikwon.dropna()
    bins = [1000, 3000, 5000, 7000, 100000]
    labels = [1, 2, 3, 4]
    df_jikwon['pay_group'] = pd.cut(df_jikwon['jikwonpay'], bins=bins, labels=labels, right=False)
    table = pd.crosstab(df_jikwon['jikwonjik'], df_jikwon['pay_group'])
    chi2, p, dof, expected = stats.chi2_contingency(table)
    print("--- 직급/연봉 그룹 교차표 ---")
    print(table)
    print(f'\n카이제곱 통계량: {chi2}')
    print(f'p-value: {p}')
    if p < 0.05:
        print("결론: 직급과 연봉은 관련이 있다")
    else:
        print("결론: 직급과 연봉은 관련이 없다")

except Exception as e:
    print(f"오류 발생: {e}")
finally:
    conn.close()
