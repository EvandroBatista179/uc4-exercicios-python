
# ATIVIDADE 3 - VERIFICAÇÃO DE TEMPERATURA
# UC4 - Desenvolver Algoritmos

import math

print("=" * 45)
print("        VERIFICAÇÃO DE TEMPERATURA")
print("=" * 45)

# Entrada e validação da temperatura
while True:
    entrada = input(
        "Digite a temperatura atual (°C): "
    ).strip().replace(",", ".")

    try:
        temperatura = float(entrada)

        if math.isfinite(temperatura):
            break

        print("Erro: informe uma temperatura válida.")

    except ValueError:
        print("Erro: digite apenas valores numéricos.")

# Processamento
temperatura_final = temperatura

if temperatura > 35:
    temperatura_final += 5

# Saída dos resultados
print("\n========== RESULTADO ==========")
print(f"Temperatura original: {temperatura:.1f} °C")
print(f"Temperatura final: {temperatura_final:.1f} °C")

print("\n========== FIM DO PROGRAMA ==========")
