from pandas import Series,DataFrame
import numpy as np

# Series 더하기
s1 = Series([1,2,3], index = ['a','b','c'])
s2 = Series([4,5,6,7], index = ['a','b','c','d'])
print(s1+s2)
print(s1.add(s2))

#sub,mul,div 등 도 가능
df =  DataFrame([[1.4,np.nan],[7,-4.5],[np.nan,np.nan],[0.5,-1]],columns=['one','two'])

print(df)
print()
print(df.isnull())
print(df.notnull())
print(df.dropna())
print(df.dropna(how='any'))

# 특정 열, 행에 NaN이 포함된 행/열 삭제
#~~~


imsi = df.drop(1) # 원본 삭제는 안됨. 삭제된 결과가 새로운 Dataframe으로 생성됨
print(imsi)
print(df)
df.drop(1,inplace=True) # 원본 삭제됨
print(df)

# 계산 관련 메소드
print(df.sum())
print(df.sum(axis=0))