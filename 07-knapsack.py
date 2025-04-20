# Aluno: Victor Alexandre da R. M. Miranda <varm@ic.ufal.br>
# Pesquisa Operacional 2024.2
# 07 - Problema da Mochila
import pulp

# instância exemplo do problema para fins de teste
itens = ["A", "B", "C", "D", "E", "F", "G", "H"]
n_itens = len(itens)
valores = {"A": 20, "B": 30, "C": 15, "D": 25,
           "E": 10, "F": 40, "G": 35, "H": 22}
pesos = {"A": 5, "B": 8, "C": 3, "D": 6, "E": 2, "F": 12, "G": 9, "H": 5}

capacidade_mochila = 25

model = pulp.LpProblem("Problema_Mochila", pulp.LpMaximize)

x = {}
for i in itens:
    x[i] = pulp.LpVariable(f"x_{i}", cat=pulp.LpBinary)

model += pulp.lpSum(valores[i] * x[i] for i in itens), "Maximizar_Valor_Total"

model += (
    pulp.lpSum(pesos[i] * x[i] for i in itens) <= capacidade_mochila,
    "Capacidade_Mochila",
)

model.solve()

print(f"Status da solução: {pulp.LpStatus[model.status]}")

print("\nItens selecionados para a mochila:")
valor_total = 0
peso_total = 0
itens_selecionados = []

for i in itens:
    if pulp.value(x[i]) > 0.5:
        itens_selecionados.append(i)
        valor_total += valores[i]
        peso_total += pesos[i]
        print(f"Item {i}: SIM (Valor: {valores[i]}, Peso: {pesos[i]})")
    else:
        print(f"Item {i}: NÃO (Valor: {valores[i]}, Peso: {pesos[i]})")

print(f"\nValor total dos itens na mochila: {valor_total}")
print(f"Peso total dos itens na mochila: {peso_total}")
print(f"Capacidade da mochila: {capacidade_mochila}")

print("\nEficiência dos itens (valor/peso):")
for i in itens:
    eficiencia = valores[i] / pesos[i]
    status = "Selecionado" if i in itens_selecionados else "Não selecionado"
    print(f"Item {i}: {eficiencia:.2f} - {status}")
