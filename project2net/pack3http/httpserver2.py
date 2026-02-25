
from http.server import HTTPServer, CGIHTTPRequestHandler

PORT = 8888

class Handler(CGIHTTPRequestHandler):
    cgi_directories = ['/cgi-bin']    

def run():
    serv = HTTPServer(('127.0.0.1', PORT), Handler)
    
    print("웹 서비스 진행중...")
    try:
        serv.serve_forever()
    except Exception as e:
        print('err : ',e)
        print("서버 종료")
    finally:
        serv.server_close()

if __name__ == "__main__":
    run()
        

