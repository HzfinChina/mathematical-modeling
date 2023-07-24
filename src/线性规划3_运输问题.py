from scipy import optimize
import numpy as np
# 这里不知道要不要加T
c = np.array([
    [500,550,630,1000,800,700],
    [800,700,600,950,900,930],
    [1000,960,840,650,600,700],
    [1200,1040,980,860,880,780]
])
# 目标函数c_ijx_ij
'''
x = [
[x_11,x_12,x_13,x_14],
[....]
...
'''
# 条件1每一行相加为a_i
# 条件2每一列相加为b_i

c_flat = c.flatten()
# c必须是一维的
# 由于这里c_flat.shape=24,1,所有x也要有24行
# 前六行是小麦，...

# 现在构建A_eq,必须保证A_eq(10x24) x(24x1)的结果是(a1,a2,a3,a4,b1,b2,b3,b4,b5,b6)
beq = np.array([76,88,96,40,42,56,44,39,60,59])
np.array([1])
def constructAeq():
    A = np.zeros((10,24),dtype=np.int8)
    # 定义a_i,i in 0到3
    a_array_list = list();
    for i in range(4):
        a_array_list.append(np.zeros((4,6)))
        a_array_list[i][i] = 1
    A = np.hstack(a_array_list)
    # 定义b_j,j in 0到5
    b_array_list = list()
    for i in range(4):
        b_array_list.append(np.eye(6))
    tempA = np.hstack(b_array_list)
    A = np.vstack((A, tempA))
    return A


Aeq = constructAeq()
beq = np.array([76,88,96,40,
                42,56,44,39,60,59])

bounds = [(0,None)]*24

Aeq = constructAeq()
# 半天不对发现是没加负号
result = optimize.linprog(c = -c_flat,A_eq=Aeq,b_eq = beq,bounds=bounds)
print(- result.fun)
print(np.array(result.x).reshape(4,6))
