
# ATIVIDADE 2 - AUMENTO SALARIAL
# UC4 - Desenvolver Algoritmos

import math

print("=" * 45)
print("            AUMENTO SALARIAL")
print("=" * 45)

# Entrada e validação do salário
while True:
    entrada = input(
        "Digite o salário atual: R$ "
    ).strip().replace(",", ".")

    try:
        salario = float(entrada)

        if math.isfinite(salario) and salario >= 0:
            break

        print("Erro: informe um salário válido e não negativo.")

    except ValueError:
        print("Erro: digite apenas valores numéricos.")

# Processamento
novo_salario = salario
aumento = 0.0

if salario < 1500:
    aumento = 200.0
    novo_salario += aumento

# Saída dos resultados
print("\n========== RESULTADO ==========")
print(f"Salário original: R$ {salario:.2f}")
print(f"Aumento aplicado: R$ {aumento:.2f}")
print(f"Salário atualizado: R$ {novo_salario:.2f}")

print("\n========== FIM DO PROGRAMA ==========")
