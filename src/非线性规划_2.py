from scipy.optimize import minimize
import numpy as np

# 计算(2+x1)/(1+x2)-3x1+4x3最小值,x1,x2,x3在0.1到0.9之间

def fun(args):
    '''
    传入minimize函数的目标函数
    '''
    value = lambda x : (2+x[0])/(1+x[1]) - 3*x[0] + 4*x[2]
    return value

def con(args):
    # 约束条件 分为eq 和ineq
    #eq表示 函数结果等于0 ； ineq 表示 表达式大于等于0
    x1min, x1max, x2min, x2max,x3min,x3max = args
    # 记住不能用含i的生成式，生成的匿名函数不知道i是谁
    cons = ({'type': 'ineq', 'fun': lambda x: x[0] - x1min},\
              {'type': 'ineq', 'fun': lambda x: -x[0] + x1max},\
             {'type': 'ineq', 'fun': lambda x: x[1] - x2min},\
                {'type': 'ineq', 'fun': lambda x: -x[1] + x2max},\
            {'type': 'ineq', 'fun': lambda x: x[2] - x3min},\
             {'type': 'ineq', 'fun': lambda x: -x[2] + x3max})
    return cons

args = None
cons_args = [0.1,0.9,0.1,0.9,0.1,0.9]
constraint = con(cons_args)
x0 = np.array([0.3,0.3,0.8])

res = minimize(fun(args),x0=x0,constraints=constraint,args=())
print(res.fun)
print(res.success)
print(res.x)
