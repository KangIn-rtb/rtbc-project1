# 캐글 santander customer satisfaction dataset 사용
# 산탄데르 은행의 고객 만족 여부 분류 처리
# 클래스 명은 target이고 0:만족, 1:불만족

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GridSearchCV
from xgboost import plot_importance
from sklearn.model_selection import train_test_split
pd.set_option('display.max_columns',None)

df = pd.read_csv('train_san.csv',encoding='latin-1')
print(df.head(2))
print(df.shape)
print(df.info())

print(df['TARGET'].value_counts())
unsatisfied_cnt = df[df['TARGET'] == 1].TARGET.count()
total_cnt = df.TARGET.count()
print(f"불만족 비율은 {unsatisfied_cnt/total_cnt}")

print(df.describe()) # feature의 분포 확인
df['var3'].replace(-999999,2,inplace=True)
df.drop('ID',axis=1,inplace=True)
print(df.describe())

# feature / label 분리
x_feature = df.iloc[:,:-1]
y_label = df.iloc[:,-1]
print(x_feature.shape)

x_train, x_test, y_train, y_test = train_test_split(x_feature, y_label,test_size=0.3)
train_cnt = y_train.count()
test_cnt = y_test.count()
print(x_train.shape,x_test.shape)
# print(y_train.value_counts() / train_cnt)
# print(y_test.value_counts() / test_cnt)

from xgboost.callback import EarlyStopping

xgb_clf = XGBClassifier(n_estimators=5,random_state=12,eval_metric='auc')
xgb_clf.fit(x_train, y_train,eval_set=[(x_test,y_test)])
xgb_roc_score = roc_auc_score(y_test, xgb_clf.predict_proba(x_test)[:,1])
print(f"{xgb_roc_score:.5f}")

pred = xgb_clf.predict(x_test)
print(pred[:5])
print(y_test[:5].values)
from sklearn import metrics
print(metrics.accuracy_score(y_test, pred))
print()
# 최적의 파라미터 구하기
params = {'max_depth':[5,7],'min_child_weight':[1,3],'colsample_bytree':[0.5,0.75]}
# depth : 트리 깊이 , weight : 가중치합 최소, colsample : 피처비트리
gridcv = GridSearchCV(xgb_clf, param_grid=params)
gridcv.fit(x_train,y_train,eval_set=[(x_test,y_test)])
print('최적 파라미터',gridcv.best_params_)
xgb_roc_score = roc_auc_score(y_test, gridcv.predict_proba(x_test)[:,1], average='macro')
print(f"{xgb_roc_score:.5f}")
# 최적 파라미터 {'colsample_bytree': 0.75, 'max_depth': 5, 'min_child_weight': 3}
xgb_clf2 = XGBClassifier(n_estimators=5,random_state=12,max_depth=5,min_child_weight=3,colsample_bytree=0.75)
xgb_clf2.fit(x_train, y_train,eval_set=[(x_test,y_test)])
xgb_roc_score = roc_auc_score(y_test, xgb_clf2.predict_proba(x_test)[:,1])
print(f"{xgb_roc_score:.5f}")

pred = xgb_clf2.predict(x_test)
print(pred[:5])
print(y_test[:5].values)
from sklearn import metrics
print(metrics.accuracy_score(y_test, pred))

# 중요 피처 시각화 
fig, ax = plt.subplots(1,1, figsize = (10,8))
plot_importance(xgb_clf2, ax=ax, max_num_features=15)
plt.show()