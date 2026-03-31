# 파이썬 데이터 분석 (NumPy 심화 및 실전)

## 1. 통계 (Statistics) 기초
통계량은 데이터의 특징을 하나의 숫자로 요약한 것이다. 표본 데이터를 추출해 전체 데이터의 형태를 짐작할 수 있으며, 주로 평균, 분산, 표준편차 등을 활용한다.

```python
import numpy as np

A = list(map(int, input().split()))

# 1. 순수 파이썬 구현
avg = sum(A) / len(A)
s = 0
for i in A:
    s += (i - avg)**2
bun = s / len(A)
pyo = bun**0.5
print(f"파이썬 계산 -> 표준편차:{pyo:.2f} 편차제곱합:{s} 분산:{bun} 평균:{avg}")    

# 2. NumPy 내장 함수 활용
print(f"NumPy 계산 -> 평균:{np.average(A)} 평균:{np.mean(A)} 분산:{np.var(A)} 표준편차:{np.std(A)}")
```


## 2. 행렬 (Matrix)과 배열 기초
NumPy 배열(`ndarray`)은 내부 요소가 모두 동일한 데이터 타입으로 자동 형변환된다. 브로드캐스팅(Broadcasting)을 지원하며, 다양한 특수 행렬과 난수 생성을 지원한다.

```python
import numpy as np

# 데이터 타입 자동 통일 (문자열 포함 시 모두 문자열로 변환됨)
ss = [1, 2, 3, 'Tom', True]
ss2 = np.array(ss)
print(ss2, type(ss2)) 

# 특수 행렬 생성
a = np.zeros((2, 3)) # 영행렬
a = np.ones((2, 3))  # 일행렬
a = np.eye(3)        # 단위행렬 (대각선이 1)

# 난수 생성
print(np.random.rand(5))  # 균등분포
print(np.random.randn(5)) # 표준정규분포 

np.random.seed(0) # 시드 고정
print(np.random.randn(2, 3))

# 파이썬의 얕은 복사 / 깊은 복사
a = np.array([1, 2, 3])
b = a          # 주소 복사 (얕은 복사)
c = np.copy(a) # 값 복사 (깊은 복사)
```


## 3. 내적 (Dot Product) 및 배열 연산

배열 간의 사칙연산, 행렬곱(내적), 그리고 집합 연산(교집합, 합집합 등)을 수행할 수 있다.

### 행렬곱과 코사인 유사도 (Cosine Similarity)
벡터의 내적은 두 데이터 간의 유사도를 측정하거나 방향성을 판단하는 근거가 된다. 코사인 각도($\theta$)는 내적값을 두 벡터의 크기(Norm)의 곱으로 나누어 구할 수 있다.
수식: $\cos(\theta) = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \|\mathbf{b}\|}$

```python
import numpy as np

x = np.array([[1, 2], [3, 4]], dtype=np.float32)
y = np.arange(5, 9).reshape((2, 2)).astype(np.float32)

print(x + y)
print(np.add(x, y))

# 행렬곱 (내적 연산)
v = np.array([9, 10])
w = np.array([11, 12])

print(np.multiply(v, w)) # 요소별 단순 곱셈
print(v.dot(w))          # 벡터 내적 (행렬곱)
print(np.dot(v, w))

# 코사인 유사도 개념 적용
a = np.array([1, 0])
b = np.array([1, 1])
print(np.dot(a, b)) # 내적
print(np.dot(a, b) / (1 * (2**0.5))) # 코사인 값 (cos 45도)

# 통계 및 집계 함수
print(np.mean(x), np.var(x))
print(np.max(x), np.min(x))
print(np.argmax(x), np.argmin(x)) # 최댓값/최솟값의 '인덱스' 반환
print(np.cumsum(x))  # 누적 합
print(np.cumprod(x)) # 누적 곱

# 집합 연산
name = np.array(['tom', 'jame', 'tom', 'oscar'])
name2 = np.array(['tom', 'page', 'john'])
print(np.unique(name))             # 중복 제거
print(np.intersect1d(name, name2)) # 교집합
print(np.union1d(name, name2))     # 합집합

# 브로드캐스팅 (크기가 다른 배열 간 연산)
x = np.arange(1, 10).reshape(3, 3)
y = np.array([1, 0, 1])
print(x + y) # y 배열이 각 행마다 반복되어 더해진다.

# 텍스트 파일로 저장
np.savetxt("my.txt", x) 
```


## 4. 배열 제어 심화 (결합, 삽입, 추출)
NumPy 배열을 원하는 형태로 분할하거나 합치고, 조건에 따라 값을 변경(`where`)할 수 있다.

```python
import numpy as np

aa = np.eye(3)

# 1. 배열 결합 및 삽입
bb = np.c_[aa, aa[2]]   # 2열과 동일한 열을 추가
cc = np.r_[aa, [aa[2]]] # 2행과 동일한 행을 추가

a = np.array([1, 2, 3])
b = np.append(a, [4, 5], axis=0)
c = np.insert(a, 1, [6, 7]) # 인덱스 1 위치에 삽입
d = np.delete(a, 1)         # 인덱스 1 위치 삭제

# 2. 조건 연산 (where)
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
conditionData = np.array([True, False, True])
result = np.where(conditionData, x, y) # 조건이 참이면 x, 거짓이면 y의 값 추출 -> [1, 5, 3]

# 3. 표본 추출 (Sampling)
li = np.arange(1, 8)

import random
print(random.sample(li.tolist(), 5)) # random 모듈 (비복원)

print(np.random.choice(range(1, 46), 6)) # np.random 모듈 (복원 추출)
print(np.random.choice(range(1, 46), 6, replace=False)) # 비복원 추출
```


