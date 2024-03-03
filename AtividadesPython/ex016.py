# Crie um programa que leia um número Real qualquer e mostre na tela a sua porção inteira.
# Ex: O número 6.152, tem sua porção intera de 6.

'''
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))
'''

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))