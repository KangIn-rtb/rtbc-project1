# 단일 표본 t-검정, One-Sample t-test

## 1. 단일 표본 t-검정 개요

단일 표본 t-검정(One-Sample t-test)은 **단일 모집단의 평균이 특정한 예상 값(기준값)과 통계적으로 차이가 있는지**를 확인하는 검정 방법이다.
* 독립변수: 범주형 (단일 집단)
* 종속변수: 연속형 (측정값)
* **선행 조건**: 표본 데이터는 **정규분포**를 따라야 한다. 데이터 개수가 30개 미만일 경우 `scipy.stats.shapiro`를 통해 정규성 검정을 먼저 수행해야 하며, 정규성을 만족하지 못하면 비모수 검정인 **윌콕슨 부호 순위 검정(`wilcoxon`)**을 대안으로 사용한다.


## 2. 실습 1: 남성 집단 평균 키 검정
* **귀무가설 ($H_0$)**: 해당 집단의 평균 키는 177cm이다.
* **대립가설 ($H_1$)**: 해당 집단의 평균 키는 177cm가 아니다.

```python
import numpy as np
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt

one_sample = [167.0, 182.7, 169.6, 176.8, 185.0]
print("표본 평균:", np.array(one_sample).mean()) # 176.22

# 단일 표본 t-검정 (popmean에 예상 기준값 입력)
result = stats.ttest_1samp(one_sample, popmean=177) 
print(result) # p-value = 0.835

# [해석] 유의수준 0.05 < p-value(0.835) 이므로 귀무가설 채택. 평균 키는 177cm라고 볼 수 있다.

# 165cm 기준 재검정
result2 = stats.ttest_1samp(one_sample, popmean=165)
print(result2) # p-value가 매우 작음. (귀무가설 기각)
```


## 3. 실습 2: 여아 신생아 몸무게 평균 검정 (정규성과 비모수 검정)
* **귀무가설 ($H_0$)**: 여아 신생아의 몸무게 평균은 2800g이다.
* **대립가설 ($H_1$)**: 여아 신생아의 몸무게 평균은 2800g이 아니다.

```python
import pandas as pd
import scipy.stats as stats
from scipy.stats import wilcoxon

data2 = pd.read_csv("[https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/babyboom.csv](https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/babyboom.csv)")
fdata = data2[data2.gender == 1] # 여아 데이터만 추출

print(f"표본 평균:{np.mean(fdata.weight):.2f}, 표본 크기:{len(fdata)}")

# 1. 정규성 검정 (Shapiro-Wilk)
print("정규성 검정:", stats.shapiro(fdata['weight'])) 
# 결과: p-value(0.017) < 0.05 이므로 정규성을 만족하지 못함.

# 2. 비모수 검정 (Wilcoxon Signed-Rank Test) 적용
# 정규성을 만족하지 못하므로 t-test 대신 wilcoxon 검정을 사용한다.
result3 = wilcoxon(fdata['weight'] - 2800)
print("비모수 검정 결과:", result3)

# [해석] 유의수준 0.05 > p-value(0.034) 이므로 귀무가설을 기각한다.
# 결론: 여아 신생아의 평균 몸무게는 2800g이 아니다.
```


## 4. 실전 연습문제

### 1) 백열전구 수명 검정
* **귀무가설 ($H_0$)**: 백열전구의 수명은 300시간이다.
```python
data = pd.Series([305, 280, 296, 313, 287, 240, 259, 266, 318, 280, 325, 295, 315, 278])
print("정규성 검정:", stats.shapiro(data)) # p=0.82 (정규성 만족)

result = stats.ttest_1samp(data, popmean=300) 
print("t-검정 결과:", result)
# [해석] p-value(0.14) > 0.05 이므로 귀무가설 채택. 수명은 300시간이라고 볼 수 있다.
```

### 2) 정부 발표 전국 평균 미용 요금 검정 (가격동향 엑셀 데이터)
* **귀무가설 ($H_0$)**: 전국 평균 미용 요금은 15,000원이다. (발표가 맞다)
* **대립가설 ($H_1$)**: 전국 평균 미용 요금은 15,000원이 아니다. (발표가 틀리다)

```python
import pandas as pd
import scipy.stats as stats

# 엑셀 파일 로드 (pip install xlrd 필요)
data3 = pd.read_excel('2026.02_data.xls')
data4 = data3.iloc[0, 2:] # 첫 번째 행의 지역 데이터만 슬라이싱
data4 = pd.to_numeric(data4, errors='coerce').dropna() # 숫자형 변환 및 결측치 제거

print('표본 평균 미용 요금:', data4.mean())
print('표본 크기:', len(data4))

# 1. 정규성 검정
print("정규성 검정:", stats.shapiro(data4))

# 2. One-Sample t-test
t_result3 = stats.ttest_1samp(data4, popmean=15000)
print("t-검정 결과:", t_result3)

# [해석] (코드 작성 중 끊긴 부분 완성)
# 만약 p-value가 0.05보다 크면 귀무가설을 채택하여 정부의 발표가 맞다고 판단한다.
# 반대로 p-value가 0.05보다 작으면 귀무가설을 기각하고, 실제 데이터와 정부 발표(15,000원) 간에는 차이가 있다고 결론 내린다.
```