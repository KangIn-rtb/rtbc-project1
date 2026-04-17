# 전통적 방법의 선형회귀 (지도학습)
from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

score_iq = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/score_iq.csv")
x = score_iq.iq
y = score_iq.score
print(x[:3])
print(y[:3])

print('상관 계수 : ', np.corrcoef(x,y)[0,1])
print(score_iq[['iq','score']].corr())
# plt.scatter(x,y)
# plt.show()
# 단순 선형회귀분석(인과관계가 있다는 가정하에 진행)
model = stats.linregress(x,y) # p 2.8476895206683644e-50 
print(model)
print(model.slope)
print(model.intercept)
print(model.pvalue)
plt.scatter(x,y)
plt.plot(x,model.slope * x + model.intercept, c='r')
plt.show()
# print(np.polyval([model.slope, model.intercept],np.array(score_iq['iq'])))
newdf = pd.DataFrame({'iq':[55,66,77,88,150]})
print(np.polyval([model.slope, model.intercept],newdf))
