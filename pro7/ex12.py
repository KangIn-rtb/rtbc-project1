import numpy as np
import matplotlib.pylab as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,explained_variance_score,mean_squared_error
from sklearn.preprocessing import MinMaxScaler

sample_size = 100
np.random.seed(1)

x = np.random.normal(0,10,sample_size)
y= np.random.normal(0,10,sample_size) + x*30
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x.reshape(-1,1))
print(x[:5])
print(x_scaled[:5])
plt.scatter(x_scaled,y)
plt.show()

model = LinearRegression().fit(x_scaled,y)
print(model)
print(model.coef_)
print(model.intercept_)
print(model.score(x_scaled,y))
ypred = model.predict(x_scaled)
print(ypred)

def myRegScoreFunc(y, ypred):
    # 결정계수 : 실제 관측값의 분산대비 예측값의 분산을 계산하여 데이터 예측의 정확도 성능 측정 지표
    print(r2_score(y, ypred))
    print(explained_variance_score(y,ypred))
    print(mean_squared_error(y,ypred))
myRegScoreFunc(y,ypred)

x2 = np.random.normal(0,1,sample_size)
y2 = np.random.normal(0,100,sample_size) + x*30
print(np.corrcoef(x2,y2)[0,1]) # -0.05484441740006399
