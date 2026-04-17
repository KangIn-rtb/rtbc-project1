# 세개이상의모집단에대한가설검정–분산분석
# ‘분산분석’이라는 용어는 분산이 발생한 과정을 분석하여 요인에의한 분산과 요인을통해 나누어진 각집단내의 분산으로 나누고 요인
# 에의한 분산이 의미있는크기를 가지는지를 검정하는것을 의미한다.
# 세집단 이상의 평균비교에서는 독립인 두 집단의 평균비교를 반복하여 실시할경우에 제1종오류가 증가하게되어 문제가발생한다.
# 이를 해결하기위해 Fisher가 개발한분산분석(ANOVA, ANalysis Of Variance)을 이용하게 된다.
# 분산이 발생한 과정을 분석하여 요인에 의한 분산과 요인을 통해 나눠진 각 집단 내의 분산으로 나누고, 요인에 의한 분산이 의미 있는 크기를 가지는지 검정한다.
# F = 집단간분산 / 집단내분산 

# 일원분산분석(one way anova)
# 실습) 세 가지 교육방법을 적용하여 1개월동안 교육받은 교육생80명을 대상으로 실기시험을 실시. three_sample.csv
# 독립변수 : 한개의 요인 : 교육방법, 방법의 종류가 3가지(그룹이 3개)
# 종속변수 : 실기시험 평균점수

import pandas as pd
import scipy.stats as stats
from statsmodels.formula.api import ols
pd.set_option('display.max_columns',None)

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/three_sample.csv")
print(data.head(3))
print(data.describe())

# import matplotlib.pyplot as plt
# plt.boxplot(data.score)
# plt.show()

data = data.query("score <= 100")
print(len(data))
print(data.describe())

# 교차표(교육방법 별 건수)
data2 = pd.crosstab(index=data['method'],columns='count')
data2.index = ['방법2','방법2','방법3']
print(data2)

# 교차표 
data3 = pd.crosstab(data['method'], data['survey'])
data3.index = ['방법2','방법2','방법3']
data3.columns = ['만족','불만족']
print(data3)

print("ANOVA 검정 - - - - - - ")
# F통계값을 얻기위해 회귀분석결과(리니어모델 필요)를 사용
import statsmodels.api as sm
linmodel = ols("data['score'] ~ data['method']", data=data).fit() # 회귀분석 모델 생성
result = sm.stats.anova_lm(linmodel,typ=1)
print(result)
#                   df        sum_sq     mean_sq         F    PR(>F)(p값)
# data['method']   1.0     27.980888   27.980888  0.122228  0.727597
# Residual        76.0  17398.134497  228.922822       NaN       NaN
# p 0.727597 > a 이므로 귀무 채택

# 사후 분석
# 정확히 어느 그룹의 평균값이 의미가 있는지 알려주지 않음
# 그러므로 그룹간의 관계를 보기 위해 추가적인 사후 분석이 필요
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukResult = pairwise_tukeyhsd(endog=data['score'],groups=data['method'])
print(tukResult)

# Tukey HSD 결과
import matplotlib.pyplot as plt
tukResult.plot_simultaneous(xlabel='mean',ylabel='group')
plt.show()
# Tukey HSD : 원래 반복 수가 동일하다는 가정하에 고안된 방법
# 집단 간 평균 차이를 정밀하게 확인 가능
# 각 집단의 표본 수의 차이가 크면 결과의 신뢰가 떨어짐
