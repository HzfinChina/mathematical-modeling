import numpy as np
import pulp

intlp = pulp.LpProblem('noname',sense=pulp.const.LpMinimize)
x1 = pulp.LpVariable('x1',0,None,'Integer')
x2 = pulp.LpVariable('x2',0,None,'Integer')
intlp += x1 + x2
intlp += 2*x1+4*x2 ==6
intlp.solve()
