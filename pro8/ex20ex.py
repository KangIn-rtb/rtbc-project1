"""
[로지스틱 분류분석 문제2] 
게임, TV 시청 데이터로 안경 착용 유무를 분류하시오.
안경 : 값0(착용X), 값1(착용O)
예제 파일 : https://github.com/pykwon  ==>  bodycheck.csv
새로운 데이터(키보드로 입력)로 분류 확인. 스케일링X
"""
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/bodycheck.csv")
print(data.keys())
print(data)

x = data.iloc[:,[1,4]]
y = data.안경유무
print(x,y)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=0)
# model = LogisticRegression(random_state=0)
model = LogisticRegression(C=0.0000049, solver='lbfgs', multi_class='auto' ,random_state=0)
model.fit(x_train,y_train)
ypred = model.predict(x_test)
print(accuracy_score(y_test,ypred))
try:
    game_input = float(input("게임 시청 시간을 입력하세요: "))
    tv_input = float(input("TV 시청 시간을 입력하세요: "))
    # 입력 데이터를 2차원 배열 형태로 생성
    new_data = [[game_input, tv_input]]
    # 예측 수행
    new_pred = model.predict(new_data)
    if new_pred[0] == 1:
        print("안경 착용")
    else:
        print("안경 미착용")
except Exception as e:
    print("입력 오류", e)