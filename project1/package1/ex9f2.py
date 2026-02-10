# def doF1():
#     print("HI")
#     return 0

# print(doF1)
# imsi = doF1
# # imsi = doF1() 이건 결과 값 즉 return값을 저장
# imsi()

# print(doF1())

# def tri(a,b):
#     c = a*b/2
#     triAP(c)

# def triAP(cc):
#     print("삼각형 면적 : ",cc)

# tri(20,30)

# def passR(kor,eng):
#     ss = str(kor) + '+' + str(eng) + '=의 합 입력'
#     ans = input(ss)
#     return 

# def funcTest():
#     print('funTest멤버 처리')
#     def funcInner():
#         print("내부함수")
#     funcInner()
# funcTest()

# def isodd(para):
#     return para % 2 == 1

# mydict = {x:x*x for x in range(11) if isodd(x)} 
# print(mydict)

# player = "전국대표"
# name = "한국인"
# def funcSoccer():
#     name = '홍길동'
#     player = "지역대표"
#     print(f"name {name} grade {player}")
# funcSoccer()
# print(f"name : {name} grade : {player}")

# a,b,c = 10,20,30
# def Foo():
#     a = 7
#     b = 100
#     def Bar():
#         global c
#         nonlocal b
#         b = 8
#         print(f"Bar 함수 수행 후 a:{a} b:{b} c:{c}")
#         c = 9
#     Bar()
# Foo()
# print(f"함수 수행 후 a:{a} b:{b} c:{c}")

g = 1
def func():
	global g
	a = g
	g = 2
	return a
print(func())
print(g)