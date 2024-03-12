# Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas
# jã são maiores.

from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))
