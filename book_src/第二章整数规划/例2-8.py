import pulp
prob = pulp.LpProblem('',pulp.LpMinimize)
x1 = pulp.LpVariable('x1',cat = pulp.LpContinuous)
x2 = pulp.LpVariable('x2',cat = pulp.LpContinuous)
x3 = pulp.LpVariable('x3',cat = pulp.LpBinary)
prob += (-3 * x1 -2 * x2 - x3)
prob +=(x1 + x2 + x3 <=7)
prob +=(4*x1+2*x2+x3 ==12)
prob.solve()
for v in prob.variables():
    print(v.varValue)

