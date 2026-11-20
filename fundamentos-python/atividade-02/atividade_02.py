
# ATIVIDADE 2 - ENTRADA E TIPOS DE DADOS
# UC4 - Desenvolver Algoritmos

print("=" * 45)
print("       VERIFICADOR DE TIPOS DE DADOS")
print("=" * 45)

# Entrada de dados
numero = input("Digite um número inteiro: ").strip()

# Identificação do tipo original
print("\n---------- ENTRADA ORIGINAL ----------")
print(f"Valor informado: {numero}")
print(f"Tipo da variável: {type(numero)}")

# Validação e conversão
if numero.isdecimal():
    numero_inteiro = int(numero)

    print("\n---------- APÓS A CONVERSÃO ----------")
    print(f"Valor convertido: {numero_inteiro}")
    print(f"Novo tipo: {type(numero_inteiro)}")

else:
    print("\nErro: informe apenas dígitos de 0 a 9.")
    print("Não foi possível converter para inteiro.")

print("\n========== FIM DO PROGRAMA ==========")
