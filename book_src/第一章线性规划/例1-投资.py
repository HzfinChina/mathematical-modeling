import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

c = -np.array([0.05,0.27,0.19,0.185,0.185])

# 加上交易费
Aeq = np.array([[1,1.01,1.02,1.045,1.065]])
beq = 1
# 风险度
risk_degree_list = np.arange(0,0.1,0.001)

A = np.array([
    [0] * 5,
    [0,0.025] + [0] * 3,
    [0] * 2 + [0.015] + [0] * 2,
    [0] * 3 + [0.055] + [0],
    [0] * 4 + [0.026]
])

bounds = (0,None)

y_fun = list()
for risk_degree in risk_degree_list:
    b = np.array([risk_degree] * 5)
    result = linprog(c,A,b,Aeq,beq,bounds = bounds)
    y_fun.append(-result.fun)

plt.plot(risk_degree_list,y_fun)
plt.xlabel("Risk")
plt.ylabel("Gain")
plt.grid()
plt.title("Gain-Risk")
plt.show()
