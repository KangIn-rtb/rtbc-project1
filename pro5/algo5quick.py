# 리스트 안에 들어있는 자료를 오름차순 정렬
# 4 퀵 정렬
# 이해 용
# 하나의 기준점을 중심으로 작은 값과 큰 값을 나눠서 각각 정렬 후 
# 마지막에 이어 붙이는 방법
# g1: 기준값 보다 작은 그룹
# 기준값
# g2 : 기준값 보다 큰 그룹

def quick_sort(a):
    n = len(a)
    if n <= 1:
        return a
    pivot = a[-1]
    
    g1 = []
    g2 = []
    
    for i in range(0, n - 1):
        if a[i] < pivot:
            g1.append(a[i])
        else:
            g2.append(a[i])
    return quick_sort(g1) + [pivot] + quick_sort(g2)

d = [8,6,3,1,2,4,7,5]
print(quick_sort(d))

def quick_sort2_sub(a, s, e):
    if e - s <= 0:
        return
    pivot = a[e]
    i = s
    for j in range(s,e):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[e] = a[e], a[i]
    quick_sort2_sub(a,s,i-1)
    quick_sort2_sub(a,i+1,e)
    
def quick_sort2(a):
    quick_sort2_sub(a, 0, len(a) - 1) # 자료, 시작 인덱스, 끝 인덱스
    
    
quick_sort2(d)
print(d)
    