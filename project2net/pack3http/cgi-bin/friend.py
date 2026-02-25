import os
import urllib.parse
import sys
sys.stdout.reconfigure(encoding='utf-8')

# ---get/post요청 받을 때---
method = os.environ.get("REQUEST_METHOD","GET")
if method == "POST":
    length = int(os.environ.get("CONTENT_LENGTH",0))
    body = sys.stdin.read(length)
else:
    body = os.environ.get("QUERY_STRING","")

params = urllib.parse.parse_qs(body)

irum = params.get("name", [""])[0]
phone = params.get("phone", [""])[0]
gen = params.get("gen", [""])[0]

print('Content-Type: text/html; charset=utf-8')
print()

print(f"""
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>결과 페이지</title>
</head>
<body>
    <h2>전달받은 데이터 확인</h2>
    <ul>
        <li><b>이름:</b> {irum}</li>
        <li><b>전화번호:</b> {phone}</li>
        <li><b>성별:</b> {gen}</li>
    </ul>
    <a href="../index.html">메인으로 돌아가기</a>
</body>
</html>
""")