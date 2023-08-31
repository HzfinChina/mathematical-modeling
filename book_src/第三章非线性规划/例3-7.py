import sympy
x = sympy.symbols('x')
f = x**3 -x**2 + 2*x -3
result = sympy.solve(f,x)
for x0 in result:
    # 近似值
    print(x0.evalf())
