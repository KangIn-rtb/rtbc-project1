# 이원카이제곱
# 동질성 검정 : 두 집단의 분포가 동일한가 다른 분포인가를 검증하는 방법
# 분포 비율 차이 검정
# 두 개 이상의 범주형 자료가 동일한 분포를 갖는 모집단에서 추출된 것인지 검정하는 방법이다.

import pandas as pd
import scipy.stats as stats

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/survey_method.csv")
ctab = pd.crosstab(index=data['method'], columns=data['survey'])
print(ctab)
ctab.index = ['방법1','방법2','방법3']
ctab.columns = ['매우만족','만족','보통','불만','매우불만']
chi2, p, dof, expected = stats.chi2_contingency(ctab)
print(chi2,p,dof)
print(expected)

# 해석 : 유의수준 < p 이므로 귀무 채택 우연히 발생한 자료라고 할 수 있다. 