# 독립 표본 t 검정 
# 서로 다른 두 집단의 평균에 대한 통계 검정에 사용
# 비교를 위해 평균과 표준편차 통계량 사용
# 두 집단의 평균과 표준편차 비율에 대한 재조 검정법이다. 

# 두 집단의 가설검정 실습시 분산을 알지 못하는 것으로 한정
# 남녀의 시험 평균이 우연히 같을 확률은 얼마나 될까
# 만약 우연히 발생했다면 평균은 같은 것이고, 우연이 아니면 평균은 다른것이다
# 95% 신뢰 구간에서 우연히 발생할 확률이 5% 이상이면 귀무가설 채택

from scipy import stats
import pandas as pd
import numpy as np

male = [75,85,100,72.5]
female = [63.2,52,100,70,76]
print(np.mean(male), ' ', np.mean(female))

# 두 개의 표본에 대한 독립 표본 t-검정 수행
two_sample = stats.ttest_ind(male, female, equal_var=True)
print(two_sample)
tv, pv = two_sample
print(tv)
print(pv)

# 선행 조건
# 1) 두 집단이 각각 정규 분포를 따라야 한다.
# 2) 두 집단의 분산이 같다는 가정이 필요. 등분산성
print(stats.shapiro(male))
print(stats.shapiro(female))
# 만약 집단의 표본 수가 30개 이상인 경우는 정규 분포를 따른다고 가정함으로 정규성 검정 안해도 됨.
# 만약 정규성을 만족하지 못하면 Mann-whitney test를 한다.
# stats.mannwhitneyu(group1,group2)

print()
# 선행 조건 2) 두 집단의 분산이 같다는 가정이 필요
from scipy.stats import levene, bartlett
#            정규성만족                      이상치         분표
# levene         X(정규성과 상관없이 사용)     민감      어떤 분표도 가능
# bartlett       O(정규성 있을 때만 사용)     덜민감     정규분포만 가능
