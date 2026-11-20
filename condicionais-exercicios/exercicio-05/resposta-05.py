
# ATIVIDADE 5 - AJUSTE DE ESTOQUE
# UC4 - Desenvolver Algoritmos

print("=" * 45)
print("             AJUSTE DE ESTOQUE")
print("=" * 45)

# Entrada e validação da quantidade
while True:
    entrada = input(
        "Digite a quantidade atual em estoque: "
    ).strip()

    if entrada.isascii() and entrada.isdecimal():
        estoque = int(entrada)
        break

    print("Erro: informe uma quantidade inteira e não negativa.")

# Processamento
estoque_final = estoque
reposicao = 0

if estoque < 20:
    reposicao = 50
    estoque_final += reposicao

# Saída dos resultados
print("\n========== RESULTADO ==========")
print(f"Estoque original: {estoque} unidades")
print(f"Reposição realizada: {reposicao} unidades")
print(f"Estoque atualizado: {estoque_final} unidades")

print("\n========== FIM DO PROGRAMA ==========")
