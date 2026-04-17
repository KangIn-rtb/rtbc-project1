#1 
"""
빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 양을 측정하였다.
기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하는지를 분산분석을 통해 알아보자.

귀 : 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 없다.
대 : 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 있다.
"""

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt 
import koreanize_matplotlib
from pingouin import welch_anova
from statsmodels.stats.multicomp import pairwise_tukeyhsd

data = {
    'kind': [1, 2, 3, 4, 2, 1, 3, 4, 2, 1, 2, 3, 4, 1, 2, 1, 1, 3, 4, 2],
    'quantity': [64, 72, 68, 77, 56, None, 95, 78, 55, 91, 63, 49, 70, 80, 90, 33, 44, 55, 66, 77]
}
df = pd.DataFrame(data)
df['quantity'] = df['quantity'].fillna(df['quantity'].mean()) # 평균으로 채우기
g1 = df[df['kind'] == 1]['quantity']
g2 = df[df['kind'] == 2]['quantity']
g3 = df[df['kind'] == 3]['quantity']
g4 = df[df['kind'] == 4]['quantity']
print(stats.shapiro(g1).pvalue)
print(stats.shapiro(g2).pvalue)
print(stats.shapiro(g3).pvalue)
print(stats.shapiro(g4).pvalue)
# 0.8680405840743664
# 0.5923924912154501
# 0.48601083943678747
# 0.4162161718602888
# 모든 p > a -> 정규성 만족
print()
print(stats.levene(g1, g2, g3, g4).pvalue) 
print(stats.bartlett(g1, g2, g3, g4).pvalue)
# 0.3268969935062273
# 0.19342011099507922
# p > a -> 등분산성 만족 
print()
print(stats.f_oneway(g1, g2, g3, g4).pvalue)
# p 0.8482436666841788 > a 이므로 귀무 채택

# 사후 검정 
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukResult = pairwise_tukeyhsd(endog=df.quantity, groups=df.kind)
print(tukResult)
# 시각화 
tukResult.plot_simultaneous(xlabel="mean",ylabel='group')
plt.show()


