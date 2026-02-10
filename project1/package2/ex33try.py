def divide(a, b):
    return a/b
print("작업 중...")


try:
    c = divide(5,0)
    print(c)
except ZeroDivisionError:
    print("두번째 값은 0을 주면 안됩니다.")
except Exception as err:
    print("Exception은 어떤 에러든지 에러가 뜨면 실행")

