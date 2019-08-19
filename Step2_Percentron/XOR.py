import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    
    tmp = np.sum(w*x) + b
    if tmp<=0:
        return 0
    else:
        return 1
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    
    tmp = np.sum(w*x) + b
    if tmp<=0:
        return 0
    else:
        return 1
    
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y    

print(XOR(0, 0), XOR(0, 1), XOR(1,0), XOR(1,1))

"""
only using NAND gate
"""
def XXOR(x1, x2) :
    s1 = NAND(x1,x2)
    s2 = NAND(x1, s1)
    s3 = NAND(x2, s1)
    y = NAND(s2, s3)
    return y

print(XXOR(0, 0),XXOR(0, 1), XXOR(1,0), XXOR(1,1))
