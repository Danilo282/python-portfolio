## Exercício 3: Inversão de nome
## Peça ao usuário para digitar seu nome completo e exiba-o no formato "Último Nome, Primeiro Nome".
##
##📌 Exemplo:
## Entrada: João Silva
## Saída: Silva, João

nome_completo = input("Digite seu nome completo: ")
partes = nome_completo.split()

ultimo_nome = partes[-1]
primeiro_nome = partes[0]

print(f"{ultimo_nome}, {primeiro_nome}")