import sympy
x,y = sympy.symbols('x y')
eq = [
    x**2 + y -6,
    y**2 + x -6
]
result = sympy.nonlinsolve(eq,(x,y))
for xy in result:
    print(f'x:{xy[0].evalf()}')
    print(f'y:{xy[1].evalf()}')
