# Desafio 006
# Crie um algoritmo que leia um número e mostre o seu dobro,
# triplo e raiz quadrada.
import math

n = int(input('Digite algum número: '))
dobro = n + n
triplo = n + n + n
raiz = math.sqrt(n)
print('Seu dobro é: {}'.format(dobro))
print('Seu triplo é: {}'.format(triplo))
print('Raiz quadrada é {:.3f}'.format(raiz))