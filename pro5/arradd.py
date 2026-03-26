import numpy as np

aa = np.eye(3)
print(aa)
bb = np.c_[aa,aa[2]] # 2열과 동일한 열 추가
print(bb)
cc = np.r_[aa,[aa[2]]] # 2행과 동일한 행 추가
print(cc)

print()

a = np.array([1,2,3])
b = np.append(a,[4,5],axis=0) # 행기준
print(b)
c = np.insert(a,1,[6,7])
print(c)
d = np.delete(a,1)
print(d)

aa = np.arange(1,10).reshape(3,3)
print(np.insert(aa,1,99)) # axis = 0,1 없으면 차원을 한차원 내린다.

print()
# 조건 연산 where(조건, 참, 거짓)
x = np.array([1,2,3])
y = np.array([4,5,6])
conditionData = np.array([True, False, True])
result = np.where(conditionData,x,y) # [1,5,3] 
print(result)
#배열 결합 concatenate
#배열 분할 split
# 배열 좌우 분할 hsplit vsplit
# 표본 추출 sampling 랜덤 추출
li = np.arange(1,8)
    # 복원 
for _ in range(5):
    print(li[np.random.randint(0,len(li)-1)],end=' ')
print()
    # 비복원    
import random
print(random.sample(li.tolist(),5)) # sample은 대상이 리스트 여야함
print()
print((np.random.choice(range(1,46),6))) # 복원
print((np.random.choice(range(1,46),6, replace=False))) # 비복원

