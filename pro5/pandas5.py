#pandas file i/o 
import pandas as pd 
import numpy as np
df = pd.read_csv('ex1.csv')
print(df,type(df))
print()
df = pd.read_table('ex1.csv',sep=',')
df = pd.read_table('ex1.csv',sep=',',skip_blank_lines=True)
# skip_blank_lines : 칼럼명, 데이터의 앞에 공백을 제거
print(df)
print()
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex2.csv')
print(df)
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex2.csv',header=None)
print(df)
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex2.csv',header=None,skiprows=1)
print(df)
print()
print()
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex3.txt')
print(df)
df = pd.read_table('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/ex3.txt',sep='\s+')
print(df)
print(df.iloc[:,0])
df = pd.read_fwf('https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/data_fwt.txt',header=None,widths=(10,3,5),names=('date','name','price'))
print(df)
print(df.iloc[:,0])
print('\nchunk : 대량의 데이터를 부분씩 메모리호 읽어 처리')
# 대용량 자료 로딩시 초과 오류 발생 방지 : 메모리를 절약
# 스트리밍 방식(일부만 순차 처리)으로 읽음
# 분산처리의 효과
# 여러번 반복해 읽어야 하므로 속도는 느리다
import time 
n_rows = 10000
data = {
    'id':range(1,n_rows+1),
    'name':[f'student_{i}' for i in range(1,n_rows+1)],
    'score1' : np.random.randint(50, 101, size=n_rows),
    'score2' : np.random.randint(50, 101, size=n_rows)
}
df = pd.DataFrame(data)
print(df.head())
print(df.tail(3))
csv_fname = 'student.csv'
df.to_csv(csv_fname,index=False) 