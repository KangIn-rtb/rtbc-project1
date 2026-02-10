class Person:
    say = "난 사람이야~"
    nai = "20"
    
    def __init__(self,nai):
        print("person 생성")
        self.nai = nai
        
    def printInfo(self):
        print(f"나이 : {self.nai}, 이야기 : {self.say}")
        
    def helloMethod(self):
        print("안녕")

print(Person.say, Person.nai)
# H = Person(10)
# H.printInfo()
