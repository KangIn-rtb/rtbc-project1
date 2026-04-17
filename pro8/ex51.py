# Perceptron : sklearn이 제공하는 단층신경망
# 이항분류 가능

import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

feature = np.array([[0,0],[0,1],[1,0],[1,1]])
print(feature)
label = np.array([0,0,0,1]) # and 
ml = Perceptron(max_iter=10).fit(feature,label)  # max_iter : 학습횟수
pred = ml.predict(feature)
print(pred)
print(accuracy_score(label,pred))
x = np.array([
    [2,3],
    [3,3],
    [1,1],
    [5,2],
    [6,1]
])
y = np.array([1,1,-1,1,-1])

model = Perceptron(max_iter=1000, eta0=0.1, random_state=42)
model.fit(x,y)
pred = model.predict(x)
print(pred)
print(y)
print(accuracy_score(y,pred))
print(model.coef_)
print(model.intercept_)

# 결정경계(w1*x1 + w2*x2 + b) 시각화
import matplotlib.pyplot as plt
plt.scatter(x[:,0],x[:,1],c=y,cmap='bwr')
w = model.coef_[0]
b = model.intercept_[0]
x_vals = np.linspace(0,7,100)
y_vals = -(w[0]*x_vals + b) / w[1]
plt.plot(x_vals,y_vals)
plt.show()