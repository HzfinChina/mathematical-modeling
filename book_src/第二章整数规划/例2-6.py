import random
import numpy as np

A = np.array([
    [1] * 5,
    [1,2,2,1,6],
    [2,1,6,0,0],
    [0,0,1,1,5]
])
b = np.array([400,800,200,200])

def fun(x_list)->int:
    x1,x2,x3,x4,x5 = x_list
    return x1**2 + x2**2 + 3*x3**2 + 4*x4**2 + 2*x5**2\
- 8*x1 - 2*x2 - 3*x3 - x4 - 2*x5

x_array = [np.array([random.randint(0,100) for _ in range(5)])for _ in range(10000000)]
max_result = 0
max_solve_list = None


for x_list in x_array:
    if not (np.dot(A,x_list) <= b).all():
        continue
    if fun(x_list) > max_result:
        max_result = fun(x_list)
        max_solve_list = x_list
print(max_result)
print(max_solve_list)


