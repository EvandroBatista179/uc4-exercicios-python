
# ATIVIDADE 6 - VALIDAÇÃO DE DESCONTO E FRETE GRÁTIS
# UC4 - Desenvolver Algoritmos

import math

print("=" * 50)
print("       VALIDAÇÃO DE DESCONTO E FRETE GRÁTIS")
print("=" * 50)

# Entrada e validação dos dados
while True:
    entrada_valor = input(
        "Digite o valor total da compra: R$ "
    ).strip().replace(",", ".")

    entrada_itens = input(
        "Digite a quantidade de itens: "
    ).strip()

    try:
        valor_compra = float(entrada_valor)

        # Verifica se os itens são números inteiros
        if not (entrada_itens.isascii() and entrada_itens.isdecimal()):
            print("\nErro: informe uma quantidade inteira válida.\n")
            continue

        quantidade_itens = int(entrada_itens)

        # Verifica os valores informados
        if not math.isfinite(valor_compra) or valor_compra < 0:
            print("\nErro: o valor da compra é inválido.\n")
            continue

        break

    except ValueError:
        print("\nErro: informe um valor numérico válido.\n")

# Processamento com operador lógico AND
beneficio = valor_compra > 150 and quantidade_itens > 3

# Saída dos resultados
print("\n========== RESULTADO ==========")
print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Quantidade de itens: {quantidade_itens}")
print(f"Direito ao benefício: {beneficio}")

# Mensagem adicional para o cliente
if beneficio:
    print("Cliente elegível ao desconto e frete grátis!")
else:
    print("Cliente não atende aos critérios do benefício.")

print("\n========== FIM DO PROGRAMA ==========")
