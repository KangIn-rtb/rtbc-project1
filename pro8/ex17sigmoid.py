# sigmoid function 적용 연습
# 로지스틱 회귀에서는 wx + b 자체는 logit한 값이다.
import numpy as np
import math
def sigmoidFunc(num):
    return 1 / (1 + math.exp(-num))

print(sigmoidFunc(3))
print(sigmoidFunc(1))
print(sigmoidFunc(-5))
print(sigmoidFunc(-10))

x = np.linspace(-10,10,50)

w = 1.5
b = -2
z = w*x+b
def sigmoid(z):
    return 1 / (1+np.exp(-z))
p = sigmoid(z)
print(p)
