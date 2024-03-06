# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou Impar.

num = int(input('Digite um número: '))
analise = num % 2
if analise == 0:
    print('O número {} é PAR.'.format(num))
else:
    print('O número {} é ÍMPAR.'.format(num))
