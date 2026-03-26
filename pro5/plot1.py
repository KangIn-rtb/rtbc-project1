# 시각화의 중요성 5가지 따로 정리

# matplotlib : 플로팅 라이브러리. 그래프 생성을 위한 다양한 함수를 제공
# 시각화의 중요성 
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font',family = "malgun gothic")
plt.rcParams['axes.unicode_minus'] = False
x = ["서울", "인천","수원"]
y = [5,3,7]
# x = {"서울", "인천","수원"} # set 타입은 쓸 수 없음
# y = [5,3,7]
plt.xlim([-1,3])
plt.ylim([0,10])
plt.grid()
plt.plot(x,y)
plt.show()

data = np.arange(1,11,2)
plt.plot(data)
x = [0,1,2,3,4]
for a, b in zip(x,data):
    plt.text(a,b,str(b))
plt.show()

x = np.arange(10)
y = np.sin(x)
print(x,y)
# plt.plot(x,y)
plt.plot(x,y,'go--',linewidth=2,markersize=12)
plt.show()

# hold 복수의 plot으로 여러개의 차트를 겹쳐 그림
x = np.arange(0,np.pi*3,0.1)
print(x)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.figure(figsize=(10,5))
plt.plot(x,y_sin,'r')
plt.scatter(x,y_cos)
plt.xlabel('x 축')
plt.ylabel('y 축')
plt.title("sin,cos")
plt.legend(['sin','cos'])
plt.show()

print()
# subplot : 하나의 figure를 여러개의 Axes(plot)으로 나누기
plt.subplot(2,1,1)
plt.plot(x,y_sin)
plt.title('sin')
plt.subplot(2,1,2)
plt.plot(x,y_cos)
plt.title('cos')
plt.show()
print()
irum = ['a','b','c','d','e']
kor = [80,50,70,75,90]
eng = [60,70,65,80,95]
plt.plot(irum,kor,'ro--')
plt.plot(irum,eng,'bo--')
plt.ylim([40,100])
plt.title("시험점수")
plt.legend(['국어','영어'],loc='best')
plt.grid()
fig = plt.gcf()
plt.show()
fig.savefig('plot1.png')    # img 출력 방법 img 저장하고 static 저장 img src로 읽기 - 정적 - 도표같은 정적 img 구현 
                            # js img 출력 라이브러리를 써서 동적 이미지 구현 - 동적 - 제대로 img 구현
from matplotlib.pyplot import imread
img = imread('plot1.png') 
plt.imshow(img)
plt.show()