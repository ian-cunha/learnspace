# Desafio 009
# Faça um programa que leia um número inteiro qualquer e
# mostre na tela a sua tabuada.

n = int(input('Tabuada de: '))
tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('-' * 12)
for tab in tabuada:
    print('{} x {:2} = {}'.format(n, tab, n * tab))
print('-' * 12)