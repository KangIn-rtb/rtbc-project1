# 1
# L = [i for i in range(101) if i%3==0 and i%2 != 0]
# print(*L)
# print(sum(L))

# 2
# for i in range(2,6):
#     for j in range(1,10):
#         print(f"{i}X{j}={i*j}")

# 3
# s = 0
# for i in range(1, 101):
#     if i%2 == 0:
#         s += i
#     elif i%2 != 0:
#         s -= i
# print(s)

# 4
# L = [i for i in range(100) if i%2 != 0]
# for i in range(len(L)):
#     if i%2 ==0:
#         L[i] = -L[i]
# print(sum(L))

# 5
# for i in range(1,101):
#     L = list(map(lambda x : int(x),list(str(i))))
#     if sum(L) >= 10:
#         print(*L,sep='')

# # 6
# s = 0
# i = 1
# while s < 1000:
#     s += i
#     i += 1
# print(i-1)
# print(s)

# #7
# for i in range(1,10):
#     for j in range(1,10):
#         if i*j > 30:
#             break
#         print(f"{i}X{j}={i*j}")

# #8
# count = 0
# for i in range(2,1001):
#     flag = 0
#     for j in range(2,i-1):
#         if i%j == 0:
#             flag = 1
#             break
#     if flag == 0:
#         print(i)
#         count += 1
# print(count)

# #9
# for i in range(1,51):
#     if i%3 == 0:
#         continue
#     print(i)

# #10
# s = 0
# for i in range(1,101):
#     if i%4 == 0 or i%6 == 0:
#         continue
#     if i%5 == 0:
#         print(i)
#         s += i
# print(s)

# # 11
# def inputfunc():
#     datas = [
#         [1, "강나루", 1500000, 2010],
#         [2, "이바다", 2200000, 2018],
#         [3, "박하늘", 3200000, 2005],
#     ]
#     return datas

# def processfunc(datas):
#     print("사번  이름    기본급   근무년수 근속수당 공제액   수령액")
#     print("--------------------------------------------------------------")
#     i = 0
#     while i<len(datas):
#         geunyen = 2026-datas[i][3]
#         if 1 <= geunyen <= 3:
#             geunsok = 150000
#         elif 4 <= geunyen <= 8:
#             geunsok = 450000
#         elif 9 <= geunyen:
#             geunsok = 1000000

#         geupye = datas[i][2]+geunsok
#         if geupye < 2000000:
#             gongje = 0.15*geupye
#         elif 2000000 <= geupye < 3000000:
#             gongje = 0.3*geupye
#         elif 3000000 < geupye:
#             gongje = 0.5*geupye

#         su = geupye-gongje

#         print(f" {datas[i][0]}   {datas[i][1]}   {datas[i][2]}     {geunyen:>2}     {geunsok:>7} {gongje:7.0f}  {su:7.0f}")
#         i += 1
#     print(f"처리건수 :{i}건")
# processfunc(inputfunc())

# 12
# def inputfunc():
#     datas = [
#         "새우깡,15",
#         "감자깡,20",
#         "양파깡,10",
#         "새우깡,30",
#         "감자깡,25",
#         "양파깡,40",
#         "새우깡,40",
#         "감자깡,10",
#         "양파깡,35",
#         "새우깡,50",
#         "감자깡,60",
#         "양파깡,20",
#     ]
#     return datas

# def outputF(datas):
#     print("상품명   수량   단가   금액")
#     print("-------------------------------")
#     i = 0
#     amount_se = 0
#     amount_gam = 0
#     amount_yang = 0
#     g_se = 0
#     g_gam = 0
#     g_yang = 0
#     while i < len(datas):
#         name, amount = datas[i].split(',')
#         amount = int(amount)
#         if name == "새우깡":
#             danga = 450
#             amount_se += amount
#             g_se += danga*amount
#         elif name == "감자깡":
#             danga = 300
#             amount_gam += amount
#             g_gam += danga*amount
#         elif name == "양파깡":
#             danga = 350
#             amount_yang += amount
#             g_yang += danga*amount
#         geum = danga*amount
#         print(f"{name}   {amount}   {danga}   {geum}")
#         i += 1
#     print()
#     print("소계")
#     print(f"새우깡 : {amount_se}  소계액 : {g_se}")
#     print(f"감자깡 : {amount_gam}  소계액 : {g_gam}")
#     print(f"양파깡 : {amount_yang}  소계액 : {g_yang}")
#     print("총계")
#     print(f"총 건수 : {amount_yang+amount_gam+amount_se}")
#     print(f"총 액 : {g_gam+g_se+g_yang}")


# outputF(inputfunc())


# 재귀로 최대값 구하기 -> len_v 를 v에 넣고 1이 될때까지 호출
# v = [7,9,15,43,32,21]
# def find_max(v,len_v):
#     if len_v == 1:
#         return v[0]
#     max_v = find_max(v,len_v-1)
#     if max_v > v[len_v-1]:
#         return max_v
#     else:
#         return v[len_v-1]
# print(find_max(v,len(v)))

