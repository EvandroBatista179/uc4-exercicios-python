
# ATIVIDADE 1 - DESCONTO EM COMPRA
# UC4 - Desenvolver Algoritmos

import math

print("=" * 45)
print("           DESCONTO EM COMPRA")
print("=" * 45)

# Entrada e validação dos dados
while True:
    entrada = input(
        "Digite o valor da compra: R$ "
    ).strip().replace(",", ".")

    try:
        valor_compra = float(entrada)

        if math.isfinite(valor_compra) and valor_compra >= 0:
            break

        print("Erro: informe um valor válido e não negativo.")

    except ValueError:
        print("Erro: digite um valor numérico.")

# Processamento
valor_final = valor_compra

if valor_compra > 200:
    valor_final -= 30

# Saída dos resultados
print("\n========== RESULTADO ==========")
print(f"Valor original: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: R$ {valor_compra - valor_final:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")

print("\n========== FIM DO PROGRAMA ==========")
