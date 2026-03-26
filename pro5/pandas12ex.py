import requests
import time
import sys
from bs4 import BeautifulSoup
import pandas as pd
url1 = "https://finance.naver.com/sise/sise_market_sum.naver?&page=1"
url2 = "https://finance.naver.com/sise/sise_market_sum.naver?&page=2"
headers = {"User-Agent":"Mozilla/5.0"}

sys.stdout.reconfigure(encoding='utf-8')
page1 = requests.get(url=url1,headers=headers)
page2 = requests.get(url=url2,headers=headers)
soup1 = BeautifulSoup(page1.text,'html.parser')
soup2 = BeautifulSoup(page2.text,'html.parser')
name1 = [tag.text.strip() for tag in soup1.select("a.tltle")]
rows1 = soup1.select("table.type_2 tbody tr")
price1 = []
for row in rows1:
    prices = row.select("td.number")
    if len(prices) >= 5:
        cap = prices[4].text.strip()
        price1.append(cap)
        
df1 = pd.DataFrame({
    '이름' : name1,
    '시가총액' : price1
})
df1.to_csv('sitotal1.csv',index=False)

name2 = [tag.text.strip() for tag in soup2.select("a.tltle")]
rows2 = soup2.select("table.type_2 tbody tr")
price2 = []
for row in rows2:
    prices = row.select("td.number")
    if len(prices) >= 5:
        cap = prices[4].text.strip()
        price2.append(cap)
        
df2 = pd.DataFrame({
    '이름' : name2,
    '시가총액' : price2
})
df2.to_csv('sitotal2.csv',index=False)
df1_read = pd.read_csv('sitotal1.csv')
df2_read = pd.read_csv('sitotal2.csv')

print(df1_read.head(3))

print(df2_read.head(3))