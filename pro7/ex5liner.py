# 전통적 방법의 선형회귀
# 각 데이터에 대한 전차 제곱합이 최소가 되는 추세선을 만들고
# 이를 통해 독립변수가 종속변수에 얼마나 영향을 주는지 인과관계를 분석
# 독립변수 : 연속형, 종속변수 : 연속형 - 두 변수는 상관관계 및 인과관계가 있어야함
# 정량적인 모델을 생성

import statsmodels.api as sm
from sklearn.datasets import make_regression
import numpy as np

np.random.seed(12)
# 모델 맛보기
# 방법 1 : make_regression 사용 model 생성 X
x,y,coef = make_regression(n_samples=50,n_features=1,bias=100,coef=True)
print(x)
print(y) # -52.1721
print(coef)
y_pred = coef * -1.70073563 + 100
print(y_pred)
xx = x
yy = y
from sklearn.linear_model import LinearRegression
model = LinearRegression()
fit_model = model.fit(xx,yy) # 최소제곱법으로 기울기, 절편을 반환
print()
print(fit_model.coef_)
print(fit_model.intercept_)

y_newpre = fit_model.predict(xx[[0]])
print(y_newpre)
print()
# 잔차 제곱합을 최소화하는 가중치 벡터를 행렬 미분으로 구하는 방법
import statsmodels.formula.api as smf
print(xx.ndim)
x1 = xx.flatten() # 차원축소 xx.ravel()
print(x1.ndim)
y1 = yy
import pandas as pd
data = np.array([x1,y1])
df = pd.DataFrame(data.T)
df.columns = ['x1','y1']
print()
mode12 = smf.ols(formula="y1~x1",data=df).fit()
print(mode12.summary())
new_df = pd.DataFrame({'x1':[-1.7007356,-0.67794537]})
new_df2 = pd.DataFrame({'x1':[0.1234,0.2345]})
print(mode12.predict(new_df))
print(mode12.predict(new_df2))