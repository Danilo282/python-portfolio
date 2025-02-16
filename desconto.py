## Exercício 8: Calculadora de desconto
## Peça ao usuário para digitar o valor de um produto e o percentual de desconto. Calcule e exiba o preço final com o desconto aplicado.


preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o percentual de desconto: "))

preco_final = preco - (preco * desconto / 100)
print(f"Preço final com desconto: R$ {preco_final:.2f}".replace(".", ","))