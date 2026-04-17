# DecistionTree 분류 모델
# 데이터 균일도에 따른 규칙기반의 결정트리
# 트리는 데이터를 지각 기준으로 나누면서 영역을 만든다

from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import numpy as np

x,y = make_classification(n_samples=100,n_features=2,n_redundant=0,n_informative=2,random_state=42)

model = DecisionTreeClassifier(criterion='gini',max_depth=3)
model.fit(x,y)

# 트리구조 시각화
plt.figure(figsize=(10,6))
plot_tree(model, feature_names=['x1','x2'], class_names=['0','1'])
plt.show()

# 결정경계 시각화
xx,yy = np.meshgrid(np.linspace(x[:,0].min(),x[:,0].max(),100),np.linspace(x[:,1].min(),x[:,1].max(),100))
z = model.predict(np.c_[xx.ravel(),yy.ravel()])
z = z.reshape(xx.shape)
# print(z)

plt.contour(xx,yy,z,alpha = 0.3)
plt.scatter(x[:,0], x[:,1],c=y)
plt.title('Decision Boundry')
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()