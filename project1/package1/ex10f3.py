# 매개변수 유형
# 위치 매개변수 : 인수와 순서대로 대응
# 기본값 매개변수 : 매개변수에 입력값이 없으면 기본값 사용
# 키워드 매개변수 : 실인수와 가인수 간 동일 이름으로 대응
# 가변 매개변수 : 인수의 갯수가 동적인 경우

# def showGugu(start, end=3):
#     for dan in range(start, end + 1,1):
#         print(str(dan) + '단 출력')
#         for i in range(1,10):
#             print(str(dan)+ "*" + str(i) + "=" + str(dan * i), end=' ')
#         print()
# showGugu(2)
# print()
# showGugu(start= 1, end=3)
# showGugu(end = 3, start= 1)

# def fun1(*ar):
#     print(ar)
# fun1('김','밥','집')

# def func3(w,h,**other):
#     print(f"몸 : {w}, 키 : {h}")
#     print(f"기타 : {other}")
# func3(80, 180,irum = '신기루', nai = 23)

# def func4(a,b,*c,**d):
#     print(a,b)
#     print(c)
#     print(d)
# func4(1,2)
# func4(1,2,3,4,5)
# func4(1,2,3,4,5, k = 9, m = 11)

def tyF(num, data):
    print(num)
    print(data)
    result = {}
    for idx, item in enumerate(data, start=1):
        print(f"idx:{idx}, item:{item}")
        result[item] = idx
    return result
rdata = tyF(1, ['1','2','3'])
print(rdata)
