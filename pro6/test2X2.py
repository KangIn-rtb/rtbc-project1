# 교차 분석 (카이제곱, 카이스퀘어) 가설 검정
# 교차빈도에 대한 통계적 유의성을 검증해 주는 분석기법
# 분산이 퍼져 있는 모습을 분포로 만든 것이 카이제곱 분포
# X² = ∑(관측값 - 기대값)² / 기대값
# 적합도 : 일원 카이제곱 검정
# 독립성, 동질성 검정 : 일원카이제곱검정

# 가설을 채택하는 두가지 방법
import pandas as pd
data = pd.read_csv('pass_cross.csv',encoding="euc-kr")
print(data.head())
print(data.shape)
print(data.shape[0])
print(data.shape[1])
print()
# 귀무가설(H0) : 벼락치기 공부하는 것과 합격여부는 관계가 없다. 
# 대립가설(H1) : 벼락치기 공부하는 것은 합격 여부와 관계가 있다. 
print(data[(data['공부함'] == 1) & (data['합격']==1)].shape[0])
print(data[(data['공부함'] == 1) & (data['불합격']==1)].shape[0])
ctab = pd.crosstab(index=data['공부안함'],columns=data['불합격'],margins=True)
ctab.columns = ['합격','불합격','행합']
ctab.index = ['공부함','공부안함','열합']
print(ctab)
# 기대도수 = (각행의 주변합) * (각열의 주변합) / 총합<전체표본수>
print((18-15)**2/15+(7-10)**2 / 10 + (12-15)**2/15+(13-10)**2 / 10)
# chi2 = 3.0
# df = 2-1 = 1
# 유의 수준 : 0.05
# 임계 값 : 3.84
# 판정 : 카이제곱 검정통계량 : 3 < 임계값 이므로 귀무 채택역 내에 있으므로 귀무가설 채택

# 검정방법2 : p-value 사용
import scipy.stats as stats
chi2,p,_,_ =  stats.chi2_contingency(ctab)
print(chi2,p) #3.0 / 0.5578254003710748
# 판정 유의 수준 0.05 < p:0.5578 이므로 귀무채택
# 두 개의 불 연속 변수 간의 상관관계를 측정, 관찰빈도가 통계적으로 유의한지 확인
