# Escreva um programa que faça o seu computador 'pensar' em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
# pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
num = int(randint(0, 5))
escolha = int(input('Digite um número entre 0 e 5: '))
if escolha == num:
    print('Você acertou!')
else:
    print('Você errou, tente novamente!')