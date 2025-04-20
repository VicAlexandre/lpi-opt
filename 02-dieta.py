# Aluno: Victor Alexandre da R. M. Miranda <varm@ic.ufal.br>
# Pesquisa Operacional 2024.2
# 02 - Problema da Dieta

import pulp

model = pulp.LpProblem("Dieta", pulp.LpMinimize)

x = [pulp.LpVariable(f"x{i + 1}", lowBound=0, cat="Integer") for i in range(6)]

costs = [35, 30, 60, 50, 27, 22]

# função objetivo: Z = 35x1 + 30x2 + 60x3 + 50x4 + 27x5 + 22x6
model += pulp.lpSum(costs[i] * x[i] for i in range(6)), "Custo_Total"

model += x[0] + 2 * x[2] + 2 * x[3] + x[4] + \
    2 * x[5] >= 9, "Vitamina_A - Restricao 1"
model += x[1] + 3 * x[2] + x[3] + 3 * x[4] + \
    2 * x[5] >= 19, "Vitamina_C - Restricao 2"

model.solve()

print("Status:", pulp.LpStatus[model.status])
for var in x:
    print(f"{var.name} = {var.varValue}")
print("Custo mínimo total: R$", pulp.value(model.objective))
