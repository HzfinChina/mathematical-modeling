import numpy as np
from scipy.optimize import linprog
import sympy

'''
进行建模
对产品1来说，设以A1,A2完成A持久的产品为x1,x2件，以B1，B2，B3完成的为x3,x4,x5件
对产品2来说，以A1,A2完成A工序的产品为x6,x7件，以B1完成的为x8件
对产品3来说，以A2,B2完成的是x9件

那么有约束条件:
x1+x2 = x3 + x4 +x5
x6 + x7 =x8
'''

material_cost = [0.25,0.35,0.5]
unit_price = [1.25,2,2.8]

# 化简
x1,x2,x3,x4,x5,x6,x7,x8,x9 = sympy.symbols('x1,x2,x3,x4,x5,x6,x7,x8,x9')
x_list = [x1,x2,x3,x4,x5,x6,x7,x8,x9]
f =(1.25 - 0.25)*(x1 + x2) + (2-0.35)*x8 + (2.8-0.5)*x9 - 300/6000*(5*x1 + 10 * x6) - 321/10000 * (7*x2 + 9*x7+12*x9) - 250/4000*(6*x3 + 8*x8) - 783/7000*(4*x4+11*x9) - 200/4000 * 7*x5
f = sympy.simplify(f)

# 求系数
c = list()
for x in x_list:
    c.append(f.coeff(x))
c = np.array(c)

A_ub = np.zeros((5,9))

assign_dict = [{1:5,6:10},{2:7,7:9,9:12},{3:6,8:8},{4:4,9:11},{5:7}]
for i in range(len(assign_dict)):
    for key,value in assign_dict[i].items():
        A_ub[i][key-1] = value

b = np.array([6000,10000,4000,7000,4000])

A_eq = np.array([
    [1,1,-1,-1,-1,0,0,0,0],
                [0,0,0,0,0,1,1,-1,0]])

b_eq = np.array([0,0])

result = linprog(-c,A_ub,b,A_eq,b_eq,(0,None))
print(result)
