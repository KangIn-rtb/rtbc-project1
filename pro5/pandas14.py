# JSON 자료 : XML에 비해 경량. 배열 개념만 있으면 처리 가능
import json
dict = {'name':'tom','age':25,'score':['90','80','88']}
print('인코딩 : dict -> str ---')
str_val = json.dumps(dict) # indent 는 들여쓰기
print(str_val,type(str_val))
print(str_val[0:20])
json_val = json.loads(str_val)
print(json_val['name'])
for k in json_val.keys():
    print(k)
for v in json_val.values():
    print(v) 

import urllib.request as req
url = "http://openapi.seoul.go.kr:8088/sample/json/SeoulLibraryTimeInfo/1/5/"
plainText = req.urlopen(url).read().decode()
# print(plainText, type(plainText))
jsonData = json.loads(plainText)
print(jsonData["SeoulLibraryTimeInfo"]["row"][0]["LBRRY_NAME"])

# dict의 get()함수
print()
libData = jsonData.get("SeoulLibraryTimeInfo").get("row")
# print(libData)
name = libData[0].get("LBRRY_NAME")
print(name)

print()
datas = []
for ele in libData:
    name = ele.get("LBRRY_NAME")
    tel = ele.get("TEL_NO")
    addr = ele.get("ADRES")
    print(name,' ',tel,' ',addr)
    datas.append([name,tel,addr])
import pandas as pd
df = pd.DataFrame(datas,columns=['도서관명', '전화','주소'])
print(df)