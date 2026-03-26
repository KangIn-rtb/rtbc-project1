from pandas import Series, DataFrame

#Series 의 재색인

data = Series([1,3,2], index = (1,4,2))
print(data)
data2 = data.reindex((1,2,4)) # 순서 바꾸기? 
print(data2)

print("\n재색인할 때 값 채워 넣기")
data3 = data2.reindex([0,1,2,3,4,5])
print(data3)
# 대응값 없는 index에는 특정값으로 채움
data3 = data2.reindex([0,1,2,3,4,5], fill_value=777)
print(data3)

import numpy as np
df = DataFrame(np.arange(12).reshape(4,3), index = ['1월','2월','3월','4월'], columns=['강남','강북','서초'])
print(df['강남'])
print(df['강남']>3)
print(df[df['강남']>3])

# df.ioc / df.iloc

