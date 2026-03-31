# 파이썬 데이터 시각화 (Matplotlib & Seaborn)

## 1. 데이터 시각화의 중요성 5가지
데이터 시각화는 텍스트와 숫자로만 이루어진 데이터를 그래픽 요소로 매핑하여 직관적인 인사이트를 도출하는 과정이다.

1. **패턴 및 추세의 직관적 파악**: 방대한 양의 데이터 흐름과 트렌드를 한눈에 파악할 수 있다.
2. **이상치(Outlier) 및 오류의 신속한 발견**: 통계 수치만으로는 찾기 힘든 데이터 내의 비정상적인 값이나 수집 오류를 쉽게 찾아낼 수 있다.
3. **변수 간의 상관관계 확인**: 여러 특성(Feature) 간의 관계와 영향력을 시각적으로 비교하고 분석할 수 있다.
4. **빠르고 정확한 의사결정 지원**: 복잡한 데이터를 단순화하여 데이터 기반의 객관적인 의사결정을 돕는다.
5. **원활한 소통 및 설득력 강화**: 데이터 비전문가(경영진, 클라이언트 등)에게도 분석 결과를 쉽게 이해시키고 인사이트를 공유할 수 있다.


## 2. Matplotlib 기초 및 인터페이스

`matplotlib.pyplot`은 파이썬의 가장 대표적인 플로팅 라이브러리이다. 차트를 그리는 방식에는 크게 두 가지 인터페이스가 존재한다.

### 1) pyplot 스타일 인터페이스
상태 기반 인터페이스로, `plt` 모듈의 함수를 직접 호출하여 현재 활성화된 차트에 요소를 추가하는 직관적인 방식이다.

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread

# 한글 폰트 및 마이너스 기호 깨짐 방지 설정
plt.rc('font', family="Malgun Gothic")
plt.rcParams['axes.unicode_minus'] = False

# 기본 선 그래프 및 속성 설정
x = np.arange(10)
y = np.sin(x)

plt.figure(figsize=(10, 5)) # 차트 크기 설정
# 'go--' : 초록색(g), 마커(o), 점선(--)
plt.plot(x, y, 'go--', linewidth=2, markersize=12) 
plt.xlabel('x 축')
plt.ylabel('y 축')
plt.title("Sin Graph")
plt.grid() # 격자 표시
plt.show()

# 복수의 차트 겹쳐 그리기 (Hold) 및 저장
irum = ['a', 'b', 'c', 'd', 'e']
kor = [80, 50, 70, 75, 90]
eng = [60, 70, 65, 80, 95]

plt.plot(irum, kor, 'ro--') # 빨간색 점선
plt.plot(irum, eng, 'bo--') # 파란색 점선
plt.ylim([40, 100]) # Y축 범위 지정
plt.legend(['국어', '영어'], loc='best') # 범례 표시

# 차트 이미지로 저장 후 다시 불러와서 출력하기
fig = plt.gcf()
fig.savefig('plot1.png')    
plt.show()

img = imread('plot1.png') 
plt.imshow(img)
plt.show()
```

### 2) 객체 지향(Object-Oriented) 인터페이스
차트(Figure)와 축(Axes) 객체를 명시적으로 생성하여 각각의 영역에 그래프를 그리는 방식이다. 복잡하고 정교한 다중 차트를 구성할 때 유리하다.

```python
fig, ax = plt.subplots(nrows=2, ncols=1) # 2행 1열의 서브플롯 생성
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))
plt.show()

# add_subplot 방식
fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1) # 1행 2열 중 첫 번째
ax2 = fig.add_subplot(1, 2, 2) # 1행 2열 중 두 번째

ax1.hist(np.random.randn(100), bins=10, alpha=0.9) # 히스토그램
ax2.plot(np.random.randn(100))
plt.show()
```


## 3. 다양한 차트 그리기 (Pie, Boxplot, Bubble, Time Series)


* **원형 차트(Pie)**: 전체 중 각 비율을 보여준다.
* **박스 플롯(Boxplot)**: 데이터의 분포(사분위수)와 이상치를 식별하는 데 효과적이다.
* **버블 차트(Bubble)**: 산점도에 데이터 점의 크기(`s`)와 색상(`c`) 요소를 추가하여 3차원 이상의 정보를 표현한다.

```python
# 원형 차트 (Pie Chart)
data = [50, 80, 100, 90, 70]
# explode를 통해 특정 조각을 분리하여 강조
plt.pie(data, colors=['yellow', 'blue', 'red'], explode=(0, 0.2, 0, 0.1, 0))
plt.show()

