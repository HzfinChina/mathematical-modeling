import numpy as np
from scipy.optimize import linprog

c = np.array([3,-1,-1])

A_ub = np.array([
    [1,-2,1],
    [4,-1,-2]
])

b_ub = np.array([11,-3])

A_eq = np.array([[-2,0,1]])
b_eq = 1
bounds = (0,None)

result = linprog(-c,A_ub,b_ub,A_eq,b_eq,bounds)
print(result)
