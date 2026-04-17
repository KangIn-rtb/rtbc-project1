import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
import statsmodels.formula.api as smf

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/weather.csv")
print(data.head(), data.shape)
data2 = pd.DataFrame()
data2 = data.drop(['Date','RainToday'], axis=1)
data2['RainTomorrow']=data2['RainTomorrow'].map({'Yes':1, 'No':0})
print(data2.head(2), data2.shape)
print(data2.RainTomorrow.unique())

# RainTomorrow : 종속변수(범주형), 나머지열 : 독립변수
# 모델의 성능을 객관적으로 파악. 모델 학습과 검증에 사용된 자료가 같다면 과적합 우려 발생
train, test = train_test_split(data2, test_size=0.3, random_state=42)
print(train.shape, test.shape)

# 모델생성
col_select = "+".join(train.columns.difference(['RainTomorrow'])) # 독립변수
print(col_select)
my_formula = 'RainTomorrow ~'+col_select
model = smf.logit(formula=my_formula, data=train).fit()
print(model.summary())
print(model.params)
print()
print(np.rint(model.predict(test)[:15].values))
print(test['RainTomorrow'][:15].values)

# 분류 정확도
conf_mat = model.pred_table()
print(conf_mat)
print((conf_mat[0][0]+conf_mat[1][1])/len(train))
from sklearn.metrics import accuracy_score
pred = model.predict(test)
print(accuracy_score(test['RainTomorrow'],np.rint(pred)))