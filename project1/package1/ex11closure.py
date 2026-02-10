# 클로저 : Scope에 제약을 받지 않는 변수들을 포함하고 있는 코드 블럭이다. 
# 클로저는 내부함수가 있을때만 가능
# 내부 함수의 주소를 반환해 함수 밖에서 함수 내의 멤버를 참조하기

# def funcTimes(a,b):
#     c = a*b
#     return c
# print(funcTimes(2,3))

# k = funcTimes(2,3)
# print(k)
# k = funcTimes
# print(k)
# print(k(2,3))
# print(id(k), id(funcTimes))

# m = s = k
# del funcTimes # funcTimes 변수 삭제
# # print(funcTimes(2,3))
# print(m(2,3))

# def out():
#     count = 0
#     def inn():
#         nonlocal count  # 즉 nonlocal count 하면 아래의 count는 out()의 count이다
#         count += 1 # 이건 inn의 count이므로 inn지역변수
#         return count
#     print(inn())
# # print(count) 에러
# out()
# def outer():
#     count = 0
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#     return inner # 실행한 결과가 아니라 주소를 return : 클로저
# val1 = outer() # 내부함수 inner의 주소를 리턴 & 저장
# print(val1())
# print(val1())
# myval = val1()
# print(myval)
# print()
# var2 = outer()
# print(var2())
# print(var2())

# def outer2(tax):
#     def inner2(su, dan):
#         amount = su*dan*tax
#         return amount
#     return inner2
# # 1분기 tax 0.1
# q1 = outer2(0.1)
# re1 = q1(5,50000)
# print('result : ', re1)
# re2 = q1(2,10000)
# print('result : ', re2)
# print()
# # 2분기 0.05
# q2 = outer2(0.05)
# re3 = q2(5,50000)
# print('result : ', re3)
# print(list(filter(lambda x:x>5, range(10))))
# print(list(filter(lambda x:x%5==0 or x%7==0, range(1,101))))