## 5. NumPy 실전 문제 풀이 (Exercises)

```python
import numpy as np

print("-" * 15, "문제 1", "-" * 15)
# 1) 5행 4열 정규분포 난수 배열의 각 행 단위 합계 및 최댓값
mun1 = np.random.randn(20).reshape(5, 4)
for i, row in enumerate(mun1):
    print(f"{i+1}행 합계: {np.sum(row)}, 최댓값: {np.max(row)}")


print("\n", "-" * 15, "문제 2-1", "-" * 15)
# 2-1) 6행 6열 배열 인덱싱
mun2_1 = np.arange(1, 37).reshape(6, 6) 
print("2번째 행 전체:", mun2_1[1, :]) 
print("5번째 열 전체:", mun2_1[:, 4])
print("15~29 구간 3x3 추출:\n", mun2_1[2:5, 2:5])


print("\n", "-" * 15, "문제 2-2", "-" * 15)
# 2-2) 6행 4열 배열 조건 채우기
mun2_2 = np.zeros((6, 4))
mun2_rand = np.random.randint(20, 100, 6)

for i in range(len(mun2_2)):
    mun2_2[i] = np.arange(mun2_rand[i], mun2_rand[i] + 4) # 시작값부터 1씩 증가

mun2_2[0] = np.array([1000] * 4) # 첫 행 수정
mun2_2[-1] = np.array([6000] * 4) # 마지막 행 수정
print(mun2_2)


print("\n", "-" * 15, "문제 3", "-" * 15)
# 3) 4행 5열 배열의 기술통계량
mun3 = np.random.randn(20).reshape(4, 5)
print('평균 :', np.mean(mun3), ' 합계 :', np.sum(mun3))
print('1사분위 수 :', np.percentile(mun3, 25))
print('3사분위 수 :', np.percentile(mun3, 75))


print("\n", "-" * 15, "문제 Q1 ~ Q4", "-" * 15)
# Q1. 브로드캐스팅 및 조건 연산
a = np.array([[1], [2], [3]])   
b = np.array([10, 20, 30])      
conc = a * b 
print("30 이상인 요소:", conc[conc <= 30])

# Q2. 다차원 배열 슬라이싱 및 재배열
mun5 = np.arange(12).reshape(3, 4)
print("1차원 평탄화:", mun5.reshape(-1))

# Q3. 3의 배수이면서 5의 배수가 아닌 값 제곱
mun6 = np.arange(1, 101)
condi2 = (mun6 % 3 == 0) & (mun6 % 5 != 0)
print("조건 추출 및 제곱:", mun6[condi2] ** 2)

# Q4. where를 이용한 조건별 값 변환
mun7 = np.array([15, 22, 8, 19, 31, 4])
print("10 이상 High/Low:", np.where(mun7 >= 10, 'High', 'Low'))
mun7_c = np.copy(np.where(mun7 >= 20, -1, mun7)) # 원본 유지, 20 이상 -1 변환
print("20 이상 -1 변환:", mun7_c)
```


## 6. 로그 변환 (Log Transformation)과 정규화

데이터 간 편차가 너무 크거나 값의 스케일 차이가 심할 때 로그 변환을 적용한다.
* 스케일 차이를 획기적으로 축소한다.
* 한쪽으로 크게 치우친(Skewed) 데이터를 정규분포 형태에 가깝게 다듬어준다.

```python
import numpy as np
np.set_printoptions(suppress=True, precision=6) # 지수 표현 억제 및 소수점 고정

def test():
    values = np.array([345, 34.5, 3.45, 0.345, 0.01, 0.1, 10, 100])
    
    log_values = np.log10(values) # 상용로그 (밑이 10)
    ln_values = np.log(values)    # 자연로그 (밑이 e)
    
    # Min-Max 정규화 (데이터를 0 ~ 1 사이로 변환)
    max_log = np.max(log_values)
    min_log = np.min(log_values)
    normalized = (log_values - min_log) / (max_log - min_log)
    print("정규화 결과 : ", normalized)

# 편차가 큰 데이터를 로그 스케일로 변환하고 역변환을 지원하는 클래스
class LogTrans:
    def __init__(self, offset: float = 1.0):
        self.offset = offset
        
    def translog(self, x: np.ndarray):
        # 0 이하의 값이 되지 않도록 offset(기본 1)을 더해 로그를 취함
        return np.log(x + self.offset)
        
    def inverse_trans(self, x_log: np.ndarray):
        # 역변환: 지수 함수(exp)를 취한 후 더했던 offset을 다시 뺌
        return np.exp(x_log) - self.offset

def main():
    test()
    data = np.array([0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000], dtype=float)
    
    log_trans = LogTrans(offset=1.0)
    data_log_scaled = log_trans.translog(data) # 로그 변환
    reversed_data = log_trans.inverse_trans(data_log_scaled) # 역변환 (원상복구)
    
    print(f"원본 : {data}")
    print(f"로그 변환 : {data_log_scaled}")
    print(f"역변환 : {reversed_data}")

if __name__ == "__main__":
    main()
```