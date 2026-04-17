# 일원 분산 분석으로 평균차이 검정 
# 강남구에 있는 편의점 GS 편의점 3개 지역 알바생의 급여에 대한 평균 차이 검정

# 귀무 : GS 편의점 3개 지역 알바생의 급여에 대한 평균은 차이가 없다.
# 대립 : GS 편의점 3개 지역 알바생의 급여에 대한 평균은 차이가 있다.

import pandas as pd
import numpy as np
import scipy.stats as stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt
import koreanize_matplotlib
import urllib.request

uri = "https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/group3.txt"

data = np.genfromtxt(urllib.request.urlopen(uri), delimiter=",")
print(data.shape)

# 세개의 집단에 월급 자료 얻기, 평균
gr1 = data[data[:,1] == 1,0]
gr2 = data[data[:,1] == 2,0]
gr3 = data[data[:,1] == 3,0]
print(gr1,' ',np.mean(gr1))
print(gr2,' ',np.mean(gr2))
print(gr3,' ',np.mean(gr3))
print()

#정규성 확인
print(stats.shapiro(gr1).pvalue)
print(stats.shapiro(gr2).pvalue)
print(stats.shapiro(gr3).pvalue)
# 0.3336828974377483
# 0.6561053962402779
# 0.8324811457153043
# 전부 만족

# 등분산성
print(stats.levene(gr1, gr2, gr3).pvalue)
print(stats.bartlett(gr1, gr2, gr3).pvalue)
# 0.045846812634186246 -> 0.05에 약간 안미치지만 반올림 하면 얼추 맞긴하니 넘어갈 수 있다. 
# 0.3508032640105389
# 바틀렛 - 표본의 개수가 차이날 때 

# 데이터 퍼짐 시각화
plt.boxplot([gr1,gr2,gr3],showmeans=True)
# plt.show()

# 일원분산분석
# 방법 1: anova_lm()
df = pd.DataFrame(data=data,columns=['pay','group'])
print(df)
l_m = ols('pay ~ C(group)', data=df).fit() # C 는 group은 범주형 이라는 뜻
print(anova_lm(l_m, type=1)) # p 0.043589
# p 0.043589 < a 이므로 귀무 기각 

# 방법 2: f_oneway()
f_stats, p_val = stats.f_oneway(gr1,gr2,gr3)
print(f_stats, p_val)

# 사후 검정 
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukResult = pairwise_tukeyhsd(endog=df.pay, groups=df.group)
print(tukResult)

# 시각화 
tukResult.plot_simultaneous(xlabel="mean",ylabel='group')
plt.show()

# 참고
# anova_lm() : 정규성, 등분산성이 깨지면 p-value 신뢰 불가
# f_oneway() : 정규성 깨지면 stats.kruskal(), 등분산성이 깨지면 welch ANOVA 사용
