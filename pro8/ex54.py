import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.neural_network import MLPClassifier
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = load_wine()
x = data.data
y = data.target
print(x[:2],' ',x.shape)
print(y[:2],' ',np.unique(y))

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42, stratify=y)

# 스케일링 (MLP는 얘를 권장)
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

model = MLPClassifier(
    hidden_layer_sizes=(50,30),
    activation='relu',
    solver='adam',
    learning_rate_init=0.001,
    max_iter=30,
    random_state=42,
    verbose=1
)
model.fit(x_train_scaled, y_train)
pred = model.predict(x_test_scaled)
print(accuracy_score(y_test,pred))

cm = confusion_matrix(y_test,pred)
plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt='d',cmap='Blues')
plt.show()

plt.plot(model.loss_curve_)
plt.show()
# 참고 : 미분이 MLP에서 어떻게 쓰이는가 미분으로 오차를 줄여나감
# MLP 구조 : 입력 -> 신경망 -> 출력 후 오차를 확인
# 예) 입력X -> 모델 -> 예측값 - 실제값 -> 오차loss 발생 
# 미분을 쓰는 이유 : 오차를 어떻게 줄일지 즉, 오차가 줄어드는 방향으로 w를 갱신
# 전체 학습 과정을 보면 
# 1. 모델이 예측 -> 2. 오차 계산 -> 3. 미분(기울기 계산) -> 4. 가중치 w를 갱신 -> 5. 반복 1~4 - 역전파