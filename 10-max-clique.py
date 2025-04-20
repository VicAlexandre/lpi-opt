# Aluno: Victor Alexandre da R. M. Miranda <varm@ic.ufal.br>
# Pesquisa Operacional 2024.2
# 10 - Problema da clique máxima
import pulp

V = [0, 1, 2, 3, 4, 5]
E = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3),
     (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)]

model = pulp.LpProblem("Clique_Maxima", pulp.LpMaximize)

x = pulp.LpVariable.dicts("No", V, cat="Binary")

model += pulp.lpSum(x[i] for i in V)

for i, j in [
    (i, j) for i in V for j in V if i < j and (i, j) not in E and (j, i) not in E
]:
    model += x[i] + x[j] <= 1

status = model.solve()

print("Status:", pulp.LpStatus[status])
print("Tamanho da clique máxima:", pulp.value(model.objective))

print("\nVértices na clique máxima:")
for i in V:
    if x[i].value() == 1:
        print(f"Vértice {i}")
