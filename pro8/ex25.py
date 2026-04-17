from sklearn.model_selection import KFold
import numpy as np
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.metrics import accuracy_score
from sklearn import datasets

iris = datasets.load_iris()
features = iris.data
label = iris.target
dt_clf2 = DecisionTreeClassifier(criterion='gini', max_depth=3,random_state=12)
kfold = KFold(n_splits=5)
cv_acc = []
print(features.shape)
n_iter = 0
for train_index, test_index in kfold.split(features):
    # print(n_iter)
    # print(train_index)
    # print(test_index)
    # n_iter += 1
    xtrain, xtest = features[train_index], features[test_index]
    ytrain, ytest = label[train_index], label[test_index]
    # 학습 및 예측
    dt_clf2.fit(xtrain, ytrain)
    pred = dt_clf2.predict(xtest)
    n_iter += 1
    acc = np.round(accuracy_score(ytest,pred),5)
    train_index = xtrain.shape[0]
    test_size = xtest.shape[0]
    cv_acc.append(acc)
print(cv_acc)
print(np.mean(cv_acc))

