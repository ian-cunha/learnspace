# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
for num in range(1,7):
    n = int(input('Escolha {} número inteiro: '.format(num)))
    soma = soma + n
print('O Total será: {}'.format(soma))
