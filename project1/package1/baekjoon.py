"""
import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    k = int(input()) # 층 (stair)
    n = int(input()) # 호 (room)

    # 0층 초기화: 1호부터 n호까지 [1, 2, 3, ..., n]
    f0 = [i for i in range(1, n + 1)]

    # k층까지 올라가며 리스트 업데이트
    for _ in range(k):
        for i in range(1, n): # 2호(인덱스 1)부터 끝까지
            # 핵심: 현재 호수 사람 수 = 이전 호수까지의 합 + 내 아랫집 사람 수
            # 사실상 리스트 안에서 누적 합을 구하는 것과 같습니다.
            f0[i] += f0[i-1]

    print(f0[n-1])
"""

"""
import sys
input = sys.stdin.readline

N = int(input())
stack = []
for i in range(N):
    comand = list(input().split())
    if comand[0] == "push":
        stack.append(int(comand[1]))
    elif comand[0] == "pop":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack.pop())
    elif comand[0] == "size":
        print(len(stack))
    elif comand[0] == "empty":
        if len(stack) == 0:
            print("1")
        else:
            print("0")
    elif comand[0] == "top":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[-1])
"""
"""
A = int(input())
B = int(input())
C = int(input())
re = list(str(A*B*C))

for i in range(10):
    re = list(map(lambda x : int(x), re))
    print(re.count(i))
"""
"""
N = int(input())
pro = N
sol = 0
count = 0
A = 0
while 1:
    A = N//10 + N%10
    sol = A%10 + (N%10)*10
    N = sol
    count += 1
    if sol == pro:
        break
print(count)
"""
"""
pibo = [0, 1]
N = int(input())
for i in range(2, N+1):
    pibo.append(pibo[i-1]+pibo[i-2])
print(pibo[N])
"""
"""
A, B = input().split()
A = list(A)
B = list(B)
A[0], A[2] = A[2], A[0]
B[0], B[2] = B[2], B[0]
A = list(map(lambda x : int(x),A))
B = list(map(lambda x : int(x),B))
A_n = A[0]*100+A[1]*10+A[2]
B_n = B[0]*100+B[1]*10+B[2]
if A_n>B_n:
    print(A_n)
else:
    print(B_n)
"""
"""
T = int(input())
for _ in range(T):
    cont = 1
    H, W, N = map(int,input().split())
    while N>H:
        N -= H
        cont += 1
    print(N*100+cont)
"""
"""
human = int(input())
dung = [list(map(int,input().split())) for _ in range(human)]
grade = []
for i in range(human):
    rank = 1
    for j in range(human):
        if dung[i][0] < dung[j][0] and dung[i][1] < dung[j][1]:
            rank += 1
    grade.append(rank)
print(*grade)
"""
"""
ascending = [1,2,3,4,5,6,7,8]
descending = [8,7,6,5,4,3,2,1]
L = list(map(int,input().split()))
if L == ascending:
    print("ascending")
elif L == descending:
    print("descending")
else:
    print("mixed")
"""
# N, M = map(int,input().split())
# L = [i for i in range(1,N+1)]
# for i in range(M):
#     a,b = map(int,input().split())
#     L[a-1:b] = L[a-1:b][::-1]
# print(*L)
# N, K = map(int,input().split())
# L = [i for i in range(1,N+1)]
# sol = []
# idx = 0
# while len(L)>0:
#     idx += K-1
#     while idx >= len(L):
#         idx -= len(L)
#     sol.append(L.pop(idx))
# print(f"<{', '.join(map(str,sol))}>")


# def fac(N):
#     if N <= 1:
#         return 1
#     else:
#         return N * fac(N - 1)


# N, K = map(int, input().split())
# E = fac(N) // (fac(N - K) * fac(K))
# print(E)

# matrix = [list(map(int,input().split())) for _ in range(9)]
# sol_max = -1
# sol_r = 0
# sol_c = 0
# for r, row in enumerate(matrix):
#     rmax = max(row)
#     if rmax > sol_max:
#         sol_max = rmax
#         sol_r = r
#         sol_c = row.index(rmax)
# print(sol_max)
# print(sol_r+1, sol_c+1)

