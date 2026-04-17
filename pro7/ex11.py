import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib
import statsmodels.formula.api as smf

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/Carseats.csv")
df = data.drop([data.columns[6],data.columns[9],data.columns[10]],axis=1)
lm = smf.ols(formula='Sales ~ Income+Advertising+Price+Age',data=df).fit()
print(lm.summary())
df_lm = df.iloc[:, [0,2,3,5,6]]
# 잔차항 구하기 
fitted = lm.predict(df_lm)
residual = df_lm['Sales'] - fitted
print('residual:',residual[:3])
print('잔차 평균:',np.mean(residual))
print()
# 독립성 검정
# 잔차가 자기상관(인접 관측치의 오차가 상관됨)이 있는지 확인
# model.summary로 확인 가능
import statsmodels.api as sm
print(sm.stats.stattools.durbin_watson(residual))
# 1.931498이므로 잔차의 자기 상관은 없다.

# 다중공선성 검정 : 다중회귀 분석 시 독립변수 간에 강한 상관관계가 있어서는 안된다.
from statsmodels.stats.outliers_influence import variance_inflation_factor
df_ind = df[['Income','Advertising','Price','Age']]
vifdf = pd.DataFrame()
vifdf['vif_value'] = [variance_inflation_factor(df_ind.values, i) for i in range(df_ind.shape[1])]
print(vifdf)



# 방법 1
# import pickle
# with open('carseat.pickle', 'wb') as obj: # 저장
#     pickle.dump(lm,obj)
# with open('carseat.pickle', 'rb') as obj: # 읽기
#     mymodel = pickle.load(lm,obj)

# 방법 2 : pickle은 binary로 i/o 해야하므로 번거롭다.
import joblib
joblib.dump(lm, 'carseat.model')
# 이후 부터는 아래 처럼 읽어 사용하면 됨
mymodel = joblib.load('carseat.model')

