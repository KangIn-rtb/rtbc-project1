# 독립 표본 t-검정, Two-Sample t-test

## 1. 독립 표본 t-검정 개요
서로 다른 두 독립된 집단(표본)의 평균이 통계적으로 유의미한 차이가 있는지를 검정하는 방법이다.
* 독립변수: 범주형 (2개의 집단)
* 종속변수: 연속형 (측정값)

### 선행 조건 (매우 중요)
1. **정규성 (Normality)**: 두 집단 모두 정규분포를 따라야 한다. (`scipy.stats.shapiro` 사용)
    * 표본 수가 30개 이상이면 중심극한정리에 의해 정규성을 따른다고 가정할 수 있다.
    * 정규성을 만족하지 못하면 비모수 검정인 **Mann-Whitney U test** (`scipy.stats.mannwhitneyu`)를 사용해야 한다.
2. **등분산성 (Homoscedasticity)**: 두 집단의 분산이 동일해야 한다.
    * `scipy.stats.levene` (일반적으로 많이 쓰임) 또는 `bartlett` (정규분포일 때만 쓰임) 검정을 통해 확인한다.
    * 등분산성을 만족하면 t-test 함수에서 `equal_var=True`를, 만족하지 않으면 `equal_var=False` (Welch's t-test)를 적용한다.


## 2. 실습 1: 남녀 시험 평균 점수 차이 검정 (기본)
* **귀무가설 ($H_0$)**: 남녀 그룹 간의 시험 점수 평균에는 차이가 없다.
* **대립가설 ($H_1$)**: 남녀 그룹 간의 시험 점수 평균에는 차이가 있다.

```python
from scipy import stats
import numpy as np

male = [75, 85, 100, 72.5]
female = [63.2, 52, 100, 70, 76]
print("남성 평균:", np.mean(male), "여성 평균:", np.mean(female))

# 정규성 검정 (데이터가 작으므로 확인 필요)
print("남성 정규성:", stats.shapiro(male))
print("여성 정규성:", stats.shapiro(female))

# 등분산을 가정(equal_var=True)하고 독립 표본 t-검정 수행
two_sample = stats.ttest_ind(male, female, equal_var=True)
tv, pv = two_sample
print(f"t-통계량: {tv:.4f}, p-value: {pv:.4f}")

# [해석] p-value가 0.05보다 크면 귀무가설 채택 (평균 차이가 우연히 발생했다고 봄)
```


## 3. 실습 2: 두 가지 교육 방법(method)에 따른 점수 차이 검정 (결측치 처리 및 등분산성 확인)
결측치(NA)를 평균값으로 대치하고, 정규성 및 등분산성 검정을 완벽하게 수행한 뒤 t-검정을 진행하는 정석적인 과정이다.

```python
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 로드
data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/two_sample.csv")

# method 1과 2로 데이터 분리
m1 = data[data['method'] == 1]
m2 = data[data['method'] == 2]

sco1 = m1['score']
sco2 = m2['score']

# 결측치(NA)를 해당 그룹의 평균으로 대체 (Imputation)
sco2 = sco2.fillna(sco2.mean()) 

# 1. 정규성 검정
print("방법1 정규성:", stats.shapiro(sco1).pvalue) # 0.367 (정규성 만족)
print("방법2 정규성:", stats.shapiro(sco2).pvalue) # 0.671 (정규성 만족)

sns.histplot(sco1, kde=True, color='red', label='Method 1')
sns.histplot(sco2, kde=True, color='blue', label='Method 2')
plt.legend()
plt.show()

# 2. 등분산성 검정 (Levene's test)
from scipy.stats import levene
print("등분산성 p-value:", levene(sco1, sco2).pvalue) 
# 결과: 0.456 > 0.05 이므로 두 집단의 분산은 같다고 본다. (등분산성 만족)

# 3. 독립 표본 t-검정 수행 (등분산 가정)
result = stats.ttest_ind(sco1, sco2, equal_var=True)
print("t-검정 결과:", result)

# [해석] p-value(0.845) > 유의수준(0.05) 이므로 귀무가설 채택. 
# 결론: 교육 방법에 따른 점수 차이는 통계적으로 유의미하지 않다.
```


## 4. 실습 3: 강수 여부에 따른 매출액 평균 차이 검정 (데이터 병합 및 박스플롯)
매출 데이터와 날씨 데이터를 날짜(YMD, tm)를 기준으로 병합(Merge)한 뒤, 비가 온 날과 안 온 날의 매출 차이를 분석한다.

* **귀무가설 ($H_0$)**: 강수 여부에 따라 매출액 평균에 차이가 없다.
* **대립가설 ($H_1$)**: 강수 여부에 따라 매출액 평균에 차이가 있다.

```python
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt 
import koreanize_matplotlib

# 1. 데이터 로드 및 전처리
sales_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/tsales.csv", dtype={'YMD':'object'})
wt_data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/tweather.csv")

# 날짜 포맷 통일 (2018-06-01 -> 20180601) 후 병합(Left Join)
wt_data.tm = wt_data.tm.map(lambda x: x.replace("-", ""))
frame = sales_data.merge(wt_data, how="left", left_on="YMD", right_on='tm')

# 필요한 컬럼만 추출 및 강수 여부 파생 변수 생성
data = frame.iloc[:, [0, 1, 7, 8]]
# 강수량(sumRn)이 0보다 크면 True(1), 아니면 False(0)로 변환
data['rain_yn'] = (data['sumRn'] > 0).astype(int) 

# 2. 비 온 날과 안 온 날 데이터 분리
sp = np.array(data.iloc[:, [1, 4]]) # [매출액, 강수여부(rain_yn)]
tg1 = sp[sp[:, 1] == 0, 0]  # 맑은 날(0) 매출 배열
tg2 = sp[sp[:, 1] == 1, 0]  # 비 온 날(1) 매출 배열

print("맑은 날 평균매출:", np.mean(tg1))
print("비 온 날 평균매출:", np.mean(tg2))

# 3. 박스플롯 시각화
plt.boxplot([tg1, tg2], meanline=True, showmeans=True, notch=True, labels=['맑은 날', '비 온 날'])
plt.title("강수 여부에 따른 매출 분포")
plt.ylabel("매출액")
plt.show()

# 4. 독립 표본 t-검정 수행
# (t-test 수행 코드는 원본에 생략되어 있으나 통상적으로 수행함)
result = stats.ttest_ind(tg1, tg2, equal_var=True)
print("t-검정 결과:", result)

# 5. 등분산성 검정
print("등분산 검정 p-value:", stats.levene(tg1, tg2).pvalue) 

# [해석] 만약 t-검정 결과의 p-value가 0.05보다 크다면 귀무가설을 채택한다.
# 매출액의 평균 차이는 비가 오고 안 오고의 영향이라기보다 우연한 편차일 가능성이 높다.
```