
# ATIVIDADE 1 - REGISTRO NO SISTEMA
# UC4 - Desenvolver Algoritmos

print("=" * 45)
print("          REGISTRO NO SISTEMA")
print("=" * 45)

# Entrada e validação do nome
while True:
    nome = input("Qual o seu nome? ").strip().title()

    if nome:
        break

    print("Erro: o nome não pode ficar em branco.")

# Entrada e validação do sobrenome
while True:
    sobrenome = input("Qual o seu sobrenome? ").strip().title()

    if sobrenome:
        break

    print("Erro: o sobrenome não pode ficar em branco.")

# Processamento
nome_completo = f"{nome} {sobrenome}"

# Saída dos dados
print("\n" + "=" * 45)
print("          REGISTRO CONCLUÍDO")
print("=" * 45)

print(f"O seu nome é {nome_completo}")
print("Registro realizado com sucesso!")
