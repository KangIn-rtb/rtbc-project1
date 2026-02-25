
# socket 통신 확인
import socket 
print(socket.getservbyname('http','tcp')) # www 환경 
print(socket.getservbyname('ssh','tcp'))  # 원격 컴 접속
print(socket.getservbyname('ftp','tcp'))  # 파일 전송
print(socket.getservbyname('smtp','tcp')) # 메일 송수신
print(socket.getservbyname('pop3','tcp')) # 이메일 

# 특정 웹서버의 ipaddress 확인
print(socket.getaddrinfo('www.naver.com',80, proto = socket.SOL_TCP))
