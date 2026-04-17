# 매출 데이터와 날씨 데이터를 활용해
# 강수 여부에 따른 매출액 평균에 차이가 있는지 검정
# 두 집단 : 강수량이 있을때, 맑을때

# 귀무 : 매출 데이터는 강수 여부에 따라 매출액 평균에 차이가 없다.
# 대립 : 매출 데이터는 강수 여부에 따라 매출액 평균에 차이가 있다.

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt 
import koreanize_matplotlib

pd.set_option("display.max_columns",None)
# 매출 데이터 읽기 
sales_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/tsales.csv", dtype = {'YMD':'object'}) # int -> object 변환해 읽기
print(sales_data.head(3))
print(sales_data.info())

# 날씨 데이터 읽기 
wt_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/tweather.csv")
print(wt_data.head(3))
print(wt_data.info())

print()
# sales : YMD 20190514, wt : 2018-06-01 병합을 위해 데이터 변환 필요
wt_data.tm = wt_data.tm.map(lambda x:x.replace("-",""))
frame = sales_data.merge(wt_data, how="left", left_on="YMD", right_on='tm')
print(frame.head()," ",len(frame))
data = frame.iloc[:,[0,1,7,8]]
print(data.head())
print(data.isnull().sum())

# print(data['sumRn'] > 0) # 강수량이 0 보다 크면 True

# data['rain_yn'] = (data['sumRn'] > 0).astype(int)
# print(data.head())
# print(True * 1, ' ', False * 1)
data['rain_yn'] = (data['sumRn'] > 0).astype(int)
print(data.head())

# box plot으로 시각화
sp = np.array(data.iloc[:,[1,4]])
print(sp)
tg1 = sp[sp[:,1] == 0, 0]  # 비 안올 때 매출
tg2 = sp[sp[:,1] == 1, 0]  # 비 올 때 매출
print(tg1[:3])
print(tg2[:3])
print(np.mean(tg1))
print(np.mean(tg2))
plt.boxplot([tg1,tg2], meanline=True, showmeans=True,notch=True)
plt.show()

print(stats.levene(tg1,tg2).pvalue) # 등분산 검정
# 해석 : p 0.9195 > a 0.05 이므로 귀무가설 채택
# 매출 데이터는 강수 여부에 따라 매출액 평균에 차이가 없다고 보여진다. 