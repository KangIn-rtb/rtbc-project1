# 군집분석: 데이터간의 유사도를 정의하고 그 유사도에 가까운 것부터 순서대로 합쳐가는 방법으로, 거리나 상관계수 등을 이용한다.
# 이는 비슷한 특성을 가진 개체를 그룹으로 만들고, 군집 분리 후 t-test, ANOVA 분석등을 통해 그룹간 평균의 차이를 확인할 수 있다. 
# 군집분석은 데이터만 주고 label은 제공하지 않는 비지도 학습이다. 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

np.random.seed(123)
var = ['x','y']
labels = ['점0','점1','점2','점3','점4']
x = np.random.random_sample([5,2])*10
df = pd.DataFrame(x,columns=var,index=labels)
print(df)
plt.scatter(x[:,0],x[:,1],c='blue',marker='o',s=50)
for i, txt in enumerate(labels):
    plt.text(x[i,0],x[i,1],txt)
plt.show()

from scipy.spatial.distance import pdist, squareform
dist_vec = pdist(df, metric='euclidean')
print(dist_vec)
row_dist = pd.DataFrame(squareform(dist_vec),columns=labels,index=labels)
print(row_dist)
print()
from scipy.cluster.hierarchy import linkage
row_clusters = linkage(dist_vec, method='ward')
df2 = pd.DataFrame(row_clusters)
print(df2)