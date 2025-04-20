# Aluno: Victor Alexandre da R. M. Miranda <varm@ic.ufal.br>
# Pesquisa Operacional 2024.2
# 04 - Problema do Transporte

import pulp

model = pulp.LpProblem("Transporte", pulp.LpMinimize)

# 01 - Fábrica 1 - Depósito 1
# 02 - Fábrica 1 - Depósito 2
# 03 - Fábrica 1 - Depósito 3
# 04 - Fábrica 2 - Depósito 1
# 05 - Fábrica 2 - Depósito 2
# 06 - Fábrica 2 - Depósito 3
# 07 - Fábrica 3 - Depósito 1
# 08 - Fábrica 3 - Depósito 2
# 09 - Fábrica 3 - Depósito 3
x = [pulp.LpVariable(f"x{i + 1}", lowBound=0, cat="Integer") for i in range(9)]

# função objetivo: Z = 8x1 + 5x2 + 6x3 + 15x4 + 10x5 + 12x6 + 3x7 + 9x8 + 10x9
model += (
    (8 * x[0])
    + (5 * x[1])
    + (6 * x[2])
    + (15 * x[3])
    + (10 * x[4])
    + (12 * x[5])
    + (3 * x[6])
    + (9 * x[7])
    + (10 * x[8]),
    "Custo_Total",
)

model += x[0] + x[1] + x[2] <= 120, "Oferta Fábrica 1 - Restrição 1"
model += x[3] + x[4] + x[5] <= 80, "Oferta Fábrica 2 - Restrição 2"
model += x[6] + x[7] + x[8] <= 80, "Oferta Fábrica 3 - Restrição 3"

model += x[0] + x[3] + x[6] == 150, "Demanda Depósito 1 - Restrição 4"
model += x[1] + x[4] + x[7] == 70, "Demanda Depósito 2 - Restrição 5"
model += x[2] + x[5] + x[8] == 60, "Demanda Depósito 3 - Restrição 6"

model.solve()

print("Status:", pulp.LpStatus[model.status])
for var in x:
    print(f"{var.name} = {var.varValue}")
print("Custo mínimo total: R$", pulp.value(model.objective))
