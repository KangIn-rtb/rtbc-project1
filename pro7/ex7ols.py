# 단순선형회귀 : ols 의 regresstion results의 이해
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/drinking_water.csv")
print(df.head(3))
model = smf.ols(formula='만족도 ~ 적절성',data=df).fit()
print(model.summary())
print("params",model.params)
print("rsquared",model.rsquared)
print("pvalues",model.pvalues)
print("predict",model.predict())

plt.scatter(df.적절성, df.만족도)
slope, intercept = np.polyfit(df.적절성,df.만족도,1)
plt.plot(df.적절성,slope * df.적절성 + intercept, c='b')
plt.show()
"""
OLS Regression Results 에 대한 기본 이해 --------------------------------------------------
R-squared(설명력) : 독립변수(x)가 종속변수(y)를 얼마나 설명하는가 판단하는 수치. 설명력은 y값의 몇 %를 x값으로 예측할 수 있는지가 중요한데 이걸 알려주는 척도가 R-squared이다. 값을 얼마나 설명하고 있는지를 알려주기 때문에 설명력이라고 부른다. 1에 가까울수록 좋으나 1에 너무 근사하면 기형모델이 될 수 있다. 과적합 모델.
Adj. R-squared(수정된 결정계수) : 독립변수가 많아지면서 자연스럽게 값이 커지는 현상을 조절한 계수. 즉, Adj. R-squared는 독립변수가 추가될 때 무조건 증가하는 R²의 문제를 보정한 지표이다. Adj. R-squared(수정된 결정계수)는독립변수가 추가될 때 무조건 증가하는 R²의 문제를 보정한 값이다.
Omnibus : “회귀모형 유의성”이 아니라 잔차(residual)의 정규성 검정이다. 잔차가 정규분포를 따르는지 검정. 
Prob(Omnibus) 
해석 방법 : p-value > 0.05 → 정규성 만족, p-value ≤ 0.05 → 정규성 깨짐
예) Omnibus: 7.616, Prob(Omnibus): 0.022     -->  0.022 < 0.05  정규성 위반
잔차가 정규분포인지 판단하는 보조 지표 두 개
1) Skew(왜도) : 데이터(잔차)의 비대칭 정도. 기준. +값 → 큰 값 쪽으로 치우침, -값 → 작은 값 쪽으로 치우침
예) Skew = 0 → 대칭 (정규분포), Skew > 0 → 오른쪽 꼬리 김 (양의 왜도), Skew < 0 → 왼쪽 꼬리 김 (음의 왜도)
2) Kurtosis(첨도) : 분포의 뾰족함 (꼬리 두꺼움) . 크면 → 극단값(outlier) 많음. 작으면 → 퍼진 분포.
예) Kurtosis = 3 → 정규분포, Kurtosis > 3 → 뾰족 + 꼬리 두꺼움, Kurtosis < 3 → 평평함
Durbin-Watson : 잔차의 자기상관(autocorrelation) 검정 지표. 잔차들이 서로 독립적인가? 시간 흐름 데이터에서 중요 (시계열)
값의 범위는 0 ~ 4 이고   2이면 정상 (자기상관 없음).   < 2이면 양의 자기상관,  > 2이면 음의 자기상관
Jarque-Bera : 잔차(residual)가 정규분포를 따르는지 검정. 해석 기준 Prob(JB) > 0.05 → 정규성 만족이고 Prob(JB) ≤ 0.05 → 정규성 위반이다.
왜도 + 첨도를 이용한 정규성 테스트이다.
Cond. No. : 독립변수 간 다중공선성(multicollinearity) 정도를 나타내는 지표. 설명변수들(X)이 서로 얼마나 비슷한가? 서로 강하게 연관되어 있으면 회귀계수 불안정 발생~  기준은 < 10이면문제 없음, 10 ~ 30은 약간 의심,  > 30이먄 다중공선성 문제 가능~
""" 
