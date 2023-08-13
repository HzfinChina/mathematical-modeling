import numpy as np
from  scipy.optimize import linprog

# 变量转化
# x_i = u_i - v_i, u_i, v_i >= 0
# 则|x_i| = u_i + v_i
# 则 u_i = (x_i + |x_i|) / 2
c = np.array([1,2,3,4] * 2)

A = np.array([
    [1,-1,-1,1],
    [1,-1,1,-3],
    [1,-1,-1,3]
])
b = np.array([-2,-1,-0.5])
uv_A = np.hstack((A,-A))
bounds = (0,None)
result = linprog(c,uv_A,b,bounds = bounds)

# 求得结果和书中相同
print(result)
