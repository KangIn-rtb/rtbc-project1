class Animal:
    age = 1
    def __init__(self):
        print("Animal 생성자")

    def move(self):
        print("움직이는 생물")

class Dog(Animal): # 상속
    def __init__(self):
        print("Dog 생성자")
        
    def my(self):
        print("댕댕이")
        
dog1 = Dog()
dog1.my()
dog1.move()
print("age : ", dog1.age)
class Horse(Animal):
    pass
horse1 = Horse()
horse1.move()
