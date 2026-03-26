import numpy as np
# data = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# print(data[:,::-1][::-1])

# 1. lxml
# 2. select
# 3. except

# 1. to_sql
# 2. index = False

# DataFrame(np.arange(12).reshape((4,3)), index = ['1월','2월','3월','4월'], columns=['강남','강북','서초'])

# data.to_csv('test.csv', index=False, header=False)

from pandas import DataFrame
# frame = DataFrame({'bun':[1,2,3,4], 'irum':['aa','bb','cc','dd']}, index=['a','b', 'c','d'])
# print(frame.transpose())
# frame2 = frame.drop(['d'],axis=0)
# print(frame2)

import pandas as pd
# df = pd.read_csv('ex.csv',names=['a','b','c','d'])
# print(df)

# 1. Series
# 2. df

# x = np.array([1,2,3,4,5])
# y = np.arange(1, 4).reshape(3, 1)
# print(x + y)
# 배열 크기 자동 맞춤 : 브로드캐스팅

import MySQLdb
import pandas as pd
import numpy as np
import sys
# def main():
#     CONFIG = {'host': '127.0.0.1', 'user': 'root', 'passwd': '123', 'db': 'test', 'port': 3306, 'charset': 'utf8'}
#     try:
#         conn = MySQLdb.connect(**CONFIG)
#         cursor = conn.cursor()
#         sql = """
#         Select jikwonno,jikwonpay from jikwon
#         left join gogek on jikwonno = gogekdamsano
#         where gogekdamsano is null;
#         """
#         df = pd.read_sql(sql, conn)
#         jik_cont = df['jikwonno'].count()
#         pay_mean = df['jikwonpay'].mean()
#         pay_std = df['jikwonpay'].std()
#         print(f"직원 수 : {jik_cont}\n연봉 평균 : {pay_mean}\n연봉 표준편차 : {pay_std:.3f}")
#     except Exception as e:
#         print(e)
#     finally:
#         conn.close()
# if __name__ == "__main__":
#     main()

# df = DataFrame(np.random.randn(9,4), columns=['가격1','가격2','가격3','가격4'])
# print(df)
# print(df.mean(axis=0))

# from pandas import DataFrame
# data = {"a": [80, 90, 70, 30], "b": [90, 70, 60, 40], "c": [90, 60, 80, 70]}
# df = pd.DataFrame(data)
# df.columns = ['국어','영어','수학']
# print(df['수학'])
# print(df['수학'].std())
# print(df.drop(['수학'],axis=1))

import matplotlib.pyplot as plt
# data = np.random.randn(1000)
# print(data)
# plt.hist(data,bins=20,alpha=0.7)
# plt.title("good")
# plt.show()

pd.options.display.float_format = '{:.0f}'.format
df = pd.read_csv('sales_data.csv')
print(df.pivot_table(index='날짜',columns='제품',values='판매수량'))