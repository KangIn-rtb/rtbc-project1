import socket
import sys

# HOST = '127.0.0.1'
HOST = '' # 알아서 본인 컴의 ip주소가 들어감
PORT = 7788
serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serversock.bind((HOST, PORT))
    serversock.listen (5)
    print('서버(무한 루프) 서비스중...')
    
    while True:
        conn, addr = serversock.accept()
        print('client info : ',addr[0],' ',addr[1])
        print('client message : ',conn.recv(1024).decode())
        # 메세지 송신
        conn.send(('from server : '+str(addr[1])+' 너도 잘 지내').encode('utf_8'))
        
except Exception as e:
    print('err : ', e)
    sys.exit()
finally:
    conn.close()
    serversock.close()