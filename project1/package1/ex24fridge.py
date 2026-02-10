class Fridge:
    isopen = False
    foods = []
    def open(self):
        self.isopen = True
        print("냉장고 문 열기")
    def close(self):
        self.isopen = False
        print("냉장고 문 닫기")
    def foodlist(self):
        for f in self.foods:
            print(f' - {f.name} {f.expiry_date}')
        print()
    def put(self, thing):
        if self.isopen:
            self.foods.append(thing)
            print(f'냉장고에 {thing.name} 넣음')    
            self.foodlist()
        else:
            print("냉장고 문이 닫혀있음")

class FoodData:
    def __init__(self, name, expiry_date):
        self.name = name
        self.expiry_date = expiry_date

fobj = Fridge()
apple = FoodData('사과','2026-08-01')
cola = FoodData('콜라','2027-11-01')
fobj.open()
fobj.put(apple)
fobj.put(cola)
fobj.close()

