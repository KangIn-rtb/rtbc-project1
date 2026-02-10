#함수 장식자
#기존 함수 코드를 고치지 않고 함수의 앞/뒤 동작을 추가하기
#함수를 받아서 

# def make2(fn):
#     return lambda:"안녕 " + fn()
# def make1(fn):
#     return lambda:"반가워 " + fn()
# def hello():
#     return "홍길동"

# hi = make2(make1(hello))
# print(hi())
# print()
# @make2
# @make1
# def hello2():
#     return "신기해"
# print(hello2())

# @make1
# @make2
# def hello2():
#     return "신기해"
# print(hello2())

def traceF(func):
    def wrapperF(a,b):
        r = func(a,b)
        print(f"함수명:{func.__name__} (a={a}, b={b}) -> {r}")
        return r
    return wrapperF
@traceF
def addF(a,b):
    return a + b
print(addF(10,20))