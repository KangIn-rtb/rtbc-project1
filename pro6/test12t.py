# Paired Sample t-test 대응표본 t검정, 동일집단 표본 t검정
# 하나의 집단에 대해 독립변수를 적용하기 전과 후의 종속변수(평균)의 수준을 측정하고
# 이들의 차이가 통계적으로 유의한지를 분석
# 동일한 관찰 대상으로 처리 이전과 이후를 1:1 대응시킨 검정 방법
# 집단 간 비교가 아니므로 등분산 가정을 할 필요는 없다. 


# 귀무 : 특강 전후의 시험 점수는 차이가 없다.
# 대립 : 특강 전후의 시험 점수는 차이가 있다. 
import numpy as np
import scipy.stats as stats
x1 = np.random.normal(75,10,100)
x2 = np.random.normal(80,10,100)

# 정규성 확인
import seaborn as sns
import matplotlib.pyplot as plt
sns.displot(x1,kde=True)
sns.displot(x2,kde=True)
plt.show()

print(stats.shapiro(x1).pvalue) # ex) 0.5206820
print(stats.shapiro(x2).pvalue) # ex) 0.7554790

# 대응표본 t 검정
print(stats.ttest_rel(x1,x2)) # p 0.000107593
# p < a 이므로 귀무가설 기각
# 특강이 시험 점수에 영향을 주었다. 라는 의견 채택