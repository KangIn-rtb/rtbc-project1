print("파일 처리 --------")
import os

try:
    print("파일 읽기 --------")
    print(os.getcwd())
    # f1 = open(os.getcwd() + r"\ftext.txt", encoding='utf-8')
    # f1 = open("ftext.txt",encoding="utf-8")
    f1 = open("ftext.txt", mode='r',encoding="utf-8")
    print(f1)
    print(f1.read())
    print("파일 저장 --------")
    f2 = open("ftext2.txt", mode="w",encoding="utf-8")
    f2.write("내 친구들\n")
    f2.write("홍길동, 한국인")
    f2.close()
    
    print("파일 내용 추가 ------")
    f3 = open("ftext2.txt", mode="a",encoding="utf-8")
    f3.write("\n 사오정")
    f3.write("\n 저팔계")
    f3.write("\n 손오공")
    f3.close()
    
    f4 = open("ftext2.txt", mode='r',encoding="utf-8")
    print(f4.read())
    f4.close()
except Exception as e:
    print("파일 처리 오류 : ", e)
