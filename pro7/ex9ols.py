# 선형회귀분석 : mtcars dataset

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import statsmodels.api 
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib

mtcars = statsmodels.api.datasets.get_rdataset('mtcars').data
print(mtcars.info())
print(np.corrcoef(mtcars.hp,mtcars.mpg))
print(np.corrcoef(mtcars.wt,mtcars.mpg))
# 시각화
plt.scatter(mtcars.hp, mtcars.mpg)
plt.xlabel('마력수')
plt.ylabel('연비')
# plt.show()
re = smf.ols(formula='mpg ~ hp', data=mtcars).fit()
print(re.summary())
print(re.predict(pd.DataFrame({'hp':[110]})).values)

re2 = smf.ols(formula='mpg ~ hp + wt',data=mtcars).fit()
print(re2.summary())
print(re2.predict(pd.DataFrame({'hp':[110],'wt':[5]})).values)
re3 = smf.ols(formula='mpg ~ wt',data=mtcars).fit()
pred = re3.predict()
print(pred[:5])

mtcars.wt = float(input('차체무게 입력 :'))
newpred = re3.predict(pd.DataFrame(mtcars.wt))
print(mtcars.wt[0],newpred[0])