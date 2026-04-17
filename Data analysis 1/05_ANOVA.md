# 분산분석, ANOVA

## 1. 분산분석(ANOVA) 개요

분산분석(ANalysis Of Variance, ANOVA)은 **세 개 이상의 모집단(집단) 간에 평균 차이가 있는지**를 검정하는 방법이다.
* 두 집단 비교(t-test)를 세 번, 네 번 반복하면 제1종 오류(귀무가설이 참인데 기각할 확률)가 기하급수적으로 증가하는 문제가 발생하므로, 이를 해결하기 위해 Fisher가 고안했다.
* 전체 분산을 '요인에 의한 집단 간 분산(Between-variance)'과 '우연에 의한 집단 내 분산(Within-variance)'으로 나누어, **집단 간 분산이 집단 내 분산보다 통계적으로 의미 있게 큰지(F-통계량)**를 검정한다.

### 선행 조건
1. **독립성**: 각 집단의 표본은 서로 독립적이어야 한다.
2. **정규성**: 각 집단의 표본은 정규분포를 따라야 한다. (`scipy.stats.shapiro`)
    * 정규성 위배 시: `scipy.stats.kruskal` (Kruskal-Wallis 비모수 검정) 사용.
3. **등분산성**: 각 집단의 분산은 동일해야 한다. (`scipy.stats.levene` 또는 `bartlett`)
    * 등분산성 위배 시: `pingouin.welch_anova` (Welch's ANOVA) 사용.

## 2. 실습 1: 편의점 3개 지역 알바생 급여 평균 차이 검정
* **귀무가설 ($H_0$)**: 3개 지역 알바생의 급여 평균에는 차이가 없다.
* **대립가설 ($H_1$)**: 3개 지역 알바생의 급여 평균에는 차이가 있다. (적어도 한 그룹은 다르다.)

```python
import pandas as pd
import numpy as np
import scipy.stats as stats
import urllib.request
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# 데이터 로드 (형태: [급여, 그룹번호])
uri = "[https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/group3.txt](https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/group3.txt)"
data = np.genfromtxt(urllib.request.urlopen(uri), delimiter=",")

# 세 그룹 분리
gr1 = data[data[:, 1] == 1, 0]
gr2 = data[data[:, 1] == 2, 0]
gr3 = data[data[:, 1] == 3, 0]

# 1. 정규성 및 등분산성 검정 (코드 원본 참조: 모두 만족함)
# shapiro, levene 테스트 통과

# 2. 일원 분산 분석 (ANOVA) 수행
# 방법 A: f_oneway 함수 사용 (가장 간단)
f_stats, p_val = stats.f_oneway(gr1, gr2, gr3)
print(f"F-통계량: {f_stats:.4f}, p-value: {p_val:.4f}")

# 방법 B: ols 모델 생성 후 anova_lm 적용
df = pd.DataFrame(data=data, columns=['pay', 'group'])
l_m = ols('pay ~ C(group)', data=df).fit() # C()는 범주형 변수임을 명시
print(anova_lm(l_m, typ=1))

# [해석] p-value(0.043) < 유의수준(0.05) 이므로 귀무가설 기각. 급여 평균에 차이가 있다.

# 3. 사후 검정 (Tukey HSD)
# ANOVA는 '어느 그룹이 다른지'는 알려주지 않으므로 사후 검정이 반드시 필요하다.
tukResult = pairwise_tukeyhsd(endog=df.pay, groups=df.group)
print(tukResult)
# reject가 True로 나오는 그룹 쌍(Pair)이 통계적으로 유의미한 차이가 있는 그룹이다.
```


## 3. 실습 2: 최고온도에 따른 음식점 매출액 차이 검정
온도 데이터를 3구간(추움, 보통, 더움)으로 범주화(Binning)한 후 분산분석을 수행한다.
이 예제는 **등분산성을 만족하지 않아 Welch's ANOVA를 적용**해야 하는 케이스다.

```python
import numpy as np
import pandas as pd
import scipy.stats as stats
from pingouin import welch_anova

# (데이터 병합 및 전처리 코드는 원본 참조)

# 온도를 3구간 범주형 데이터로 분리
data['ta_gubun'] = pd.cut(data.maxTa, bins=[-5, 8, 24, 37], labels=[0, 1, 2])

x1 = np.array(data[data.ta_gubun == 0].AMT)
x2 = np.array(data[data.ta_gubun == 1].AMT)
x3 = np.array(data[data.ta_gubun == 2].AMT)

# 정규성 및 등분산성 검정
print("정규성 만족 여부:", stats.shapiro(x1).pvalue > 0.05, stats.shapiro(x2).pvalue > 0.05, stats.shapiro(x3).pvalue > 0.05)
print("등분산성 p-value:", stats.levene(x1, x2, x3).pvalue) 

# 등분산성 p-value(0.039) < 0.05 이므로 등분산성을 위배함.
# 따라서 기본 f_oneway 대신 welch_anova를 사용해야 한다.
print(welch_anova(dv="AMT", between='ta_gubun', data=data))
# [해석] Welch ANOVA 결과 p-value(0.379) > 0.05 이므로 귀무가설 채택. 온도에 따른 매출액 평균 차이는 없다.
```


## 4. 실전 연습문제 풀이

### 1) 빵 튀김용 기름 4종류 흡수량 차이 검정
* **결측치 대치**: 평균값으로 대치 (`fillna`)
* **정규성/등분산성**: 모두 만족 (`shapiro`, `levene` p > 0.05)
* **ANOVA 수행**: `stats.f_oneway` 사용
```python
# (전처리 생략)
print("ANOVA p-value:", stats.f_oneway(g1, g2, g3, g4).pvalue)
# 결과: p(0.848) > 0.05. 귀무가설 채택 (기름 종류에 따른 흡수량 평균 차이 없음)
```

### 2) DB 연동: 4개 부서 연봉 평균 차이 검정 (정규성 위배 시 비모수 검정)
* **귀무가설**: 4개 부서에 따른 연봉 평균은 차이가 없다.
* **정규성 검정**: 총무부 데이터의 p-value(0.026) < 0.05 이므로 정규성 조건을 위배함.
* **비모수 검정 (Kruskal-Wallis)**: 3개 이상의 집단 비교에서 정규성을 위배했으므로 ANOVA 대신 Kruskal 검정을 수행한다.

```python
import pymysql
import pandas as pd
import scipy.stats as stats

# (DB 연동 및 데이터 분리 코드 생략)

# 정규성 위배 확인 (총무부)
# print(stats.shapiro(gc).pvalue) -> 0.026

# Kruskal-Wallis 비모수 검정 수행
print("Kruskal 검정 p-value:", stats.kruskal(gc, gy, gj, gg).pvalue)
# 결과: p(0.787) > 0.05. 귀무가설 채택 (부서에 따른 연봉 평균 차이는 통계적으로 유의미하지 않음)
```
