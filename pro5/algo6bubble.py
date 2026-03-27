

def bubble_sort(a):
    n = len(a)
    while True:
        change = False    
        for i in range(0,n-1):
            if a[i] > a[i+1]:
                print(a)
                a[i], a[i+1] = a[i+1], a[i]
                change = True
        if change == False:
            return
        
d = [2, 4, 5, 1, 3]
bubble_sort(d)
print(d)