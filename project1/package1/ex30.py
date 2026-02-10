class Tiger:
    data = "호랑이"
    
    def cry(self):
        print('호랑이 : 어흥')
        
    def eat(self):
        print("맹수는 고기")
class Lion:
    def cry(self):
        print("사자 : 으르렁")
    
    def hobby(self):
        print("백수의 왕은 낮잠이 취미")
        
# class Liger1(Tiger,Lion):
#     pass

# a1 = Liger1()
# print(a1.data)
# a1.eat()
# a1.hobby()
# a1.cry()
def hobby():
    print("모듈 멤버 : 일반 함수")

class Liger2(Lion,Tiger):
    data = "라이거 만세"
    
    def play(self):
        print("라이거 고유 메소드")
    def hobby(self):
        print("라이거는 공원 걷기를 좋아함")
    def showData(self):
        self.hobby()
        super().hobby()
        hobby()
        
        self.eat()
        super().eat()
        print(self.data + ' '+ super().data)
a2 = Liger2()
a2.cry()
a2.showData()