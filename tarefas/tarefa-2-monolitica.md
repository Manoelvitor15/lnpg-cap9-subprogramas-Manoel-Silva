produtos = {
    1: ("PRODUTO A", 50),
    2: ("PRODUTO B", 20),
    3: ("PRODUTO C", 40),
    4: ("PRODUTO D", 90),
    5: ("PRODUTO E", 30),
    6: ("PRODUTO F", 100)
}

carrinho = []
total = 0

while True:
    print("******************************************")
    print("*          PRODUTOS DISPONIVEIS          *")
    print("******************************************")
    print("* ID  *     NOME     *      VALOR        *")
    print("******************************************")

    for codigo, dados in produtos.items():
        nome, preco = dados
        print(f"{codigo} - {nome} | R$ {preco:.2f}")

    try:
        escolha = int(input("Digite o código do produto: "))
    except ValueError:
        print("Entrada inválida. Por favor digite um número.")
        continue

    if escolha in produtos:
        try:
            qtd = int(input("Quantidade: "))
        except ValueError:
            print("Quantidade inválida. Digite um número inteiro.")
            continue

        nome, preco = produtos[escolha]
        subtotal = preco * qtd

        carrinho.append((nome, qtd, subtotal))
        total += subtotal

        print(f"{nome} adicionado ao carrinho!")
    else:
        print("Produto inválido!")
        continue

    continuar = input("Deseja adicionar mais produtos? S/N: ").strip().lower()
    if continuar != "s":
        break

print("*" * 54)
print("\n*                     CUPOM FISCAL                   *")
print("*" * 54)
for item in carrinho:
    nome, qtd, subtotal = item
    print(f"* {nome:10} * Quantidade: {qtd:2d} * Subtotal: R$ {subtotal:7.2f} *")

print("*" * 54)
print(f"* Total bruto: R$ {total:.2f}                             *")

if total > 500:
    print("* Desconto aplicado por compras acima de R$ 500: 10%                             *")
    desconto = total * 0.10
elif total > 200:
    print("* Desconto aplicado por compras acima de R$ 200: 5%                              *")
    desconto = total * 0.05
else:
    desconto = 0.0

print(f"* Desconto: R$ {desconto:.2f}                                 *")
print(f"* Total final: R$ {total - desconto:.2f}                             *")
print("* Compra finalizada com sucesso!                     *")
print("*" * 54)
