"""
특성공학기법 - 좋은 성능을 내기 위해 입력 자료를 변형하거나 가공하는 방법
- 차원 축소
    1) feature selection : 변수 선택
    2) feature extraction : 차원 축소(방법: 주성분분석(PCA))
- Scaling (정규화 표준화)
- Transform (변형)
    1) Binning(비닝) : 연속적 자료를 구간으로 분류 (연속형 -> 범주형)
    2) Dummy : 범주형을 연속형으로 변환
"""
"""
PCA : 선형대수 관점에서, 입력데이터의 공분산 행렬을 고윳값 분해하고
이렇게 구한 고유벡터에 입력 데이터를 선형변환하는 것이다.
이 고유 벡터가 PCA의 주성분 벡터로서 입력 데이터의 분산이 큰 방향을 나타낸다.
입력 데이터의 성질을 최대한 유지한 상태로 고차원을 저차원 데이터로 변환하는 기법
"""

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_iris
import koreanize_matplotlib

iris = load_iris()
n = 10
x = iris.data[:n,:2] # sepal width, height 열만 선택
print(x,x.shape,type(x))
print(x.T)

# 시각화
plt.plot(x.T, 'o:')
plt.xticks(range(2),['꽃받침길이','꽃바침너비'])
plt.grid(True)
plt.legend(['표본 {}'.format(i + 1) for i in range(n)])
plt.show()


# 두개의 그래프 결과 두 변수는 공통적인 특징이 있으므로 차원축소의 근거가 생김
# PCA 진행 - 선형변환을 통해 
# 1 입력 데이터의 공분산 행렬을 생성
# 2 공분산 행렬의 고유벡터와 고윳값을 계산
# 3 고윳값이 큰 순서대로 k개 만큼 고유벡터 추출
# 4 고윳값이 가장 큰 수능로 추출된 고유벡터를 이용해 새 입력 데이터 변환
# PCA가 순서대로 진행함
pca1 = PCA(n_components=1) # 변환할 차원수
x_low = pca1.fit_transform(x) # 특징 행렬을 낮은 차원의 근사행렬로 변환
print(x_low, ' ', x_low.shape)
x2 = pca1.inverse_transform(x_low) # 주성분 원복하기
print(x2,' ',x2.shape)

pc1 = pca1.components_[0] # components_ : 주성분 벡터
mean = x.mean(axis=0) # 데이터 평균

df = pd.DataFrame(x)
ax = sns.scatterplot(x=0,y=1,data=df,markers='s')
