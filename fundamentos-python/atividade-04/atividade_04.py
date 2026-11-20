
# ATIVIDADE 4 - CALCULADORA DE TROCO
# UC4 - Desenvolver Algoritmos
# Simulação de caixa com 5 compras

# Variáveis de controle financeiro
total_caixa = 0.0
total_recebido = 0.0
total_troco = 0.0

historico_compras = []


# Função para validar valores monetários
def ler_valor(mensagem, minimo=0):
    while True:
        entrada = input(mensagem).strip().replace(",", ".")

        try:
            valor = float(entrada)

            if not (minimo <= valor < float("inf")):
                print("Erro: informe um valor válido.")
                continue

            return round(valor, 2)

        except ValueError:
            print("Erro: digite apenas valores numéricos.")


print("=" * 50)
print("          SISTEMA DE CAIXA")
print("=" * 50)

# Processamento de 5 compras
for compra in range(1, 6):

    print(f"\n========== COMPRA {compra} ==========")

    # Entrada do valor da compra
    valor_compra = ler_valor(
        "Digite o valor da compra: R$ ",
        0.01
    )

    # Entrada e validação do pagamento
    while True:
        valor_pago = ler_valor(
            "Digite o valor recebido: R$ "
        )

        if valor_pago >= valor_compra:
            break

        print("Pagamento insuficiente!")
        print("Informe um valor igual ou superior à compra.")

    # Cálculo do troco usando o operador -=
    troco_cliente = valor_pago
    troco_cliente -= valor_compra
    troco_cliente = round(troco_cliente, 2)

    # Exibir informações para o operador
    print("\n---------- PAGAMENTO ----------")
    print(f"Valor da compra: R$ {valor_compra:.2f}")
    print(f"Valor recebido: R$ {valor_pago:.2f}")
    print(f"TROCO DO CLIENTE: R$ {troco_cliente:.2f}")

    # Confirmação da entrega do troco
    if troco_cliente > 0:
        input(
            "\nEntregue o troco e pressione ENTER para confirmar."
        )
    else:
        print("Não é necessário entregar troco.")

    # Movimentação financeira
    entrou_no_caixa = valor_pago
    saiu_do_caixa = troco_cliente

    total_caixa += entrou_no_caixa
    total_caixa -= saiu_do_caixa

    total_recebido += entrou_no_caixa
    total_troco += saiu_do_caixa

    # Armazenar histórico da compra
    historico_compras.append({
        "compra": compra,
        "valor": valor_compra,
        "pagamento": valor_pago,
        "troco": troco_cliente
    })

    # Resumo de cada transação
    print("\n---------- MOVIMENTAÇÃO ----------")
    print(f"Entrou no caixa: R$ {entrou_no_caixa:.2f}")
    print(f"Saiu do caixa: R$ {saiu_do_caixa:.2f}")
    print(f"Saldo em caixa: R$ {total_caixa:.2f}")
    print("Compra finalizada com sucesso!")


# Fechamento do caixa
print("\n========== FECHAMENTO DO CAIXA ==========")

for registro in historico_compras:
    print(f"\nCompra {registro['compra']}")
    print(f"Valor: R$ {registro['valor']:.2f}")
    print(f"Pagamento: R$ {registro['pagamento']:.2f}")
    print(f"Troco: R$ {registro['troco']:.2f}")

print("\n========== RESUMO FINANCEIRO ==========")
print(f"Total de compras: {len(historico_compras)}")
print(f"Total recebido: R$ {total_recebido:.2f}")
print(f"Total de troco: R$ {total_troco:.2f}")
print(f"Saldo final do caixa: R$ {total_caixa:.2f}")

print("\n========== CAIXA ENCERRADO ==========")
