import numpy as np

def MLPerceptron(X, W1, W2):
    x = np.array(x)
    w1  = np.array(w1)
    w2 = np.array(w2)
    s1 = np.array([0.0] * len(X))
    s2 = np.array([0.0] * len(X))
    
    for num in range(len(x)) :
        s1[num] = (np.sum(x *w1[num]) > 0)
    for num in range(len(x)):
        s2[num] = np.sum(s1*w2[num]) > 0
    return s2    

W1 = [[-0.5,-0.5,0,0,0,0.7],
      [0.5,0.5,0,0,0,-0.2],
      [0,0,0,0,0,0],
      [0,0,0,0,0,0],
      [0,0,0,0,0,0],
      [0,0,0,0,0,1]]

W2 = [[0.5,0.5,0,0,0,-0.7],    
      [0,0,0,0,0,0],    
      [0,0,0,0,0,0],    
      [0,0,0,0,0,0],    
      [0,0,0,0,0,0],    
      [0,0,0,0,0,0]]

X = [0,0,0,0,0,1]
print(MLPerceptron(X,W1,W2))
X = [0,1,0,0,0,1]
print(MLPerceptron(X,W1,W2))
X = [1,0,0,0,0,1]
print(MLPerceptron(X,W1,W2))
X = [1,1,0,0,0,1]
print(MLPerceptron(X,W1,W2))
