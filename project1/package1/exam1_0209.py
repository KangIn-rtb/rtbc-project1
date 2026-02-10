# 1
# li = [1, 2, 2, 2, 3, 4, 5, 5, 5, 2, 2]
# im = set(li)
# li = list(im)
# print(li)

#2
# for i in {1, 2, 3, 4, 5, 5, 5, 5}:
#     print(i, end = ' ')

#3
# count = 0
# S = 0
# for i in range(1,101):
#     if i % 3 == 0 or i % 4 == 0:
#         if i % 7 != 0:
#             print(i, end = ' ')
#             S += i
#             count += 1
# print("\n건수 : ", count)
# print("배수의 총합 : ", S)

#4
"""
제어문과 함수 등을 이용하여 반복 처리를 할 수 있다. 이 때 사용할 수 있는 명령문이나 함수를 아는 대로 적으시오
while , for
"""
# def Re(n):
#     if n == 1:
#         return 1
#     else:
#         return n+Re(n-1)

#5
# 나눗셈 연산자 차이

#6
# a = 1.5; b = 2; c = 3
# def Kbs():
#     a = 20
#     b = 30
#     def Mbc():
#         global c
#         nonlocal b
#         print("Mbc 내의 a:{}, b:{}, c:{}".format(a, b, c))
#         c = 40
#         b = 50
#     Mbc()
# Kbs()

#7
# *v1, v2, v3 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
# print(v1)
# print(v2)
# print(v3)

#8
# def Hap(m, n):
#   return m + n * 5
# print(Hap(1,2))
# print((lambda m,n : m+n*5)(1,2))

#9
# print(list(range(6, 1, -1)))

#10
# try:
#     aa = int(input())
#     bb = 10 / aa
#     print(bb)
# except Exception as err:
#     print("ERROR : ",err)

#11
# for i in range(10):
#     print(f"{"*"*(10-i):>10}")

#12
# year = int(input("연도 입력:"))
# if year % 4 == 0:
#     if year % 100 != 0 or year % 400 == 0:
#         print(f"{year}년은 윤년")
#     else:
#         print(f"{year}년은 평년")  
# else:
#     print(f"{year}년은 평년")    

#13
# i = 0
# while True:
#     if list(str(i))[-1] != "3":
#         i += 1
#         continue
#     if i > 100:break    
#     print(i, end=' ')
#     i += 1

#14
# f_i = 3
# b_i = 1
# while True:
#     print(f"{f_i}*{b_i}={f_i*b_i}", end=' ')
#     if b_i == 9:
#         f_i += 2
#         b_i = 0
#         print()
#         if f_i == 11:
#             break
#     b_i += 1

#15
# class Bicycle:
#     name = "이름"
#     wheel = 0
#     price = 0
    
#     def __init__(self, name, wheel, price):
#         self.name = name
#         self.wheel = wheel
#         self.price = price
    
#     def display(self):
#         total = self.wheel*self.price
#         return print(f"길동님 자전거 바퀴 가격 총액은 {total}원 입니다.")
# gildong = Bicycle('길동', 2, 50000) # 생성자로 name, wheel, price 입력됨
# gildong.display()