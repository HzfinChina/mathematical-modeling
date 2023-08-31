from scipy.optimize import linear_sum_assignment
import numpy as np
gain_matrix = np.array([
    [4,2,3,4],
    [6,4,5,5],
    [7,6,7,6],
    [7,8,8,6],
    [7,9,8,6],
    [7,10,8,6]
])

# 如果多件事可以分配给一个人的话那么就hstack多个虚拟的人
# 一个人可以做几件事就hstack几个,最多hstack事情的个数
gain_matrix = np.hstack([gain_matrix for _ in range(6)])
row_indices, col_indices = linear_sum_assignment(gain_matrix,maximize = True)
sum = 0
for i in range(len(row_indices)):
    sum+= gain_matrix[row_indices[i]][col_indices[i]]
print(row_indices,col_indices)
print(sum)
