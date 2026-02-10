def zipProcess():
    # dong = input("동이름 입력: ")
    dong = "개포1동"
    # print(dong)
    
    with open(r"zipcode.txt",mode='r',encoding="EUC-kr") as f:
        line = f.readline()
        # lines = line.split('\t')
        # print(lines)
        while line:
            lines = line.split('\t')
            if lines[3].startswith(dong):
                print(lines)
            line = f.readline()
            
if __name__ == "__main__":
    zipProcess()
