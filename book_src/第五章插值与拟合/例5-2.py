from scipy import interpolate
from scipy.integrate import quad
import numpy as np
t = [0.15,0.16,0.17,0.18]
vt = [3.5,1.5,2.5,2.8]
f_spl = interpolate.interp1d(t,vt,kind=3)

def f_quad(t):
    return f_spl(t)
print(quad(f_quad,t[0],t[-1]))
