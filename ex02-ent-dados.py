##Exercício 2: Calculadora de IMC
##Peça ao usuário para digitar seu peso (em kg) e sua altura (em metros). Calcule o Índice de Massa Corporal (IMC) usando a fórmula do IMC
## Exiba o resultado formatado com duas casas decimais.

p = float(input("Digite o seu peso: "))
a = float(input("Digite a sua altura por exemplo - 1.84: "))
imc = p / (a ** 2)
print(f"Seu IMC é {imc:.2f}")