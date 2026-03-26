# 통계량 : 데이터의 특징을 하나의 숫자로 요약한 것
# 표본 데이터를 추출해 전체 데이터를 짐작 가능
# 평균, 분산, 표준편차
import numpy

A = list(map(int,input().split()))

avg = sum(A) / len(A)
s = 0
for i in A:
    s += (i-avg)**2
bun = (s)/len(A)
pyo = bun**0.5

print(f"pyo:{pyo:.2f} s:{s} bun:{bun} avg:{avg}")    
print(f"평균:{numpy.average(A)} 평균:{numpy.mean(A)} 분산:{numpy.var(A)} 표준편차:{numpy.std(A)}")