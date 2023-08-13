import numpy as np
from scipy.optimize import linprog

# x_i = u_i - v_i,u_i,v_i >= 0
c = np.array([1,2,3,4] * 2)

A_eq = np.array([
    [1,-1,-1,1],
    [1,-1,1,-3],
    [1,-1,-2,3]
])
uv_eq = np.hstack([A_eq,-A_eq])
b_eq = np.array([0,1,-0.5])

result = linprog(c,A_eq = uv_eq, b_eq = b_eq,bounds = (0,None))

print(result)
