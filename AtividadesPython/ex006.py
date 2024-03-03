# Desafio 006
# Crie um algoritmo que leia um número e mostre o seu dobro,
# triplo e raiz quadrada.

n = int(input('Digite algum número: '))
dobro = n * 2
triplo = n * 3
raiz = pow(n, (1/2))
print('Seu dobro é: {}'.format(dobro))
print('Seu triplo é: {}'.format(triplo))
print('Raiz quadrada é {:.2f}'.format(raiz))