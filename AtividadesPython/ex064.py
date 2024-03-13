# Crie um programa que leia vários números inteiros pelo teclado. O programa só
# vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (Desconsiderando o flag).

n = c = s = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    s += n
    c += 1
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre ele foi {}.'.format(c, s))

'''
n = 0
lista = []
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    lista.append(n)
lista.remove(999)
soma = sum(lista)
qtd = len(lista)
print('Você digitou {} números e a soma entre ele foi {}.'.format(qtd, soma))
'''
