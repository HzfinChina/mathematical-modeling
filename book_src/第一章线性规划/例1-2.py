from scipy.optimize import linprog
import numpy as np
c = np.array([-2,-3,5])

A = np.array([
    [-2,5,-1],
    [1,3,1]
])
b = np.array([-10,12])

A_eq = np.array([[1,1,1]])
b_eq = np.array([7])

# 见例1-1，应用于所有x
x_bounds = (0,None)

result = linprog(c = c,A_ub = A, b_ub = b,A_eq = A_eq,b_eq = b_eq,bounds = x_bounds)
# 求得和书相同
print(result)
