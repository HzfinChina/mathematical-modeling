from scipy.optimize import fmin
def func(x_ls):
    x,y = x_ls
    return x**3 - y**3 + 3 *x**2 + 3*y**2 - 9 *x

