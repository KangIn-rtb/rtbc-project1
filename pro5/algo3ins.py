# 리스트 안에 들어있는 자료를 오름차순 정렬
# 2 삽입 정렬
# 이해 용
def find_ins_idx(r, v):
    for i in range(0, len(r)):
        # v 값이 i번 위치값 보다 작으면 
        if v < r[i]:
            return i
    # 적정한 위치를 찾지 못함 -> 맨뒤에 섬
    return len(r)
def ins_sort(a):
    result = []
    while a:
        value = a.pop(0)
        ins_idx = find_ins_idx(result,value)
        result.insert(ins_idx,value) 
        print(result)
    return result
d = [2,4,5,1,3]
# print(find_ins_idx(d,1))
# print(ins_sort(d))

# 일반적
def ins_sort2(a):
    n = len(a)
    for i in range(1,n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j+1] = key  # 삽입 위치에 key 저장 
        
ins_sort2(d)
print(d)