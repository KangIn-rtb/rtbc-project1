

from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/two_sample.csv")
# print(data.head())
# print(data.isnull().sum())
# print(data['score'].isnull.sum())

ms = data[['method','score']]
m1 = ms[ms['method'] == 1]
m2 = ms[ms['method'] == 2]
print(m1.head)
print(m2.head)

sco1 = m1['score']
sco2 = m2['score']
print(sco1.isnull().sum())
print(sco2.isnull().sum())

sco2 = sco2.fillna(sco2.mean()) # NA 를 평균으로 대체

# 정규성 검정
print(stats.shapiro(sco1)) # 0.3679 정규성 만족
print(stats.shapiro(sco2)) # 0.6714 정규성 만족

sns.histplot(sco1, kde=True)
sns.histplot(sco2, kde=True, color='blue')
plt.show()

# 등분산성 검정
from scipy.stats import levene
print(levene(sco1,sco2).pvalue) # 0.456842 만족
result = stats.ttest_ind(sco1,sco2,equal_var=True)
print(result)
# a 0.05 < p 0.845053 우연히 발생한 자료 귀무 채택



