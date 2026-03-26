#iris dataset : 150행, 3가지 종류, 4개의 특성
import matplotlib.pyplot as plt
import pandas as pd

# %matplotlib inline # jupyter 노트북에서 실습시 show() 생략

iris_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/iris.csv")
print(iris_data.info())
print(iris_data.head(3))
print(iris_data.tail(3))

# 산점도 
plt.scatter(iris_data['Sepal.Length'],iris_data['Petal.Length'])
plt.show()

print()
print(iris_data['Species'].unique())
print(set(iris_data['Species']))

import seaborn as sns
sns.pairplot(iris_data,hue='Species',height=2)
plt.show()