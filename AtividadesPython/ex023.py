# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um
# dos digitos separados. 
# Ex: Digite um numero: 1934
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

num = str(input('Digite um número entre 0 a 9999: '))
print('Unidade: {}'.format(num))
print('Dezena: {}'.format(num))
print('Centena: {}'.format(num))
print('Milhar: {}'.format(num))