# 고수준의 자료구조와 빠르고 쉬운 데이터 분석용 함수 제공
# 통합된 시계열 연산, 축약연산, 누락 데이터 처리, ... 등을 제공
# 데이터 랭글링, 데이터 먼징을 효율적으로 처리 가능
import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# Series : 일련의 객체를 담을 수 있는 1차원 배열과 같은 자료구조로 색인(index)을 갖는다. 
obj = pd.Series([3,7,-5,4])
# obj = pd.Series([3,7,-5,'사']) # type -> object로 바뀜
# obj = pd.Series((3,7,-5,4))
# obj3 = pd.Series({3,7,-5,4}) # set은 순서가 없어 안됨
print(obj,type(obj))
# print(obj3)
obj2 = pd.Series([3,7,-5,4], index=['a','b','c','d']) # 색인 부여 가능
print(obj2.sum(),' ', np.sum(obj),' ',sum(obj2))
print()
print(obj.std())
print(obj2.values)
print(obj2.index)
print(obj2['a']) # 3
print(obj2[['a']]) # a   3
print(obj2[['a','b']])  # a   3
                        # b   7
print(obj2['a':'c'])    # a   3
                        # b   7
                        # c  -5
print(obj2[2]) # -5
print(obj2.iloc[2]) # -5
print(obj2[1:4])

print(obj2[[2,1]])
print(obj2.iloc[[2,1]])
"""
dict 와 Series
1. 구조적 공통점: "이름표가 붙은 데이터"둘 다 특정 데이터에 접근하기 위해 '인덱스(키)'를 사용합니다.dict: {'사과': 1000, '바나나': 2000}Series: 사과: 1000, 바나나: 2000 (인덱스가 '사과', '바나나'가 됨)실제로 Pandas에서는 딕셔너리를 그대로 Series로 변환하는 것이 매우 자연스럽습니다.Pythonimport pandas as pd
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_series = pd.Series(my_dict) # 딕셔너리가 바로 시리즈가 됨!
2. 주요 차이점: 왜 Series를 쓸까?단순히 키-값 쌍이 필요하다면 딕셔너리로 충분하지만, 대량의 데이터를 다루거나 계산할 때는 Series가 압도적으로 유리합니다.특징파이썬 dictPandas Series순서(Order)삽입 순서 유지 (Py 3.7+)명시적인 순서가 있으며, 인덱싱/슬라이싱 가능연산 속도반복문(for)을 써야 해서 느림벡터화 연산 (통째로 계산)으로 매우 빠름인덱스 접근키(Key)로만 접근 가능**라벨(Key)**뿐만 아니라 **정수 위치(Index)**로도 접근 가능기능(Method)기본 기능 위주통계(mean, sum), 필터링, 결측치 처리 등 강력한 기능 제공메모리데이터마다 타입이 달라 메모리 사용 비효율적동일한 타입(dtype)으로 묶어 메모리 효율적 관리
3. 결정적인 차이: 벡터화 연산 (Vectorization)딕셔너리는 모든 값에 10을 더하려면 반복문을 돌려야 하지만, Series는 한 번에 가능합니다.dict의 경우: for k in d: d[k] += 10Series의 경우: series += 10 (넘파이 기반의 강력한 기능!)요약하자면:dict는 데이터를 개별적으로 저장하고 관리하는 '보관함' 느낌이라면,Series는 그 데이터를 가지고 복잡한 수학적 계산이나 통계를 내기 위한 '전문 도구'라고 볼 수 있습니다.
"""
# dict Series 변환
name = {'mouse' : 5000, 'keyboard' : 25000, 'monitor' : 450000, 'add' : '원'}
obj3 = Series(name)
print(obj3)
obj3.index = ['마우스','키보드','모니터', '더하기']
print(obj3)
obj3.name = "상품가격"
print(obj3)
re = obj3.astype(str) + '임' # 숫자 + 문자는 안되니 astype으로 문자로 변환
print(re)
"""
마우스      5000임
키보드     25000임
모니터    450000임
더하기         원임
Name: 상품가격, dtype: object
"""

# DataFramne - Series로 구성되있는 자료구조
df = pd.DataFrame(obj3)
print(df,' ', type(df))
data = {
    'irum':['홍','구', '한', '신', '공'],
    'juso':('역','신', '삼', '역', '신'),
    'nai' : [23,25,33,231,35]
}
frame = pd.DataFrame(data)
print(frame['irum'])
print(frame.irum)
print(type(frame.irum))
print(DataFrame(data=data, columns=['juso','irum','nai']))

#NaN 결측치
frame2 = pd.DataFrame(data,columns=['irum','nai','juso','tel'],index=['a','b','c','d','e'])
frame2['tel'] = '111-1111'

val = pd.Series(['222-2222','333-3333','444-4444'],index = ('b','c','e'))
print(val)
frame2['tel'] = val # 덮어쓰기 헤서 이전의 111-1111은 NaN으로 덮어짐
print(frame2)
print(frame2.values)
print()
print(frame2.T)
print(frame2.T.values)
print()
print(frame2.values[0,1])
print(frame2.values[0:2])
frame3 = frame2.drop('d')
print(frame3)

# ----- 정렬
print(frame2.sort_index(axis=0, ascending=False))
print(frame2.sort_index(axis=1, ascending=True))
print(frame2.rank(axis=0))
counts = frame2['juso'].value_counts()
print(counts)

data = {
    'juso':['강남구 역삼동', '중구 신당동', '강남구 대치동'],
    'inwon' : [23,25,15]
}
fr = pd.DataFrame(data)
print(fr)
re1 = Series([x.split()[0] for x in fr.juso])
re2 = Series([x.split()[1] for x in fr.juso])
print(re1)
print(re2)