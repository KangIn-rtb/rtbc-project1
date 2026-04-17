from sklearn.linear_model import LinearRegression
import statsmodels.api
import matplotlib.pyplot as plt
import koreanize_matplotlib
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error

mtcars = statsmodels.api.datasets.get_rdataset('mtcars').data
print(mtcars.head())
print(mtcars.corr(method='pearson'))

x = mtcars[['hp']].values
y = mtcars[['mpg']].values

lmodel = LinearRegression().fit(x,y)
plt.scatter(x,y)
plt.plot(x, lmodel.coef_ * x + lmodel.intercept_, c='r')
plt.show() # 잔차 제곱이 최소가 되는 선

# mpg 예측 
pred = lmodel.predict(x)
print(np.round(pred[:5],1))
print(y[:5])

# 모델 성능 지표
# MSE : 모델 내부 비교
# RMSE : 보고/해석용 
print('MSE : ', mean_squared_error(y,pred))
print('RMSE : ', np.sqrt(mean_squared_error(y,pred)))
print('r2_score : ', r2_score(y,pred))
# r2_score 하나만 보고 모델 판단 X(이상치에 민감, 변수가 많으면 증가), 설명력만 봄
# 모델 성능은 r2_score와 MSE or r2_score와 RMSE를 사용하도록 한다.

new_hp = [[100],[110],[120],[130]]
new_pred = lmodel.predict(new_hp)
print(new_pred.flatten())