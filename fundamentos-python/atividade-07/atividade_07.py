
# ATIVIDADE 7 - CLASSIFICAÇÃO DE STATUS DE COMPRA
# UC4 - Desenvolver Algoritmos

import math

print("=" * 50)
print("          CLASSIFICAÇÃO DE STATUS DE COMPRA")
print("=" * 50)

# Entrada e validação dos valores
while True:
    entrada_saldo = input(
        "Digite o saldo disponível: R$ "
    ).strip().replace(",", ".")

    entrada_produto = input(
        "Digite o valor do produto: R$ "
    ).strip().replace(",", ".")

    try:
        saldo = float(entrada_saldo)
        valor_produto = float(entrada_produto)

        if (
            math.isfinite(saldo)
            and math.isfinite(valor_produto)
            and saldo >= 0
            and valor_produto >= 0
        ):
            break

        print("\nErro: informe valores válidos e não negativos.\n")

    except ValueError:
        print("\nErro: digite apenas valores numéricos.\n")

# Processamento usando operador ternário
status = (
    "Compra Aprovada"
    if saldo >= valor_produto
    else "Saldo Insuficiente"
)

# Saída dos resultados
print("\n========== RESULTADO ==========")
print(f"Saldo disponível: R$ {saldo:.2f}")
print(f"Valor do produto: R$ {valor_produto:.2f}")
print(f"Status da compra: {status}")

print("\n========== FIM DO PROGRAMA ==========")
