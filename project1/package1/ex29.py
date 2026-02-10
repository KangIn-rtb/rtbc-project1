class Parent:
    def printData(self):
        pass



class Child1(Parent):
    def abc():
        pass
    def printData(self):
        print("Child1에서 printData override")
        msg = "부모와 동일 메소드 명이나 내용은 다르다"
        print(msg)
        
        
class Child2(Parent):
    def printData(self):
        print("Child2에서 printData override")
        msg = "부모와 동일 메소드 명이나 내용은 다르다"
        print(msg)

c1 = Child1()
c2 = Child2()
c1.printData()
print()
c2.printData()
print("\n 다형성-----")
par = Parent()
par = c1
par.printData()
print()
par = c2
par.printData()
print("-------------")
imsi = c1
imsi.printData()
imsi = c2
imsi.printData()