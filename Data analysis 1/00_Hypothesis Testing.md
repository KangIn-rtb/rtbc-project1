# 가설 검정과 카이제곱 분석

## 1. 가설 검정 (Hypothesis Testing) 기초와 데이터 시각화

통계 분석에서 가설 검정은 표본 데이터를 통해 모집단에 대한 주장의 타당성을 검증하는 과정이다. 두 집단 간의 평균 차이를 비교할 때는 주로 **t-검정(t-test)**을 사용하며, 3개 이상의 집단은 분산분석(ANOVA)을 사용한다.

* **귀무가설 ($H_0$)**: '차이가 없다', '효과가 없다'를 기본으로 설정하는 가설이다. (예: 두 반의 국어 점수 분포는 차이가 없다.)
* **대립가설 ($H_1$)**: 입증하고자 하는 새로운 주장이다. (예: 두 반의 국어 점수 분포는 차이가 있다.)
* **1종 오류 ($\alpha$)**: 귀무가설이 참인데도 이를 잘못 기각할 확률이다. (보통 유의수준 $\alpha=0.05$로 설정한다.)
* **p-value**: 표본 데이터가 귀무가설을 지지하는 정도를 나타내는 확률값이다.
  * **판정 기준**: `p-value < 유의수준(0.05)` 이면 귀무가설을 기각하고 대립가설을 채택한다.

### 두 집단의 데이터 생성 및 시각화 실습
평균은 같으나 표준편차가 다른 두 학급의 점수 데이터를 생성하고, 산점도, 박스플롯, 히스토그램으로 분포의 차이를 확인하는 코드이다.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

np.random.seed(42)

# 1. 두 집단의 데이터 생성
target_mean = 60
std_dev_small = 10
std_dev_large = 20

# 정규분포를 따르는 난수 생성
class1_raw = np.random.normal(loc=target_mean, scale=std_dev_small, size=100)
class2_raw = np.random.normal(loc=target_mean, scale=std_dev_large, size=100)

# 평균 보정 및 정수화 (10점~100점 사이로 제한)
class1 = np.clip(np.round(class1_raw - np.mean(class1_raw) + target_mean), 10, 100).astype(int)
class2 = np.clip(np.round(class2_raw - np.mean(class2_raw) + target_mean), 10, 100).astype(int)

# 2. 통계량 확인
mean1, mean2 = np.mean(class1), np.mean(class2)
std1, std2 = np.std(class1), np.std(class2)
print(f"1반 평균: {mean1}, 2반 평균: {mean2}")
print(f"1반 표준편차: {std1:.2f}, 2반 표준편차: {std2:.2f}")

# 데이터를 DataFrame으로 합친 후 CSV 저장
df = pd.DataFrame({
    'class': ['1반'] * 100 + ['2반'] * 100,
    'score': np.concatenate([class1, class2])
})
df.to_csv('test1vari.csv', index=False, encoding='utf-8-sig')

# 3. 데이터 시각화
# 3-1. 산점도 (Scatter Plot)
x1 = np.random.normal(1, 0.05, size=100)
x2 = np.random.normal(2, 0.05, size=100)
plt.figure(figsize=(10, 6))
plt.scatter(x1, class1, alpha=0.8, label=f"1반(σ={std1:.2f})")
plt.scatter(x2, class2, alpha=0.8, label=f"2반(σ={std2:.2f})")
plt.hlines(target_mean, 0.5, 2.5, colors='red', linestyles='dashed', label="공통평균")
plt.xticks([1, 2], ['1반', '2반'])
plt.ylabel("시험 점수")
plt.legend()
plt.grid()
plt.show()

# 3-2. 박스플롯 (Boxplot)
plt.figure(figsize=(8, 5))
plt.boxplot([class1, class2], labels=['1반', '2반'])
plt.grid()
plt.show()

