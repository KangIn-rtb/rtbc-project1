# Python 데이터 분석 기초 (Pandas)

Pandas는 고수준의 자료구조와 빠르고 쉬운 데이터 분석용 함수를 제공하는 라이브러리이다. 통합된 시계열 연산, 축약 연산, 누락 데이터(결측치) 처리 등을 지원하여 데이터 랭글링(Data Wrangling)과 먼징(Munging)을 효율적으로 수행할 수 있다.


## 1. Series 와 DataFrame

### Series (시리즈)
일련의 객체를 담을 수 있는 1차원 배열과 같은 자료구조로, 각 데이터에 이름표인 **색인(Index)**을 갖는다.

* **Dict와 Series의 차이점**: 딕셔너리(Dict)는 단순히 키-값 쌍을 보관하지만, Series는 넘파이(NumPy) 기반의 강력한 **벡터화 연산**을 지원하여 반복문 없이 통째로 계산할 수 있어 압도적으로 빠르다.

```python
import pandas as pd
from pandas import Series, DataFrame
import numpy as np

# 1. Series 생성 및 색인(Index) 부여
obj2 = pd.Series([3, 7, -5, 4], index=['a', 'b', 'c', 'd'])
print(obj2.values)   # [ 3  7 -5  4]
print(obj2.index)    # Index(['a', 'b', 'c', 'd'], dtype='object')

# 2. 인덱스 라벨 및 정수 위치로 접근
print(obj2['a'])        # 3
print(obj2[['a', 'b']]) # 여러 개 추출 (대괄호 2개 사용)
print(obj2[2])          # -5 (정수 인덱스로도 접근 가능)
print(obj2.iloc[2])     # -5 (명시적인 정수 위치 기반 접근)

# 3. Dict를 Series로 변환
name = {'mouse': 5000, 'keyboard': 25000, 'monitor': 450000, 'add': '원'}
obj3 = Series(name)
obj3.index = ['마우스', '키보드', '모니터', '더하기'] # 인덱스 이름 변경
obj3.name = "상품가격" # Series 자체의 이름 설정
```

### DataFrame (데이터프레임)
Series가 여러 개 모여 만들어진 2차원 형태(행과 열)의 자료구조이다.

```python
data = {
    'irum': ['홍', '구', '한', '신', '공'],
    'juso': ('역', '신', '삼', '역', '신'),
    'nai' : [23, 25, 33, 231, 35]
}
frame = pd.DataFrame(data)

# 열 접근
print(frame['irum'])
print(frame.irum) # 속성처럼 접근 가능

# 행 삭제 (drop)
frame3 = frame.drop(1) # 인덱스 번호가 1인 행 삭제 (원본은 유지되고 새 객체 반환)

# 정렬 및 카운트
print(frame.sort_index(axis=0, ascending=False)) # 행(axis=0) 기준 내림차순 정렬
print(frame['juso'].value_counts()) # 특정 열의 값별 개수 세기
```


## 2. 재색인 (Reindexing) 및 불리언 인덱싱
데이터의 순서를 바꾸거나, 새로운 인덱스를 추가하여 데이터를 재배치할 때 사용한다. 대응하는 값이 없는 빈 인덱스에는 특정한 값을 채워 넣을 수 있다.

```python
# 1. 재색인 (Reindexing)
data = Series([1, 3, 2], index=(1, 4, 2))
data2 = data.reindex((1, 2, 4)) # 순서 변경

# 비어있는 인덱스에 값 채워 넣기 (fill_value)
data3 = data2.reindex([0, 1, 2, 3, 4, 5], fill_value=777)
print(data3)

# 2. 불리언 인덱싱 (조건 필터링)
df = DataFrame(np.arange(12).reshape(4,3), 
               index=['1월', '2월', '3월', '4월'], 
               columns=['강남', '강북', '서초'])

print(df[df['강남'] > 3]) # '강남' 열의 값이 3보다 큰 행만 필터링하여 출력
```


## 3. 데이터 연산 및 결측치(NaN) 처리
Pandas 객체 간의 사칙연산이 가능하며, 짝이 맞지 않는 인덱스끼리 연산하면 결측치(`NaN`)가 발생한다.

