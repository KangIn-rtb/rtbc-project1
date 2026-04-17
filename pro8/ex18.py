# LogisticRegresion 로지스틱 회귀분석
# 선형결합을 로그오즈로 해석하고 이를 시그모이드 함수를 통해 확률로 변환
# 이항분류, 독립변수 : 연속형, 종속변수 : 범주형
# LogisticRegresion을 근거로 뉴럴넷의 뉴런에서 사용함

import statsmodels.api as sm

data = sm.datasets.get_rdataset('mtcars')
print(data.keys())
mtcars = sm.datasets.get_rdataset('mtcars').data
print(mtcars.head(2))
print(mtcars.info())

# 연비와 마력수에 따른 변속기 분류
mtcar = mtcars.loc[:,['mpg','hp','am']]
print(mtcar.head(2))
print(mtcar['am'].unique())

import numpy as np
import statsmodels.formula.api as smf
formula = 'am ~ hp + mpg' 
result = smf.logit(formula=formula, data=mtcar).fit()
print(result.summary())

pred = result.predict(mtcar[:10])
print(pred.values)
print(np.around(pred.values))
print(mtcar['am'][:10].values)
print()
conf_tab = result.pred_table()
print(conf_tab)
"""
          예측값
         P     N
실  참  [[16.  3.]
값 거짓 [ 3. 10.]]
모델이 제대로 예측한 것은 26개 이다. (대각선)
"""

# 모듈로 확인2 - accuracy_score이용
from sklearn.metrics import accuracy_score
pred2 = result.predict(mtcar)
print(accuracy_score(mtcar['am'], np.around(pred2)))

print()
# 모델 작성 방법2 : glm() - 일반화된 선형모델
result2 = smf.glm(formula=formula, data=mtcar, family=sm.families.Binomial()).fit()
print(result2.summary())
glm_pred = result2.predict(mtcar[:10])
print(np.around(glm_pred.values))
print(mtcar['am'][:10].values)

glm_pred2 = result2.predict(mtcar)
print(accuracy_score(mtcar['am'], np.around(glm_pred2)))

#logit()은 변환 함수, glm()은 logit()을 포함한 전체 모델
print('새로운 값으로 분류-----')
import pandas as pd
newdf = pd.DataFrame()
newdf['mpg'] = [10,30,120,200]
newdf['hp'] = [100,110,80,130]
print(newdf)
new_pred = result2.predict(newdf)
print(np.around(new_pred.values))