import sympy as sp

# 定义变量
x, y = sp.symbols('x y')

# 定义目标函数
f = x**3 - y**3 +  3*x**2 + 3*y**2 - 9*x

# 计算目标函数的偏导数
grad_f = [sp.diff(f, var) for var in (x, y)]

# 求解对x,y偏导数为零的方程组
solutions = sp.solve(grad_f, (x, y))

# 判断极值点的类型
for solution in solutions:
    opt_x = solution[0]
    opt_y = solution[1]

    # 计算目标函数的二阶偏导数
    hessian = sp.hessian(f, (x, y))
    hessian_val = hessian.subs([(x, opt_x), (y, opt_y)])

    # 判断极值点类型
    # 确定hessian矩阵是否是正定矩阵
    # 如果是，那么是极小值点
    if hessian_val.is_positive_definite:
        opt_type = "极小值"
    # 如果是负定矩阵，那么是极大值点
    elif hessian_val.is_negative_definite:
        opt_type = "极大值"
    else:
        opt_type = "鞍点"

    opt_f = f.subs([(x, opt_x), (y, opt_y)])
    print('解 x:', opt_x, ' y:', opt_y, ' 目标函数值:', opt_f, ' 类型:', opt_type)

