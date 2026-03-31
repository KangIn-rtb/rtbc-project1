# Python 웹 스크래핑 기초 (BeautifulSoup 4)

## 1. BeautifulSoup4 기본 개념 및 객체 생성

`BeautifulSoup`은 HTML이나 XML 문서를 파싱(Parsing)하여 개발자가 원하는 데이터를 쉽게 추출할 수 있도록 돕는 파이썬의 대표적인 라이브러리이다. `requests` 모듈로 웹 페이지의 소스코드를 가져온 후, 이를 객체화하여 탐색한다.

* `lxml`이나 `html.parser` 같은 구문 분석기(Parser)를 지정하여 객체를 생성한다.
* 웹 서버에 요청 시 브라우저인 것처럼 속이기 위해 `headers`에 `User-Agent`를 포함하는 것이 좋다.

```python
import requests
from bs4 import BeautifulSoup

baseurl = "[https://www.naver.com](https://www.naver.com)"
headers = {"User-Agent" : "Mozilla/5.0"} # 봇(Bot) 차단을 막기 위한 헤더 설정

source = requests.get(baseurl, headers=headers)
print(source.status_code) # 200이면 정상 접속

# HTML 소스코드를 읽어와 BeautifulSoup 객체로 변환 (lxml 파서 사용)
conv_data = BeautifulSoup(source.text, 'lxml')

# 문서 내의 모든 <a> 태그를 찾아 순회
for atag in conv_data.find_all('a'):
    href = atag.get('href') # href 속성값 추출
    title = atag.get_text(strip=True) # 태그 안의 텍스트 추출 (앞뒤 공백 제거)
    
    if title:
        print(href)
        print(title)
        print('-------')
```


## 2. DOM 탐색 및 `find` 메서드 활용
객체화된 문서 트리(DOM) 구조를 따라 내려가며 태그를 직접 찾거나, `find()` 함수를 통해 속성값(id, class 등)으로 태그를 찾아낸다.

```python
from bs4 import BeautifulSoup

html_page = """
<html><body>
<h1 id="title">제목 태그</h1>
<p>웹문서 연습</p>
<p id="my" class="our">원하는 자료 확인</p>
</body></html>
"""
soup = BeautifulSoup(html_page, 'html.parser')

# 1. 트리 구조(DOM)를 이용한 직접 접근
h1 = soup.html.body.h1
print(h1.string) # '제목 태그'

p1 = soup.html.body.p
print(p1.string) # '웹문서 연습'

# 형제 노드(sibling)로 이동 (줄바꿈 문자가 섞여 있어 두 번 이동해야 다음 p태그가 나옴)
p2 = p1.next_sibling.next_sibling 
print(p2.string) # '원하는 자료 확인'

print('\n-- find 메소드 사용 --')
# 2. find(태그명, 속성) 메서드를 이용한 접근
print(soup.find('p').string) # 문서에서 가장 처음 만나는 p태그 찾기
print(soup.find('p', id="my").string) # id가 "my"인 p태그 찾기
print(soup.find(id="title").string)   # 태그명 없이 id만으로 찾기
print(soup.find(class_="our").string) # class 속성으로 찾기 (파이썬의 class 키워드와 겹치므로 class_ 사용)
print(soup.find(attrs={"class": "our"}).string) # attrs 딕셔너리로 찾기
```


## 3. CSS 선택자(`select`) 활용 및 실전 응용

웹 개발에서 요소를 꾸밀 때 사용하는 CSS 선택자(Selector) 문법을 그대로 사용하여 데이터를 더 정교하게 추출할 수 있다. 
* `select_one("선택자")`: 가장 먼저 매칭되는 태그 1개만 가져온다.
* `select("선택자")`: 매칭되는 모든 태그를 리스트(배열) 형태로 가져온다.

### CSS 선택자 기초
```python
from bs4 import BeautifulSoup

html_page = """
<html><body>
<div id="hello">
    <a href="[https://www.naver.com](https://www.naver.com)">naver</a><br>
    <ul class="world">
        <li>안녕</li>
        <li>반가워</li>
    </ul>
</div>
<div id="hi" class="good">두번째 div</div>
</body></html>
"""
soup = BeautifulSoup(html_page, 'lxml')

# 1. 태그 계층(자식) 선택
aa = soup.select_one("div#hello > a") # id가 hello인 div의 바로 아래 직계 자식 a태그
print(aa.string) # 'naver'

# 2. 태그 계층(자손) 다중 선택
bb = soup.select("div#hello ul.world > li") # div#hello 하위의 ul.world 직계 자식인 모든 li태그
for i in bb:
    print(i.text) # '안녕', '반가워'
```

### [실습 1] 위키백과 데이터 추출 및 불필요한 태그 제거 (`decompose`)
```python
import requests
from bs4 import BeautifulSoup

url = "[https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0](https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0)"
headers = {"User-Agent":"Mozilla/5.0"}
wiki = requests.get(url=url, headers=headers)

soup = BeautifulSoup(wiki.text, 'html.parser')
result = soup.select("#mw-content-text p") # 본문 영역의 모든 p태그 추출

for s in result:
    # 각 p태그 안에 있는 주석 번호 <sup> 태그들을 찾아 아예 삭제해버림
    for sup in s.find_all("sup"):
        sup.decompose() 
        
    print(s.get_text(strip=True)) # 깔끔하게 본문 텍스트만 출력
```

