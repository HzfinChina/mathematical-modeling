from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,9,1)
y = np.array([15.3,20.5,27.4,36.6,49.1,65.6,87.87,117.6])
def func(x,a,b):
    return a * np.e ** (b * x)

par,_ = curve_fit(func,x,y)
y_fitted = func(x,*par)
plt.scatter(x,y)
plt.plot(x,y_fitted)
plt.show()
