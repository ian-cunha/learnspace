# Faça um programa que jogue par ou ímpar com o computador. O jogo só será
# interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo.

from random import randint
print('-='*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*10)
computador = randint(1, 100)
escolhapc = randint(0, 1)
jogador = int(input('Diga um valor: '))
escolha = str(input('Par ou Ímpar? [P/I] '))

soma = 0
soma += (computador + jogador)
base = soma % 2
if base == 0:
    resultado = 'Par'
else:
    resultado = 'Ímpar'
print(f'Você jogou {jogador} e o computator {computador}. Total de {soma} deu {base}')
