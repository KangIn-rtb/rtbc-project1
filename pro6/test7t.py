# A 중학교 1학년 1반 학생들의 시험 결과가 담긴 파일을 읽어 처리
# 국어 점수 평균검정
# 귀무 : 학생들의 국어 점수 평균은 80이다.
# 대립 : 학생들의 국어 점수 평균은 80이 아니다.

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import wilcoxon

pd.set_option('display.max_columns',None)
data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/student.csv")
print(data.head())
print(data.describe())
print(data['국어'].mean())
print(len(data)) # 30 행이 넘으면 중심극한정리에 따라 정규성을 따른다고 가정
# 30개가 넘지 않으므로 정규성 검정 실시
print(stats.shapiro(data['국어']))
# 0.05 > p 0.0129 정규성을 만족하지 않음 --> 정규성을 만족한다면 ttest 
# 하지만 정규성을 만족하지 못하니 ttest 불가 
# 대안법 
# Wilcoxon : 비모수 검정 
wilcox_result = wilcoxon(data['국어'] - 80)
print()
result = stats.ttest_1samp(data['국어'],popmean=80)
print(result)
# 결론 : 정규성은 부족하나 귀무가설 채택이라는 동일 결론을 얻음
# 표본 수가 크다면 그냥 ttest_1samp을 써도 된다. 

print('---------------------')
# 여아신생아 몸무게의 평균 검정 수행
# 여아신생아의 몸무게는 평균이 2800g 로 알려져 왔으나 이보다 크다는 주장
# 18명의 표본
# 귀무 : 여아신생아의 몸무게 평균은 2800
# 대립 : 여아신생아의 몸무게 평균은 2800이 아님

data2 = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/babyboom.csv")
print(data2.head(3))
print(data2.describe())
print()
fdata = data2[data2.gender==1]
print(fdata,' ',len(fdata))
# 2800과 3132는 평균에 차이가 있는가
print(f"평균:{np.mean(fdata.weight)} 표준편차:{np.std(fdata.weight)}")
result2 = stats.ttest_1samp(fdata['weight'], popmean=2800)
print(result2)
# 해석 1 : 0.05 > p 0.0392 이므로 귀무가설 기각
# 해석 2 : t 2.2331, df 17, a 0.05, cv = 1.740 -> t분포표 
#           t 값이 cv 값 오른쪽에 있으므로 귀무가설 기각 
#                   ** ** |**   
#                 **      |  **
#               **        |t(값)**
#           ** *          |       * **
#      ------(귀무가설채택)--(귀무가설기각)----------------
#                      cv=1.740 
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# 선행조건인 정규성 검정을 한 경우
print(stats.shapiro(fdata['weight']))
# a 0.05 > p 0.017 정규성을 만족하지 않음 

# 정규성 만족여부 시각화
sns.histplot(fdata['weight'],kde=True)
plt.show()
# 시각화 2 Q-Q plot
stats.probplot(fdata['weight'],plot=plt) # QQ에서 잔차가 정규성을 만족하지 못함
plt.show()
# 회귀선의 잔차가 곡선을 그리면 정규성 X
result3 = wilcoxon(fdata['weight'] - 2800)
print(result3)
# 해석 3 : a 0.05 > p 0.034233 이므로 귀무가설 기각