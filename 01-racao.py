# Aluno: Victor Alexandre da R. M. Miranda <varm@ic.ufal.br>
# Pesquisa Operacional 2024.2
# 01 - Problema da Ração

import pulp

model = pulp.LpProblem("Racao", pulp.LpMaximize)

x = pulp.LpVariable("AMGS", lowBound=0, cat="Integer")
y = pulp.LpVariable("RE", lowBound=0, cat="Integer")

# função objetivo: Z = 11x + 10y
model += 11 * x + 12 * y, "Lucro"

model += 1 * x + 4 * y <= 10_000, "Carne - Restricao 1"
model += 5 * x + 2 * y <= 30_000, "Cereais - Restricao 2"

model.solve()

print("Status:", pulp.LpStatus[model.status])
print("Quantidade de AMGS a ser produzida:", x.varValue)
print("Quantidade de RE a ser produzida:", y.varValue)
print("Lucro total:", pulp.value(model.objective))
