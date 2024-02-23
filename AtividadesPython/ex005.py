# Desafio 005
# Faça um programa que leia um número inteiro e 
# mostre na tela o seu sucessor e seu antecessor.

numero = int(input('Digite um número: '))
anterior = numero - 1
proximo = numero + 1
print('O número anterior é {}, e o próximo é {}.'.format(anterior, proximo))