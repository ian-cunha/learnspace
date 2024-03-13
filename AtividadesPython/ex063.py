# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os
# n primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

print('-='*10, 'Sequência de Fibonacci', '=-'*10)
seq = int(input('Quantos termos você quer mostrar? '))
cont = 3
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
while cont <= seq:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    cont += 1
    t1 = t2
    t2 = t3
print(' -> Fim!')
