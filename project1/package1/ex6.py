"""
def pacto(n):
    if n > 1:
        return n*pacto(n-1)
    else:
        return 1

a = 0
while a <= 5:
    print(pacto(int(input())))
    a += 1
print("end")
"""
"""
import time 
sw = input("폭탄 스위치 [y/n]")
if sw == "y" or sw == "Y":
    cont = 5
    while 1 <= cont:
        print("%d초 남음"%cont)
        time.sleep(1)
        cont -= 1
    print("폭발")
elif sw == "n" or sw == "N":
    print("취소")
else:
    print("y or n press")
print("sw : ", sw)
print("end")
"""
"""
import re
for test_ss in ['111-1234', '일이삼-일이삼사', '222-1234','333&1234']:
    if re.match(r'^\d{3}-\d{4}$',test_ss):
        print(test_ss, '전화번호 맞아요')
    else:
        print(test_ss, '전화번호 아니야')
"""
"""
a = [1,2,3,4,5,6,7,8,9,10]
li = []
for i in a:
    if i % 2 == 0:
        li.append(i)
print(li)

print(list(i for i in a if i%2==0))

datas = [1,2,'a',True,3.0]
li2 = [i*i for i in datas if type(i) == int]
print(li2)

id_name = {1:"tom", 2:"oscar"}
name_id = {val:key for key, val in id_name.items()}
print(name_id)
"""
"""
for i in range(2,10):
    for j in range(1,10):
        print(f"{i}X{j}={i*j}")
"""
