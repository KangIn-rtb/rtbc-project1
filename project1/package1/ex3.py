# 기본 자료형 : int, float, bool, complex
# 묶음 자료형 : str, list, tuple, set, dict

# s = 'sequence'

# print("길이 : ", s.find("e"), s.find("e",3), s.rfind("e"))



# import copy
# name = ['A', 'B', 'C']
# name2 = name
# name3 = copy.deepcopy(name)
# print(name, name3, id(name), id(name3))
# name[0] = "D"
# print(name)
# print(name2)
# print(name3)

mydic = dict(k1 = 1, k2 = "ok", k3 = 3.13)
print(mydic, type(mydic))

dic = {"파이썬":'뱀', "자바":"커피", "인사": "안녕"}
print(dic)
print(len(dic))
print(dic["자바"])
# print(dic["커피"])
dic["금요일"] = "와우"
print(dic)
del dic["인사"]
print(dic)