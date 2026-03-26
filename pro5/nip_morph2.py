import requests
from bs4 import BeautifulSoup
from konlpy.tag import Okt
import pandas as pd
from urllib import parse

okt = Okt()
# url = "https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0"
para = "이순신"
url = "https://ko.wikipedia.org/wiki/"+para
headers = {"User-Agent":"Mozilla/5.0"}
response = requests.get(url,headers=headers)

if response.status_code == 200:
    page = response.text
    # print(page,type(page))
    soup = BeautifulSoup(page,'lxml')
    wordlist = []
    for item in soup.select("#mw-content-text p"):
        if item.string != None:
            wordlist += okt.nouns(item.string)
            
    print(wordlist)
    print(len(wordlist))
    print(len(set(wordlist)))
    
    word_dict = {}
    for i in wordlist:
        if i in word_dict:
            word_dict[i] += 1
        else:
            word_dict[i] = 1
    print(word_dict)