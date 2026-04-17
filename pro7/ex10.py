# 선형회귀분석 모형의 적절성 선행조건

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib
import statsmodels.formula.api as smf



data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/Advertising.csv", usecols=[1,2,3,4])
print(data.head())

print()
# 단순선형회귀모델
lm = smf.ols(formula='sales ~ tv',data=data).fit()   
print(f"par:{lm.params}, pval:{lm.pvalues}, rq:{lm.rsquared}")
print(lm.summary())

# 예측
x_new = pd.DataFrame({'tv':data.tv[:3]})
print(x_new)
print(data.sales[:3].values)
print(lm.predict(x_new).values)
print(lm.params.Intercept + lm.params.tv)

# 경험하지 않은 tv 광고비에 따른 상품 판매량 예측
my_new = pd.DataFrame({'tv':[100, 350, 780]})
print('예측 상품 판매량 : ',lm.predict(my_new).values)
plt.scatter(data.tv, data.sales)
plt.xlabel('tv광고비')
plt.ylabel('상품판매량')
ypred = lm.predict(data.tv)
plt.plot(data.tv, ypred, c='red')
plt.title('단순선형회귀')
# plt.show()

# 잔차 : 실제 관측값과 모델이 예측한 값의 차이를 의미한다.
# 모델이 데이터를 얼마나 잘 설명하는지 보여주는 척도
fitted = lm.predict(data)
residual = data['sales'] - fitted
print(data['sales'][:5].values)
print(fitted[:5].values)
print(residual[:5].values)
print(np.mean(residual[:5]))
from scipy.stats import shapiro
import statsmodels.api as sm
stat, p = shapiro(residual)
print(stat, p)
# p 0.2133 정규성 만족
sm.qqplot(residual,line='s')
# plt.show()

# 독립변수와 종속변수 간에 선형형태로 적절하게 모델링 되었는지 확인
from statsmodels.stats.diagnostic import linear_reset
reset_result = linear_reset(lm, power=2, use_f=True)
print(reset_result.pvalue)
print("만족"if reset_result.pvalue > 0.05 else "위베")

# 등분산성 검정
from statsmodels.stats.diagnostic import het_breuschpagan
bp_test = het_breuschpagan(residual, sm.add_constant(data['tv']))
bp_stat, bp_pvalue = bp_test[0], bp_test[1]
print("통계량:",bp_stat, "p:",bp_pvalue)
print("등분산성 만족"if bp_pvalue > 0.05 else "등분산성 위배")
print()
# 영향력 있는 관측치를 탐지하는 진단 방법
# 데이터가 적을 때, 이상치가 의심스러울 때, 모델 결과가 이상하게 나올 때
from statsmodels.stats.outliers_influence import OLSInfluence
cd, _ = OLSInfluence(lm).cooks_distance # 쿡 거리, 인덱스
print(cd.sort_values(ascending=False).head())
# 쿡거리가 가장 큰 (영향력이 큰) 관측치 원본 확인 
print(data.iloc[[35,178,25,175,131]])
"""
        tv  radio  newspaper  sales
35   290.7    4.1        8.5   12.8
178  276.7    2.3       23.7   11.8
25   262.9    3.5       19.5   12.0
175  276.9   48.9       41.8   27.0
131  265.2    2.9       43.0   12.7
""" 
# tv 광고비 대부분은 매우 높으나 sales가 낮다. - 모델이 예측하기 어려운 포인트들
# 시각화
fig = sm.graphics.influence_plot(lm, alpha=0.05, criterion="cooks")
# plt.show()

print()
# 다중선형회귀모델
lm_mul = smf.ols(formula='sales ~ tv + radio + newspaper',data=data).fit()   
print(lm_mul.summary())
# newspaper의 p값은 0.05보다 크니 빼고 하는것이 좋다.
# R-squared 는 정확도가 아니라 설명도 0.896 이면 89.6%로 설명한다.