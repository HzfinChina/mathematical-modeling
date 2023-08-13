from scipy import optimize
import scipy
import numpy as np

# 注意，这里c的shape为3x1,刚开始我以为是1x3
# 但是注意只有一个中括号时，np默认创建的是一列矩阵
c = np.array([2,3,-5])
A = np.array([[-2,5,-1],[1,3,1]])
b = np.array([-10,12])

# 由于是矩阵乘那么Aeq必须要是1x3才能和x(3x1)点乘
Aeq = np.array([[1,1,1]])
print(Aeq.shape)
beq = np.array([7])

res = optimize.linprog(-c,A,b,Aeq,beq)