# class CoinIn:
#     coin = 0
#     change = 0
#     cup = 0
#     COFFEE = 200
#     def __init__(self):
#         print("-"*30)
#         """
#         내가 기존에 짠 코드 
#         self.__init__()를 함으로서 재귀 한도에 걸릴 수 있음
#         -> 따라서 while문으로 개선함.
#         self.coin = int(input("코인을 넣어주세요 : "))
#         if self.coin < 200:
#             print("요금이 부족합니다 200원 이상 넣으세요.")
#             self.__init__()
#         """
#         while self.coin < 200:
#             self.coin = int(input("코인을 넣어주세요 : "))
#             if self.coin < 200:
#                 print("200원 이상 넣어주세요.")
#         self.cup = int(input("몇 잔을 원하세요 : "))
#     def culc(self, cup):
#         self.change = self.coin - self.COFFEE*self.cup
#         if self.change < 0:
#             print("금액이 부족합니다!!")
#             exit()

# class Machine:
#     cupCount = 1
#     def __init__(self):
#         self.coinin = CoinIn()
#         self.cupCount = self.coinin.cup
#         self.coinin.culc(self.cupCount)
#     def showData(self):
#         print(f"커피 {self.cupCount}잔과 잔돈 {self.coinin.change}원")
        
# if __name__ == "__main__":
#     human = Machine()
#     human.showData()

"""
제미니 코드
class CoinIn:
    def __init__(self):
        self.coin = 0
        self.change = 0
        self.COFFEE = 200
    def culc(self, cupCount):
        # 다이어그램의 culc(cupCount)를 반영
        self.change = self.coin - (self.COFFEE * cupCount)
        return self.change
class Machine:
    def __init__(self):
        # 1. 포함 관계: CoinIn 객체를 생성하여 멤버로 보유
        self.coinin = CoinIn()
        self.cupCount = 0
    def showData(self):
        # 2. 키보드 입력 로직 (요구사항 반영)
        self.coinin.coin = int(input("동전을 입력하세요 : "))
        
        # 100원 넣고 커피 요구 시 요금 부족 메시지 (조건 반영)
        if self.coinin.coin < 200:
            print("요금이 부족합니다.")
            return
        self.cupCount = int(input("몇 잔을 원하세요 : "))
        
        # 3. 계산 수행
        change = self.coinin.culc(self.cupCount)
        # 4. 잔돈 확인 및 출력
        if change < 0:
            print("요금이 부족합니다.")
        else:
            print(f"커피 {self.cupCount}잔과 잔돈 {change}원")
if __name__ == "__main__":
    vending_machine = Machine()
    vending_machine.showData()
"""
# 클래스 2번
# class ElecProduct:
#     volume = 0
    
#     def volumeControl(self,volume):
#         print("super class method volume : ", self.volume)

# class ElecTv(ElecProduct):
#     def volumeControl(self, volume):
#         self.volume = volume
#         print("ElecTv volume : ",self.volume)
# class ElecRadio(ElecProduct):
#     def volumeControl(self, volume):
#         self.volume = volume
#         print("ElecRadio volume : ",self.volume)
        
# tv = ElecTv()
# radio = ElecRadio()
# tv.volumeControl(100)
# radio.volumeControl(50)


#클래스 3번
# class Animal:
#     def move(self):
#         print("동물의 움직임")

# class Cat(Animal):
#     name = "고양이"
#     def move(self):
#         print("고양이 움직임")
# class Dog(Animal):
#     name = "개"
#     def move(self):
#         print("개 움직임")
        
# class Wlof(Dog, Cat):
#     pass

# class Fox(Cat, Dog):
#     def move(self):
#         print("여우 움직임")
#     def foxmethod(self):
#         print("여우 행동 양식")


# animal = [Dog(), Cat(), Wlof(), Fox()]
# for a in animal:
#     print(a.name + ' ')
#     a.move()
#     # if a.foxmethod:
#     #     print(a.foxmethod)
# af = Fox()
# af.foxmethod()

from abc import *  

class Employee(metaclass=ABCMeta):
    def __init__(self, irum, nai):
        self.irum = irum
        self.nai = nai
        
    @abstractmethod
    def pay(self):
        pass
    @abstractmethod
    def data_print(self):
        pass
    
    def irumnai_print(self):
        print("이름 : "+self.irum+" 나이 : "+ str(self.nai), end=' ')
        
        
class Temporary(Employee):
    ilsu = 0
    ildang = 0
    def __init__(self, irum, nai, ilsu, ildang):
        Employee.__init__(self, irum, nai)
        self.ilsu = ilsu
        self.ildang = ildang
    def pay(self):
        return self.ilsu*self.ildang
    def data_print(self):
        self.irumnai_print()
        print(f", 월급 : {self.pay():.0f}")
        
class Regular(Employee):
    salary = 0
    def __init__(self,irum,nai,salary):
        Employee.__init__(self, irum, nai)
        self.salary = salary
    def pay(self):
        return self.salary
    def data_print(self):
        self.irumnai_print()
        print(f", 급여 : {self.pay():.0f}")
    
class Salesman(Regular):
    sales = 0
    commission = 0
    def __init__(self,irum,nai,salary,sales,commision):
        super().__init__(irum,nai,salary)
        self.sales = sales
        self.commission = commision

    def pay(self):
        return self.salary + (self.sales*self.commission)
    def data_print(self):
        self.irumnai_print()
        print(f", 수령액 : {self.pay():.0f}")

t = Temporary("홍길동",25,20,150000)
r = Regular("한국인", 27, 3500000)
s = Salesman("손오공", 29, 1200000, 5000000, 0.25)

t.data_print()
r.data_print()
s.data_print()