import numpy as np
x=np.array([[1,2],[3,4]], dtype=np.float32)
y = np.arange(5,9).reshape((2,2))
y = y.astype(np.float32)
print(y, ' ', y.dtype)

print(x+y)
print(np.add(x,y))

# dot은 numpy 모듈의 함수나 배열 객체의 인스턴트 메소드로 사용 가능
v = np.array([9,10])
w = np.array([11,12])
print(np.multiply(v,w))
# 벡터 내적 : 행렬곱
print(v.dot(w))
print(np.dot(v,w))

# 벡터의 내적은 데이터들의 직선중 최적의 직선을 판단하는 근거가 되는건가? 
# -> 내적값 / 두 벡터의 스칼라 곱셈값 = cos@ => 이용해 @ 값 구해 각도 꺼내기


print(np.dot(x,v))

a = np.array([1,0])
b = np.array([1,1])
print(np.dot(a,b))
print(np.dot(a,b)/(1*(2**0.5)))
print()
print()
# 배열계산 함수
print(x)
print(np.mean(x),' ',np.var(x))
print(np.max(x),' ',np.min(x))
print(np.argmax(x),' ',np.argmin(x))
print(np.cumsum(x))
print(np.cumprod(x))

print()
name = np.array(['tom', 'jame','tom', 'oscar'])
name2 = np.array(['tom', 'page','john'])
print(np.unique(name))
print(np.intersect1d(name,name2)) # 교집합
print(np.union1d(name,name2)) # 합집합

print(x.T)
print()
# Broadcasting : 크기가 다른 배열 간의 연산 - 작은 배열을 여러 번 반복해 큰 배열과 연산
x = np.arange(1,10).reshape(3,3)
y = np.array([1, 0, 1])
print(x + y)
np.savetxt("my.txt",x)  # 값을 문서로 출력