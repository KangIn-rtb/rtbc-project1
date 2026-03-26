import requests
import time
import sys
from bs4 import BeautifulSoup
url = "https://finance.naver.com/marketindex/"
headers = {"User-Agent":"Mozilla/5.0"}

while True:
    sys.stdout.reconfigure(encoding='utf-8')
    res = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    nation = soup.select_one("h3.h_lst span.blind").get_text(strip=True)
    # print(nation) # 미국 USD

    # 환률값
    price = soup.select_one(".value").get_text(strip=True)
    # print(price)
    unit = soup.select_one(".txt_krw .blind").get_text(strip=True)
    # print(unit)
    change = soup.select_one(".change").get_text(strip=True)
    # print(change)
    updown = soup.select("div.head_info.point_up span.blind")[-1].get_text(strip=True)
    # print(updown)

    print(f"{nation.replace(' ','')} {price}{unit} {updown} {change}")
    time.sleep(5)