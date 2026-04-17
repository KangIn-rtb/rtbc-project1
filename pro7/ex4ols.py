# 최소 제곱해를 선형 행렬 방정식으로 얻기
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib

x = np.array([0,1,2,3])
y = np.array([-1,0.2,0.5,2.1])
plt.scatter(x,y)
plt.show()

A = np.vstack([x,np.ones(len(x))]).T
print(A)

# 본래 데이터를 직선으로 표현하기 위해 선형 대수학을 이용
import numpy.linalg as lin
w, b = lin.lstsq(A, y)[0] # 최소제곱법 연산(내부적으로 편미분 사용)
print(w,' ',b)
# 회귀식 y^ = 0.96 * x + -0.9899999999999998
print()
print(0.96 * 0 + -0.9899999999999998) # 실제값 -1 예측값 -0.9899  
print(0.96 * 1 + -0.9899999999999998) #                 -0.02999
print(0.96 * 2 + -0.9899999999999998) #                 0.9300000
print(0.96 * 3 + -0.9899999999999998) #                 1.89000


plt.scatter(x,y,marker='o',label="실제값")
plt.plot(x,w * x + b,'r',label="실제값")
plt.show()

x = 1.23456
yhat = w * x + b
print(yhat)

x = 7.654321
yhat = w * x + b
print(yhat)