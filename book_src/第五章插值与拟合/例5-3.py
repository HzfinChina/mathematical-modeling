from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(100,501,100)
y = np.arange(100,401,100)
X,Y = np.meshgrid(x,y)
Z = np.array([
    [636,697,624,478,450],
    [698,712,630,478,420],
    [680,674,598,412,400],
    [662,626,552,334,310],
])

x1 = np.linspace(100,501,10000)
y1 = np.linspace(100,401,10000)
X1,Y1 = np.meshgrid(x1,y1)
f = interpolate.interp2d(x,y,Z,kind='cubic')
Z1 = f(x1,y1)

print(np.max(Z1))
x_index,y_index = np.unravel_index(np.argmax(Z1),Z1.shape)
print(x1[y_index],y1[x_index])

fig1 = plt.figure(figsize=(9,8))
ax1 = fig1.add_subplot( projection='3d')
surf1 = ax1.plot_surface(X,Y,Z,cmap=plt.cm.viridis)
ax2 = fig1.add_subplot( projection='3d')
surf2 = ax2.plot_surface(X1,Y1,Z1,cmap=plt.cm.viridis)
plt.show()
