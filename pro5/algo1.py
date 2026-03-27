# 1부터 N 까지 연속한 숫자의 합을 구하는 알고
# def sum_n():
#     n = int(input())
#     s = 0
#     for i in range(n+1):
#         s += i
#     print(s)
#     return s
# def sum_n2():
#     n = int(input())
#     s = (n/2)*(n+1)
#     print(int(s))
#     return s
# sum_n()
# sum_n2()

# print("최대값 구하기 ---")
# d = list(map(int,input().split()))
# def find_max(d):
#     n = len(d)
#     max_v = d[0]
#     for i in range(1,n):
#         if d[i] > max_v:
#             max_v = d[i]
#     return max_v
# print(find_max(d))

# print("최대 공약수 -- 유클리드 호제법")
# a,b = map(int,input().split())
# def ucle(a,b):
#     while b != 0:
#         a,b = b,a%b # 뭐가 큰지 중요하지 않은게 어짜피 정렬됨
#                     # 4 6 이면 한번 돌때 6 4 됨 
#     return a
# print(ucle(a,b))

