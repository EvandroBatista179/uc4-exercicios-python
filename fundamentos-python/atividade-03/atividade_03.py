
# ATIVIDADE 3 - ANO ANTERIOR E POSTERIOR
# UC4 - Desenvolver Algoritmos

print("=" * 45)
print("        ANO ANTERIOR E POSTERIOR")
print("=" * 45)

# Entrada e validação do ano
while True:
    entrada = input("Digite o ano atual: ").strip()

    if entrada.isdecimal() and int(entrada) > 0:
        ano = int(entrada)
        break

    print("Erro: informe um ano inteiro positivo.")

# Processamento
ano_anterior = ano - 1
ano_posterior = ano + 1

# Saída dos resultados
print("\n---------- RESULTADO ----------")
print(f"Ano anterior: {ano_anterior}")
print(f"Ano informado: {ano}")
print(f"Ano posterior: {ano_posterior}")

# Verificação do tipo da variável
print("\n---------- TIPO DE DADO ----------")
print(f"Tipo da variável ano: {type(ano)}")

print("\n========== FIM DO PROGRAMA ==========")
