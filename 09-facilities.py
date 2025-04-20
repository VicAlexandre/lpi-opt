# Aluno: Victor Alexandre da R. M. Miranda <varm@ic.ufal.br>
# Pesquisa Operacional 2024.2
# 09 - Problema das Facilidades
import pulp

N = 5
M = 10

custos_instalacao = [100, 150, 200, 120, 180]

custos_atendimento = [
    [10, 15, 20, 12, 18, 22, 14, 16, 19, 11],
    [12, 18, 22, 15, 20, 25, 16, 14, 21, 13],
    [8, 12, 15, 10, 14, 18, 11, 9, 13, 7],
    [15, 20, 25, 18, 22, 28, 19, 17, 24, 16],
    [11, 16, 19, 13, 17, 21, 14, 12, 18, 10],
]

model = pulp.LpProblem("Problema_das_Facilidades", pulp.LpMinimize)

x = pulp.LpVariable.dicts(
    "Atendimento", [(i, j) for i in range(N) for j in range(M)], cat="Binary"
)

y = pulp.LpVariable.dicts("Deposito", [i for i in range(N)], cat="Binary")

model += pulp.lpSum(custos_instalacao[i] * y[i] for i in range(N)) + pulp.lpSum(
    custos_atendimento[i][j] * x[(i, j)] for i in range(N) for j in range(M)
)

for j in range(M):
    model += pulp.lpSum(x[(i, j)] for i in range(N)) == 1

for i in range(N):
    for j in range(M):
        model += x[(i, j)] <= y[i]

status = model.solve()

print("Status:", pulp.LpStatus[status])
print("Custo total:", pulp.value(model.objective))

print("\nDepósitos construídos:")
for i in range(N):
    if y[i].value() == 1:
        print(f"Depósito {i + 1}")

print("\nAlocação de clientes:")
for j in range(M):
    for i in range(N):
        if x[(i, j)].value() == 1:
            print(f"Cliente {j + 1} -> Depósito {i + 1}")
            break
