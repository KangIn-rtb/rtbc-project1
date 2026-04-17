# 나이브베이즈 알고리즘을 이용한 분류
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/weather.csv")
print(df.head(2))
print(df.info())