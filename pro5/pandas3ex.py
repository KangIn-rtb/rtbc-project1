from pandas import DataFrame, Series
import pandas as pd
import numpy as np

# # ex1)
# """
# pandas 문제 1)

#   a) 표준정규분포를 따르는 9 X 4 형태의 DataFrame을 생성하시오. 

#      np.random.randn(9, 4)

#   b) a에서 생성한 DataFrame의 칼럼 이름을 - No1, No2, No3, No4로 지정하시오

 

#   c) 각 컬럼의 평균을 구하시오. mean() 함수와 axis 속성 사용
# """
# a = np.random.randn(9,4)
# df = DataFrame(a)
# df.columns = ['No1','No2','No3','No4']
# print(df.mean(axis=0))

# # ex2)
# """
# a) DataFrame으로 위와 같은 자료를 만드시오. colume(열) name은 numbers, row(행) name은 a~d이고 값은 10~40.

# b) c row의 값을 가져오시오.

# c) a, d row들의 값을 가져오시오.

# d) numbers의 합을 구하시오.

# e) numbers의 값들을 각각 제곱하시오. 아래 결과가 나와야 함.

# f) floats 라는 이름의 칼럼을 추가하시오. 값은 1.5, 2.5, 3.5, 4.5    아래 결과가 나와야 함.
# g) names라는 이름의 다음과 같은 칼럼을 위의 결과에 또 추가하시오. Series 클래스 사용.
# """
# df2 = DataFrame([10,20,30,40],index=('a','b','c','d'))
# df2.columns = ['numbers']
# print(df2)
# print(df2.loc['c'])
# print(df2.loc[['a','d']])
# print(df2.sum())
# print(df2**2) 
# df2['float'] = [1.5,2.5,3.5,4.5]
# print(df2)
# name = Series(['길동','오정','팔계','오공'],index=('a','b','c','d'))
# df2['names'] = name
# print(df2)

# # ex3)
# val = np.random.randint(1,21,15).reshape(5,3)
# df = DataFrame(val,index=('r1','r2','r3','r4','r5'))
# df.columns = ['A','B','C']
# print(df)
# print(df[df['A']>10])
# df['D'] = df['A'].add(df['B'])
# print(df)
# df.drop('r3',inplace=True)
# print(df)
# df.loc['r6'] = [15,10,2,15+10]
# print(df)

# #ex4)
# data = {
#     'product': ['Mouse', 'Keyboard', 'Monitor', 'Laptop'],
#     'price':   [12000,     25000,      150000,    900000],
#     'stock':   [  10,         5,          2,          3 ]
# }
# df = DataFrame(data,index=('p1','p2','p3','p4'))
# print(df)
# df['total'] = df['price'].mul(df['stock'])
# print(df)
# df.columns = ['상품명','가격','재고','총가격']
# print(df)
# print(df[df['재고']<=3])
# print(df.iloc[[1]])
# print(df.loc[['p2']])
# print(df.drop('p3'))
# df.loc['p5'] = ['USB메모리',15000,10,15000*10]
# print(df)

#ex5)
df = pd.read_csv('titanic_data.csv')
bins = [1, 20, 35, 60, 150]
labels = ["소년", "청년", "장년", "노년"]
df['나이대'] = pd.cut(df['Age'],bins=bins,labels=labels)
df2 = df[df['Survived']==1]
print(df2['나이대'].value_counts())
print(df.pivot_table(index=['Sex'],columns=['Pclass'],values=['Survived']))
print(df.pivot_table(index=['Sex','나이대'],columns=['Pclass'],values=['Survived']))

#ex6
df = pd.read_csv('human.csv')
df.columns = df.columns.str.strip()
df = df[df['Group'].str.strip() != 'NA']
print(df)
print(df[['Career','Score']].mean())

df = pd.read_csv('tips.csv')
print(df)
print(df.head(3))
print(df.describe())
print(df.value_counts(['smoker']))
print(df['day'].unique())