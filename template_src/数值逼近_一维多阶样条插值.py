import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams["font.sans-serif"]=["Source Han Serif CN"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题


# 生成10个从0到2.25pi间隔均匀的点,是实验数据
x = np.linspace(0,2* np.pi,40 )
y = np.sin(4*x)

plt.plot(x,y,'o',label = '原始数据')

# 生成拟合点的x坐标
x_new = np.linspace(0,2*np.pi,200)

# zero:0阶,linear:一阶，quadratic:二阶,cubic:三阶
for kind in ['nearest','zero','linear','quadratic','cubic',]:
    f = interpolate.interp1d(x,y,kind=kind)
    y_new = f(x_new)
    plt.plot(x_new,y_new,label = kind)

plt.xlabel("安培/A")
plt.ylabel('伏特/V')
# 显示label
plt.legend(loc = 'upper right')
plt.show()
