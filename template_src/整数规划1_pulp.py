import pulp
Prob = pulp.LpProblem(sense=pulp.LpMinimize)

c = [3,4,1]

A_gq = [[1,6,2],[2,0,0]]
b_gq = [5,3]

x = [pulp.LpVariable(f'x{i}',lowBound=0,cat='Integer') for i in [1,2,3]]


# 添加目标函数
Prob += pulp.lpDot(c,x)

# 注意这里添加约束是用循环，而不是直接用矩阵表示，我也不知道直接用矩阵行不行，可以去看官方文档
for i in range(len(A_gq)):
    Prob += (pulp.lpDot(A_gq[i],x) >= b_gq[i])

Prob.solve()
print(f'优化结果:{pulp.value(Prob.objective)}')
print(f'参数取值:{[pulp.value(var) for var in x]}')
