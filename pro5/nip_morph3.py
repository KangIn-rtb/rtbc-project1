# 웹에서 특정 단어 관련 문서들 검색 후 명사만 추출
# 워드 클라우드 그리기
# pip install pygame
# pip install simplejson
# pip install pytagcloud

from bs4 import BeautifulSoup
from urllib.parse import quote
import urllib.request
from konlpy.tag import Okt
from collections import Counter # 단어수 카운팅
import pytagcloud
import matplotlib.pyplot as plt
import koreanize_matplotlib
import matplotlib.image as mpimg
import webbrowser

keyword = input("검색어")
target_url = "https://www.donga.com/news/search?query=" + quote(keyword) # 변환?
source_code = urllib.request.urlopen(target_url)
# print(source_code)
soup = BeautifulSoup(source_code,'lxml', from_encoding='utf-8')
# print(soup)
msg = ""
for title in soup.find_all("h4",class_="tit"):
    title_link = title.find('a')
    # print(title_link)
    article_url = title_link['href']
    # print(article_url)
    
    try:
        source_article = urllib.request.urlopen(article_url)
        soup2 = BeautifulSoup(source_article, 'lxml',from_encoding='utf-8')
        contents = soup2.select('div.article_txt')
        # print(contents)
        for i in contents:
            item = str(i.find_all(string=True))
            msg += item
    except Exception as e:
        pass
    # print(msg)
    okt = Okt()
    nouns = okt.nouns(msg)
    result = []
    for i in nouns:
        if len(i) > 1:
            result.append(i)
count = Counter(result)
# print(count)
tag = count.most_common(50)
# print(tag)
taglist = pytagcloud.make_tags(tag,maxsize=100)
# print(taglist)
pytagcloud.create_tag_image(taglist,'word.png', size=(800,500),background=(0,0,0),rectangular=False,fontname='Korean')
img = mpimg.imread('word.png')
plt.imshow(img)
plt.show()