# from collections import deque
# import sys 
# input = sys.stdin.readline
# dp = deque()
# N = int(input())
# for _ in range(N):
#     command = list(input().split())
#     if command[0] == "push_front":
#         dp.appendleft(int(command[1]))
#     elif command[0] == "push_back":
#         dp.append(int(command[1]))
#     elif command[0] == "pop_front":
#         if len(dp) == 0:
#             print("-1")
#         else:
#             print(dp.popleft())
#     elif command[0] == "pop_back":
#         if len(dp) == 0:
#             print("-1")
#         else:
#             print(dp.pop())
#     elif command[0] == "size":
#         print(len(dp))
#     elif command[0] == "empty":
#         if len(dp) == 0:
#             print("1")
#         else: 
#             print("0")
#     elif command[0] == "front":
#         if len(dp) == 0:
#             print("-1")
#         else: 
#             print(dp[0])    
#     elif command[0] == "back":
#         if len(dp) == 0:
#             print("-1")
#         else: 
#             print(dp[len(dp)-1])

# while True:
#     N = list(input())
#     if N[0] == "0":
#         break
#     elif N == N[::-1]:
#         print("yes")
#     else:
#         print("no")

# from collections import deque
# T = int(input())
# for i in range(T):
#     count = 1
#     amount, where_idx = map(int,input().split())
#     print_que = deque(list(map(int,input().split())))
#     print_que[where_idx] = str(print_que[where_idx])
#     while True:
#         if int(print_que[0]) != max(list(map(lambda x:int(x),print_que))):
#             print_que.append(print_que.popleft())
#         elif type(print_que[0]) == type("str_check"):
#             print(count)
#             break
#         else:
#             print_que.popleft()
#             count += 1
"""
제미니 팁 적용
"""
# from collections import deque
# T = int(input())
# for i in range(T):
#     count = 1
#     amount, where_idx = map(int,input().split())
#     val_list = list(map(int,input().split()))
#     print_que = deque((val,idx) for idx,val in enumerate(val_list))
#     val_list.sort(reverse=True)
#     while print_que:
#         cur_val, cur_idx = print_que[0]
#         if cur_val == val_list[0]:
#             if cur_idx == where_idx:
#                 print(count)
#                 break
#             print_que.popleft()
#             val_list.pop(0)
#             count += 1
#         else:
#             print_que.append(print_que.popleft())

# import sys, math
# from collections import Counter
# input = sys.stdin.readline
# N = int(input())
# L = list(int(input()) for _ in range(N))
# # 1. 산술평균 : 평균
# sanavr = sum(L)/len(L)
# print(f"{math.floor(sanavr+0.5):.0f}")
# # 2. 중간값 : sort 후 중간값 
# middle_L = sorted(L)
# middle = middle_L[N//2]
# print(middle)
# # 3. 최빈값 : 많이 나온거. 여러개면 2번째 작은거
# ######################################
# L = sorted(L)
# fri_max = sorted(list(set(L))) # [1, 2,2,2, 3, 8,8,8,8,] -> [1,2,3,8] 중복 삭제 후 정렬
# count = []
# for i in range(len(fri_max)):
#     count.append(L.count(fri_max[i]))
# max_count = max(count)
# mode = []
# for i in range(len(fri_max)):
#     if count[i] == max_count:
#         mode.append(fri_max[i])
# if len(mode) > 1:
#     print(mode[1])
# else:
#     print(mode[0])
    
# #########################################

# if len(L) == 1:
#     print(0)
# else:
#     print(max(L)-min(L))

# import sys

# input = sys.stdin.readline
# N = int(input())
# L = [int(input()) for _ in range(N)]
# L.sort() # 모든 계산의 기초

# # 1. 산술평균 (수동 반올림)
# avg = sum(L) / N
# if avg >= 0:
#     print(int(avg + 0.5))
# else:
#     print(int(avg - 0.5))

# # 2. 중앙값
# print(L[N // 2])

# # 3. 최빈값 (딕셔너리로 직접 구현)
# counts = {}
# for x in L:
#     counts[x] = counts.get(x, 0) + 1 # x가 없으면 0으로 시작

# max_f = max(counts.values())
# modes = []
# for key, val in counts.items():
#     if val == max_f:
#         modes.append(key)

# modes.sort() # 최빈값이 여러 개일 수 있으니 정렬
# if len(modes) > 1:
#     print(modes[1])
# else:
#     print(modes[0])
# # 4. 범위
# print(L[-1] - L[0])


# days = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
# week = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
# day_sum = 0
# M, D = map(int,input().split())
# for i in range(1,M):
#     day_sum += days[i]
# day_sum += D - 1 
# while day_sum >= len(week):
#     day_sum -= 7
# print(week[day_sum])


