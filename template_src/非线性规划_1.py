from scipy.optimize import minimize
import numpy as np

# 计算1/x  + x 在(0,+infty)的最小值

def fun(args = 1):
    '''
    传入minimize函数的目标函数
    '''
    value = lambda x : args/x + x
    return value

args = 1
x0 = 1
res = minimize(fun(args),x0=x0)
print(res.fun)
print(res.x)
