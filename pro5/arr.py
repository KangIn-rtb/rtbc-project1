import numpy as np
ss = [1, 2, 3, 'Tom', True]
ss2 = np.array(ss)
print(ss2, type(ss2)) # 배열은 안의 내용이 모두 문자열 -> 동일타입으로 바뀜
li = list(range(1,10))
li2 = list(map(lambda x:x*10,li))
li3 = np.array(li)
#배열은 요소의 주소가 다 같음
print(li3*3)


# .shape : 매트리스 행렬 확인

a = np.zeros((2,3))
print(a)
a = np.ones((2,3))
print(a)
a = np.eye(3)
print(a)
print(np.random.rand(5)) # 균둥분포
print(np.random.randn(5)) # 정규분포 

np.random.seed(0)
print(np.random.randn(2,3))

print()
print()
# 배열이더라도 파이썬 기조는 따라감
a = np.array([1,2,3])
b = a # 주소복사 
b[0] = 6
print(a, b)
c = np.copy(a)
c[0] = 1
print(a,c) 