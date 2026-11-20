
# ATIVIDADE 5 - VERIFICADOR DE MAIORIDADE
# UC4 - Desenvolver Algoritmos

print("=" * 45)
print("         VERIFICADOR DE MAIORIDADE")
print("=" * 45)

# Entrada e validação dos anos
while True:
    nascimento = input(
        "Digite o ano de nascimento: "
    ).strip()

    atual = input(
        "Digite o ano atual: "
    ).strip()

    # Verificar se os dados são números inteiros
    if nascimento.isascii() and nascimento.isdecimal() \
            and atual.isascii() and atual.isdecimal():

        ano_nascimento = int(nascimento)
        ano_atual = int(atual)

        # Verificar se os anos são válidos
        if 0 < ano_nascimento <= ano_atual:
            break

    print("\nErro: informe anos inteiros positivos e válidos.")
    print("O nascimento não pode ser posterior ao ano atual.\n")

# Processamento
idade = ano_atual - ano_nascimento

# Operador relacional - resultado booleano
maior_idade = idade >= 18

# Classificação
if maior_idade:
    status = "Maior de idade"
else:
    status = "Menor de idade"

# Saída dos resultados
print("\n========== RESULTADO ==========")
print(f"Ano de nascimento: {ano_nascimento}")
print(f"Ano atual: {ano_atual}")
print(f"Idade calculada: {idade} anos")
print(f"Classificação: {status}")
print(f"Maior de idade? {maior_idade}")

print("\n========== FIM DO PROGRAMA ==========")
