##Rhino 8 사용중이며
##Python 3 스크립트 적용 후
##타사 스크립트 설치하여 작성하였습니다.

##notion에 제시해주신 문제풀이 방법으로 
##모듈 설치 없이 작성하는게 더 바람직한 (초보에게는 더 나은) 방법 같긴 한데
##방법을 찾지 못해 모듈을 쓰는 방법으로 했습니다.

##검증은 새로운 방식으로는 잘 되지 않아 1주차때 했던 방식으로 해봤습니다.
##4번 문제는 못풀었습니다.


##1. unit x

import numpy as np
a = np.array([float(x),0,0])

##2. distance

import numpy as np
v=x-y
a = np.linalg.norm(v)

##3. unit_vector

import numpy as np
a = x / np.linalg.norm(x)

##4. closest point
##실패

##5. fibonacci

def fib(x, y, z):
    sequence = [x, y]
    for n in range(2, z+2):
        n = sequence[-1] + sequence[-2]
        sequence.append(n)

    return sequence

a = fib(x, y, z)
