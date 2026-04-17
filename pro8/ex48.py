#  최근접 이웃
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

data = load_breast_cancer()
x = data.data
y = data.target # 0 malignant  1 benign
print(x[:2],' ',x.shape)
print(y[:2],' ',np.unique(y))

x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size=0.2,random_state=42,stratify=y
)
# 스케일링 필요(∵ 거리기반 모델이므로 크기가 영향을 미침)
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# K-NN은 K값이 중요
# k 값 변화에 따른 정확도 비교로 최적의 k값 얻기
# k 값 작으면 과적합, k값 크면 과소적합
train_acc = []
test_acc = []
k_range = range(3, 12)
for k in k_range:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(x_train_scaled, y_train)
    # 예측 
    y_train_pred = model.predict(x_train_scaled)   
    y_test_pred = model.predict(x_test_scaled)
    # 정확도
    train_acc.append(accuracy_score(y_train, y_train_pred))
    test_acc.append(accuracy_score(y_test, y_test_pred))

# 시각화 
import matplotlib.pyplot as plt
plt.figure()
plt.plot(k_range, train_acc, marker='o',label='Train acc')
plt.plot(k_range, test_acc, marker='s',label='Test acc')
plt.xlabel('k value')
plt.ylabel('accuracy')
plt.title('knn acc comp')
plt.legend()
plt.show()
# 그래프 기준으로 최적은 k = 3
# test acc가 가장 높은 지점이 3 (과적합 의심)
# 4는 불안, 7~9는 안정적 
# 그래프상 위치 관계 없이 차이가 크면 과적합의 영향이 있다. 즉 9 처럼 딱붙은게 젤 좋다. 

best_k = k_range[np.argmax(test_acc)]
print('최적의 k ', best_k) # 얘는 그냥 가장 큰 지점을 최적이라고 줌

# 최종 모델 작성
best_k = 9
final_model = KNeighborsClassifier(n_neighbors=best_k)
final_model.fit(x_train_scaled, y_train)
# 성능 확인
y_pred = final_model.predict(x_test_scaled)
print('final_model 정확도', accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test,y_pred))

# 새로운 자료로 예측 (그냥 기존꺼 씀)
new_data = x[0].copy()
new_data = new_data + np.random.normal(0,0.1, size=new_data.shape)
new_data_scaled = scaler.transform([new_data])
prediction = final_model.predict(new_data_scaled)
prob = final_model.predict_proba(new_data_scaled)
print(prediction[0])
print(prob)