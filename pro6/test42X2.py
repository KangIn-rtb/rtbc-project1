# 이원 카이제곱
# : 두 개 
# 분석대상의
# 독립성 : 동일 집단의 두 변인 학력수준과ㅓ 대학진학 여부를 대상으로 관련성이 있는가 없는가
# 독립성 검정은 2 변수 사이의 연관성을 검정


import pandas as pd
import scipy.stats as stats

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/smoke.csv")
print(data['education'].unique())
print(data['smoking'].unique())

ctab = pd.crosstab(index=data['education'],columns=data['smoking'])
ctab.index = ['대학원', '대학', '고']
ctab.columns = ['과흡','보통','노흡']

# ~~~
# 판정1: 유의 수준 0.05 < p 0. 000818 이므로 귀무가설이 기각
# 교육 수준과 흡연율 간에 관계가 있다. 
# 판정2: chi 18.910915, dof 4, critical val 9.49 
# chi 값이 임계치 우측이므로 대립가설 채택

