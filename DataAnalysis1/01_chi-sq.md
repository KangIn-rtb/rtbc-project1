# 카이제곱 적합도, 독립성, 동질성 검정

## 1. 일원 카이제곱 검정 (적합도 검정)
단일 범주형 변인에 대해, 관찰된 도수(빈도)가 이론적으로 기대되는 도수 분포와 일치하는지를 검정하는 방법이다.

### 주사위 적합도 검정 예제
특정 주사위를 60번 던졌을 때 각 눈금이 나온 횟수(관측 빈도)를 바탕으로, 이 주사위가 조작되지 않은 정상적인 주사위인지(게임에 적합한지) 검증한다.

* **귀무가설 ($H_0$)**: 관찰치와 기대치는 차이가 없다. 즉, 각 눈금이 나올 확률은 동일하며 이 주사위는 게임에 적합하다.
* **대립가설 ($H_1$)**: 관찰치와 기대치는 차이가 있다. 이 주사위는 조작되었거나 불량이며 게임에 적합하지 않다.

```python
import pandas as pd
import scipy.stats as stats

# 각 눈금(1~6)에 대한 관측 빈도 수 (총 60회)
data = [4, 6, 17, 16, 8, 9] 

# 일원 카이제곱 검정 수행 (기대 빈도는 자동으로 평균값인 10으로 설정됨)
stat, p = stats.chisquare(data)
print(f"카이제곱 통계량: {stat:.2f}, p-value: {p:.4f}") 
# 결과: 통계량 14.20, p-value 0.0144

# [판정 기준]
# 1. p-value 기준: 유의수준 0.05 > p-value(0.0144) 이므로 귀무가설을 기각한다.
# 2. 임계값 기준: 자유도(df) = n-1 = 5. 유의수준 0.05에서의 임계값은 11.07이다. 
#    계산된 통계량(14.2)이 임계값(11.07)보다 크므로 기각역에 속해 귀무가설을 기각한다.

# 결론: 데이터의 편차는 우연히 발생한 것이 아니다. 이 주사위는 게임에 적합하지 않다.
```


## 2. 이원 카이제곱 검정 (독립성 검정)

두 개의 범주형 변수(예: 부모의 학력과 자녀의 대학 진학)가 서로 연관성이 있는지, 아니면 서로 독립적인지를 검정하는 방법이다.

### [실습 1] 부모 학력과 자녀 진학 여부의 연관성
```python
import pandas as pd
import scipy.stats as stats

# 데이터 로드 및 결측치 제거
data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/cleanDescriptive.csv")
data_clean = data.dropna(subset=['level', 'pass'])

# 두 변수에 대한 교차표(Contingency Table) 생성
table = pd.crosstab(data_clean['level'], data_clean['pass'])
print("--- 교차표 ---")
print(table)

# 이원 카이제곱 검정 수행
chi2, p, dof, expected = stats.chi2_contingency(table)

print(f'\n카이제곱 통계량: {chi2:.2f}')
print(f'p-value: {p:.4f}')

if p < 0.05:
    print("결론: p < 0.05 이므로 부모 학력과 자녀 진학은 관련이 있음 (귀무가설 기각)")
else:
    print("결론: p >= 0.05 이므로 부모 학력과 자녀 진학은 관련이 없음 (귀무가설 채택)")
```

### [실습 2] DB 연동: 직급과 연봉 그룹 간의 연관성
연속형 변수인 연봉 데이터를 `pd.cut()`을 이용하여 범주형 그룹으로 나눈 뒤 독립성 검정을 수행한다.

```python
import pymysql
import pandas as pd
from scipy import stats

config = {
    'host': '127.0.0.1', 'user': 'root', 'password': '123',
    'database': 'test', 'port': 3306, 'charset': 'utf8mb4'
}

try:
    conn = pymysql.connect(**config)
    sql = "SELECT jikwonjik, jikwonpay FROM jikwon"
    df_jikwon = pd.read_sql(sql, conn)
    df_jikwon = df_jikwon.dropna()
    
    # 연속형 데이터(연봉)를 4개의 구간(범주)으로 이산화(Binning)
    bins = [1000, 3000, 5000, 7000, 100000]
    labels = [1, 2, 3, 4]
    df_jikwon['pay_group'] = pd.cut(df_jikwon['jikwonpay'], bins=bins, labels=labels, right=False)
    
    # 직급과 연봉 그룹 간의 교차표 생성
    table = pd.crosstab(df_jikwon['jikwonjik'], df_jikwon['pay_group'])
    print("--- 직급/연봉 그룹 교차표 ---\n", table)
    
    chi2, p, dof, expected = stats.chi2_contingency(table)
    
    print(f'\n카이제곱 통계량: {chi2:.2f}')
    print(f'p-value: {p:.4f}')
    
    if p < 0.05:
        print("결론: 직급과 연봉 그룹은 통계적으로 유의미한 관련이 있다.")
    else:
        print("결론: 직급과 연봉 그룹은 관련이 없다.")

except Exception as e:
    print(f"오류 발생: {e}")
finally:
    conn.close()
```


## 3. 이원 카이제곱 검정 (동질성 검정)
두 개 이상의 집단(모집단)이 특정 범주형 변수에 대해 동일한 분포를 가지고 있는지(비율 차이가 없는지)를 검정하는 방법이다. 
* 예: 설문조사 '방법1', '방법2', '방법3' 에 따른 '만족도' 분포가 모두 동일한가?

```python
import pandas as pd
import scipy.stats as stats

# 데이터 로드
data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/survey_method.csv")

# 조사 방법(method)과 만족도(survey) 교차표 생성
ctab = pd.crosstab(index=data['method'], columns=data['survey'])

# 인덱스와 컬럼 이름 직관적으로 변경
ctab.index = ['방법1', '방법2', '방법3']
ctab.columns = ['매우만족', '만족', '보통', '불만', '매우불만']
print("교차표:\n", ctab)

# 동질성 검정 수행
chi2, p, dof, expected = stats.chi2_contingency(ctab)

print(f"\n카이제곱 통계량: {chi2:.2f}")
print(f"p-value: {p:.4f}")
print(f"자유도(dof): {dof}")
# print("기대도수 배열:\n", expected)

# [해석]
# 만약 p-value가 0.05보다 크다면 귀무가설을 채택한다. 
# 즉, 설문조사 방법에 따른 만족도의 차이는 통계적으로 유의미하지 않으며, 각 셀의 빈도 차이는 우연히 발생한 자료라고 해석할 수 있다.
```