# 일회용 서버 

from socket import *
# socket 객체 생성
serversock = socket(AF_INET, SOCK_STREAM) # address femily의 INET을 사용 
# socket을 특정 컴과 바인딩 
serversock.bind(('127.0.0.1', 8888)) # 튜플로 작성 / ip 주소, 포트
serversock.listen (5) # 클라이언트와 연결 정보 수 1~5 까지 / 리스너 설정
print('서버 서비스중...')
conn, addr = serversock.accept() # 요청이 있다면 기다리다가 받음 / 수동적으로 연결을 받아들임 
print('client addr : ', addr )
print('from client message : ', conn.recv(1024).decode()) # 클라이언트 메세지 받기(recv) 버퍼 크기는 1바이트 메세지 받고 binary를 decode 해독 하기
conn.close()
serversock.close()