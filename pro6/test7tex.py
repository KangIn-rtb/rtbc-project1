import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import wilcoxon
import koreanize_matplotlib

# 1) 50시간 늘린 백열전구의 수명이 맞는지 
# 귀무 : 백열전구의 수명은 300이다.
# 대립 : 백열전구의 수명은 300이 아니다.
print("1)")
data = pd.Series([305, 280, 296, 313, 287, 240, 259, 266, 318, 280, 325, 295, 315, 278])
print(data.mean()) # 289.785714
print(stats.shapiro(data))
# a 0.05 < p 0.82086 이므로 정규성 만족 -> ttest 진행
result = stats.ttest_1samp(data,popmean=300) 
print(result) # p 0.1436062
# a 0.05 < p 0.1436062 이므로 귀무 채택 통계적으로 백열전구의 수명은 300시간이다. -> 이 데이터는 우연히 발견된 데이터다.

# 2) 노트북 평균 시간 5.2 시간 
# 귀무 : 노트북 평균 사용 시간은 5.2시간이다.
# 대립 : 노트북 평균 사용 시간은 5.2시간이 아니다.
print("2)")
data2 = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/one_sample.csv")
data2['time'] = pd.to_numeric(data2['time'], errors='coerce')
data2 = data2.dropna(subset=['time'])
print(data2['time'].mean()) # 5.556880733944953
print(len(data2)) # 109
result2 = stats.ttest_1samp(data2['time'],popmean=5.2)
print(result2) # p 0.0001416669
# a 0.05 > p 0.000141666 이므로 노트북 평균 사용시간은 5.2시간이 아니다.

plt.figure(figsize=(6, 4))
sns.boxplot(y=data2['time'])
plt.axhline(y=5.2, color='r', linestyle='--', label='기준값(5.2)')
plt.title("노트북 사용 시간 분포")
plt.legend()
plt.show()

# [one-sample t 검정 : 문제3] 
# https://www.price.go.kr/tprice/portal/main/main.do 에서 
# 메뉴 중  가격동향 -> 개인서비스요금 -> 조회유형:지역별, 품목:미용 자료(엑셀)를 파일로 받아 미용 요금을 얻도록 하자. 
# 정부에서는 전국 평균 미용 요금이 15000원이라고 발표하였다. 이 발표가 맞는지 검정하시오. (월별)
# 문제 : 정부의 전국 평균 미용 요금 15,000원이 실제 데이터와 차이가 있는지 검정
# 귀무 : 전국 평균 미용 요금은 15,000원이다. (발표가 맞다.)
# 대립 : 전국 평균 미용 요금은 15,000원이 아니다. (발표가 틀리다.)

print("3)")
# pip install xlrd
data3 = pd.read_excel('2026.02_data.xls')
data4 = data3.iloc[0, 2:]    # 지역 데이터만 추출
data4 = pd.to_numeric(data4, errors='coerce')
data4 = data4.dropna()
print('표본 평균 미용 요금 :', data4.mean())
print('표본 크기 :', len(data4))
# 정규성 검정
result3 = stats.shapiro(data4)
print(result3)
# one-sample t-test
t_result3 = stats.ttest_1samp(data4, popmean=15000)
print(t_result3)
# a 0.05 < p 3.20576619 이므로 
