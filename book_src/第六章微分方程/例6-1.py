import sympy as sy

def differential_equation(x,f):
    return x**2 + f(x) + (x-2*f(x)) * sy.diff(f(x),x,1)
x=sy.symbols('x')#约定变量
f=sy.Function('f')#约定函数
print(sy.dsolve(differential_equation(x,f),f(x)))#打印
sy.pprint(sy.dsolve(differential_equation(x,f),f(x)))#漂亮的打印
