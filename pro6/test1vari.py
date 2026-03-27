import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

np.random.seed(42)

target_mean = 60
std_dev_samall = 10
std_dev_large = 20

class1_raw = np.random.normal(loc=target_mean, scale=std_dev_samall,size=100)
class2_raw = np.random.normal(loc=target_mean, scale=std_dev_large,size=100)

print(class1_raw[:5])
#평균보정
class1_adj = class1_raw - np.mean(class1_raw) + target_mean
class2_adj = class2_raw - np.mean(class2_raw) + target_mean
# 정수화
class1 = np.clip(np.round(class1_adj),10,100).astype(int)
print(class1[:10])
class2 = np.clip(np.round(class2_adj),10,100).astype(int)
print(class2[:10])
# 통계 계산
mean1, mean2 = np.mean(class1), np.mean(class2)
std1, std2 = np.std(class1), np.std(class2)
var1, var2 = np.var(class1), np.var(class2)
print(mean1, mean2)
print(std1, std2)
print(var1, var2)

df = pd.DataFrame({
    'class':['1반']*100 + ['2반']*100,
    'score':np.concatenate([class1,class2])
})
print(df.head())
df.to_csv('test1vari.csv',index=False,encoding='utf-8-sig')
print()
# 시각화
x1 = np.random.normal(1,0.05,size=100)
x2 = np.random.normal(2,0.05,size=100)
plt.figure(figsize=(10,6))
plt.scatter(x1,class1,alpha=0.8,label=f"1반(평균={mean1:.2f}),표준편차(σ)={std1:.2f}")
plt.scatter(x2,class2,alpha=0.8,label=f"2반(평균={mean2:.2f}),표준편차(σ)={std2:.2f}")
plt.hlines(target_mean, 0.5,2.5,colors='red',linestyles='dashed',label=f"공통평균={target_mean}")
plt.xticks([1,2],['1반','2반'])
plt.ylabel("시험 점수")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))
plt.boxplot([class1, class2],label=['1반','2반'])
plt.grid()
plt.show()

plt.figure(figsize=(10,6))
plt.hist(class1, bins=15,alpha=0.6,label='1반',edgecolor='black')
plt.hist(class2, bins=15,alpha=0.6,label='2반',edgecolor='blue')
plt.axvline(target_mean, color='red',linestyle = 'dotted',label=f"공통평균={target_mean}")
plt.xlabel('시험 점수')
plt.ylabel('빈도')
plt.legend()
plt.tight_layout()
plt.show()

# 국어 선생님 입장
# 귀무 가설 : 두 반의 국어 점수의 표준편차는 차이가 없다.
# 누군가가 실험을 통해 데이터 수집 후 두 반의 점수에 통계 계산 후 새로운 주장
# 대립 가설 : 두 반의 국어 점수의 표준편차는 차이가 있다. 
# 두 집단의 평균의 차이를 비교하는 것 t test 3개이상은 아노바?
# 가설 검정 : t-test 를 통해 두 의견의 채택, 기각을 판단 할 수 있다. 
