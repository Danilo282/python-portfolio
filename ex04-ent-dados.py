## Exercício 4: Cálculo de tempo de vida
##Peça ao usuário para digitar o ano em que nasceu e calcule sua idade.
##
##📌 Dica: Use import datetime para obter o ano atual.

import datetime

ano_nascimento = int(input("Digite o ano em que você nasceu: "))
ano_atual = datetime.datetime.now().year

idade = ano_atual - ano_nascimento

print(f"Você tem {idade} anos.")