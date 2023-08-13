import numpy as np
from scipy.optimize import linprog

c = np.array(
    [3100] * 3 + [3800] * 3 + [3500] * 3 + [2850] * 3
)
# x1 + x2 + x3 <= 18
# x4 + x5 + x6 <= 15
# x7+...
# x10+...

# 重量限制
# x1 + x4 + x7 +x10<= 10

# 体积限制
# x1 * 400 + x4 + ...
# x2 x5 x8 x11
# x3 x6 x9 x12

# 成比例
# (x1 + x4 + x7+x10)/10 = (x2 + x5+x8+x11)/16
# (x1 + x4 + x7+x10)/10 = (x3 + x6+x9+x12)/8
volume_list = [480,650,580,390]

A_ub = np.array([
    [1]*3 + [0] *9,
    [0]*3+[1]*3+[0]*6,
    [0]*6+[1]*3+[0]*3,
    [0]*9+[1]*3,
    [1 if i%3 == 0 else 0 for i in range(12)],
    [1 if i%3 == 1 else 0 for i in range(12)],
    [1 if i%3 == 2 else 0 for i in range(12)],
    [volume_list[int(i/3)] if i%3 == 0 else 0 for i in range(12)],
    [volume_list[int(i/3)] if i%3 == 1 else 0 for i in range(12)],
    [volume_list[int(i/3)] if i%3 == 2 else 0 for i in range(12)],
])
b = np.array([18,15,23,12,10,16,8,6800,8700,5300])

A_eq = np.array([
    [0.1 if i % 3==0 else -1/16 if i %3 == 1 else 0 for i in range(12)],
    [0.1 if i % 3==0 else -1/8 if i %3 == 2 else 0 for i in range(12)],
])
b_eq = np.array([0]*2)

result = linprog(-c,A_ub,b,A_eq,b_eq,(0,None))
print(result)
