import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pymysql

# 1
blue = [70, 68, 82, 78, 72, 68, 67, 68, 88, 60, 80]
red = [60, 65, 55, 58, 67, 59, 61, 68, 77, 66, 66]
# 귀 : 포장지 색상에 따른 제품의 매출액 차이가 존재하지 않는다.
# 대 : 포장지 색상에 따른 제품의 매출액 차이가 존재한다.
print(stats.shapiro(blue).pvalue) # 0.5102310078114559
print(stats.shapiro(red).pvalue) # 0.5347933246260025

print(stats.ttest_rel(blue,red)) # p 0.008676456
# 해석 : p < a 이므로 귀무 기각

# 2 
men_pop = np.array([0.9, 2.2, 1.6, 2.8, 4.2, 3.7, 2.6, 2.9, 3.3, 1.2, 3.2, 2.7, 3.8, 4.5, 4, 2.2, 0.8, 0.5, 0.3, 5.3, 5.7, 2.3, 9.8])
women_pop = np.array([1.4, 2.7, 2.1, 1.8, 3.3, 3.2, 1.6, 1.9, 2.3, 2.5, 2.3, 1.4, 2.6, 3.5, 2.1, 6.6, 7.7, 8.8, 6.6, 6.4])
men_sample = np.random.choice(men_pop, 15, replace=False)
women_sample = np.random.choice(women_pop, 15, replace=False)
# 귀무 : 남녀 간 콜레스테롤 양에 차이가 없다.
# 대립 : 남녀 간 콜레스테롤 양에 차이가 있다.
shapiro_men = stats.shapiro(men_sample)
shapiro_women = stats.shapiro(women_sample)
print("--- 2. 정규성 검정 결과 ---")
print(f"남자 p-value: {shapiro_men.pvalue:.4f}")
print(f"여자 p-value: {shapiro_women.pvalue:.4f}")
if shapiro_men.pvalue > 0.05 and shapiro_women.pvalue > 0.05:
    # 등분산성 확인
    levene = stats.levene(men_sample, women_sample)
    is_equal = levene.pvalue > 0.05
    t_stat, p_val = stats.ttest_ind(men_sample, women_sample, equal_var=is_equal)
    test_name = "독립표본 t-검정"
else:
    # Mann-Whitney U 검정 수행
    u_stat, p_val = stats.mannwhitneyu(men_sample, women_sample, alternative='two-sided')
    test_name = "Mann-Whitney U 검정"
print(f"분석 방법: {test_name}")
print(f"p-value: {p_val:.4f}")
alpha = 0.05
if p_val < alpha:
    print("\n결론: p-value가 0.05보다 작으므로 귀무가설을 기각")
    print("남녀 간 콜레스테롤 양에 통계적으로 유의미한 차이가 존재")
else:
    print("\n결론: p-value가 0.05보다 크므로 귀무가설을 채택")
    print("남녀 간 콜레스테롤 양에 통계적으로 유의미한 차이가 있다고 볼 수 없음.")

# 3 
config = {
    'host':'127.0.0.1', 'user':'root', 'password':'123',
    'database':'test', 'port':3306, 'charset':'utf8mb4'
}
try:
    conn = pymysql.connect(**config)
    sql = """
        SELECT b.busername, j.jikwonpay 
        FROM jikwon j 
        JOIN buser b ON j.busernum = b.buserno 
        WHERE b.busername IN ('총무부', '영업부')
    """
    df = pd.read_sql(sql, conn)
except Exception as e:
    pass
finally:
    conn.close()
# 결측치 처리 
df['jikwonpay'] = df['jikwonpay'].fillna(
    df.groupby('busername')['jikwonpay'].transform('mean')
)
# 데이터 분리
total_dept = df[df['busername'] == '총무부']['jikwonpay']
sales_dept = df[df['busername'] == '영업부']['jikwonpay']

# 귀무 : 연봉 평균에 차이가 없다.
# 대립 : 연봉 평균에 차이가 있다.

# 정규성 검정
print(stats.shapiro(total_dept)) # 0.02604493
print(stats.shapiro(sales_dept)) # 0.06420810
# p < 0.05 정규성 만족 안함
print(stats.mannwhitneyu(total_dept, sales_dept, alternative='two-sided'))
# p 0.4721 > 0.05 이므로 귀무 채택

# 4 
import numpy as np
mid = np.array([80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80])
fin = np.array([90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95])

# 귀무 : 중간고사와 기말고사 성적의 차이가 없다.
# 대립 : 중간고사와 기말고사 성적의 차이가 있다.

# 정규성 검정
print(stats.shapiro(fin - mid))
# p 0.3011 > 0.05 정규성 만족
print(stats.ttest_rel(mid, fin)) # 0.023486
# p < a 귀무 기각

