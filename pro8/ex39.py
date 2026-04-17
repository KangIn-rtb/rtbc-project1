import random
random.seed(12)

def cald_bmiFunc(h,w):
    bmi = w/(h/100)**2
    if bmi < 18.5: return 'thin'
    elif bmi < 25.0: return 'normal'
    return 'fat'

# print(cald_bmiFunc(170,68))

# fp = open('bmi.csv',mode='w')
# fp.write('height,weight,label\n')

# cnt = {'thin':0,'normal':1,'fat':2}

# for i in range(50000):
#     h = random.randint(150,200)
#     w = random.randint(35,100)
#     label = cald_bmiFunc(h,w)
#     cnt[label] += 1
#     fp.write('{0},{1},{2}\n'.format(h,w,label))
# fp.close()

from sklearn import svm,metrics
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('bmi.csv')
print(df.head(2))
print(df.info())
label = df['label']
print(label[:2])
w = df['weight']/100 
h = df['height'] / 200
wh = pd.concat([w,h],axis=1)
print(wh.head(2))
# label은 dummy화 
label = label.map({'thin':0,'normal':1,'fat':2})
print(label[:2])