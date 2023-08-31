import numpy
import random
total_sum = 100000000
x_ls = [random.uniform(0,12) for i in range(total_sum)]
y_ls = [random.uniform(0,9) for i in range(total_sum)]

in_num = 0
for i in range(len(x_ls)):
    x = x_ls[i]
    y = y_ls[i]
    if (y < x**2 and y < 12 -x ):
        in_num+=1
area = 12 * 9 * in_num / total_sum
print(area)
