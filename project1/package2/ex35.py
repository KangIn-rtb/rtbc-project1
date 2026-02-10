# #with 구문 - 내부적으로 close() 함
# try:
#     with open("ftext3.txt", mode='w',encoding="utf-8") as fob1:
#         fob1.write("파이썬에서 문서 저장\n")
#         fob1.write("with 구문은\n")
#         fob1.write("close 자동으로 해줌\n")
        
        
# except Exception as e:
#     print("err : ",e)

# import pickle
# try:
#     dictData = {"t":"111-1111", "m":"222-2222"}
#     listData = ["mouse", "keyboard"]
#     tupleData = (dictData, listData)
    
#     with open("hello.dat",mode='wb')as fob3:
#         pickle.dump(tupleData,fob3)
#         pickle.dump(listData,fob3)
        
#     with open("hello.dat",mode='rb') as fob4:
#         a, b = pickle.load(fob4)
#         print(a)
#         print(b)
#         c = pickle.load(fob4)
#         print(c)
# except Exception as e:
#     print(e)


