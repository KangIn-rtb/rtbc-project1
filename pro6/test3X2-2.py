# 5개의 스포츠 음료에 대한 선호도에 차이가 있는지 검정하기
# 대립가설 : 기대치와 관찰치는 차이가 있다. 스포츠 음료에 선호도 차이가 있다.
# 귀무가설 : 기대치와 관찰치는 차이가 없다. 스포츠 음료에 선호도 차이가 없다.

import pandas as pd
import scipy.stats as stats
url = "https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/drinkdata.csv"
# 5개의 자료 다 더하고 5로 나누면 기대 빈도
data = pd.read_csv(url)
print(data)
print(stats.chisquare(data['관측도수']))
exp = [data['관측도수'].sum() / 5] * 5
print(exp) # 기대빈도 50.8
stat, p = stats.chisquare(f_obs=data['관측도수'],f_exp=exp)
print(stat, p)

# 판정 : 유의 수준 0.05 < p : 0.000399991 이므로 귀무 기각
# 스포츠 음료의 선호도에 차이가 있다. 라는 의견이 받아 들여짐

import matplotlib.pylab as plt
import koreanize_matplotlib
import numpy as np
# 기대도수 
total = data['관측도수'].sum()
expected = [total / len(data)] * len(data)
x = np.arange(len(data))
width = 0.35 
plt.figure(figsize=(10,5))
plt.bar(x-width / 2 , data['관측도수'],width=width, label='관측도수')
plt.bar(x-width / 2 , expected,width=width, label='기대도수',alpha=0.6)
plt.xticks(x,data['음료종류'])
plt.xlabel('음료종류')
plt.ylabel('도수')
plt.legend()
plt.show()


