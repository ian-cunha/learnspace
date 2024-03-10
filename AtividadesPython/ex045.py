# Crie um programa que faça o computador jogar Jokenpô com você.
# Pedra, papel e tesoura.

from random import randint
print('{:=^20}'.format(' JOKENPÔ '))
print('''Escolha entre:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
computador = randint(1, 3)
jogador = int(input('Qual sua escolha? '))
if jogador == 1 and computador == 3:
    print('Você ganhou!')
    print('Eu escolhi: {}'.format(computador))
elif jogador == 2 and computador == 1:
    print('Você ganhou!')
    print('Eu escolhi: {}'.format(computador))
elif jogador == 3 and computador == 2:
    print('Você ganhou!')
    print('Eu escolhi: {}'.format(computador))
elif jogador == computador:
    print('Empate')
    print('Eu também escolhi: {}'.format(computador))
elif jogador > 3:
    print('Opção inválida, tente novamente!')
else:
    print('Você perdeu!')
    print('Eu escolhi: {}'.format(computador))
