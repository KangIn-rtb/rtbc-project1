# 파이썬 데이터 포맷 처리 (JSON과 XML)

## 1. JSON (JavaScript Object Notation) 데이터 처리

JSON은 XML에 비해 가볍고(Lightweight) 읽기 쉬운 데이터 교환 형식이다. 파이썬의 딕셔너리(Dict) 및 리스트(List) 구조와 거의 동일하여 다루기가 매우 수월하다.

* **`json.dumps()`**: 파이썬 객체(딕셔너리 등)를 JSON 형태의 문자열로 변환(인코딩)한다.
* **`json.loads()`**: JSON 형태의 문자열을 파이썬 객체(딕셔너리/리스트)로 변환(디코딩)한다.

### 1) JSON 기본 인코딩 및 디코딩
```python
import json

# 파이썬 딕셔너리 생성
my_dict = {'name': 'tom', 'age': 25, 'score': ['90', '80', '88']}

# 1. Dict -> JSON 문자열 변환 (인코딩)
str_val = json.dumps(my_dict) # indent=4 옵션을 주면 들여쓰기가 되어 보기 좋게 출력된다.
print("인코딩 결과:", str_val, type(str_val))

# 2. JSON 문자열 -> 파이썬 Dict 변환 (디코딩)
json_val = json.loads(str_val)
print("디코딩 결과 이름:", json_val['name'])

# 딕셔너리 키와 값 순회
for k in json_val.keys():
    print("키:", k)
for v in json_val.values():
    print("값:", v) 
```

### 2) 공공데이터(API) JSON 수신 및 Pandas 데이터프레임 변환
서울시 도서관 오픈 API를 호출하여 JSON 데이터를 받고, 원하는 데이터만 추출하여 표(DataFrame) 형태로 가공하는 실습이다. 데이터 추출 시 키 에러를 방지하기 위해 `.get()` 메서드를 사용하는 것이 안전하다.

```python
import urllib.request as req
import json
import pandas as pd

# 서울시 도서관 JSON 샘플 데이터 API
url = "http://openapi.seoul.go.kr:8088/sample/json/SeoulLibraryTimeInfo/1/5/"

# urlopen으로 데이터를 읽고 문자열로 디코딩
plainText = req.urlopen(url).read().decode()

# 문자열을 파이썬 딕셔너리로 변환
jsonData = json.loads(plainText)

# 깊은 계층의 데이터 접근 (딕셔너리 연속 접근)
print(jsonData["SeoulLibraryTimeInfo"]["row"][0]["LBRRY_NAME"])

# 안전하게 get() 함수를 사용한 계층 접근
libData = jsonData.get("SeoulLibraryTimeInfo").get("row")
name = libData[0].get("LBRRY_NAME")
print("첫 번째 도서관:", name)

print("-" * 30)

# 전체 도서관 데이터를 순회하며 리스트에 담기
datas = []
for ele in libData:
    name = ele.get("LBRRY_NAME")
    tel = ele.get("TEL_NO")
    addr = ele.get("ADRES")
    print(name, tel, addr)
    datas.append([name, tel, addr]) # 2차원 리스트 구조로 누적

# 추출한 데이터를 Pandas DataFrame으로 깔끔하게 변환
df = pd.DataFrame(datas, columns=['도서관명', '전화', '주소'])
print("\n[DataFrame 변환 결과]")
print(df)
```


## 2. XML (eXtensible Markup Language) 데이터 처리
XML은 HTML과 유사하게 태그(Tag)를 사용하여 데이터를 계층적인 트리(Tree) 구조로 표현하는 마크업 언어이다. 파이썬 내장 라이브러리인 `xml.etree.ElementTree`를 사용하여 해석(Parsing)한다.

### 1) 로컬 XML 파일 읽기
로컬에 저장된 XML 파일을 읽을 때는 `etree.parse()`를 사용한다.
```python
import xml.etree.ElementTree as etree # XML 해석기

# 로컬 파일 파싱
xmlfile = etree.parse('my.xml')
print(xmlfile, type(xmlfile))

# XML 트리의 최상위 루트(Root) 노드 가져오기
root = xmlfile.getroot()
print(root.tag)       # 루트 태그 이름
print(root[0].tag)    # 루트의 첫 번째 자식 태그 이름
print(root[0][0].tag) # 첫 번째 자식의 첫 번째 자식 태그 이름

# find()를 이용한 특정 태그 검색 및 text 추출
myname = root.find("item").find("name").text
mytel = root.find("item").find("tel").text
print(myname + ' ' + mytel)
```

### 2) 기상청 날씨 API (XML) 수신 및 네임스페이스 처리
웹에서 `requests`를 통해 받아온 XML 문자열을 객체화할 때는 `etree.fromstring()`을 사용한다.
태그 이름 앞에 불필요한 네임스페이스(`{url}`)가 붙어 나오는 경우, 문자열 처리를 통해 태그명만 깔끔하게 남기는 기법을 활용한다.

```python
import requests
import xml.etree.ElementTree as etree

# 기상청 날씨 정보 XML API
url = 'https://www.kma.go.kr/XML/weather/sfc_web_map.xml'
headers = {"User-Agent": "Mozilla/5.0"}

res = requests.get(url, headers=headers)
res.raise_for_status() # 통신 에러 발생 시 예외 발생
print("수신 타입:", type(res.text)) # <class 'str'> (XML 모양의 문자열)

# 문자열을 XML 노드 트리 객체로 변환
root = etree.fromstring(res.text)

# [중요] 네임스페이스 제거 정제 작업
# XML 파싱 시 태그 이름 앞에 '{http://...}weather' 처럼 네임스페이스가 붙는 경우가 있다.
for elem in root.iter():
    if '}' in elem.tag:
        # '}' 문자를 기준으로 1번만 쪼갠 뒤, 뒤쪽(인덱스 1)의 순수 태그명만 남긴다.
        elem.tag = elem.tag.split('}', 1)[1] 

# 1. weather 태그의 속성(attribute) 값 가져오기
weather = root.find('weather')
year = weather.get('year')
month = weather.get('month')
day = weather.get('day')
hour = weather.get('hour')
print(f"발표 일시: {year}년 {month}월 {day}일 {hour}시")

# 2. 모든 local 태그를 순회하며 지역명과 기온(ta) 추출
for local in weather.findall("local"):
    name = local.text.strip() # 태그 사이의 텍스트 값 (지역명)
    ta = local.get('ta')      # 태그의 속성 값 (기온)
    print(f"지역: {name}, 기온: {ta}도")
```