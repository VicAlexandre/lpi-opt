# Aluno: Victor Alexandre da R. M. Miranda <varm@ic.ufal.br>
# Pesquisa Operacional 2024.2
# 03 - Problema das Tintas

import pulp

prob = pulp.LpProblem("Problema_Tintas", pulp.LpMinimize)

SolA_SR = pulp.LpVariable("SolA_SR", lowBound=0)
SolB_SR = pulp.LpVariable("SolB_SR", lowBound=0)
SEC_SR = pulp.LpVariable("SEC_SR", lowBound=0)
COR_SR = pulp.LpVariable("COR_SR", lowBound=0)

SolA_SN = pulp.LpVariable("SolA_SN", lowBound=0)
SolB_SN = pulp.LpVariable("SolB_SN", lowBound=0)
SEC_SN = pulp.LpVariable("SEC_SN", lowBound=0)
COR_SN = pulp.LpVariable("COR_SN", lowBound=0)

prob += (
    1.5 * (SolA_SR + SolA_SN)
    + 1.0 * (SolB_SR + SolB_SN)
    + 4.0 * (SEC_SR + SEC_SN)
    + 6.0 * (COR_SR + COR_SN),
    "Custo_Total",
)

prob += SolA_SR + SolB_SR + SEC_SR + COR_SR == 1000, "Volume_Total_SR"
prob += SolA_SN + SolB_SN + SEC_SN + COR_SN == 250, "Volume_Total_SN"

prob += 0.3 * SolA_SR + 0.6 * SolB_SR + 1.0 * SEC_SR >= 250, "Min_SEC_SR"
prob += 0.7 * SolA_SR + 0.4 * SolB_SR + 1.0 * COR_SR >= 500, "Min_COR_SR"

prob += 0.3 * SolA_SN + 0.6 * SolB_SN + 1.0 * SEC_SN >= 50, "Min_SEC_SN"
prob += 0.7 * SolA_SN + 0.4 * SolB_SN + 1.0 * COR_SN >= 125, "Min_COR_SN"

prob.solve()

print("Status:", pulp.LpStatus[prob.status])

if prob.status == pulp.LpStatusOptimal:
    print("\nQuantidades ótimas:")

    print("\nPara tinta de Secagem Rápida (SR) - 1000 litros:")
    print(f"Solução A: {SolA_SR.value():.2f} litros")
    print(f"Solução B: {SolB_SR.value():.2f} litros")
    print(f"Componente SEC: {SEC_SR.value():.2f} litros")
    print(f"Componente COR: {COR_SR.value():.2f} litros")

    print("\nPara tinta de Secagem Normal (SN) - 250 litros:")
    print(f"Solução A: {SolA_SN.value():.2f} litros")
    print(f"Solução B: {SolB_SN.value():.2f} litros")
    print(f"Componente SEC: {SEC_SN.value():.2f} litros")
    print(f"Componente COR: {COR_SN.value():.2f} litros")

    total_SolA = SolA_SR.value() + SolA_SN.value()
    total_SolB = SolB_SR.value() + SolB_SN.value()
    total_SEC = SEC_SR.value() + SEC_SN.value()
    total_COR = COR_SR.value() + COR_SN.value()

    print("\nQuantidade total a ser comprada:")
    print(f"Solução A: {total_SolA:.2f} litros")
    print(f"Solução B: {total_SolB:.2f} litros")
    print(f"Componente SEC: {total_SEC:.2f} litros")
    print(f"Componente COR: {total_COR:.2f} litros")

    custo_total = (
        1.5 * total_SolA + 1.0 * total_SolB + 4.0 * total_SEC + 6.0 * total_COR
    )
    print(f"\nCusto total: R$ {custo_total:.2f}")

    SEC_na_SR = (
        (0.3 * SolA_SR.value() + 0.6 * SolB_SR.value() + SEC_SR.value()) / 1000 * 100
    )
    COR_na_SR = (
        (0.7 * SolA_SR.value() + 0.4 * SolB_SR.value() + COR_SR.value()) / 1000 * 100
    )

    SEC_na_SN = (
        (0.3 * SolA_SN.value() + 0.6 * SolB_SN.value() + SEC_SN.value()) / 250 * 100
    )
    COR_na_SN = (
        (0.7 * SolA_SN.value() + 0.4 * SolB_SN.value() + COR_SN.value()) / 250 * 100
    )

    print("\nComposição final das tintas:")
    print(f"SR: {SEC_na_SR:.2f}% SEC, {COR_na_SR:.2f}% COR")
    print(f"SN: {SEC_na_SN:.2f}% SEC, {COR_na_SN:.2f}% COR")
else:
    print("Não foi possível encontrar uma solução ótima.")
