
# ATIVIDADE 8 - MÉDIA E APROVAÇÃO DIRETA
# UC4 - Desenvolver Algoritmos

import math

print("=" * 50)
print("          MÉDIA E APROVAÇÃO DIRETA")
print("=" * 50)

# Entrada e validação das notas
while True:
    entrada_nota1 = input(
        "Digite a primeira nota: "
    ).strip().replace(",", ".")

    entrada_nota2 = input(
        "Digite a segunda nota: "
    ).strip().replace(",", ".")

    try:
        nota1 = float(entrada_nota1)
        nota2 = float(entrada_nota2)

        # Verificar se as notas estão entre 0 e 10
        if (
            math.isfinite(nota1)
            and math.isfinite(nota2)
            and 0 <= nota1 <= 10
            and 0 <= nota2 <= 10
        ):
            break

        print("\nErro: as notas devem estar entre 0 e 10.\n")

    except ValueError:
        print("\nErro: informe apenas valores numéricos.\n")

# Processamento - média aritmética simples
media = (nota1 + nota2) / 2

# Classificação usando operador ternário
status = "Aprovado" if media >= 7 else "Atenção"

# Saída dos resultados
print("\n========== RESULTADO ==========")
print(f"Primeira nota: {nota1:.2f}")
print(f"Segunda nota: {nota2:.2f}")
print(f"Média final: {media:.2f}")
print(f"Status do aluno: {status}")

print("\n========== FIM DO PROGRAMA ==========")
