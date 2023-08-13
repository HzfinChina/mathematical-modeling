from scipy.optimize import linprog
import numpy as np

c = np.array([2,3,1])

# 注意，由于s.t.中为大于号，所以A_ub 和 b_ub都要转成相反数
A = -np.array([
    [1,4,2],
    [3,2,0]
])
b = -np.array([8,6])

x_bounds = (0,None)

result = linprog(c = c,A_ub = A, b_ub = b,bounds = x_bounds)
# 和书中相同
print(result)
