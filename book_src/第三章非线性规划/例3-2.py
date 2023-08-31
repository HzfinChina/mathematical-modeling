from scipy.optimize import minimize


def func(x):
    return x[0]**2 + x[1]**2 + x[2]**2 + 8


def ineq_con1(x):
    return x[0] ** 2 - x[1] + x[2]**2
def ineq_con2(x):
    return 20-(x[0] + x[1]**2 + x[2]**3)
def eq_con1(x):
    return -x[0]-x[1]**2+2
def eq_con2(x):
    return x[1] + 2*x[2]**2 -3

cons = (
    {'type':'ineq','fun':ineq_con1},
    {'type':'ineq','fun':ineq_con2},
    {'type':'eq','fun':eq_con1},
    {'type':'eq','fun':eq_con2}
)


bnds = tuple((0, None) for _ in range(3))

result = minimize(func, x0=(1,1,1),bounds = bnds, constraints=cons,method='SLSQP')
print(result.fun)
print(result.x)
