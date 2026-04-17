# 범주형 자료의 집단이 두 개일 경우 T검정 한다. 
# 범주형 자료의 집단이 세 개이상일 경우 ANOVA 분석(분산분석)
# 단일 표본  t검정 
# 정규분포의 표본에 대한 기대값을 조사하는 검정방법
# 예상평균값과 표본 자료간에 평균의 차이를 검정
# 독립변수 : 범주형, 종속변수 : 연속형
# 하나의 집단에 대한 표본 평균이 예측된 평균과 같은지 여부를 확인

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
# 실습 1 : 어느 남성 집단의 평균 키 검정 
# 귀무 : 해당 집단의 평균 키가 177이다. (모수)
# 대립 : 해당 집단의 평균 키가 177이 아니다. 
one_sample = [167.0,182.7,169.6,176.8,185.0]
print(np.array(one_sample).mean())
result = stats.ttest_1samp(one_sample,popmean=177) # popmean에는 검증하려는 평균값
print(result)
# 해석 p 값이 더 크므로 귀무가설 채택

print()
result2 = stats.ttest_1samp(one_sample,popmean=165)
print(result2)
# p 값이 작으므로 귀무가설 기각
sns.displot(one_sample, bins=10)
plt.show()
