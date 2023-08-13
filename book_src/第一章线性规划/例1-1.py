from scipy.optimize import linprog
import numpy as np

# c,x都是列向量，shape = (n,1)
# 目标函数z = c^T x,shape = (1,1)
c = np.array([4,3])

# A_ub x <=   b
# Aeq x = beq
# lb <= x <= ub
A = np.array([
    [2,1],
    [1,1],
    [0,1]
])
b = np.array([10,8,7])

# 看源码，如果只有一个元组提供，那么对所有变量都生效
x_bounds = (0,None)

# 由于要求最大值，所以变成-c!!!
result = linprog(c=-c,A_ub = A,b_ub=b,bounds = x_bounds)
# 而最大值就是(-求出的最小值)
print(result)
