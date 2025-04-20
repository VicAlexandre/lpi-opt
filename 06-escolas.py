# Aluno: Victor Alexandre da R. M. Miranda <varm@ic.ufal.br>
# Pesquisa Operacional 2024.2
# 06 - Problema das Escolas
import pulp

# instância exemplo do problema para fins de teste
bairros = ["A", "B", "C", "D", "E", "F", "G", "H"]
n_bairros = len(bairros)
coberturas = {
    "A": ["A", "B", "C"],
    "B": ["A", "B", "D"],
    "C": ["A", "C", "E", "F"],
    "D": ["B", "D", "E"],
    "E": ["C", "D", "E", "G"],
    "F": ["C", "F", "H"],
    "G": ["E", "G", "H"],
    "H": ["F", "G", "H"],
}

model = pulp.LpProblem("Cobertura_Escolas", pulp.LpMinimize)

x = {}
for j in bairros:
    x[j] = pulp.LpVariable(f"x_{j}", cat=pulp.LpBinary)

model += pulp.lpSum(x[j] for j in bairros), "Minimizar_Escolas"

for i in bairros:
    model += pulp.lpSum(x[j]
                        for j in coberturas[i]) >= 1, f"Cobertura_Bairro_{i}"

model.solve()

print(f"Status: {pulp.LpStatus[model.status]}")

print("\nEscolas a serem construídas nos bairros:")
escolas_construidas = []
for j in bairros:
    if pulp.value(x[j]) > 0.5:
        escolas_construidas.append(j)
        print(f"Bairro {j}: SIM")
    else:
        print(f"Bairro {j}: NÃO")

print(f"\nQuantidade total de escolas necessárias: {len(escolas_construidas)}")

print("\nVerificação de cobertura:")
for i in bairros:
    bairros_que_cobrem = [j for j in coberturas[i] if j in escolas_construidas]
    print(f"Bairro {i} é coberto por escolas em: {
          ', '.join(bairros_que_cobrem)}")
