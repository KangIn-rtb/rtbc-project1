from abc import *

class AbstractClass(metaclass=ABCMeta):  #추상클래스
    
    @abstractmethod
    
    def abcMethod(self):     #추상메소드
        pass
    
    def normalMethod(self):  #일반메소드
        print('추상클래스 내의 일반 메소드')

# parent = AbstractClass() # 에러

class Child1(AbstractClass):
    name = "난 Child1"

    def abcMethod(self):
        print("abcMethod를 오버라이드함")
c1 = Child1()
print("name : ", c1.name)

class Child2(AbstractClass):
    def abcMethod(self):
        print("추상 클래스 내의 abcMethod 재정의")
        
    def normalMethod(self):
        print("일반 메소드 내 맘대로 내용 변경")

c2 = Child2()
c2.abcMethod()
c2.normalMethod()
print("-"*20)
happy = c1
happy.abcMethod()
happy = c2
happy.abcMethod()