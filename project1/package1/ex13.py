# def countDown(n):
#     if n == 0:
#         print("완료")
#     else:
#         print(n,end=' ')
#         countDown(n-1)
# countDown(5)

def totFunc(n):
    if n == 0:
        print("탈")
        return 0
    return n+totFunc(n-1)
result = totFunc(10)
print(result)