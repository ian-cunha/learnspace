# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os
# 10 primeiros termos da progressão usando a estrutura while.

print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)

num = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
termo = num
cont = 1
while cont <= 10:
    print('{}'.format(termo), end=' => ')
    termo += raz
    cont += 1
print('Fim!')
