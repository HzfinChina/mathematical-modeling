import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

t = np.arange(1790,2001,10)
x = np.array([3.9,5.3,7.2,9.6,12.9,17.1,23.2,31.4,38.6,50.2,62.9,76.0,92.0,106.5,123.2,131.7,150.7,179.3,204.0,226.5,251.4,281.4])

x0 = x[0]
t0 = t[0]

def func(t,xm,r):
    return xm/\
    (1 + (xm/x0 -1)*np.exp(-r*(t-t0)))
par,_ = curve_fit(func,t,x)
t_new = np.linspace(t[0],2010,100)
x_fitted = func(t_new,*par)
plt.plot(t,x)
#plt.plot(t_new,x_fitted)
plt.show()

