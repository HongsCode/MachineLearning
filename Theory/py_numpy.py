import numpy as np

# numpy 실습
"""
"""
#1.5.3 numpy
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
print(x)
print(type(x))

print(x+y)
print(x-y)
print(x*y)
print(x/y)

#1.5.4 numpy 
A = np.array([1,2], [3,4])
print("A = \n", A)
print(A.shape)
print(A.dtype)

B = np.array([3,0], [0,6])
print("B = \n", B)
print("A+B=\n", A+B)
print("A-B=\n", A-B)

print("A*10=\n", A*10)

# 브로드 캐스트
# A, B의 행렬이 다른 경우
# numpy에서 작은 것에 맞춰준다.
# 1x3 , 1*1 => 1*3
# 3x3, 1x3 => 3x3
# 3x1, 1x3 => 3x3

A = np.array([1,2], [3,4])
B = np.array([10, 20])

print("A*B = \n", A*B)

