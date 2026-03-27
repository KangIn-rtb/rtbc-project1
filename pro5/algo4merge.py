# 리스트 안에 들어있는 자료를 오름차순 정렬
# 3 병합 정렬
# 이해 용
# 리스트를 반으로 나눔 요소가 1개 씩 남을 때 까지 반복
# 분할된 리스트를 정렬하며 하나로 합친다

def merge_sort(a):
    n = len(a)
    
    if n<=1:
        return a
    mid = n//2
    g1 = merge_sort(a[:mid])
    g2 = merge_sort(a[mid:])

    result = []
    while g1 and g2:
        # print(g1[0], ' ', g2[0])
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))
        # print("re",result)
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result
d = [6,8,3,1,2,4,7,5]

merge_sort(d)
print(merge_sort(d))

# 일반적
def merge_sort2(a):
    if len(a) <= 1:
        return a
    mid = len(a)//2
    left = merge_sort2(a[:mid])
    right = merge_sort2(a[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        # 남은 요소 추가
    result += left[i:]
    result += right[j:]
    return result
sorted_d = merge_sort2(d) 
print(sorted_d)