# 3-3. 히스토그램 (Histogram)
plt.figure(figsize=(10, 6))
plt.hist(class1, bins=15, alpha=0.6, label='1반', edgecolor='black')
plt.hist(class2, bins=15, alpha=0.6, label='2반', edgecolor='blue')
plt.axvline(target_mean, color='red', linestyle='dotted', label="공통평균")
plt.xlabel('시험 점수')
plt.ylabel('빈도')
plt.legend()
plt.show()
```


## 2. 교차 분석 (Chi-Square Test of Independence)
교차 분석(카이제곱 검정)은 명목형(범주형) 두 변수 간에 상관관계(독립성)가 있는지 검증하는 기법이다. (예: 공부 여부와 합격 여부가 서로 관계가 있는가?)
* **식**: $\chi^2 = \sum \frac{(관측값 - 기대값)^2}{기대값}$

```python
import pandas as pd
import scipy.stats as stats

# 가상 데이터 불러오기
data = pd.read_csv('pass_cross.csv', encoding="euc-kr")

# 가설 설정
# 귀무가설(H0): 벼락치기 공부 여부와 합격 여부는 관계가 없다. (독립적이다)
# 대립가설(H1): 벼락치기 공부 여부와 합격 여부는 관계가 있다.

# 1. 교차표(빈도표) 생성
ctab = pd.crosstab(index=data['공부안함'], columns=data['불합격'], margins=True)
ctab.columns = ['합격', '불합격', '행합']
ctab.index = ['공부함', '공부안함', '열합']
print("교차표:\n", ctab)

# 2. 수동으로 기대도수 및 카이제곱 통계량 계산 예시
# 기대도수 = (각 행의 주변합 * 각 열의 주변합) / 총합
# 직접 계산한 결과 chi2 값은 약 3.0이 나온다.
print("수동계산:", (18-15)**2/15 + (7-10)**2/10 + (12-15)**2/15 + (13-10)**2/10)

# 3. 라이브러리를 이용한 p-value 계산 (검정 방법)
chi2, p, dof, expected = stats.chi2_contingency(ctab)
print(f"카이제곱 통계량: {chi2:.2f}, p-value: {p:.4f}") 
# 결과: p-value(0.5578) > 유의수준(0.05) 이므로 귀무가설 채택. 즉, 관계가 없다고 판단한다.
```


## 3. 적합도 검정 (일원 카이제곱 검정)
하나의 범주형 변수에 대해 관측된 빈도가 기존에 기대했던 빈도(이론적 분포)와 동일한지 확인하는 검정이다.

```python
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import koreanize_matplotlib
import numpy as np

# 가설 설정
# 귀무가설(H0): 5개 스포츠 음료에 대한 선호도 차이가 없다. (관측치 = 기대치)
# 대립가설(H1): 5개 스포츠 음료에 대한 선호도 차이가 있다.

url = "https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/drinkdata.csv"
data = pd.read_csv(url)

# 1. 기대빈도 계산 (총합을 음료 종류 수(5)로 나눈 값)
exp = [data['관측도수'].sum() / len(data)] * len(data)
print("기대빈도:", exp) # 모두 50.8로 동일하게 설정됨

# 2. 일원 카이제곱 검정 수행
stat, p = stats.chisquare(f_obs=data['관측도수'], f_exp=exp)
print(f"통계량: {stat:.2f}, p-value: {p:.5f}")

# 판정: p-value(0.0004) < 유의수준(0.05) 이므로 귀무가설 기각. 
# 즉, 스포츠 음료 간에 통계적으로 유의미한 선호도 차이가 존재한다.

# 3. 관측도수 vs 기대도수 시각화 비교
total = data['관측도수'].sum()
expected = [total / len(data)] * len(data)
x = np.arange(len(data))
width = 0.35 

plt.figure(figsize=(10, 5))
plt.bar(x - width/2, data['관측도수'], width=width, label='관측도수')
plt.bar(x + width/2, expected, width=width, label='기대도수 (차이 없음 가정)', alpha=0.6)
plt.xticks(x, data['음료종류'])
plt.xlabel('음료종류')
plt.ylabel('도수')
plt.title('스포츠 음료 선호도: 관측치 vs 기대치')
plt.legend()
plt.show()
```