# 리스트 안에 들어있는 자료를 오름차순 정렬
# 1 선택 정렬 
# 방법 1 : 이해 위주
# d = [2,4,5,1,3]
# def find_min_dix(a):
#     n = len(a)
#     min_idx = 0
#     for i in range(1,n):
#         if a[i] < a[min_idx]:
#             min_idx = i
#     return min_idx
# def select_sort(a):
#     result = []
#     while a:
#         min_dix = find_min_dix(a)
#         value = a.pop(min_dix)
#         result.append(value)
        
#     return result
# print(select_sort(d))

# 방법 2 : 일반 알고리즘
# def select_sort2(a):
#     n = len(a)
#     for i in range(0,n-1):
#         min_idx = i
#         for j in range(i+1,n):
#             if a[j] < a[min_idx]:
#                 min_idx = j
#         a[i], a[min_idx] = a[min_idx], a[i]

# select_sort2(d)
# print(d)
