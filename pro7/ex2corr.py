# 공분산 상관계수
import pandas as pd
import numpy as np
import koreanize_matplotlib
import matplotlib.pyplot as plt

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/drinking_water.csv")
print(np.std(data.친밀도))
print(np.std(data.적절성))
print(np.std(data.만족도))
plt.hist([np.std(data.친밀도), np.std(data.적절성),np.std(data.만족도)])
plt.show()

print(np.cov(data.친밀도, data.적절성))
print(np.cov(data.친밀도, data.만족도))
print()
print(data.cov())
print()
print(np.corrcoef(data.친밀도, data.적절성))
print(np.corrcoef(data.친밀도, data.만족도))
print()
print(data.corr(method='pearson')) # 변수가 연속형 정규성 따름
print(data.corr(method='spearman')) # 변수가 서열형 정규성 따르지 않음
print(data.corr(method='kendall')) 

co_re = data.corr()
print(co_re['만족도'].sort_values(ascending=False))
data.plot(kind='scatter',x='만족도',y='적절성')
plt.show()

from pandas.plotting import scatter_matrix
attr = ['친밀도','적절성','만족도']
scatter_matrix(data[attr],figsize=(10,6))
plt.show()

import seaborn as sns
sns.heatmap(data.corr(), annot=True)
plt.show()

# heatmap에 텍스트 표시 추가사항 적용해 보기
corr = data.corr()
# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)  # 상관계수값 표시
mask[np.triu_indices_from(mask)] = True
# Draw the heatmap with the mask and correct aspect ratio
vmax = np.abs(corr.values[~mask]).max()
fig, ax = plt.subplots()     # Set up the matplotlib figure

sns.heatmap(corr, mask=mask, vmin=-vmax, vmax=vmax, square=True, linecolor="lightgray", linewidths=1, ax=ax)

for i in range(len(corr)):
    ax.text(i + 0.5, len(corr) - (i + 0.5), corr.columns[i], ha="center", va="center", rotation=45)
    for j in range(i + 1, len(corr)):
        s = "{:.3f}".format(corr.values[i, j])
        ax.text(j + 0.5, len(corr) - (i + 0.5), s, ha="center", va="center")
ax.axis("off")
plt.show()