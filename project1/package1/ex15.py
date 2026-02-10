# package1/ex15.py - main
print("사용자 정의 모듈 처리하기")
s = 20
print("\n경로 지정 방법1 : import 모듈명")
import package1.mymod1 as mymod1

print(dir(mymod1))
print(mymod1.__file__)
print(mymod1.__name__)
list1 = [1, 2]
list2 = [3, 4, 5]
mymod1.listHap(list1, list2)

if __name__ == "__main__":
    print("main module")

from package1.mymod1 import mbc, tot

mbc()
print(tot)

from package1.mymod1 import *

print("tot: ", tot)
from package1.mymod1 import mbc as mbc별명  # 별명 만들기

mbc별명()

print("\n경로 지정 방법 3 : import 하위패키지.모듈명")
import package1.subpack.sbs
package1.subpack.sbs.sbsMansae()
import package1.subpack.sbs as nick
nick.sbsMansae()

print('\n경로 지정 방법 4 : 현 package와 동등한 다른 패키지 모듈 읽기')
from package1_other import mymod2
mymod2.hapF(4,3)

import mymod3
re = mymod3.gopF(4,3)
print('path 설정된 곳의 module 읽기 - result : ',re)