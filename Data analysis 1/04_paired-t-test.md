# 대응표본 t-검정 및 종합 실습

## 1. 대응표본 t-검정 (Paired Sample t-test) 개요

대응표본 t-검정(동일집단 표본 t-검정)은 **하나의 동일한 집단**에 대해 특정 처리(사건, 교육, 투약 등)를 하기 **전과 후**의 평균 차이가 통계적으로 유의미한지 분석하는 검정 방법이다.
* 동일한 관찰 대상을 1:1로 대응시켜(Pair) 전/후의 '차이(Difference)'를 검정한다.
* 두 개의 독립된 집단을 비교하는 것이 아니므로, **등분산성 가정(분산이 같아야 한다는 조건)을 할 필요가 없다.**
* 단, 전후 데이터의 '차이값'이 정규분포를 따른다는 정규성 가정은 필요하다.

수식으로는 다음과 같이 표현된다. ($d$는 전후의 차이)
$$t = \frac{\bar{d}}{s_d / \sqrt{n}}$$

## 2. 실습 1: 특강 전후의 시험 점수 차이 검정
* **귀무가설 ($H_0$)**: 특강 전후의 시험 점수에는 차이가 없다.
* **대립가설 ($H_1$)**: 특강 전후의 시험 점수에는 차이가 있다.

```python
import numpy as np
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
# 특강 전(x1)과 후(x2)의 가상 데이터 생성
x1 = np.random.normal(75, 10, 100)
x2 = np.random.normal(80, 10, 100)

# 1. 정규성 확인 (Shapiro-Wilk)
print("특강 전 정규성:", stats.shapiro(x1).pvalue) 
print("특강 후 정규성:", stats.shapiro(x2).pvalue) 

# 시각화를 통한 분포 확인
sns.displot(x1, kde=True, color='blue', label='Before')
sns.displot(x2, kde=True, color='red', label='After')
plt.legend()
plt.show()

# 2. 대응표본 t-검정 수행 (ttest_rel)
result = stats.ttest_rel(x1, x2)
print("대응표본 t-검정 결과:", result)

# [해석] p-value(0.0001) < 유의수준(0.05) 이므로 귀무가설 기각.
# 결론: 특강이 시험 점수에 유의미한 영향을 주었다고 판단한다.
```


## 3. 실습 2: 수술 전후 몸무게 변화 검정
* **귀무가설 ($H_0$)**: 수술 전후 몸무게의 변화는 없다.
* **대립가설 ($H_1$)**: 수술 전후 몸무게의 변화는 있다.

```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import koreanize_matplotlib

baseline = [67.2, 67.4, 71.5, 77.6, 86.0, 89.1, 59.5, 81.9, 105.5]
follow_up = [62.4, 64.6, 70.4, 62.6, 80.1, 73.2, 58.2, 71.0, 101.0]

# 평균 차이 확인
print("몸무게 평균 차이:", np.mean(baseline) - np.mean(follow_up)) 

# 막대 그래프 시각화 비교
plt.bar(['수술 전 (Baseline)', '수술 후 (Follow-up)'], [np.mean(baseline), np.mean(follow_up)], color=['gray', 'skyblue'])
plt.ylabel('몸무게 (평균)')
plt.title('수술 전후 평균 몸무게 비교')
plt.show()

# (통계 검정 수행 시)
print("검정 결과:", stats.ttest_rel(baseline, follow_up))
```


## 4. 종합 연습문제 풀이 (독립표본, 대응표본, 비모수 검정)

### 문제 1. 포장지 색상(블루 vs 레드)에 따른 매출액 차이 (독립표본)
* **귀무가설**: 포장지 색상에 따른 제품의 매출액 차이가 없다.
```python
blue = [70, 68, 82, 78, 72, 68, 67, 68, 88, 60, 80]
red = [60, 65, 55, 58, 67, 59, 61, 68, 77, 66, 66]

print("Blue 정규성:", stats.shapiro(blue).pvalue) # 0.51 (만족)
print("Red 정규성:", stats.shapiro(red).pvalue)   # 0.53 (만족)

# (참고) 원본 코드에는 ttest_rel(대응표본)이 쓰였으나, 문맥상 완전히 다른 매장/그룹의 비교라면 ttest_ind(독립표본)가 적절하다. 
# 여기서는 원본에 따라 대응표본으로 계산된 결과를 보여준다.
print("검정 결과:", stats.ttest_rel(blue, red)) 
# [해석] p-value(0.008) < 0.05 이므로 귀무가설 기각. 매출액 차이가 존재한다.
```

### 문제 2. 남녀 간 콜레스테롤 양 차이 (정규성 검정에 따른 분기 처리)
* **귀무가설**: 남녀 간 콜레스테롤 양에 차이가 없다.
```python
# 샘플 추출
men_sample = np.random.choice(men_pop, 15, replace=False)
women_sample = np.random.choice(women_pop, 15, replace=False)

shapiro_men = stats.shapiro(men_sample)
shapiro_women = stats.shapiro(women_sample)

# 정규성 만족 여부에 따라 모수 검정(t-test)과 비모수 검정(Mann-Whitney) 자동 분기
if shapiro_men.pvalue > 0.05 and shapiro_women.pvalue > 0.05:
    # 정규성 만족 시 등분산성 확인 후 t-test
    levene = stats.levene(men_sample, women_sample)
    is_equal = levene.pvalue > 0.05
    t_stat, p_val = stats.ttest_ind(men_sample, women_sample, equal_var=is_equal)
    test_name = "독립표본 t-검정"
else:
    # 정규성 불만족 시 비모수 검정
    u_stat, p_val = stats.mannwhitneyu(men_sample, women_sample, alternative='two-sided')
    test_name = "Mann-Whitney U 검정"

print(f"분석 방법: {test_name}, p-value: {p_val:.4f}")
```

### 문제 3. DB 연동: 부서별(총무부 vs 영업부) 연봉 평균 차이 (결측치 처리 & 비모수)
* **귀무가설**: 두 부서 간 연봉 평균에 차이가 없다.
```python
# (DB 연결 및 데이터 분리 코드 생략 - 위 원본 코드 참조)
# 결측치는 해당 부서의 평균으로 대치 (Transform 사용)

print("총무부 정규성:", stats.shapiro(total_dept).pvalue) # 0.026 (정규성 불만족)
print("영업부 정규성:", stats.shapiro(sales_dept).pvalue) # 0.064 (정규성 만족)

# 한 집단이라도 정규성을 만족하지 못하므로 비모수 검정(Mann-Whitney) 수행
result = stats.mannwhitneyu(total_dept, sales_dept, alternative='two-sided')
print("비모수 검정 결과:", result)
# [해석] p-value(0.47) > 0.05 이므로 귀무가설 채택. 연봉 평균에 차이가 없다고 본다.
```

### 문제 4. 중간고사 vs 기말고사 성적 차이 (대응표본)
* **귀무가설**: 중간고사와 기말고사 성적에는 차이가 없다.
```python
mid = np.array([80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80])
fin = np.array([90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95])

# 전후 차이값(d)에 대한 정규성 검정
print("차이값 정규성:", stats.shapiro(fin - mid).pvalue) # 0.301 (정규성 만족)

# 대응표본 t-검정
print("대응표본 t-검정 결과:", stats.ttest_rel(mid, fin))
# [해석] p-value(0.023) < 0.05 이므로 귀무가설 기각. 성적의 차이가 통계적으로 유의미하다.
```