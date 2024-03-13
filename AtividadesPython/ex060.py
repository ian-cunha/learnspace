# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5!=5x4x3x2x1=120
# Fazer com FOR e WHILE

n = int(input('Digite um número para calcular o seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

#from math import factorial
#num = int(input('Digite um número para calcular o Fatorial: '))
#print('O fatorial de {} è {}'.format(num, fat))
