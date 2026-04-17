# 전통적 방법의 선형회귀 (지도학습)
from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    '구분': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    '지상파': [0.9, 1.2, 1.2, 1.9, 3.3, 4.1, 5.8, 2.8, 3.8 , 4.8, None, 0.9, 3.0, 2.2, 2.0],
    '종편': [0.7, 1.0, 1.3, 2.0, 3.9, 3.9, 4.1, 2.1, 3.1, 3.1, 3.5, 0.7, 2.0, 1.5, 2.0],
    '운동': [4.2, 3.8, 3.5, 4.0, 2.5, 2.0, 1.3, 2.4, 1.3, 35.0, 4.0, 4.2, 1.8, 3.5, 3.5]
}
broad_df = pd.DataFrame(data)
broad_df = broad_df[broad_df['운동'] < 10]
broad_df['지상파'] = broad_df['지상파'].fillna(broad_df['지상파'].mean())
x = broad_df.지상파
y = broad_df.운동
z = broad_df.종편
model1 = stats.linregress(x,y)  # 지상파 운동 
model2 = stats.linregress(x,z)  # 지상파 종편 
print(model1.pvalue)
print(model2.pvalue)
# 4.343472198146363e-05 인과 O
# 3.4783962315596494e-05 인과 O
plt.scatter(x,y)
plt.plot(x,model1.slope * x + model1.intercept, c='r')
plt.show()
plt.scatter(x,z)
plt.plot(x,model2.slope * x + model2.intercept, c='r')
plt.show()
xadd = float(input("지상파 시청시간 입력"))
print(np.polyval([model1.slope, model1.intercept],xadd))
print(np.polyval([model2.slope, model2.intercept],xadd))
