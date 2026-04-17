# 공분산 / 상관계수
# 변수가 하나인 경우에는 분산은 거리와 관련이 있다. 
# 변수가 두 개인 경우에는 분산은 방향을 가진다. 

import numpy as np

# 공분산
print(np.cov(np.arange(1,6), np.arange(2,7)))
print(np.cov(np.arange(10,60,10), np.arange(20,70,10)))
print(np.cov(np.arange(100,600,100), np.arange(200,700,100)))
print(np.cov(np.arange(1,6), (3,3,3,3,3)))
print(np.cov(np.arange(1,6), np.arange(6,1,-1)))

print()
x = [8,3,6,6,9,4,3,9,3,4]
print(np.mean(x))
print(np.var(x))
y = [6,2,4,6,9,5,1,8,4,5]
print(np.mean(y))
print(np.var(y))

import matplotlib.pyplot as plt
# plt.plot(x, y, 'o')
# plt.show()
print(np.cov(x,y))
print(np.cov(x,y)[0,1])
x2 = list(map(lambda x:x*10,x))
y2 = list(map(lambda x:x*10,y))
print(np.cov(x2,y2))
# plt.plot(x2,y2,'o')
# plt.show()
print()
# 두 데이터의 단위에 따라 패턴이 일치할지라도 공분산의 크기가 달라지므로 절대적 크기 판단이 어려움
# 공분산을 표준화해서 -1에서 1 사이의 범위로 만든 것이 상관계수(r)이다.
print(np.corrcoef(x,y)) # 피어슨 상관계수
print(np.corrcoef(x,y)[0,1])
print(np.corrcoef(x2,y2)[0,1])
print()
m = [-3,-2,-1,0,1,2,3]
n = [9,4,1,0,1,4,9]
print(np.corrcoef(m,n)[0,1])
plt.plot(m,n,'o')
plt.show()