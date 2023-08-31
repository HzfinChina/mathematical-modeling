from scipy.optimize import linear_sum_assignment
import numpy as np
cost_matrix = np.array([
    [3,8,2,10,3],
    [8,7,2,9,7],
    [6,4,2,7,5],
    [8,4,2,3,5],
    [9,10,6,9,10]
])
assign_matrix = np.zeros((5,5))
row_index,column_index = linear_sum_assignment(cost_matrix)
for i in range(5):
    assign_matrix[row_index[i]][column_index[i]] = 1
print(assign_matrix)
