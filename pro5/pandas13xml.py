# 도서관 정보 XML 샘플 자료 5개 읽기
import urllib.request as req
import pandas as pd
from bs4 import BeautifulSoup
url = "http://openapi.seoul.go.kr:8088/sample/xml/SeoulLibraryTimeInfo/1/5/"
plainText = req.urlopen(url).read().decode()
# print(plainText)
xmlobj = BeautifulSoup(plainText,'xml')
libData = xmlobj.select('row')
# print(libData)
rows = []
for data in libData:
    name = data.find("LBRRY_NAME").string
    addr = data.find("ADRES").string
    print(name)
    print(addr)
    print()
    rows.append({"도서관명":name,"주소":addr})
df = pd.DataFrame(rows)
print(df)
print("건수 : ",len(df))