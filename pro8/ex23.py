from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import numpy as np
x = [[180,15],[177,42],[156,35],[174, 65],[161, 25]]
y = ['man','woman','woman','man','woman']
feature_names = ['height','hair_length']
class_names = ['man','woman']

model = DecisionTreeClassifier(criterion='entropy',max_depth=3, random_state=0)
model.fit(x,y)

# 모델성능점수
print(model.score(x,y))
print(model.predict(x))
print(y)