# 전통적인 분류 방법 
# 1. bagging - random forest - 속도
# 2. boosting - XGboost - 성능

# 머신러닝에서 분류와 회귀 분석에 널리 사용되는 강력한 앙상블 학습 알고리즘이다.
# 여러개의 결정 트리를 생성하고, 이들의 예측 결과를 종합하여 최종적인 분류결과를 도출합니다.

# 앙상블 기법 중 배깅(Bootstrap Aggregation)
# : 복수의 샘플 데이터와 DisistionTree를 학습 시키고 결과를 집계

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score


data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/titanic_data.csv")
print(data.head(3))
df = data.dropna(subset=['Pclass','Age','Sex'])
print(df.shape)

df_x = df[['Pclass','Age','Sex']]
print(df_x.head(3))
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
df_x.loc[:,'Sex'] = encoder.fit_transform(df_x['Sex'])
print(df_x.head(3))
df_y = df['Survived']
print(df_y.head(3))
print()
train_x, test_x, train_y, test_y = train_test_split(df_x,df_y, test_size=0.3,random_state=12)
print(train_x.shape, test_x.shape, train_y.shape, test_y.shape)
# (499, 3) (215, 3) (499,) (215,)
# 모델 생성
model = RandomForestClassifier(criterion='gini',n_estimators=500,random_state=12)
# n_estimators=결정트리수
model.fit(train_x,train_y)
pred = model.predict(test_x)
print(pred[:5])
print(test_y[:5])
print(sum(test_y==pred))
print(sum(test_y==pred)/len(test_y))
print(accuracy_score(test_y,pred))