# 박스 플롯 (Box Plot)
data = [1, 50, 80, 100, 90, 70, 300]
plt.boxplot(data)
plt.show()

# 버블 차트 (Bubble Chart)
n = 30
np.random.seed(0)
x = np.random.rand(n)
y = np.random.rand(n)
color = np.random.rand(n)
scale = np.pi * (np.random.rand(n) * 15)**2 # 점의 크기 동적 할당

plt.scatter(x, y, c=color, s=scale)
plt.show()

# Pandas를 이용한 시계열 데이터 선 그래프
import pandas as pd
fdata = pd.DataFrame(np.random.randn(1000, 4), 
                     index=pd.date_range('1/1/2000', periods=1000), 
                     columns=list('abcd'))
fdata = fdata.cumsum() # 누적합 연산
fdata.plot() # DataFrame 자체의 plot 메서드 활용
plt.show()
```


## 4. Seaborn 라이브러리와 이상치(Outlier) 처리

`Seaborn`은 Matplotlib을 기반으로 하여 더 수려한 디자인과 고수준의 통계용 차트를 쉽게 그릴 수 있도록 돕는 라이브러리이다.

### Seaborn 기본 차트 (타이타닉 데이터셋)
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Seaborn 내장 타이타닉 데이터셋 로드
titanic = sns.load_dataset("titanic")

# 1. 히스토그램 분포 (displot)
sns.displot(titanic['age'])
plt.title('나이 분포 차트')
plt.show()

# 2. 박스 플롯
sns.boxplot(y='age', data=titanic, palette="Paired")
plt.show()

# 3. 산점도 (relplot)
sns.relplot(x='sex', y='age', data=titanic)
plt.show()

# 4. 히트맵 (Heatmap) - 크로스탭 빈도수 시각화
titanic_pivot = titanic.pivot_table(index='class', columns='sex', aggfunc='size')
# annot=True(값 표시), fmt='d'(정수형 표시)
sns.heatmap(titanic_pivot, cmap=sns.light_palette("gray"), annot=True, fmt='d')
plt.show()
```

### [실습] IQR 기반 이상치 탐지 및 박스플롯 시각화 비교
사분위 범위(IQR) 방식을 사용하여 정상 데이터 구간(Lower Bound ~ Upper Bound)을 벗어나는 값을 이상치로 판별하여 제거한다.

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. 데이터 정의 (100은 명백한 이상치)
data = [10, 12, 13, 15, 14, 12, 11, 100]
df = pd.DataFrame({'score': data})

# 2. IQR 기반 이상치 기준 계산
Q1 = df['score'].quantile(0.25) # 1사분위수 (25%)
Q3 = df['score'].quantile(0.75) # 3사분위수 (75%)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# 3. 이상치와 정상치 분리 (불리언 인덱싱)
outliers = df[(df['score'] < lower_bound) | (df['score'] > upper_bound)]
filtered_df = df[(df['score'] >= lower_bound) & (df['score'] <= upper_bound)]

print("이상치 값:\n", outliers)

# 4. 박스플롯 시각화: 이상치 제거 전/후 비교
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 제거 전 (이상치 포함)
sns.boxplot(y=df['score'], ax=axes[0], color='salmon')
axes[0].set_title('이상치 포함 데이터')
axes[0].grid(True)

# 제거 후 (정상 데이터만)
sns.boxplot(y=filtered_df['score'], ax=axes[1], color='lightblue')
axes[1].set_title('이상치 제거 후 데이터')
axes[1].grid(True)

plt.tight_layout()
plt.show()
```

## 5. 실전 예제 (Iris Dataset과 Pairplot)

꽃받침(Sepal)과 꽃잎(Petal)의 길이에 따른 붓꽃(Iris) 종류를 시각화한다. `pairplot`을 사용하면 여러 특성(Feature) 간의 모든 산점도 쌍을 한 번에 그려내어 상관관계를 빠르게 파악할 수 있다.

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 외부 CSV 파일 로드
iris_data = pd.read_csv("[https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/iris.csv](https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/iris.csv)")
print(iris_data.info())

# 1. Matplotlib 기본 산점도
plt.scatter(iris_data['Sepal.Length'], iris_data['Petal.Length'])
plt.title("Iris Sepal vs Petal")
plt.show()

print("붓꽃 종류:", iris_data['Species'].unique())

# 2. Seaborn Pairplot (다중 산점도)
# hue='Species' 옵션을 주면 종(Species)별로 색상을 다르게 칠하여 구분을 돕는다.
sns.pairplot(iris_data, hue='Species', height=2)
plt.show()
```