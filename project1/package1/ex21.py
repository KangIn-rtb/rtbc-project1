kor = 100
def abc():
    print("모듈의 멤버 함수")
class My:
    kor = 80
    def abc(self):
        print('My 멤버 메소드')
    def show(self):
        kor = 77
        print(kor)
my = My()
my.show()