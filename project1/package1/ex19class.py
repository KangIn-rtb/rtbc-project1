class TestClass:
    aa = 1 #멤버필드 변수.현재 클래스 내에서 전역
    
    def __init__(self): # 특별한 메소드 : 이름->__init__ : 생성자 / 이름이 정해진 메소드 초기화 할게 없다면 안적어도 됨
        print('생성자 : 객체 생성시 가장 먼저 1회만 호출 - 초기화 담당')
        
    def __del__(self):  # call back Function 프로그램 끝날때 자동으로 호출
        print('소멸자 : 프로그램 종료시 자동 실행. 마무리 작업')
    
    def printMsg(self):  #일반 메소드 메소드는 반드시 argument를 가지고 있어야함 없으면 self 넣기 
        name = '한국인'
        print(name)

print(TestClass)
test = TestClass() # 객체 생성
print("test 객체의 멤버 aa : ", test.aa)
test.printMsg()     # 얘는 Bound Method call <- 얜 자동적으로 argument 들어감 객체변수가 이미 앞에 있어서 그게 argument로 들어감
TestClass.printMsg(test) # 얘는 unBound Method call <- 얜 argument 필요함
print(type(1))
print(type(1.0))
print(type(test))
print(id(test))
print(id(TestClass))
test2 = TestClass()
print(id(test2))
