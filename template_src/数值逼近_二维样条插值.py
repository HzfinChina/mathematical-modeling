import numpy as np
from scipy import interpolate
import matplotlib as mpl
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams["font.sans-serif"]=["Source Han Serif CN"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题


# 生成10个从0到2.25pi间隔均匀的点,是实验数据
x = np.linspace(0,2* np.pi,40 )
y = np.sin(4*x)

def func(x,y):
    return (x+y) * np.exp(-5*(x**2 + y**2))

# 形成网络

z = func(x,y)
func_new = interpolate.interp2d(x,y,z,kind = 'cubic')
x_new = np.linspace(-1,1,1000)
y_new = np.linspace(-1,1,1000)
# 生成网格上的z值
z_new = func_new(x_new,y_new)

ax2 = plt.subplot(1,2,2,projetion = '3d')
