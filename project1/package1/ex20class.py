class car:
    handle = 0
    speed = 0
    
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        print("생성자 on")
        
    def showData(self):
        km = "킬로미터"
        msg = "속도" + str(self.speed)+km+str(self.handle)
        return msg
# print(car.handle) # 원형클래스의 멤버 호출
car1 = car('tom',10) # 생성자 호출 후 객체 생성(인스턴스화) 원형클래스를 이용한 새로운 객체
# print('car1 : ', car1.name,' ', car1.speed,' ',car1.handle)
# print()

car1.handle = 10
print(car1.showData())
car2 = car('mak', 10)
# car2.handle = 20
print(car2.showData())