# from collections import defaultdict, deque
# N, M, V = map(int,input().split())
# load = defaultdict(list)
# for _ in range(M):
#     a, b = map(int,input().split())
#     load[a].append(b)
#     load[b].append(a) # 양방향 길 만들기 
# for key in load:
#     load[key].sort() # 낮은 수 부터 방문
# #1 DFS
# def dfs(v):
#     visited[v] = True
#     print(v, end= ' ')
#     for node in load[v]:
#         if not visited[node]:
#             dfs(node)
# #2 BFS
# def bfs(V):
#     queue = deque([V])
#     visited[V] = True
#     while queue:
#         V = queue.popleft()
#         print(V, end=' ')
#         for node in load[V]:
#             if not visited[node]:
#                 queue.append(node)
#                 visited[node] = True        
# visited = [False]*(N+1) # 방문 노드 0은 안씀 편의 위해 N+1 해서 맞춤    
# dfs(V)
# visited = [False]*(N+1) # 방문 노드 0은 안씀 편의 위해 N+1 해서 맞춤
# print()
# bfs(V)


# from collections import deque
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# N,M = map(int,input().split())
# L = [list(map(int, input().strip())) for _ in range(N)]
# def bfs(x,y):
#     queue = deque([(x,y)])
#     while queue:
#         x,y = queue.popleft()
#         if x == N-1 and y == M-1:
#             return L[x][y]
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < N and 0 <= ny < M and L[nx][ny] == 1:
#                 L[nx][ny] = L[x][y] + 1
#                 queue.append((nx,ny))
# print(bfs(0,0))


# from collections import defaultdict
# load = defaultdict(list)
# N = int(input())
# connection = int(input())
# for i in range(connection):
#     a, b = map(int,input().split())
#     load[a].append(b)
#     load[b].append(a)
# visit = [0]*(N+1)
# # count = 0
# def dfs(v):
#     visit[v] = 1
#     # count += 1
#     for node in load[v]:
#         if visit[node] == 0:
#             dfs(node)
# dfs(1)
# print(visit.count(1)-1)


# from collections import deque
# N = int(input())
# home = [list(map(int,input().strip())) for _ in range(N)]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# count = 2
# ans = []
# def bfs(x,y):
#     queue = deque([(x,y)])
#     queue_vist = deque()
#     home[x][y] = count
#     home_count = 1
#     while queue:
        
#         x, y = queue.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0<=nx<N and 0<=ny<N and home[nx][ny] == 1:
#                 home[nx][ny] = count
#                 queue.append((nx,ny))
#                 home_count += 1
#     return home_count
# for x in range(N):
#     for y in range(N):
#         if home[x][y] == 1:
#             re = bfs(x,y)
#             ans.append(re)
# ans.sort()
# print(len(ans))
# for i in ans:
#     print(i)

# import sys
# input = sys.stdin.readline

# T = int(input())
# S = 0
# for i in range(T):
#     L = input().split()
#     com = L[0]
#     if com == "add":
#         x = int(L[1])
#         S |= (1 << x)
#     elif com == "remove":
#         x = int(L[1])
#         S &= ~(1 << x)
#     elif com == "check":
#         x = int(L[1])
#         if S & (1 << x):
#             print(1)
#         else:
#             print(0)
#     elif com == "toggle":
#         x = int(L[1])
#         S ^= (1 << x)
#     elif com == "all":
#         S = (1 << 21) - 1
#     elif com == "empty":
#         S = 0

# from collections import deque
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# T = int(input())
# def bfs(x,y):
#     queue = deque([(x,y)])
#     matrix[x][y] = 0
#     while queue:
#         x,y = queue.popleft()
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0<= nx < N and 0<= ny < M and matrix[nx][ny] == 1:
#                 matrix[nx][ny] = 0
#                 queue.append((nx,ny))
#     return True

# for _ in range(T):
#     M, N, K = map(int,input().split())
#     matrix = [[0 for _ in range(M)]for _ in range(N)]
#     sol = 0
#     for _ in range(K):
#         a,b = map(int,input().split())
#         matrix[b][a] = 1
#     for x in range(N):
#         for y in range(M):
#             if matrix[x][y] == 1:
#                 if bfs(x,y):
#                     sol += 1
#     print(sol)


# N = int(input())
# dp = [0]*(N+1) # 숫자 i 를 1로 만드는 연산 횟수
# # dp[i] 와 연산 값 중 더 낮은 값 업데이트
# dp[1] = 0
# for i in range(2,N+1):
#     dp[i] = dp[i-1]+1
#     if i % 2 == 0:
#         dp[i] = min(dp[i//2] +1,dp[i])
#     if i % 3 == 0:
#         dp[i] = min(dp[i//3] +1,dp[i])

# print(dp[-1])

