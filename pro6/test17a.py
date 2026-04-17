# 이원분산분석 : 요인 복수 - 각 요인의 레벨도 복수
# 두 개의 요인에 대한 집단 각각이 종속변수에 영향을 주는지 검정
# 주효과 : 독립변수들이 각각 독립적으로 종속변수에 미치는 영향을 검정하는 것
# 상호작용효과(교호작용): 독립변수들이 서로 연관되어 종족변수에 미치는 영향을 검정하는 것
# 한 독립변수가 종속변수에 미치는 영향이 다른 독립변수의 수준에 따라 달라지는 현상
# 이원분산분석의 선형 회귀모델에서 교호작용을 신경쓰는게 보통이다.

# 실습1 : 태아 수와 관측자 수가 태아의 머리둘레 평균에 영향을 주는가?
# 주효과 가설
# 귀 : 태아 수와 태아의 머리둘레 평균은 차이가 없다.
# 대 : 태아 수와 태아의 머리둘레 평균은 차이가 있다.
# 교호작용 가설
# 귀 : 교호작용이 없다 (태아수와 관측자 수는 관련이 없다)
# 대 : 교호작용이 있다 (태아수와 관측자 수는 관련이 있다)

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt 
import koreanize_matplotlib
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/group3_2.txt")
# data.boxplot(column='머리둘레',by='태아수')
# plt.show()
# data.boxplot(column='머리둘레',by='관측자수')
# plt.show()
# linreg = ols("머리둘레 ~ C(태아수) + C(관측자수)", data=data).fit() # 교호작용 X
# linreg = ols("머리둘레 ~ C(태아수) + C(관측자수) + C(태아수):C(관측자수)", data=data).fit() # 교호작용 O
linreg = ols("머리둘레 ~ C(태아수) * C(관측자수)", data=data).fit() # 교호작용 O
result = anova_lm(linreg,typ=2)
print(result)
# 태아수 PR 1.051039e-27 : 귀무 기각
# 관측자수 PR 6.497055e-03 : 귀무 기각
# C(태아수):C(관측자수) PR 3.295509e-01 : 귀무 채택
# 해석 : 태아수와 관측자 수는 각각 종속변수에 유의한 영향을 미친다. 
# 그러나 태아수와 관측자 수 간의 상호작용 효과는 유의하지 않다.