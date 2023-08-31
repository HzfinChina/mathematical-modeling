from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt

x = [0,3,5,7,9,11,12,13,14,15]
y = [0,1.2,1.7,2.0,2.1,2.0,1.8,1.2,1,1.6]

f = interpolate.interp1d(x,y,kind=3)

tck = interpolate.splrep(x,y)
y_bspl = interpolate.splev(x,tck)

x_new = np.linspace(x[0],x[-1],1000)
y_new = f(x_new)
# fig = plt.figure(figsize=(8,4))
ax = plt.subplot(2,1,1)
ax.scatter(x,y)
ax.plot(x_new,y_new,'red')
ax = plt.subplot(2,1,2)
ax.scatter(x,y)
ax.plot(x,y_bspl,'red')
plt.show()
