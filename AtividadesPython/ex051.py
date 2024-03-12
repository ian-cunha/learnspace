# Desenvolva um programa que leia o primeiro termo e a razão de um PA.
# (PROGRESSÃO ARITMETRICA) No final, mostre os 10 primeiros termos dessa progressão.

print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)

num = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
dec = num + (10 - 1) * raz
for c in range(num, dec + raz, raz):
    print('{}'.format(c), end=' => ')
print('Fim!')
