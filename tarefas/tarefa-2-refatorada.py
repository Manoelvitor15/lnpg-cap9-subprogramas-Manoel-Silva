# Implemente um sistema de vendas em Python que:
# leia produtos;
# leia quantidade;
# leia preço unitário;
# calcule subtotal;
# calcule desconto:
# 5% acima de R$ 200;
# 10% acima de R$ 500;
# calcule total final;
# imprima cupom formatado.

produtos = {
    1: ("PRODUTO A", 50),
    2: ("PRODUTO B", 20),
    3: ("PRODUTO C", 40),
    4: ("PRODUTO D", 90),
    5: ("PRODUTO E", 30),
    6: ("PRODUTO F", 100)
}

carrinho = []


def ler_produto():
    print("******************************************")
    print("*          PRODUTOS DISPONIVEIS          *")
    print("******************************************")
    print("* ID  *     NOME     *      VALOR        *")
    print("******************************************")

    for codigo, dados in produtos.items():
        nome, preco = dados
        print(f"{codigo} - {nome} | R$ {preco:.2f}")

    while True:
        escolha_text = input("Digite o código do produto: ")
        if not escolha_text.isdigit():
            print("Código inválido. Digite um número de produto válido.\n")
            continue

        escolha = int(escolha_text)
        if escolha not in produtos:
            print("Código inválido. Digite um produto existente.\n")
            continue

        qtd_text = input("Quantidade: ")
        if not qtd_text.isdigit():
            print("Quantidade inválida. Digite um número inteiro.\n")
            continue

        qtd = int(qtd_text)
        if qtd <= 0:
            print("Quantidade deve ser maior que zero.\n")
            continue

        nome, preco = produtos[escolha]
        return nome, preco, qtd


def calcular_subtotal(preco, qtd):
    return preco * qtd


def calcular_desconto(total):
    if total > 500:
        return total * 0.10
    elif total > 200:
        return total * 0.05
    return 0.0


def calcular_total(total, desconto):
    return total - desconto


def imprimir_cupom(carrinho, total, desconto, total_final):
    print("*" * 54)
    print("*                     CUPOM FISCAL                   *")
    print("*" * 54)

    for nome, qtd, subtotal in carrinho:
        print(f"* {nome:10} * Quantidade: {qtd:2d} * Subtotal: R$ {subtotal:7.2f} *")

    print("*" * 54)
    print(f"* Total bruto: R$ {total:.2f}                             *")
    print(f"* Desconto: R$ {desconto:.2f}                                 *")
    print(f"* Total final: R$ {total_final:.2f}                             *")
    print("* Compra finalizada com sucesso!                     *")
    print("*" * 54)


def main():
    total = 0.0

    while True:
        nome, preco, qtd = ler_produto()
        subtotal = calcular_subtotal(preco, qtd)
        carrinho.append((nome, qtd, subtotal))
        total += subtotal

        print(f"{nome} adicionado ao carrinho!\n")
        continuar = input("Deseja adicionar mais produtos? S/N: ").strip().lower()
        if continuar != "s":
            break

    desconto = calcular_desconto(total)
    total_final = calcular_total(total, desconto)
    imprimir_cupom(carrinho, total, desconto, total_final)


if __name__ == "__main__":
    main()
