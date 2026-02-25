import sys
sys.stdout.reconfigure(encoding='utf-8')

ss = "파이썬 자료 출력"
# print(ss) 개발자가 자신의 컴 표준 출력 장치로 값 확인
# 클라이언트 브라우저로 출력
ss2 = 123
print('Content-Type:text/html;charset=utf-8')
print()
print("<html><head><meta charset='UTF-8'></head><body>")
print("<b>안녕 파이썬 모듈로 작성한 문서야</b><br/>")
print("파이썬 변수 값 : %s, %d" %(ss, ss2))
print("</body></html>")