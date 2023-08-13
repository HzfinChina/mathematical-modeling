import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams["font.sans-serif"]=["Source Han Serif CN"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题


# 生成10个从0到2.25pi间隔均匀的点,是实验数据
x = np.linspace(0,2.25* np.pi,10 )
y = np.sin(x)

# 生成拟合点的x坐标
x_new = np.linspace(0,2.25*np.pi,100)

# 线性插值
f_linear = interpolate.interp1d(x,y)

# 计算样条曲线，返回三元组(t,c,k)
# t是一维数组，表示曲线上的节点
# c一维数组，表示曲线上的B- spline系数
# k是一个整数，表示样条曲线的次数，也就是曲线在每个节点处的导数阶数
tck = interpolate.splrep(x,y)
# 用x_new和得到的样条曲线得到y_bspline
y_bspline = interpolate.splev(x_new,tck)

# 画图
plt.xlabel("安培/A")
plt.ylabel('伏特/V')
plt.plot(x,y,"o",label="原始数据")
plt.plot(x_new,f_linear(x_new),label="线性插值")
plt.plot(x_new,y_bspline,label="B-spline插值")
# 显示label
plt.legend()
plt.show()


