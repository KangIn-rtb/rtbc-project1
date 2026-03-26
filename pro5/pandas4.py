import pandas as pd
import numpy as np

df = pd.DataFrame(1000+np.arange(6).reshape(2,3),
                    index=['대전','서울'],columns=['2020','2021','2022'])
print(df)

print()
df_row = df.stack()
print(df_row)
df_col = df_row.unstack() # 행을 열로 이동
print(df_col)

price = [10.3,5.5,7.8,3.6]
cut = [4,7,9,11] # 구간 기준값
re_cut = pd.cut(price, cut) # 연속형 -> 범주화
print(re_cut) #[(4, 7] < (7, 9] < (9, 11]]

print()
datas = pd.Series(np.arange(1,1001))
print(datas.head(3))
print(datas.tail(2))
re_cut2 = pd.qcut(datas,3)
print(re_cut2)

# groupby(~~)
group_col = datas.groupby(re_cut2,observed=True)
#써머리
def summaryF(gr):
    return {'count' : gr.count(),
            'mean' : gr.mean(),
            'std' : gr.std(),
            'min' : gr.min()
    }
print(group_col.apply(summaryF))

print('\nmerge : 데이터 프레임 객체 변환')
df1 = pd.DataFrame({'data1' : range(7), 'key':['b','b','a','c','a','a','b']})
print(df1)

# concat
df3 = pd.DataFrame({'key2':['a','b','d'],'data2':range(3)})
print(pd.concat([df1,df3],axis=0))
print(pd.concat([df1,df3],axis=1))

# pivot
print('\n\n')
data = {'city' : ['강남','강북','강남','강북'],
        'year':[2000,2001,2002,2002],
        'pop':[3.3,2.5,3.0,2.0]}
df = pd.DataFrame(data)
print(df)
print(df.pivot(index='city',columns='year',values='pop'))
print(df.pivot(index='year',columns='city',values='pop'))
print()
print(df.set_index(['city','year']).unstack())
print()
print(df['pop'].describe())
print()
print(df)
print(df.pivot_table(index=['city']))
print(df.pivot_table(index=['city'],aggfunc='mean')) # 위와 같음 아무것도 안쓰면 평균
print(df.pivot_table(index=['city','year'],aggfunc=[len,'sum']))
print(df.pivot_table(values='pop',index='city'))
print(df.pivot_table(values='pop',index='city',aggfunc=len))