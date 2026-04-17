# 단순 선형 회귀 - iris dataset
# 상관관계가 약한 경우와 강한 경우로 분석모델을 생성 후 비교

from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import seaborn as sns

iris = sns.load_dataset('iris')
print(iris.head(3),type(iris))
print(iris.iloc[:,0:4].corr())

re1 = smf.ols(formula='sepal_length ~ sepal_width',data=iris).fit()
print(re1.summary())
plt.scatter(iris.sepal_width,iris.sepal_length)
plt.plot(iris.sepal_width, re1.predict(),color='r')
plt.show()


re2 = smf.ols(formula='sepal_length ~ petal_length',data=iris).fit()
print(re2.summary())
plt.scatter(iris.petal_length,iris.sepal_length)
plt.plot(iris.petal_length, re2.predict(),color='b')
plt.show()

print(iris.sepal_length[:10].values)
print(re2.predict()[:10])

newdata = pd.DataFrame({'petal_length':[1.1, 0.5, 6.0]})
ypred = re2.predict(newdata)
print(ypred.values)

print()
columnselect = "+".join(iris.columns.difference(['sepal_length','sepal_width','species']))
re3 = smf.ols(formula='sepal_length ~ '+columnselect, data=iris).fit()
print(re3.summary())