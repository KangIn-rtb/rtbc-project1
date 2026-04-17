# 최고온도에 따른 매출액의 평균에 차이가 있는지 검정
# 세 집단 : 추움, 보통, 더움

# 귀무 : 어느 음식점의 매출 데이터는 온도에 따라 매출액 평균에 차이가 없다.
# 대립 : 어느 음식점의 매출 데이터는 온도에 따라 매출액 평균에 차이가 있다.

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt 
import koreanize_matplotlib

pd.set_option("display.max_columns",None)
# 매출 데이터 읽기 
sales_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/tsales.csv", dtype = {'YMD':'object'}) # int -> object 변환해 읽기
print(sales_data.head(3))
print(sales_data.info())

# 날씨 데이터 읽기 
wt_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/tweather.csv")
print(wt_data.head(3))
print(wt_data.info())

print()
# sales : YMD 20190514, wt : 2018-06-01 병합을 위해 데이터 변환 필요
wt_data.tm = wt_data.tm.map(lambda x:x.replace("-",""))
frame = sales_data.merge(wt_data, how="left", left_on="YMD", right_on='tm')
print(frame.head()," ",len(frame))
data = frame.iloc[:,[0,1,7,8]]
print(data.head())
print(data.isnull().sum())

print(data.maxTa.describe())
# plt.boxplot(data.maxTa)
# plt.show()

# 온도를 세 그룹으로 분리 (int -> 범주형)
print(data.isnull().sum()) # null 확인
data['ta_gubun'] = pd.cut(data.maxTa, bins=[-5,8,24,37], labels=[0,1,2])
print(data.head(3),' ',data['ta_gubun'].unique())

# 정규성, 등분산성
x1 = np.array(data[data.ta_gubun == 0].AMT)
x2 = np.array(data[data.ta_gubun == 1].AMT)
x3 = np.array(data[data.ta_gubun == 2].AMT)
print(x1[:5])

print()
print(stats.levene(x1, x2, x3).pvalue) # 0.039002
print(stats.bartlett(x1, x2, x3).pvalue) # 0.00967
# 등분산성 만족 X
print()
print(stats.shapiro(x1).pvalue)
print(stats.shapiro(x2).pvalue)
print(stats.shapiro(x3).pvalue)
# 0.2481924204382751
# 0.03882572120522948
# 0.3182989573650957
# 정규성 만족 
print()
# 온도별 매출액 평균
np.set_printoptions(suppress=True, precision=10)
spp = data.loc[:, ["AMT",'ta_gubun']]
print(spp.groupby('ta_gubun').mean())
print(np.mean(x1))
print(np.mean(x2))
print(np.mean(x3))
# 1032362.3188405797
# 818106.8702290077
# 553710.9375
group1 = x1
group2 = x2
group3 = x3
print(stats.f_oneway(group1,group2,group3))
# 해석 : p 2.360737101 > a 이므로 귀무 기각
print()
print(stats.kruskal(group1,group2,group3))
# p 1.527814
print()
#pip install pingouin
from pingouin import welch_anova
print(welch_anova(dv="AMT",between='ta_gubun',data=data)) # 0.379 귀무 기각

# 사후 검정 
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukResult = pairwise_tukeyhsd(endog=spp['AMT'], groups=spp['ta_gubun'])
print(tukResult)

# 시각화 
tukResult.plot_simultaneous(xlabel="mean",ylabel='group')
plt.show()

# 참고
# anova_lm() : 정규성, 등분산성이 깨지면 p-value 신뢰 불가
# f_oneway() : 정규성 깨지면 stats.kruskal(), 등분산성이 깨지면 welch ANOVA 사용
