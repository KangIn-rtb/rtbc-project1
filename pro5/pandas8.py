import xml.etree.ElementTree as etree # xml 해석기
xmlfile = etree.parse('my.xml')
print(xmlfile,type(xmlfile))
root = xmlfile.getroot()
print(root.tag)
print(root[0].tag)
print(root[0][0].tag)
# .....
print()
myname = root.find("item").find("name").text
mytel = root.find("item").find("tel").text
print(myname + ' '+ mytel)
# -----------------------
print()
import requests
url = 'https://www.kma.go.kr/XML/weather/sfc_web_map.xml'
headers = {"User-Agent":"Mozilla/5.0"}
res = requests.get(url, headers=headers)
res.raise_for_status()
print(res.text, type(res.text)) # xml 모양의 문자열

root = etree.fromstring(res.text)
print(root)
for elem in root.iter():
    if '}' in elem.tag:
        elem.tag = elem.tag.split('}',1)[1] # '}'을 기준으로 잘라 태그명만 남김
weather = root.find('weather')
year = weather.get('year')
month = weather.get('month')
day = weather.get('day')
hour = weather.get('hour')
print(f"{year} {month} {day} {hour}")

# 각 지역 순회
for local in weather.findall("local"):
    name = local.text.strip()
    ta = local.get('ta')
    print(f"{name} {ta}")