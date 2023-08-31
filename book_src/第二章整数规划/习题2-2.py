import pulp
prob = pulp.LpProblem()
x1,x2,x3,x4,x5,x6 = [pulp.LpVariable(f'B{i+1}',cat = pulp.LpBinary) for i in range(6)]
prob+= (x1 + x2 + x3 + x4  +x5 + x6)
prob+= (x1 + x2 + x3 >= 1)
prob+= (x2+x4>=1)
prob+= (x3+x5>=1)
prob+= (x4+x6>=1)
prob+= (x5+x6>=1)
prob+= (x1>=1)
prob+=(x2+x4+x6>=1)
prob.solve()
print(prob.objective.value())
for var in prob.variables():
    print(f"{var.name}: {var.value()}")