### [실습 2] 교촌치킨 메뉴 스크래핑 및 Pandas 통계 분석
```python
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "[https://kyochon.com/menu/chicken.asp](https://kyochon.com/menu/chicken.asp)"
headers = {"User-Agent":"Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup2 = BeautifulSoup(response.text, 'html.parser')

# List Comprehension을 이용해 이름과 가격 배열을 한 번에 생성
names = [tag.text.strip() for tag in soup2.select("dl.txt > dt")]

# 가격은 쉼표(,)를 제거하고 정수형(int)으로 변환
prices = [int(tag.text.strip().replace(',', '')) for tag in soup2.select("p.money strong")]

# Pandas DataFrame으로 변환
df = pd.DataFrame({"상품명": names, "가격": prices})
print(df.head(3))

# Pandas 통계 분석
print(f"가격 평균 : {df['가격'].mean():.2f}")
print(f"가격 표준편차 : {df['가격'].std():.2f}")
cv = (df['가격'].std() / df['가격'].mean()) * 100
print(f"가격 변동계수(cv) : {cv:.2f}%")
```


## 4. 실시간 네이버 금융 데이터 스크래핑


### 1) 환율 실시간 감시 봇
`time.sleep`을 활용해 무한루프를 돌며 특정 주기로 실시간 데이터를 스크래핑하는 예제이다.
```python
import requests
import time
import sys
from bs4 import BeautifulSoup

url = "[https://finance.naver.com/marketindex/](https://finance.naver.com/marketindex/)"
headers = {"User-Agent":"Mozilla/5.0"}

while True:
    sys.stdout.reconfigure(encoding='utf-8') # 터미널 한글 깨짐 방지
    res = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    
    # CSS 선택자로 국가, 가격, 단위, 변동치 추출
    nation = soup.select_one("h3.h_lst span.blind").get_text(strip=True)
    price = soup.select_one(".value").get_text(strip=True)
    unit = soup.select_one(".txt_krw .blind").get_text(strip=True)
    change = soup.select_one(".change").get_text(strip=True)
    updown = soup.select("div.head_info.point_up span.blind")[-1].get_text(strip=True)

    print(f"{nation.replace(' ', '')} {price}{unit} {updown} {change}")
    time.sleep(5) # 5초 대기 후 다시 요청
```

### 2) 네이버 시가총액 1, 2페이지 추출 후 CSV 저장
페이지네이션(Pagination) 처리가 된 게시판의 여러 페이지를 한 번에 긁어와 Pandas로 합치고 저장하는 기법이다.
```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

url1 = "[https://finance.naver.com/sise/sise_market_sum.naver?&page=1](https://finance.naver.com/sise/sise_market_sum.naver?&page=1)"
url2 = "[https://finance.naver.com/sise/sise_market_sum.naver?&page=2](https://finance.naver.com/sise/sise_market_sum.naver?&page=2)"
headers = {"User-Agent":"Mozilla/5.0"}

# 1페이지 처리
page1 = requests.get(url=url1, headers=headers)
soup1 = BeautifulSoup(page1.text, 'html.parser')

name1 = [tag.text.strip() for tag in soup1.select("a.tltle")] # 종목명
rows1 = soup1.select("table.type_2 tbody tr") # 행 데이터 추출

price1 = []
for row in rows1:
    prices = row.select("td.number")
    # 시가총액이 있는 열은 td 중 4번째 인덱스에 존재하므로 길이 체크
    if len(prices) >= 5: 
        cap = prices[4].text.strip()
        price1.append(cap)
        
df1 = pd.DataFrame({'이름': name1, '시가총액': price1})
df1.to_csv('sitotal1.csv', index=False) # 1페이지 저장

# 2페이지도 위와 동일한 로직으로 처리하여 sitotal2.csv 로 저장했다고 가정

# 저장한 CSV 파일 불러와서 확인
df1_read = pd.read_csv('sitotal1.csv')
df2_read = pd.read_csv('sitotal2.csv')

print(df1_read.head(3))
print(df2_read.head(3))
```


## 5. XML 데이터 파싱 (서울시 도서관 정보)
BeautifulSoup은 HTML뿐만 아니라 공공데이터 API 등에서 많이 제공되는 XML 포맷 문서도 동일한 방식으로 파싱(`lxml-xml` 또는 `xml` 파서 사용)할 수 있다.

```python
import urllib.request as req
import pandas as pd
from bs4 import BeautifulSoup

# 서울시 도서관 샘플 XML 데이터 API
url = "[http://openapi.seoul.go.kr:8088/sample/xml/SeoulLibraryTimeInfo/1/5/](http://openapi.seoul.go.kr:8088/sample/xml/SeoulLibraryTimeInfo/1/5/)"

# urlopen을 통해 문서를 읽고 문자열(UTF-8)로 디코딩
plainText = req.urlopen(url).read().decode()

# xml 파서로 객체화
xmlobj = BeautifulSoup(plainText, 'xml')

# <row> 태그로 묶인 데이터 리스트 추출
libData = xmlobj.select('row')

rows = []
for data in libData:
    # 각 row 내의 자식 태그 값 추출
    name = data.find("LBRRY_NAME").string
    addr = data.find("ADRES").string
    
    rows.append({"도서관명": name, "주소": addr})

# 추출한 리스트-딕셔너리를 데이터프레임으로 변환
df = pd.DataFrame(rows)
print(df)
print("건수 : ", len(df))
```