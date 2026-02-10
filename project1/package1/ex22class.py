class Singer:
    title_song = "빛나라 대한민국"
    name = "가수 이름"
    
    def sing(self):
        msg = "노래는"
        print(self.co, self.name, msg, self.title_song)


gasu = Singer()
gasu.name = input("가수 이름 입력 : ")
gasu.title_song = input("노래제목 입력 : ")
gasu.co = input("소속사 입력 : ") # gasu만 가지고 있는 멤버변수
gasu.sing()

gasu2 = Singer()
gasu2.name = input("가수 이름 입력 : ")
gasu2.title_song = input("노래제목 입력 : ")
gasu2.co = input("소속사 입력 : ") # gasu만 가지고 있는 멤버변수
gasu2.sing()