```python
# 1. 사칙 연산
s1 = Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = Series([4, 5, 6, 7], index=['a', 'b', 'c', 'd'])
print(s1 + s2) # 'd' 인덱스는 s1에 없으므로 연산 결과가 NaN이 된다.
print(s1.add(s2)) # sub, mul, div 등의 메서드도 사용 가능

# 2. 결측치(NaN) 확인 및 삭제
df = DataFrame([[1.4, np.nan], [7, -4.5], [np.nan, np.nan], [0.5, -1]], 
               columns=['one', 'two'])

print(df.isnull())   # 결측치 여부를 True/False로 반환
print(df.notnull())  # 결측치가 아닌 것만 True로 반환

print(df.dropna())   # NaN이 하나라도 포함된 행을 모두 삭제
print(df.dropna(how='all')) # 모든 값이 NaN인 행만 삭제

# 원본 데이터에서 직접 삭제 반영
df.drop(1, inplace=True) 

# 3. 새로운 파생 변수(열) 생성
df['total'] = df['one'].mul(df['two']) # one과 two 열을 곱하여 total 열 생성
```


## 4. 데이터 재구조화 (Group, Pivot, Concat)

데이터를 요약하거나 형태를 변형할 때 사용하는 강력한 기능들이다.

### 데이터 회전 및 범주화 (Stack, Cut)
```python
# 1. Stack / Unstack
# stack: 열(Column)을 행(Row)으로 회전시킨다.
# unstack: 행(Row)을 열(Column)로 회전시킨다.
df_row = df.stack()

# 2. Cut / Qcut (연속형 데이터를 구간별 범주형으로 변환)
price = [10.3, 5.5, 7.8, 3.6]
cut_bins = [4, 7, 9, 11] # 구간 기준값
re_cut = pd.cut(price, bins=cut_bins) # (4, 7] < (7, 9] < (9, 11] 형태로 범주화
```

### 그룹화 (Groupby)와 병합 (Concat)
```python
# 1. Groupby (그룹화하여 요약 통계 계산)
datas = pd.Series(np.arange(1, 1001))
re_cut2 = pd.qcut(datas, 3) # 3등분으로 범주화
group_col = datas.groupby(re_cut2, observed=True)

# 그룹별 통계량(개수, 평균, 표준편차, 최솟값)을 한 번에 구하는 함수 적용
def summaryF(gr):
    return {'count': gr.count(), 'mean': gr.mean(), 'std': gr.std(), 'min': gr.min()}
print(group_col.apply(summaryF))

# 2. Concat (데이터프레임 이어 붙이기)
df1 = pd.DataFrame({'key': ['b', 'b', 'a'], 'data1': range(3)})
df3 = pd.DataFrame({'key2': ['a', 'b', 'd'], 'data2': range(3)})

print(pd.concat([df1, df3], axis=0)) # 위아래(행 기준)로 이어 붙이기
print(pd.concat([df1, df3], axis=1)) # 좌우(열 기준)로 이어 붙이기
```

### 피벗 테이블 (Pivot Table)
특정 열을 기준으로 데이터를 재배치하거나 집계(평균, 합계 등)를 수행한다.
```python
data = {'city': ['강남', '강북', '강남', '강북'],
        'year': [2000, 2001, 2002, 2002],
        'pop' : [3.3, 2.5, 3.0, 2.0]}
df = pd.DataFrame(data)

# city를 행으로, year를 열로 하여 pop 값을 배치
print(df.pivot(index='city', columns='year', values='pop'))

# 중복된 값이 있을 경우 집계 함수(aggfunc)를 통해 처리 (기본값은 평균, mean)
print(df.pivot_table(index=['city', 'year'], aggfunc=[len, 'sum']))
```


## 5. 데이터 입출력 (Pandas I/O)
CSV, 텍스트(txt), 웹 상의 데이터 파일 등을 읽고 쓰는 기능이다.

```python
# 1. 파일 읽기 (CSV, Table)
df = pd.read_csv('ex1.csv')
df = pd.read_table('ex1.csv', sep=',', skip_blank_lines=True) # 공백 줄 제거
df = pd.read_csv('http://...', header=None, skiprows=1) # 웹 URL에서 직접 읽고, 첫 줄은 스킵

# 2. 고정 너비 텍스트 파일 읽기 (fwf)
df = pd.read_fwf('data_fwt.txt', header=None, widths=(10, 3, 5), names=('date', 'name', 'price'))

# 3. 대용량 데이터 처리 (Chunk)
# 파일 용량이 너무 커서 메모리 초과(OOM) 오류가 발생할 때, 데이터를 분할(스트리밍)해서 순차적으로 읽는다.
# 여러 번 반복해 읽어야 하므로 속도는 다소 느리지만 메모리를 획기적으로 절약할 수 있다.

# 파일 내보내기 (저장)
csv_fname = 'student.csv'
df.to_csv(csv_fname, index=False) # index=False로 설정하면 불필요한 행 번호를 저장하지 않는다.
```