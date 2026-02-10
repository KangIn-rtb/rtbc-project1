# 여러 개의 부품 객체를 조립해 완성차 생성
# 클래스의 포함 관계 사용(자원의 재활용)
# 다른 클래스를 마치 자신의 멤버 처럼 선언하고 사용

from ex23handle import PohamHandle

class PohamCar:
    turnShowMessage = "정지"
    
    def __init__(self, ownerNmae):
        self.ownerName = ownerNmae
        self.handle = PohamHandle()
        
    def turnHandle(self, q):
        if q > 0:
            self.turnShowMessage = self.handle.rightTurn(q) # 위에 __init__ 에서 self.handle = PohamHandle()
            # 이후 PohamHandle()의 메소드인 rightTurn 불러오기 가능
        elif q < 0:
            self.turnShowMessage = self.handle.leftTurn(q)
        elif q == 0:
            self.turnShowMessage = self.handle.straight(q)

if __name__ =='__main__':
    tom = PohamCar('Tom')
    tom.turnHandle(10)
    print(tom.ownerName + '의 회전량은 ' + tom.turnShowMessage +' ' +str(tom.handle.quantity))
    
    jon = PohamCar('jon')
    jon.turnHandle(-20)
    print(jon.ownerName + '의 회전량은 ' + jon.turnShowMessage +' ' +str(jon.handle.quantity))

    jon.turnHandle(0)
    print(jon.ownerName + '의 회전량은 ' + jon.turnShowMessage +' ' +str(jon.handle.quantity))