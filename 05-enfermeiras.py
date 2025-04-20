# Aluno: Victor Alexandre da R. M. Miranda <varm@ic.ufal.br>
# Pesquisa Operacional 2024.2
# 05 - Problema da Escala das Enfermeiras

import pulp

# dados de demanda mockados para o exemplo
demand = [3, 4, 2, 3, 4, 5, 2]

model = pulp.LpProblem("Enfermeiras", pulp.LpMinimize)

x = [pulp.LpVariable(f"x{i + 1}", cat="Binary") for i in range(7)]

model += pulp.lpSum(x), "Custo_Total"

model += pulp.lpSum(x[i]
                    for i in range(7)) >= demand[0], "Demanda_1 - Restricao 1"
model += pulp.lpSum(x[i]
                    for i in range(7)) >= demand[1], "Demanda_2 - Restricao 2"
model += pulp.lpSum(x[i]
                    for i in range(7)) >= demand[2], "Demanda_3 - Restricao 3"
model += pulp.lpSum(x[i]
                    for i in range(7)) >= demand[3], "Demanda_4 - Restricao 4"
model += pulp.lpSum(x[i]
                    for i in range(7)) >= demand[4], "Demanda_5 - Restricao 5"
model += pulp.lpSum(x[i]
                    for i in range(7)) >= demand[5], "Demanda_6 - Restricao 6"
model += pulp.lpSum(x[i]
                    for i in range(7)) >= demand[6], "Demanda_7 - Restricao 7"


model.solve()

print("Status:", pulp.LpStatus[model.status])
for var in x:
    print(f"{var.name} = {var.varValue}")
print("Enfermeiras mínimas necessárias:", pulp.value(model.objective))
