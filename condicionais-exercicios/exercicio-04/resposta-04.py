
# ATIVIDADE 4 - META DE PONTUAÇÃO
# UC4 - Desenvolver Algoritmos

print("=" * 45)
print("             META DE PONTUAÇÃO")
print("=" * 45)

# Entrada e validação da pontuação
while True:
    entrada = input(
        "Digite a pontuação do jogador: "
    ).strip()

    if entrada.isascii() and entrada.isdecimal():
        pontuacao = int(entrada)
        break

    print("Erro: informe uma pontuação inteira e não negativa.")

# Processamento
pontuacao_final = pontuacao
bonus = 0

if pontuacao >= 500:
    bonus = 100
    pontuacao_final += bonus

# Saída dos resultados
print("\n========== RESULTADO ==========")
print(f"Pontuação original: {pontuacao}")
print(f"Bônus recebido: {bonus} pontos")
print(f"Pontuação final: {pontuacao_final}")

print("\n========== FIM DO PROGRAMA ==========")
