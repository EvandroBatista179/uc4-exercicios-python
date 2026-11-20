
# ATIVIDADE 6 - TAXA DE PROCESSAMENTO
# UC4 - Desenvolver Algoritmos

import math

print("=" * 45)
print("          TAXA DE PROCESSAMENTO")
print("=" * 45)

# Entrada e validação do valor da transferência
while True:
    entrada = input(
        "Digite o valor da transferência: R$ "
    ).strip().replace(",", ".")

    try:
        valor_transferencia = float(entrada)

        if (
            math.isfinite(valor_transferencia)
            and valor_transferencia >= 0
        ):
            break

        print("Erro: informe um valor válido e não negativo.")

    except ValueError:
        print("Erro: digite apenas valores numéricos.")

# Processamento
valor_final = valor_transferencia
taxa = 0.0

# Aplicação da taxa de processamento
if valor_transferencia > 1000:
    taxa = 15.0
    valor_final += taxa

# Saída dos resultados
print("\n========== RESULTADO ==========")
print(f"Valor da transferência: R$ {valor_transferencia:.2f}")
print(f"Taxa de processamento: R$ {taxa:.2f}")
print(f"Valor total a pagar: R$ {valor_final:.2f}")

print("\n========== FIM DO PROGRAMA ==========")
