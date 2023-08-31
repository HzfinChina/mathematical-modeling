from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt

x = [129, 140, 103.5, 88, 185.5, 195, 105,
     157.5, 107.5, 77, 81, 162, 162, 117.5]
y = [7.5, 141.5, 23, 147, 22.5, 137.5, 85.5,
     85.5-6.5, -81, 3, 56.5, - 66.5, 84, -33.5]
z = [4, 8, 6, 8, 6, 8, 8, 9, 9, 8, 8, 9, 4, 9]

l = len(x)
x_min = min(x)
x_max = max(x)
y_min = min(y)
y_max = max(y)
f = interpolate.interp2d(x,y,z,kind='cubic')
x_new = np.linspace(x_min,x_max,10000)
y_new = np.linspace(y_min,y_max,10000)
Z = f(x_new,y_new)

X,Y = np.meshgrid(x_new,y_new)
fig1 = plt.figure(figsize=(9,8))
ax1 = fig1.add_subplot( projection='3d')
surf1 = ax1.plot_surface(X,Y,Z,cmap=plt.cm.viridis)
plt.show()
