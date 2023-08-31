from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt

x = np.array([19,25,31,38,44])
y = np.array([19,32.3,49,73.3,97.8])

def f(x,a,b):
      return a + b * x **2

par, _ = curve_fit(f,x,y)
print(par)
y_fitted = f(x,*par)
plt.scatter(x,y)
plt.plot(x,y_fitted)
#plt.show()
