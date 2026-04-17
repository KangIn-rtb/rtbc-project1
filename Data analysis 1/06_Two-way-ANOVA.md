# 이원 분산분석 및 독립성 검정

## 1. 이원 분산분석 (Two-Way ANOVA) 개요

이원 분산분석은 **독립변수(요인)가 2개**일 때 종속변수의 평균에 어떤 영향을 미치는지 분석하는 방법이다. 일원 분산분석과 달리 두 요인이 결합하여 나타나는 시너지 효과인 **교호작용(상호작용 효과)**을 추가로 검정하는 것이 핵심이다.

* **주효과 (Main Effect)**: 각 독립변수(요인 A, 요인 B)가 각각 종속변수에 미치는 독립적인 영향이다.
* **상호작용효과/교호작용 (Interaction Effect)**: 한 요인의 영향력이 다른 요인의 수준에 따라 달라지는 현상이다. 

### 실습: 태아 수와 관측자 수가 머리둘레 평균에 미치는 영향
* **주효과 가설**
    * 귀무가설: 태아 수(또는 관측자 수)에 따라 머리둘레 평균에 차이가 없다.
* **교호작용 가설**
    * 귀무가설: 태아 수와 관측자 수 간의 상호작용 효과는 없다.
    * 대립가설: 태아 수와 관측자 수 간의 상호작용 효과가 있다.

```python
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt 
import koreanize_matplotlib
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

# 데이터 로드
data = pd.read_csv("[https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/group3_2.txt](https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/group3_2.txt)")

# 선형 회귀 모델 생성 (ols 사용)
# '종속변수 ~ C(독립변수1) * C(독립변수2)' 형태로 작성하면 교호작용을 포함하여 분석한다.
linreg = ols("머리둘레 ~ C(태아수) * C(관측자수)", data=data).fit() 

# 이원 분산분석 수행
result = anova_lm(linreg, typ=2)
print(result)

# [해석 결과]
# 1. C(태아수) PR(>F) = 1.05e-27  -> p < 0.05 이므로 귀무가설 기각. (태아수는 유의미한 영향을 미침)
# 2. C(관측자수) PR(>F) = 6.49e-03 -> p < 0.05 이므로 귀무가설 기각. (관측자수도 유의미한 영향을 미침)
# 3. C(태아수):C(관측자수) PR(>F) = 0.329 -> p > 0.05 이므로 귀무가설 채택.
# 
# 결론: 태아 수와 관측자 수는 각각 머리둘레에 유의미한 영향을 미치지만, 둘이 결합하여 생기는 교호작용(상호작용)은 없다.
```


## 2. 이원 카이제곱 (독립성 검정)

이원 카이제곱 분석은 **동일 집단에서 측정된 두 개의 범주형 변인** 간에 서로 관련성(연관성)이 있는지를 검정하는 방법이다.

### 실습: 교육 수준(학력)과 흡연율의 연관성 검정
* **귀무가설 ($H_0$)**: 교육 수준과 흡연 여부는 서로 관계가 없다. (독립적이다)
* **대립가설 ($H_1$)**: 교육 수준과 흡연 여부는 서로 관계가 있다. (연관성이 있다)

```python
import pandas as pd
import scipy.stats as stats

# 데이터 로드
data = pd.read_csv("[https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/smoke.csv](https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/smoke.csv)")

# 1. 교차표(Contingency Table) 생성
ctab = pd.crosstab(index=data['education'], columns=data['smoking'])
ctab.index = ['대학원', '대학', '고졸']
ctab.columns = ['과흡연', '보통', '비흡연']
print("--- 교차표 ---")
print(ctab)

# 2. 이원 카이제곱(독립성) 검정 수행
chi2, p, dof, expected = stats.chi2_contingency(ctab)

print(f"\n카이제곱 통계량(chi2): {chi2:.4f}")
print(f"p-value: {p:.6f}")
print(f"자유도(dof): {dof}")

# [해석 기준]
# 판정 1 (p-value): 유의수준 0.05 > p-value(0.0008) 이므로 귀무가설을 기각한다.
# 판정 2 (임계값): 계산된 chi2 통계량(18.91)이 자유도 4에서의 임계값(9.49)보다 우측(기각역)에 위치하므로 대립가설을 채택한다.
#
# 결론: 교육 수준과 흡연율 간에는 통계적으로 유의미한 연관성이 존재한다.
```