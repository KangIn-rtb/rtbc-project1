import os
import sys
import io
from urllib import parse

# [필수] 지난번에 고생했던 한글 깨짐 방지 필살기
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

# 1. 환경변수에서 'QUERY_STRING' (주소창 데이터) 가져오기
# 예: "name=tom&age=23"
query = os.environ.get("QUERY_STRING", "")

# 2. 문자열 데이터를 파이썬 딕셔너리 형태로 변환
# 결과: {'name': ['tom'], 'age': ['23']}
params = parse.parse_qs(query)

# 3. 데이터 추출 (값이 없을 경우를 대비해 기본값 설정)
irum = params.get("name", ["이름없음"])[0]
nai = params.get("age", ["0"])[0]

# 4. 브라우저로 출력
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
        <li><b>나이:</b> {nai}세</li>
    </ul>
    <p>반갑습니다, {irum}님! {nai}살이시군요.</p>
    <br/>
    <a href="../index.html">메인으로 돌아가기</a>
</body>
</html>
""")