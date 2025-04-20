# Aluno: Victor Alexandre da R. M. Miranda <varm@ic.ufal.br>
# Pesquisa Operacional 2024.2
# 08 - Problema da Fábrica de Latinhas
import pulp

folhas_tipo1 = 200
folhas_tipo2 = 90
preco_latinha = 50
custo_estoque_corpo = 50
custo_estoque_tampa = 3

padroes = [
    [2, 1, 7, 2],  # Padrão 1
    [1, 2, 3, 3],  # Padrão 2
    [1, 0, 9, 2],  # Padrão 3
    [1, 4, 4, 1],  # Padrão 4
]

model = pulp.LpProblem("Maximizar_Lucro_Fabrica_Latinhas", pulp.LpMaximize)

x = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(4)]

corpos_nao_usados = pulp.LpVariable(
    "corpos_nao_usados", lowBound=0, cat="Integer")
tampas_nao_usadas = pulp.LpVariable(
    "tampas_nao_usadas", lowBound=0, cat="Integer")

model += (
    preco_latinha * pulp.lpSum(padroes[i][1] * x[i] for i in range(4))
    - custo_estoque_corpo * corpos_nao_usados
    - custo_estoque_tampa * tampas_nao_usadas
)

model += (
    pulp.lpSum(padroes[i][0] * x[i] for i in range(4) if padroes[i][0] == 1)
    <= folhas_tipo1
)
model += (
    pulp.lpSum(padroes[i][0] * x[i] for i in range(4) if padroes[i][0] == 2)
    <= folhas_tipo2
)

model += (
    pulp.lpSum(padroes[i][1] * x[i] for i in range(4))
    - (1 / 2) * pulp.lpSum(padroes[i][2] * x[i] for i in range(4))
    == corpos_nao_usados
)

model += (
    pulp.lpSum(padroes[i][2] * x[i] for i in range(4))
    - 2 * pulp.lpSum(padroes[i][1] * x[i] for i in range(4))
    == tampas_nao_usadas
)

status = model.solve()

print("Status:", pulp.LpStatus[status])
print(f"Lucro máximo: R${pulp.value(model.objective):.2f}")
print("\nQuantidade de cada padrão a ser impresso:")
for i in range(4):
    print(f"Padrão {i + 1}: {int(x[i].value())} impressões")

print(f"\nCorpos não utilizados: {int(corpos_nao_usados.value())}")
print(f"Tampas não utilizadas: {int(tampas_nao_usadas.value())}")
